# Install runbook for AI agents

This file is for an AI coding agent (Claude Code, Codex, Gemini CLI, Cursor, Cline and similar). A person hands it to you with a line like the one below. Follow the steps in order. Do not skip the checks.

```
Install the Decision Ledger for me. Follow INSTALL-AGENT.md from https://github.com/ninaneev/decision-ledger
```

## Rules for you, the agent

- Never overwrite an existing file. If a target file exists, show the user what you would add and ask before changing it.
- Never touch `.env` or any file that holds keys.
- Ask at most three questions, all in step 1. Then work without asking.
- At the end, print the checklist from step 7 with each line ticked or explained.

## Step 1. Ask the user three things

1. Which project folder should the ledger protect? (Default: the folder you are running in.)
2. One ledger for this project, or one shared ledger in the home folder for every project? (Default: this project.)
3. Where should it live? Markdown files, Notion, Airtable or a spreadsheet? (Default: markdown.)

Call the answers PROJECT, SCOPE and BACKEND.

## Step 2. Get the files

If this repo is not on disk yet, clone it into a temporary folder.

```bash
git clone --depth 1 https://github.com/ninaneev/decision-ledger.git "$TMPDIR/decision-ledger"
```

On Windows PowerShell use `$env:TEMP\decision-ledger` as the target. Call that folder REPO.

## Step 3. Install the skill

Work out which tool you are, then copy `REPO/skills/decision-ledger/SKILL.md` into a folder named `decision-ledger` inside the skill folder for that tool.

| You are | Skill folder |
|---|---|
| Claude Code | `~/.claude/skills/` |
| Cline | `~/.cline/skills/` |
| Codex CLI, Gemini CLI, Cursor, OpenClaw, Windsurf | `~/.agents/skills/` |

Check. The file must sit at `<skill folder>/decision-ledger/SKILL.md`. If it sits directly in the skill folder it will not load.

## Step 4. Add the ledger (markdown only)

Skip this step if BACKEND is Notion, Airtable or a spreadsheet.

- SCOPE this project. Copy `REPO/ledger/` to `PROJECT/ledger/`.
- SCOPE home folder. Copy `REPO/ledger/` to `~/ledger/`.

If a `ledger/` folder already exists there, do not copy. Tell the user and use the existing one.

## Step 5. Add the always on guard

Pick the rules file for your tool. Create it if it does not exist. If it exists, append, never replace.

| You are | Rules file | Block to append |
|---|---|---|
| Claude Code | `PROJECT/CLAUDE.md` (or `~/.claude/CLAUDE.md` for SCOPE home folder) | the block in `REPO/setup/CLAUDE-snippet.md` |
| Codex CLI, Windsurf, OpenClaw | `PROJECT/AGENTS.md` | the guard block in `REPO/setup/other-tools.md` |
| Gemini CLI | `PROJECT/GEMINI.md` | the guard block in `REPO/setup/other-tools.md` |
| Cursor | `PROJECT/.cursor/rules/decision-ledger.mdc` | the `.mdc` header and guard block in `REPO/setup/other-tools.md` |
| Cline | `PROJECT/.clinerules/decision-ledger.md` | the guard block in `REPO/setup/other-tools.md` |

For SCOPE home folder, replace every `ledger/` in the block with the full path, for example `~/ledger/`.

For BACKEND Notion, Airtable or spreadsheet, append the matching block from `REPO/setup/storage.md` instead. Leave placeholders such as the parent page name for the user to fill in, and tell them which line to fill.

## Step 6. Optional hook (Claude Code and markdown only)

Ask nothing. Tell the user the hook exists and point to the "Optional" section of `REPO/setup/CLAUDE-snippet.md`. If `PROJECT/.claude/settings.json` does not exist, offer to copy `REPO/setup/session-start-hook.json` there. Never merge it into an existing settings file without showing the user the result first.

## Step 7. Check and report

Print this list, ticked or with the reason it is not.

```
[ ] Skill file at <skill folder>/decision-ledger/SKILL.md
[ ] Ledger at <path>/DECISIONS.md, with the Invariants and Decisions headers (markdown only)
[ ] Guard block in <rules file>
[ ] Hook (optional): installed / offered / skipped
[ ] Next step for the user: start a new session in PROJECT and type "/decision-ledger seed" (or "seed my decision ledger")
```

The ledger starts empty. Tell the user the seed interview is what makes it useful, and that it takes about 10 minutes.
