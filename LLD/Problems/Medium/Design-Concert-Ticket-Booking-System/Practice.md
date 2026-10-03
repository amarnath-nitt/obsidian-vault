# Design a Concert Ticket Booking System - Practice

## Key Concepts
- **Holds expire by themselves** — `heldUntil` turns a stuck cart into freed inventory with zero human effort
- **Two clocks, one truth** — pay re-checks expiry *and* seat status; the sweep is just hygiene
- **Tier pricing as a strategy** — early-bird vs surge is a function of (tier, days to show)

## Common Moves in LLD
1. **Validate-all-then-mark** — every seat is checked FREE before any flips to HELD (no partial holds)
2. **Same transaction, two writes** — booking state and seat status always move together
3. **Sold-out is derived** — after each payment, check the tier for remaining FREE/HELD seats and notify
4. **Clock injected** — `Clock.fixed` in tests advances time to expire holds deterministically

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design a Concert Ticket Booking System](solutions/Design-Concert-Ticket-Booking-System.md) — Medium · State, Strategy, Observer

---

## Extra Practice (self-study)

- [ ] Add general-admission zones — quantity-based, no seat numbers (different inventory model)
- [ ] Add per-customer limits — max N seats per show
- [ ] Add a queue — virtual waiting room before high-demand on-sales

## Tips
- Say **"holds are leases with a deadline; payment is the purchase"** — clarity beats extra classes
- The expiry path is the interview — rehearse it before the happy path
- Concurrency: one lock around the hold-check for a study answer; per-seat locks when asked to scale

---

#lld #machine-coding #concert #medium #practice