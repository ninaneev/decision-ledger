# Paste this into your CLAUDE.md

Copy everything between the lines into the CLAUDE.md of your project (or into ~/.claude/CLAUDE.md to use one ledger everywhere). It makes the guard run every session, even when you forget to ask.

---

## Decision Ledger

My decision index is imported below, so it is always in front of you:

@ledger/DECISIONS.md

- One file per decision lives in `ledger/`. Open a record when you need the full reason or the reopen condition.
- Never suggest anything that breaks a rule in the Invariants section.
- Before recommending any strategy, tool, price, name, channel, offer, hire or plan, check the Discarded column above. If the idea was discarded, tell me the date, the reason and the reopen condition instead of suggesting it again.
- Before any suggestion in an area that has an irreversible decision (Reversible = no), name that decision first.
- When I commit to something or drop an option, log it with the decision-ledger skill, including what was discarded and why.
- At the start of a session, tell me in one line if a Revisit date has passed.

---

Using one ledger for every project? Replace `ledger/` with the full path everywhere, including the import line, for example `@~/ledger/DECISIONS.md`.

Why the import line matters. An instruction to "check the ledger" gets skipped when a question looks simple. The import puts the index in front of the AI every session, so the check costs nothing and cannot be skipped. Keep the index short for the same reason. When it passes about 40 rows, the skill offers to move old superseded rows into `ledger/ARCHIVE.md`.

## Optional: enforce it with a SessionStart hook

The import above loads the index when the session starts. A hook goes one step further. Claude Code runs it at every session start, after `/clear` and after the context is compacted, and prints the index straight into Claude's context. Use it if you work in long sessions that get compacted.

Claude Code adds the plain text a SessionStart hook prints to the context Claude sees ([hooks reference](https://code.claude.com/docs/en/hooks)). This block prints your index:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume|clear|compact",
        "hooks": [
          {
            "type": "command",
            "command": "cat \"${CLAUDE_PROJECT_DIR}/ledger/DECISIONS.md\" 2>/dev/null || true"
          }
        ]
      }
    ]
  }
}
```

Where to put it

| You want | File |
|---|---|
| This project only (recommended) | `.claude/settings.json` in your project folder |
| Every project | `~/.claude/settings.json` |

No settings file there yet? Copy the ready one from this repo.

macOS or Linux, from the repo folder
```bash
mkdir -p /path/to/your-project/.claude && cp setup/session-start-hook.json /path/to/your-project/.claude/settings.json
```

Windows (PowerShell), from the repo folder
```powershell
New-Item -ItemType Directory -Force C:\path\to\your-project\.claude; Copy-Item setup\session-start-hook.json C:\path\to\your-project\.claude\settings.json
```

Already have a settings file? Do not overwrite it. Open it and add the `"SessionStart"` entry inside its existing `"hooks"` object (or add the whole `"hooks"` key if it has none).

Notes

- The command runs in bash. On Windows Claude Code uses Git Bash for hooks, and falls back to PowerShell when Git Bash is missing. Without Git Bash, add `"shell": "powershell"` next to `"type"` and use `Get-Content \"$env:CLAUDE_PROJECT_DIR\\ledger\\DECISIONS.md\" -ErrorAction SilentlyContinue` as the command.
- One ledger in your home folder? Use `cat \"$HOME/ledger/DECISIONS.md\"` instead.
- If the project has no ledger yet, the hook prints nothing and does no harm.
- Type `/hooks` in Claude Code to check that it is loaded.
