# Design a Library Management System - Practice

## Key Concepts
- **Book vs copy** — one `Book` (metadata) has many `BookItem`s (barcodes); availability is per copy
- **Return triggers a cascade** — fine → copy status → waitlist promotion → notification, in one method
- **FIFO waitlist** — a `Deque` per book; the front waiter gets first refusal on the freed copy

## Common Moves in LLD
1. **Statuses own availability** — borrow scans for `AVAILABLE` copies; no separate counter to drift
2. **Fine is a pure function** — `fine(loan, returnedOn)`; free days, caps, and grace periods are strategies
3. **Renew = extend due date** — only when nobody waits; otherwise queue respect wins
4. **Limits checked per member** — a simple count before the loan, from the member's own list

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design a Library Management System](solutions/Design-Library-Management-System.md) — Medium · State, Strategy, Observer

---

## Extra Practice (self-study)

- [ ] Add copy-level hold shelf — a promoted copy waits N days for the notified member
- [ ] Add lost/damaged handling — status LOST + replacement fine
- [ ] Add search ranking — exact ISBN > title > author; Strategy again

## Tips
- Say **"metadata is shared, copies are the inventory"** — the first insight interviewers check
- Walk a return: fine, status, waitlist — all three in one breath
- Renew is the sneaky case — check the waitlist before extending

---

#lld #machine-coding #library #medium #practice