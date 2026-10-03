# Design Movie Ticket Booking System - Practice

## Key Concepts
- **Locks are data** — `lockedBy` + `lockedUntil` maps; `sweep(now)` releases everything expired, lazily or on tick
- **Two records, one truth** — a booking that outlives its lock expires; confirm validates through the lock manager
- **Pricing reads three facts** — category, show start, now — and returns money; no state touched

## Common Moves in LLD
1. **Lock first, then price** — the booking starts as PENDING holding a lock token; money comes at confirm time
2. **All-or-nothing locks** — validate every seat before registering any lock entry (no partial holds)
3. **Sold is separate from locked** — `confirm` moves seats from locked → sold; cancellation only frees locks
4. **Clock injected** — `Clock.fixed` expires locks deterministically in demos and tests

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design Movie Ticket Booking System](solutions/Design-Movie-Ticket-Booking-System.md) — Hard · State, Strategy

---

## Extra Practice (self-study)

- [ ] Add friend shows — consecutive-seat preference with an adjacency check
- [ ] Add refund tiers — full refund > 2h before show, none after
- [ ] Add dynamic pricing — weekday matinee vs opening-night surge, another strategy

## Tips
- Say **"the lock manager is the concurrency story; the booking is just its record"**
- Show the sweep: expired lock → seats free → booking EXPIRED, all without a user
- Distinguish cancel (frees locks) from refund (money policy) — different concerns

---

#lld #machine-coding #movie-tickets #hard #practice