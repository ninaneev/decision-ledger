# Where your ledger lives

Same skill, same rules, four places to keep the rows. You pick one by naming it in your `CLAUDE.md` (or your tool's instructions). If you name nothing, it uses markdown.

| Backend | What you need | Who it suits | Setup effort |
|---|---|---|---|
| Markdown (default) | Nothing. A `ledger/` folder | Anyone using Claude Code or another agent tool. Works offline, fits in git | 2 minutes |
| Notion | The Notion connector (MCP) added to your AI tool once | People who already run their business in Notion | 5 minutes |
| Airtable | The Airtable connector (MCP) added to your AI tool once | People who like filtered views and forms | 5 minutes |
| Spreadsheet (CSV, Excel or Google Sheets) | A `.csv` or `.xlsx` file. A Google Sheets connector is optional | People who live in spreadsheets, and chat tool users who want rows they can sort | 3 minutes |

All four use the same fields.

| Field | What goes in it |
|---|---|
| Date | When it was decided |
| Decision | The decision in one sentence (the title) |
| Why | Why this one won, in your words |
| Discarded | One line per option that lost, `option: why it lost` |
| Reopen only if | What must happen before a discarded option comes back |
| Reversible | yes or no |
| Status | open, active, superseded, reversed |
| Area | One word you would search for |
| Revisit | When to look at it again |
| Supersedes | The older decision this one replaces |
| Superseded by | The newer decision that replaced this one |
| Type | decision or invariant (a rule you never break) |

## Markdown

This is the default. Follow the README install. Your `CLAUDE.md` block is in [`CLAUDE-snippet.md`](CLAUDE-snippet.md).

## Notion

You connect Notion to your AI tool once (in Claude Code, Claude.ai or ChatGPT, through its connectors or MCP settings). No share link is needed. Then pick one of two paths.

**Let the skill create the database.** Make an empty page in Notion where the ledger should live, for example "Decision Ledger". Paste this into your `CLAUDE.md`, then start a session and say "set up my ledger".

```markdown
## Decision Ledger (Notion)

My decision ledger lives in Notion. Use the decision-ledger skill in Notion mode.

- Parent page: "Decision Ledger" (create the database there if it does not exist yet)
- Data source: (empty until the skill creates it, then paste the collection:// id here)
- Before recommending any strategy, tool, price, name, channel, offer, hire or plan, query the rows and check invariant rows, Discarded and Reversible.
- When I commit to something or drop an option, log a row, including what was discarded and why.
- Never delete a row. A change of mind is a new row that supersedes the old one.
- At the start of a session, tell me in one line if a Revisit date has passed.
```

The skill creates the database with the fields above and gives you its `collection://` id. Paste that id into the Data source line, so it never creates a second one.

**Use a database you already have.** Follow [`notion.md`](notion.md). It has the column mapping block, for databases whose columns have other names.

## Airtable

Connect Airtable to your AI tool once, through its connectors or MCP settings. Then pick one of two paths.

**Let the skill create the table.** Have a base ready (an empty one is fine). Paste this into your `CLAUDE.md`, then say "set up my ledger".

```markdown
## Decision Ledger (Airtable)

My decision ledger lives in Airtable. Use the decision-ledger skill in Airtable mode.

- Base: "My Business" (create a "Decision Ledger" table there if it does not exist yet)
- Base id: (empty until the skill creates the table)
- Table id: (empty until the skill creates the table)
- Before recommending any strategy, tool, price, name, channel, offer, hire or plan, list the records and check invariant records, Discarded and Reversible.
- When I commit to something or drop an option, add a record, including what was discarded and why.
- Never delete a record. A change of mind is a new record that supersedes the old one.
- At the start of a session, tell me in one line if a Revisit date has passed.
```

The skill gives you the base id (starts with `app`) and table id (starts with `tbl`). Paste both in.

**Use a table you already have.** Fill in the ids and add a mapping, changing only the right side.

```markdown
- Base id: appXXXXXXXXXXXXXX
- Table id: tblXXXXXXXXXXXXXX
- Column mapping:
  - Decision = "Name"
  - Why = "Notes"
  - Discarded = "Discarded"
  - Reopen only if = "Reopen only if"
  - Reversible = "Reversible"
  - Status = "Status" (active = "Active", superseded = "Replaced")
  - Revisit = "Revisit"
```

Fields you do not have yet? Add them in Airtable first, with the same types as in the table above.

## Spreadsheet

One sheet with this header row. Copy it as is.

```
Date,Decision,Why,Discarded,Reopen only if,Reversible,Status,Area,Revisit,Supersedes,Superseded by,Type
```

Save it as `ledger/decisions.csv` in your project (or `.xlsx` if you prefer Excel).

**Claude Code.** Paste this into your `CLAUDE.md`.

```markdown
## Decision Ledger (spreadsheet)

My decision ledger is the spreadsheet ledger/decisions.csv. Use the decision-ledger skill in spreadsheet mode.

- Read it at the start of every session and before recommending any strategy, tool, price, name, channel, offer, hire or plan. Check rows with Type = invariant first, then Discarded and Reversible.
- When I commit to something or drop an option, add a row at the top, under the header.
- Never delete a row. A change of mind is a new row; set the old row's Status to superseded.
```

Claude Code edits a CSV directly. An `.xlsx` file needs a spreadsheet library such as openpyxl on your machine. Without it, keep the ledger as CSV and open it in Excel when you want to read it.

**Claude.ai, ChatGPT or other chat tools.** Upload the sheet as project knowledge, paste the instructions from [`claude-ai-and-chatgpt.md`](claude-ai-and-chatgpt.md), and add this line to them.

```
My ledger is a spreadsheet, not DECISIONS.md. When you log a decision, give me one row with the values in header order, separated by tabs, so I can paste it into the sheet.
```

**Google Sheets.** Optional. If your AI tool has a Google Sheets or Google Drive connector, add "My ledger is the Google Sheet called Decision Ledger" to the block above and it reads and adds rows through the connector. Without a connector it works like the chat tools above, with rows to paste.
