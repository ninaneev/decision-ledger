---
name: decision-ledger
description: Use when a decision is made or an option is dropped in conversation ("let's go with", "we decided", "drop that", "not doing X", "park it"), when the user types /decision-ledger, asks "why did we", "what did we decide about", "did we already try", "what did we discard", or before recommending any strategy, tool, price, name, channel or plan. Keeps a ledger of decisions AND the options that were discarded, with reasons, and stops the AI from re-proposing what was already rejected.
---

# Decision Ledger

The ledger lives in `ledger/` at the project root (or the folder named in
CLAUDE.md). `ledger/DECISIONS.md` is the index. Every decision has one file.

A memory that only keeps what you chose is half a memory. The other half is
what you said no to and why. Without it, the AI suggests the same rejected idea
every few weeks and you argue the same argument again. This skill keeps both.

## 0. Seed: when the ledger is empty or the user says "seed"

An empty ledger protects nothing. On first use, offer a 10 minute interview:

1. Ask, one question at a time, for the decisions of the last 3 months in
   these areas: offer and pricing, customers, marketing channels, tools,
   and one personal one. For each: what did you choose, what else was on
   the table, why did it lose, what would make you reconsider.
2. Stop at 5 decisions or when the user says enough.
3. Log each one as in §2, with the real date if they remember it, or the
   first day of the month they name. Mark guessed dates `(approx)`.
4. End with: "Your ledger has N decisions and M discarded options. From now
   on I check it before I suggest anything."

## 1. Guard: before you recommend anything

Before you recommend a strategy, tool, price, name, channel, hire, feature or
plan:

1. Read `ledger/DECISIONS.md`. It is short. Scan the Decision and Discarded
   columns for anything close to what you are about to suggest.
2. If your suggestion matches a discarded option, do not present it as new.
   Say it plainly, quoting the record:
   "You discarded this on 2026-03-02 because pricing per seat scared off solo
   buyers (ledger/2026-03-02-pricing-model.md). It can come back only if:
   a team of 5 or more asks for it. That has not happened, so I'm not
   suggesting it."
3. If the reopen condition HAS been met, say so and propose a revisit instead
   of silently reversing the decision.
4. If your suggestion contradicts an active decision, name the decision first,
   then make your case. Never route around a decision quietly.

## 2. Log: when a decision is made

A decision is made when the user commits to one path ("let's do X", "go with
B", "approved", "kill it", "park that"). Discarding counts as a decision.

1. Confirm in one line what you are about to log: the decision, the options
   that lost, and the reason for each. Ask only if a reason is missing; never
   invent one. If the user gives no reason, write `reason not given`.
2. Create `ledger/YYYY-MM-DD-<slug>.md` from the format in §5.
3. Add one row at the TOP of the table in `ledger/DECISIONS.md`.
4. Tell the user in one line: "Logged: <decision>. Discarded: <options>."

Log in the user's words. Short beats complete. A record nobody rereads is
worthless; one that takes 20 seconds to read gets used.

## 3. Recall: when asked

- "Why did we ...?" → open the record, answer with the Why and the date.
- "What did we discard?" / "did we already try ...?" → search the Discarded
  column, then the files. Answer with date, reason and reopen condition.
- "What's still open?" → list rows with status `open` or a Revisit date that
  has passed.

Always cite the record file. If nothing is in the ledger, say "nothing logged
about that" and do not guess from general knowledge.

## 4. Revisit and change your mind

Decisions are never deleted or edited to look like they were always right.

- At the start of a session, if any Revisit date in the index has passed,
  mention it once in one line.
- When a decision changes: set the old record to `superseded`, add
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
Revisit: 2026-06-01 or when we pass 50 customers

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

Status is one of: `open` (still deciding), `active`, `superseded`, `reversed`.
`Area` is one word the user would search for (pricing, hiring, product,
marketing, tools, offer, personal).

## 6. Index format

`ledger/DECISIONS.md`, newest first, one row per record:

```markdown
| Date | Decision | Discarded | Status | Revisit | Record |
|---|---|---|---|---|---|
| 2026-03-02 | Flat €49/month | per seat, free tier | active | 2026-06-01 | [record](2026-03-02-pricing-model.md) |
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
