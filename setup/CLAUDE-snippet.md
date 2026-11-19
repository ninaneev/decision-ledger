# Paste this into your CLAUDE.md

Copy everything between the lines into the CLAUDE.md of your project (or into ~/.claude/CLAUDE.md to use one ledger everywhere). It makes the guard run every session, even when you forget to ask.

---

## Decision Ledger

My decision index is imported below, so it is always in front of you:

@ledger/DECISIONS.md

- One file per decision lives in `ledger/`. Open a record when you need the full reason or the reopen condition.
- Before recommending any strategy, tool, price, name, channel or plan, check the Discarded column above. If the idea was discarded, tell me the date, the reason and the reopen condition instead of suggesting it again.
- When I commit to something or drop an option, log it with the decision-ledger skill, including what was discarded and why.
- At the start of a session, tell me in one line if a Revisit date has passed.

---

Using one ledger for every project? Replace `ledger/` with the full path everywhere, including the import line, for example `@~/ledger/DECISIONS.md`.

Why the import line matters: an instruction to "check the ledger" gets skipped when a question looks simple. The import puts the index in front of the AI every session, so the check costs nothing and cannot be skipped. Keep the index short for the same reason.
