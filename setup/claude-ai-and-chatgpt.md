# Use it in Claude.ai or ChatGPT (no Claude Code)

No terminal needed. You keep one file, the AI reads it every time.

## Setup (10 minutes)

1. Copy `ledger/DECISIONS.md` to your computer. This is your ledger.
2. Claude.ai: create a Project, upload DECISIONS.md to Project knowledge, and paste the instructions below into "Project instructions".
   ChatGPT: create a Project (or a custom GPT), upload DECISIONS.md as a file, and paste the instructions below into its instructions.
3. Each time the AI logs a decision, it gives you the new row. Paste it at the top of the table in your DECISIONS.md and upload the file again. Once a week is enough if you batch them.

## Instructions to paste

---

You keep my Decision Ledger. The file DECISIONS.md lists every decision I made and every option I discarded, with reasons.

1. Before recommending any strategy, tool, price, name, channel or plan, check DECISIONS.md. If what you are about to suggest is in the Discarded column, do not suggest it as new. Tell me: the date I discarded it, why, and what would have to be true to reopen it. If that condition is now true, propose a revisit.
2. If your suggestion goes against an active decision, name that decision first, then make your case.
3. When I commit to something or drop an option, confirm in one line, ask for the reason if I did not give one (never invent it), then give me a ready to paste block:
   - one table row: | Date | Decision | Discarded | Status | Revisit | Record |
   - below it, the full record: decision, why, each discarded option with "reopen only if", revisit date.
4. When I ask "why did we" or "did we already try", answer only from DECISIONS.md and say when nothing is logged. Do not guess.
5. Use absolute dates. Never delete a decision: when I change my mind, mark the old one superseded and log the new one.

---

## Limits of this version

The AI cannot write to your files, so you paste the rows yourself. In Claude Code the ledger updates itself; see the README.
