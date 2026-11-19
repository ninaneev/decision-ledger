# Keep the ledger in Notion

Same skill, same rules. The decisions live in a Notion database instead of markdown files. You need Claude Code with the Notion MCP connected.

## 1. Create the database (2 minutes)

New page in Notion, type `/database`, call it `Decision Ledger`, and add these columns:

| Column | Type | What goes in it |
|---|---|---|
| Decision | Title | The decision in one sentence |
| Why | Text | Why this one won, in your words |
| Discarded | Text | One line per option that lost: `option: why it lost` |
| Reopen only if | Text | What must happen before a discarded option comes back |
| Status | Select: open, active, superseded, reversed | Where it stands |
| Area | Select: pricing, product, marketing, tools, hiring, personal | One word you would search for |
| Revisit | Date | When to look at it again |
| Supersedes | Relation to this same database | The older decision this one replaces |
| Superseded by | Relation to this same database | The newer decision that replaced this one |
| Created | Created time | Filled in by Notion |

Already have a database you like? Keep it. Add the missing columns and map your names in step 2.

## 2. Find the data source URL

Ask Claude: "fetch my Decision Ledger database in Notion and tell me its data source URL". It starts with `collection://`.

## 3. Paste this into your CLAUDE.md

---

## Decision Ledger (Notion mode)

My decision ledger is a Notion database. Use the decision-ledger skill in Notion mode (§7), not files.

- Data source: collection://PASTE-YOUR-ID-HERE
- Column mapping:
  - Decision = "Decision"
  - Why = "Why"
  - Discarded = "Discarded"
  - Reopen only if = "Reopen only if"
  - Status = "Status" (open = "open", active = "active", superseded = "superseded", reversed = "reversed")
  - Area = "Area"
  - Revisit = "Revisit"
  - Supersedes = "Supersedes"
  - Superseded by = "Superseded by"
- Before recommending any strategy, tool, price, name, channel or plan, query the rows and check Discarded. If the idea was discarded, tell me the date, the reason and the reopen condition instead of suggesting it again.
- When I commit to something or drop an option, log a row, including what was discarded and why.
- Never delete a row. A change of mind is a new row that supersedes the old one.
- At the start of a session, tell me in one line if a Revisit date has passed.

---

Your columns have other names? Change only the right side of the mapping. Example, for a database where the title column is "Entry", the reasons live in "Evidence", and decisions share the table with other row types:

```
- Column mapping:
  - Decision = "Entry" (only rows where "Type" = "Decision")
  - Why = "Evidence"
  - Status = "Status" (open = "Open", active = "In progress", superseded = "Superseded")
- Every new row: "Type" = "Decision", "Gate" = "Proposed"
```

The last line is how you add your own defaults, for example an approval column that only you may change.

Unlike the file version, the index is not imported into every session. The guard runs a query instead, so keep the CLAUDE.md block: it is what makes the check happen.
