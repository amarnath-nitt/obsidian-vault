# Design Airline Management System - Practice

## Key Concepts
- **Holds are leases, not locks** — a hold is a booking in PENDING with `heldUntil`; time releases it, not a user
- **One transition table** — PENDING → CONFIRMED (payment) → CANCELLED (refund); expiry is also PENDING → CANCELLED
- **Strategies at the edges** — fare and refund math are pure functions; the core only moves states and seat statuses

## Common Moves in LLD
1. **`Clock` injected, not `System.currentTimeMillis()` inline** — tests advance time to expire holds deterministically
2. **Sweep or lazy check** — expire holds by a periodic sweep *and* a stale-check on confirm (belt and braces)
3. **Seat status mirrors booking state** — hold → HELD, confirm → BOOKED, cancel/expire → FREE, always together
4. **Refund tiers** — full refund > 48h, half ≤ 48h, none after departure — as a `RefundPolicy`, not ifs

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design Airline Management System](solutions/Design-Airline-Management-System.md) — Medium · State, Strategy, Observer

---

## Extra Practice (self-study)

- [ ] Add multi-city itineraries — one booking, several flight legs, all-or-nothing
- [ ] Add a waitlist — confirmed flights overflow into a FIFO list
- [ ] Add fare classes per seat — pricing becomes (class, demand) with a strategy chain

## Tips
- Say **"a hold is a booking with an expiry"** — it collapses two subsystems into one state machine
- Always demo the expired-hold path — interviewers love the seat that frees itself
- Confirm must re-check expiry *and* seat status — never trust state from minutes ago

---

#lld #machine-coding #airline #medium #practice