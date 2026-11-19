# Install in other AI tools

The skill file follows the open [Agent Skills](https://agentskills.io) format (a folder with a `SKILL.md` inside), so the same file works in every tool below. Each path here was checked against the tool's own docs on 19 November 2026. The link is in each section.

Every tool needs two things.

1. **The skill**, so the AI knows how to seed, log, guard, recall and revisit.
2. **An always on guard**, a few lines in the tool's rules file, so the AI checks the ledger before recommending anything. A skill alone only loads when the AI thinks it is relevant, and the guard must run every time.

You also need the `ledger/` folder in your project, as in step 2 of the README.

## One folder for most tools

Codex CLI, Gemini CLI, Cursor, OpenClaw and Windsurf all read skills from `~/.agents/skills/`. Install once there and all of them see it.

macOS or Linux, from the repo folder
```bash
mkdir -p ~/.agents/skills/decision-ledger && cp skills/decision-ledger/SKILL.md ~/.agents/skills/decision-ledger/
```

Windows (PowerShell), from the repo folder
```powershell
New-Item -ItemType Directory -Force $HOME\.agents\skills\decision-ledger; Copy-Item skills\decision-ledger\SKILL.md $HOME\.agents\skills\decision-ledger\
```

Cline uses its own folder, see below.

## The guard block

Paste this into the rules file named for your tool below.

```markdown
## Decision Ledger

My decisions live in ledger/DECISIONS.md (an Invariants section and an index table). One file per decision sits next to it.

- Read ledger/DECISIONS.md at the start of every session and before recommending any strategy, tool, price, name, channel, offer, hire or plan.
- Never suggest anything that breaks an invariant.
- If an idea is in the Discarded column, tell me the date, the reason and the reopen condition instead of suggesting it again.
- Before any suggestion in an area with an irreversible decision (Reversible = no), name that decision first.
- When I commit to something or drop an option, log it with the decision-ledger skill.
- Tell me in one line if a Revisit date has passed.
```

## Per tool

| Tool | Skill folder | Where the guard block goes | Docs checked |
|---|---|---|---|
| OpenAI Codex CLI | `~/.agents/skills/` or `.agents/skills/` in the repo | `AGENTS.md` in the project, or `~/.codex/AGENTS.md` for all projects | [Skills](https://developers.openai.com/codex/skills), [AGENTS.md](https://developers.openai.com/codex/guides/agents-md) |
| Gemini CLI | `~/.gemini/skills/` or `~/.agents/skills/` | `GEMINI.md` in the project, or `~/.gemini/GEMINI.md` | [Agent Skills](https://geminicli.com/docs/cli/skills/), [GEMINI.md](https://geminicli.com/docs/cli/gemini-md/) |
| Cursor | `~/.cursor/skills/` or `~/.agents/skills/` (Cursor also reads `~/.claude/skills/`) | `AGENTS.md` in the project, or a rule file, see below | [Skills](https://cursor.com/docs/skills), [Rules](https://cursor.com/docs/context/rules) |
| Cline | `~/.cline/skills/` (Windows `C:\Users\YOU\.cline\skills\`) or `.cline/skills/` in the project | a file in `.clinerules/` in the project, or in `Documents/Cline/Rules` for all projects | [Skills](https://docs.cline.bot/features/skills), [Rules](https://docs.cline.bot/features/cline-rules) |
| Windsurf (now Devin Local) | `~/.agents/skills/`, or `.windsurf/skills/` in the project | `AGENTS.md` in the project, or a rule file in `.windsurf/rules/` | [Customizations](https://docs.windsurf.com/windsurf/cascade/skills) |
| OpenClaw | `~/.agents/skills/`, `<workspace>/skills/`, or `~/.openclaw/skills/` for all agents | the workspace `AGENTS.md` | [Skills](https://docs.openclaw.ai/tools/skills), [Workspace](https://docs.openclaw.ai/concepts/agent-workspace) |

### OpenAI Codex CLI

Codex reads `AGENTS.md` from `~/.codex/` and from every folder between the repo root and where you start it. Paste the guard block into the project's `AGENTS.md`.

### Gemini CLI

Gemini CLI asks you to approve a skill the first time it activates it. Paste the guard block into `GEMINI.md`. Google notes that for unpaid and Google One users, Gemini CLI was replaced by Antigravity CLI in June 2026; this section covers Gemini CLI only.

### Cursor

Project rules must be `.mdc` files. Create `.cursor/rules/decision-ledger.mdc` with this header and the guard block under it.

```markdown
---
description: Decision Ledger guard
alwaysApply: true
---
```

Or paste the guard block into `AGENTS.md` at the project root, which Cursor also reads.

### Cline

Copy the skill folder to `~/.cline/skills/decision-ledger/`. The folder name must match the `name` in the skill, which is `decision-ledger`.

macOS or Linux
```bash
mkdir -p ~/.cline/skills/decision-ledger && cp skills/decision-ledger/SKILL.md ~/.cline/skills/decision-ledger/
```

Windows (PowerShell)
```powershell
New-Item -ItemType Directory -Force $HOME\.cline\skills\decision-ledger; Copy-Item skills\decision-ledger\SKILL.md $HOME\.cline\skills\decision-ledger\
```

Then save the guard block as `.clinerules/decision-ledger.md` in your project. Cline loads every file in `.clinerules/` as an always on rule.

Using Cline's memory bank? Keep it. The ledger is a separate, narrower thing. It holds only decisions and what was rejected.

### Windsurf (now Devin Local)

The Windsurf docs now live under the Devin Local name. It reads `~/.agents/skills/` globally and `.windsurf/skills/` in the project. `AGENTS.md` at the project root is always on, so the guard block goes there.

### OpenClaw

Either copy the folder to `~/.agents/skills/` as above, or install it with OpenClaw's own command from the repo folder.

```bash
openclaw skills install ./skills/decision-ledger --global
```

`--global` puts it in `~/.openclaw/skills/` for every local agent. Leave it out to install into the current workspace only.

OpenClaw works inside its workspace folder (by default `~/.openclaw/workspace`), so put the `ledger/` folder there. Add the guard block to the workspace `AGENTS.md`, which OpenClaw loads at the start of every session ([Agent workspace](https://docs.openclaw.ai/concepts/agent-workspace)).

## Not covered

Tools not listed here may still work if they read Agent Skills or an `AGENTS.md` file. They are left out because their install path was not checked.
