---
name: decision-ledger
description: Use when a decision is made or an option is dropped in conversation ("let's go with", "we decided", "drop that", "not doing X", "park it", "never do X"), when the user types /decision-ledger, asks "why did we", "what did we decide about", "did we already try", "what did we discard", or before recommending any strategy, tool, price, name, channel, offer, hire or plan. Keeps a ledger of business decisions AND the options that were discarded, with reasons, and stops the AI from re-proposing what was already rejected.
---

# Decision Ledger

The ledger lives in `ledger/` at the project root (or the folder named in
CLAUDE.md or the user's instructions). `ledger/DECISIONS.md` is the index.
Every decision has one file. If the instructions name another backend
(Notion, Airtable or a spreadsheet), follow §7 for storage. Every other rule
stays the same.

A memory that only keeps what you chose is half a memory. The other half is
what you said no to and why. Without it, the AI suggests the same rejected idea
every few weeks and you argue the same argument again. This skill keeps both.

## 0. Seed: when the ledger is empty or the user says "seed"

An empty ledger protects nothing. On first use, offer a 10 minute interview.

1. Ask, one question at a time, for the decisions of the last 3 months in
   these areas. Offer and pricing, customers, marketing channels, tools,
   hires, and one personal one. For each ask what they chose, why that one,
   what else was on the table, why each lost, what would make them
   reconsider, and whether it can be undone cheaply.
2. Ask once for rules that must never be broken (invariants). Log each one in
   the Invariants section, see §5.
3. Stop at 5 decisions or when the user says enough.
4. Log each one as in §2, with the real date if they remember it, or the
   first day of the month they name. Mark guessed dates `(approx)`.
5. End with "Your ledger has N decisions, M discarded options and K
   invariants. From now on I check it before I suggest anything."

## 1. Guard: before you recommend anything

Before you recommend a strategy, tool, price, name, channel, offer, hire,
feature or plan:

1. Read `ledger/DECISIONS.md`. It is short. Scan the Invariants section, then
   the Decision and Discarded columns, for anything close to what you are
   about to suggest.
2. Invariants come first. Never suggest something that breaks one. If the user
   asks for it, name the invariant and ask whether they want to change the
   rule. Changing it is a decision and gets logged.
3. If your suggestion matches a discarded option, do not present it as new.
   Say it plainly, quoting the record. For example "You discarded food
   delivery apps on 2026-05-12 because they take 30% of each order
   (ledger/2026-05-12-one-channel.md). They come back only if a second bakery
   opens within 1 km. That has not happened, so I'm not suggesting them."
4. If the reopen condition HAS been met, say so and propose a revisit instead
   of silently reversing the decision.
5. If your suggestion contradicts an active decision, name the decision first,
   then make your case. Never route around a decision quietly.
6. Irreversible decisions (`Reversible: no`) are stricter. Before ANY
   suggestion that touches the same area, name every irreversible decision
   in it, even when you think your idea fits. Treat them as fixed constraints
   for the plan you propose.

## 2. Log: when a decision is made

A decision is made when the user commits to one path ("let's do X", "go with
B", "approved", "kill it", "park that"). Discarding counts as a decision.

1. Confirm in one line what you are about to log. The decision, why it won,
   the options that lost and why each lost, and whether it is reversible.
   The Why of the decision is its own reason (what makes this path right),
   never a copy of the discard reasons. Ask once for any missing reason and
   never invent one. If the user still gives none, write `reason not given`.
   If they do not say whether it can be undone, ask once. If still unclear,
   write `Reversible: yes`.
2. Create `ledger/YYYY-MM-DD-<slug>.md` from the format in §5.
3. Add one row at the TOP of the table in `ledger/DECISIONS.md`.
4. Tell the user in one line, "Logged: <decision>. Discarded: <options>."
5. If the table now has more than about 40 rows, suggest once that you move
   the `superseded` and `reversed` rows into `ledger/ARCHIVE.md` (same table
   format, newest first). Move them only after the user says yes. Their
   record files stay where they are.

Log in the user's words. Short beats complete. A record nobody rereads is
worthless; one that takes 20 seconds to read gets used.

## 3. Recall: when asked

- "Why did we ...?" → open the record, answer with the Why and the date.
- "What did we discard?" / "did we already try ...?" → search the Discarded
  column, then the files, then `ledger/ARCHIVE.md` if it exists. Answer with
  date, reason and reopen condition.
- "What's still open?" → list rows with status `open` or a Revisit date that
  has passed.

Always cite the record. If nothing is in the ledger, say "nothing logged
about that" and do not guess from general knowledge.

## 4. Revisit and change your mind

Decisions are never deleted or edited to look like they were always right.

- At the start of a session, if any Revisit date in the index has passed,
  mention it once in one line.
- When a decision changes, set the old record to `superseded`, add
  `Superseded by: <new file>` to it, log the new decision normally, and put
  `Supersedes: <old file>` in the new one. The trail is the point.
- When an option comes back from the discard pile, record which reopen
  condition was met.

## 5. Record format

```markdown
# <Decision in one sentence>

Date: 2026-03-02
Status: active
Area: pricing
Reversible: yes
Revisit: 2026-06-01 or when we pass 100 orders a week

## Decision
What we are doing, in one or two sentences.

## Why
The reason in the user's words. What we knew at the time.

## Discarded
- <Option>: <why it lost>. Reopen only if: <condition>.
- <Option>: <why it lost>. Reopen only if: <condition>.

## Supersedes
(none)
```

Status is one of `open` (still deciding), `active`, `superseded`, `reversed`.
`Area` is one word the user would search for (pricing, hiring, product,
marketing, tools, offer, operations, personal). `Reversible` is `yes` or `no`. Use `no`
when undoing it would cost real money, time or trust (a lease, a hire, a
public promise, a signed contract).

Invariants are rules that must never be broken, such as "we never sell
customer data". They have no Discarded list and no Revisit date. Keep them in
the Invariants section of the index (§6), one row each. A record file is
optional; write one only when the reason needs more than one line.

## 6. Index format

`ledger/DECISIONS.md`, newest first, one row per record:

```markdown
## Invariants

| Since | Rule | Why |
|---|---|---|
| 2026-03-02 | Bread goes out the same day it is baked | It is the whole promise |

## Decisions

| Date | Decision | Discarded | Reversible | Status | Revisit | Record |
|---|---|---|---|---|---|---|
| 2026-03-02 | €3 delivery fee per order | free delivery, loyalty card | yes | active | 2026-06-01 | [record](2026-03-02-pricing-model.md) |
```

Keep the Discarded column to short names. The guard scans it every time, so
it must stay readable at a glance.

## Rules

- Absolute dates only. "Last week" means nothing in two months.
- One decision per file. Two decisions in one conversation = two files.
- Never log something the user did not commit to. Ideas are not decisions.
- Never paraphrase a reason into something stronger than what was said.
- The ledger beats your general knowledge. If the user decided against best
  practice, respect it and mention the record, do not re-argue it every time.

## 7. Storage modes

The user names the backend in CLAUDE.md or in their instructions. If nothing
is named, use markdown. Every rule above holds in every mode. Only where the
rows live changes. Each backend uses the same fields. Date, Decision, Why,
Discarded, Reopen only if, Reversible, Status, Area, Revisit, Supersedes,
Superseded by, Type (decision or invariant).

If any read fails in any mode, say so and do not recommend as if the ledger
were empty.

### Markdown (default)

Files in `ledger/` as described in §2 to §6.

### Notion

Uses the Notion MCP tools.

- Create. If the instructions name a parent page but no database, and no
  database called "Decision Ledger" exists under it, create one there with
  the fields above (Decision as title, Status, Area, Reversible and Type as
  selects, Revisit and Date as dates, Supersedes and Superseded by as
  relations to the same database). Tell the user its link and its data
  source id, and ask them to paste the id into their instructions so you
  never create a second one.
- Map. If the instructions give a data source (`collection://...`) and a
  column mapping, use the user's column names and option values exactly as
  mapped. Add any defaults the block sets, such as an approval column.
- Guard. Fetch the data source once per session for the schema, then query
  the rows (only decision and invariant rows if the mapping names a type
  filter). Scan Decision, Discarded, Reopen only if and Reversible.
- Log. Create one row with the decision as the title, Why, Discarded (one
  line per option, `<option>: <why it lost>`), Reopen only if, Reversible,
  Status, Revisit and Area. Read the row back and tell the user in one line,
  with its link.
- Recall. Search or query the rows by keyword in Decision and Discarded, and
  cite the row link and its date.
- Supersede. Create the new row first with Supersedes pointing to the old
  one. Then on the old row change only Status and Superseded by. Never delete
  a row, never rewrite its text.
- Revisit. At session start, query rows whose Revisit date has passed and
  mention them once in one line.

### Airtable

Uses the Airtable MCP tools, with the same create or map choice.

- Create. If the instructions name a base but no table, and no table called
  "Decision Ledger" exists in it, create one with the fields above (Decision
  as the primary field, selects for Status, Area, Reversible and Type, dates
  for Date and Revisit, links to the same table for Supersedes and
  Superseded by). Tell the user the base id and table id and ask them to
  paste both into their instructions.
- Map. If the instructions give a base id, a table id and a column mapping,
  use them exactly. Never guess ids; list them with the MCP tools.
- Guard, log, recall, supersede and revisit work as in Notion mode, with
  records instead of rows.

### Spreadsheet (CSV, XLSX or Google Sheets)

One sheet, one row per decision or invariant, with the fields above as the
header row.

- Claude Code with a `.csv` file. Read and edit it directly. Add new rows at
  the top, under the header. Quote any cell that has a comma in it.
- Claude Code with a `.xlsx` file. Edit it only if you can run a spreadsheet
  library such as openpyxl. If you cannot, say so and suggest saving it as CSV.
- Chat tools (Claude.ai, ChatGPT). You cannot write the file. When you log,
  hand the user one ready row with the values in header order, separated by
  tabs, so it pastes into Excel or Google Sheets as separate cells.
- Google Sheets through a connector. Optional. If the user's tool has a
  Google Sheets or Drive connector, use it to read and append rows. If not,
  work as in chat tools.

Setup steps and ready blocks for every backend live in `setup/storage.md` in
the repo.
