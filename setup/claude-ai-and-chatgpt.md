# Use it in Claude.ai or ChatGPT (no install)

No terminal needed. You keep one file, the AI reads it every time.

In chat tools the ledger is one file, `DECISIONS.md`. The table sits at the top and the full record of each decision goes below it, because the AI needs the reasons and the reopen conditions, not just the table. Prefer Notion, Airtable or a spreadsheet? Read [`storage.md`](storage.md) first.

## Pick your tool

| Tool | Where the instructions go | Where the ledger goes |
|---|---|---|
| Claude.ai Projects | Project instructions | Project knowledge |
| ChatGPT Projects | Project settings, instructions | Project files |
| ChatGPT custom GPT | Configure, Instructions | Configure, Knowledge |

### Claude.ai Projects

1. Download [`ledger/DECISIONS.md`](../ledger/DECISIONS.md) from this repo.
2. Create a Project, upload DECISIONS.md to Project knowledge, and paste the instructions below into Project instructions.

### ChatGPT Projects

Checked against OpenAI's help article [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt).

1. Download [`ledger/DECISIONS.md`](../ledger/DECISIONS.md) from this repo.
2. Select New project in the sidebar and give it a name.
3. Add DECISIONS.md with Add files.
4. Open the project menu (•••), choose Project settings and paste the instructions below.

### ChatGPT custom GPT

Checked against OpenAI's help article [Creating a GPT](https://help.openai.com/en/articles/8554397-creating-a-gpt). Read this first. OpenAI is retiring custom GPTs. Personal accounts (Free, Go, Plus, Pro) can no longer create new ones, and standard retirement is scheduled for 11 December 2026. Use a ChatGPT Project unless you already have a GPT or your workspace still allows them.

1. Open chatgpt.com/gpts, select Create, then the Configure tab.
2. Paste the instructions below into Instructions.
3. Upload DECISIONS.md under Knowledge.

## Every week

Each time the AI logs a decision, it gives you a new row and a full record. Paste the row at the top of the Decisions table and the record at the bottom of the file, then upload the file again. Once a week is enough if you batch them.

## Instructions to paste

---

You keep my Decision Ledger. The file DECISIONS.md has a short Invariants section (rules I never break), a table of every decision I made and every option I discarded, and below it the full record of each one with reasons and reopen conditions.

1. Never suggest anything that breaks an invariant. If I ask for it, name the invariant and ask if I want to change the rule.
2. Before recommending any strategy, tool, price, name, channel, offer, hire or plan, check the table and the records in DECISIONS.md. If what you are about to suggest is in the Discarded column, do not suggest it as new. Tell me the date I discarded it, why, and what would have to be true to reopen it. If that condition is now true, propose a revisit.
3. If your suggestion goes against an active decision, name that decision first, then make your case. Decisions marked Reversible = no are fixed constraints, so name them before any suggestion in the same area.
4. When I commit to something or drop an option, confirm in one line, ask for any missing reason (why this one won, why each other option lost; never invent one) and whether it can be undone, then give me two ready to paste blocks.
   - One table row: | Date | Decision | Discarded | Reversible | Status | Revisit | Record |
   - The full record, starting with a heading of the decision, then date, status, reversible, decision, why, each discarded option with "reopen only if", and the revisit date.
5. When I ask "why did we" or "did we already try", answer only from DECISIONS.md and say when nothing is logged. Do not guess.
6. Use absolute dates. Never delete a decision. When I change my mind, mark the old one superseded and log the new one.
7. When the table passes about 40 rows, suggest I move superseded rows to a separate ARCHIVE.md file.

---

## Seed prompt (paste once)

---

My ledger is empty. Interview me, one question at a time, about my 5 biggest decisions of the last 3 months. Cover offer and pricing, customers, marketing channels, tools or hires, and one personal one. For each ask what I chose, why that one, what else was on the table, why each lost, what would make me reconsider, and whether it can be undone cheaply. Then ask once for any rules I never break. Give me the invariant rows, the 5 table rows and the 5 full records, ready to paste into DECISIONS.md.

---

## Limits of this version

The AI cannot write to your files, so you paste the rows yourself. In Claude Code the ledger updates itself. See the README.
