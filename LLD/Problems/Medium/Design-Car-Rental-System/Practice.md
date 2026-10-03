# Design Car Rental System - Practice

## Key Concepts
- **Half-open ranges** — `[start, end)` overlap is `start < other.end && other.start < end`; shared range type with Hotel
- **State guards on the reservation** — pickup/completion/cancel each check the state they expect, nothing else
- **The ledger decides availability** — the car has no `isRented` flag; search overlays active reservations

## Common Moves in LLD
1. **Ledger, not flags** — one list of reservations; availability = "no overlapping non-cancelled entry"
2. **Search returns candidates** — filters by type + branch first, overlap second
3. **Quote before reserve** — pricing is a pure function of (type, days); no state touched
4. **Cancel releases inventory** — a cancelled reservation stops blocking; completed too

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design Car Rental System](solutions/Design-Car-Rental-System.md) — Medium · State, Strategy

---

## Extra Practice (self-study)

- [ ] Add branch capacity — N cars per branch with waitlist on overflow
- [ ] Add late-return penalty — pricing strategy variant on completed rentals
- [ ] Add one-active-rental-per-license rule — check the ledger on reserve

## Tips
- Say **"availability is an overlap query, not a flag"** — that is the whole design
- Pick one date convention up front (we use end-exclusive) and stay consistent
- Cancel semantics first — it is where half the bugs live

---

#lld #machine-coding #car-rental #medium #practice