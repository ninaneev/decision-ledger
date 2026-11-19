# Decisions

> Fictional example. Little Oven is a made up neighbourhood bakery that delivers bread and pastries by bike.

Newest first. One row per decision. Status: open, active, superseded, reversed. Reversible: yes or no.

## Invariants

Rules that must never be broken. The AI names them before any suggestion that touches them.

| Since | Rule | Why |
|---|---|---|
| 2026-03-02 | Bread goes out the same day it is baked | Fresh bread at the door is the whole promise |
| 2026-03-02 | No customer addresses outside our own list | Neighbours trust us with their door codes |

## Decisions

| Date | Decision | Discarded | Reversible | Status | Revisit | Record |
|---|---|---|---|---|---|---|
| 2026-06-03 | 3 year lease on the corner kitchen | shared kitchen across town, home kitchen | no | active | 2027-06-03 | [record](2026-06-03-kitchen-lease.md) |
| 2026-05-12 | Building lobbies only, 90 days | food delivery apps, paid local ads | yes | active | 2026-08-12 | [record](2026-05-12-one-channel.md) |
| 2026-04-20 | Weekly bread box €18, delivery included | single orders only, daily box | yes | active | 2026-07-20 | [record](2026-04-20-bread-box.md) |
| 2026-03-02 | €3 delivery fee per order | free delivery over €25, free delivery, loyalty card | yes | superseded | 2026-06-01 | [record](2026-03-02-pricing-model.md) |
