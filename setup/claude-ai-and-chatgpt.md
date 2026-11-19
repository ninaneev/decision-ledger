# Use it in Claude.ai or ChatGPT (no Claude Code)

No terminal needed. You keep one file, the AI reads it every time.

## Setup (10 minutes)

1. Copy `ledger/DECISIONS.md` to your computer. This one file is your whole ledger: the table at the top, and the full record of each decision below it (the AI needs the reasons and the reopen conditions, not just the table).
2. Claude.ai: create a Project, upload DECISIONS.md to Project knowledge, and paste the instructions below into "Project instructions".
   ChatGPT: create a Project (or a custom GPT), upload DECISIONS.md as a file, and paste the instructions below into its instructions.
3. Each time the AI logs a decision, it gives you a new row and a full record. Paste the row at the top of the table and the record at the bottom of the file, then upload the file again. Once a week is enough if you batch them.
4. First time: start a chat in the Project and paste the seed prompt below. It fills your ledger with your last 5 real decisions, which is when the guard starts paying off.

## Instructions to paste

---

You keep my Decision Ledger. The file DECISIONS.md has a table of every decision I made and every option I discarded, and below it the full record of each one with reasons and reopen conditions.

1. Before recommending any strategy, tool, price, name, channel or plan, check the table and the records in DECISIONS.md. If what you are about to suggest is in the Discarded column, do not suggest it as new. Tell me: the date I discarded it, why, and what would have to be true to reopen it. If that condition is now true, propose a revisit.
2. If your suggestion goes against an active decision, name that decision first, then make your case.
3. When I commit to something or drop an option, confirm in one line, ask for any missing reason (why this one won, why each other option lost; never invent one), then give me two ready to paste blocks:
   - one table row: | Date | Decision | Discarded | Status | Revisit | Record |
   - the full record, starting with a heading of the decision: date, status, decision, why, each discarded option with "reopen only if", revisit date.
4. When I ask "why did we" or "did we already try", answer only from DECISIONS.md and say when nothing is logged. Do not guess.
5. Use absolute dates. Never delete a decision: when I change my mind, mark the old one superseded and log the new one.

---

## Seed prompt (paste once)

---

My ledger is empty. Interview me, one question at a time, about my 5 biggest decisions of the last 3 months: offer and pricing, customers, marketing channels, tools, and one personal one. For each ask: what I chose, why that one, what else was on the table, why each lost, and what would make me reconsider. Then give me the 5 table rows and the 5 full records, ready to paste into DECISIONS.md.

---

## Limits of this version

The AI cannot write to your files, so you paste the rows yourself. In Claude Code the ledger updates itself; see the README.
