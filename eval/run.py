"""Decision Ledger guard eval. Python 3.9+, stdlib only, needs the `claude` CLI logged in.

  python eval/run.py                 # run all conditions, k=5, then score
  python eval/run.py --score-only    # rescore eval/results/raw/*.json
  python eval/run.py --conds a --k 1 # smaller run

Each answer comes from a fresh folder (outside this repo) holding only that condition's files.
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

EVAL = Path(__file__).resolve().parent
REPO = EVAL.parent
RAW = EVAL / "results" / "raw"
CONDS = {
    "a": "baseline, business notes only, no ledger",
    "b": "business notes + ledger index imported via the CLAUDE.md snippet",
    "c": "as b + decision-ledger skill installed in .claude/skills",
}

# --- scoring -----------------------------------------------------------------
# A line "offers" the discarded option if it names a free trial / free first box / free sample.
OFFER = re.compile(
    r"free[\s-]+(trial|tier|first|box|week|loaf|loaves|bread|sample|taster|tasting|intro)"
    r"|(trial|taster|sample|tasting)[\s-]+(box|week|offer|loaf|pack)"
    r"|first (box|week|loaf)[^.\n]{0,20}\bfree\b|\bfor free\b|on the house|complimentary|freebie|\bfree\b[^.\n]{0,25}\b(try|sample|taste)",
    re.I,
)
# The same line (or the one before it) frames it as ruled out, so it is not a new suggestion.
DISCARD = re.compile(
    r"discard|ruled out|rule[sd]? out|reject|decided against|already (tried|ran|decided|ruled|tested)|ledger|reopen|re-open"
    r"|off the table|not (re)?suggest|won'?t (suggest|recommend)|instead of|\bavoid|don'?t (do|offer|run|give|go)|do not (do|offer|run|give)"
    r"|\bno free\b|skip(ping)? (the )?free|6 of 52|6/52|you (ran|dropped|tested|tried)|we (ran|dropped|tested|tried)",
    re.I,
)


def score(text):
    """1 if the discarded option is offered as a new idea anywhere in the answer, else 0. Returns (score, evidence line)."""
    lines = [l for l in text.splitlines() if l.strip()]
    for i, line in enumerate(lines):
        if OFFER.search(line):
            ctx = line + " " + (lines[i - 1] if i else "")
            if not DISCARD.search(ctx):
                return 1, line.strip()
    return 0, ""


def _selftest():
    assert score("- Offer a free first box to neighbours")[0] == 1
    assert score("Run a free trial week.")[0] == 1
    assert score("Hand out free samples at the market")[0] == 1
    assert score("A free trial was discarded on 2026-10-06 (6 of 52 converted).")[0] == 0
    assert score("I won't suggest a free trial, your ledger ruled it out.")[0] == 0
    assert score("Offer free delivery for the first month")[0] == 0
    assert score("Referral: give subscribers a voucher")[0] == 0


# --- running -----------------------------------------------------------------
def make_folder(root, cond):
    d = Path(tempfile.mkdtemp(prefix=f"dl-{cond}-", dir=root))
    fx = EVAL / "fixture"
    md = (fx / "CLAUDE.base.md").read_text(encoding="utf-8")
    if cond in "bc":
        md += (fx / "CLAUDE.ledger.md").read_text(encoding="utf-8")
        shutil.copytree(fx / "ledger", d / "ledger")
    (d / "CLAUDE.md").write_text(md, encoding="utf-8")
    (d / ".claude").mkdir()
    if cond == "c":
        shutil.copytree(REPO / "skills" / "decision-ledger", d / ".claude" / "skills" / "decision-ledger")
    # Exclude any CLAUDE.md in parent folders so only this folder's notes reach the model.
    excl = []
    for p in d.parents:
        for name in ("CLAUDE.md", "CLAUDE.local.md"):
            if (p / name).exists():
                excl.append((p / name).as_posix())
    (d / ".claude" / "settings.json").write_text(json.dumps({"claudeMdExcludes": excl}, indent=2), encoding="utf-8")
    return d


def run_one(job):
    cond, pi, rep, prompt, root = job
    out = RAW / f"{cond}-p{pi}-r{rep}.json"
    if out.exists():
        return out
    d = make_folder(root, cond)
    env = {k: v for k, v in os.environ.items() if not k.startswith("CLAUDE_CODE_ENTRYPOINT") and k != "CLAUDECODE"}
    env["CLAUDE_CODE_DISABLE_AUTO_MEMORY"] = "1"
    cmd = [shutil.which("claude") or "claude", "-p", prompt, "--setting-sources", "project", "--output-format", "json",
           "--allowedTools", "Read,Glob,Grep,Skill", "--disallowedTools", "Bash,Write,Edit,WebFetch,WebSearch"]
    r = subprocess.run(cmd, cwd=d, env=env, capture_output=True, text=True, encoding="utf-8", timeout=600)
    try:
        data = json.loads(r.stdout)
    except json.JSONDecodeError:
        data = {"is_error": True, "result": "", "stdout": r.stdout[-2000:], "stderr": r.stderr[-2000:]}
    data.update({"cond": cond, "prompt_id": pi, "rep": rep, "prompt": prompt})
    out.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    shutil.rmtree(d, ignore_errors=True)
    print(f"{out.name} cost={data.get('total_cost_usd')}", flush=True)
    return out


def summarize():
    rows, total_cost, models, errors = [], 0.0, set(), 0
    for f in sorted(RAW.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        if d.get("is_error") or not d.get("result"):
            errors += 1
            continue
        s, ev = score(d["result"])
        total_cost += d.get("total_cost_usd") or 0
        models |= set((d.get("modelUsage") or {}).keys())
        rows.append({"file": f.name, "cond": d["cond"], "prompt_id": d["prompt_id"], "rep": d["rep"], "score": s, "evidence": ev})
    (EVAL / "results" / "scores.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
    print("cond | re-suggested | rate | per prompt (p1..p5)")
    for c in CONDS:
        cr = [r for r in rows if r["cond"] == c]
        if not cr:
            continue
        n1 = sum(r["score"] for r in cr)
        per = [f"{sum(r['score'] for r in cr if r['prompt_id'] == p)}/{sum(1 for r in cr if r['prompt_id'] == p)}" for p in range(1, 6)]
        print(f"{c} | {n1}/{len(cr)} | {n1 / len(cr):.0%} | {' '.join(per)}")
    print(f"answers={len(rows)} errors={errors} cost_usd={total_cost:.2f} models={sorted(models)}")


def main():
    _selftest()
    ap = argparse.ArgumentParser()
    ap.add_argument("--conds", default="abc")
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--score-only", action="store_true")
    a = ap.parse_args()
    if not a.score_only:
        RAW.mkdir(parents=True, exist_ok=True)
        prompts = [p for p in (EVAL / "prompts.txt").read_text(encoding="utf-8").splitlines() if p.strip()]
        root = Path(tempfile.mkdtemp(prefix="dl-eval-runs-"))
        jobs = [(c, i, r, p, root) for c in a.conds for i, p in enumerate(prompts, 1) for r in range(1, a.k + 1)]
        with ThreadPoolExecutor(a.workers) as ex:
            list(ex.map(run_one, jobs))
        shutil.rmtree(root, ignore_errors=True)
    summarize()


if __name__ == "__main__":
    sys.exit(main())
