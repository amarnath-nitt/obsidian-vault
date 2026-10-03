# Design Hotel Management System - Practice

## Key Concepts
- **Two lifecycles, one room** — reservation state (booked → in-house → out) and room status (available → occupied → cleaning) move together but are not the same thing
- **Overlap ledger per room** — availability = no non-cancelled overlapping reservation *and* status is not MAINTENANCE
- **Checkout fans out** — billing reads the pricing strategy; housekeeping is an Observer that flips the room to CLEANING

## Common Moves in LLD
1. **Search = type filter + overlap filter + status filter** — cheap predicates composed in one query
2. **Check-in performs two transitions** — reservation to CHECKED_IN *and* room to OCCUPIED, atomically
3. **Bill = sum of nightly rates** — per-day pricing lets weekends differ from weekdays
4. **Cleaning is a state, not a flag** — a cleaning room is not bookable until turned AVAILABLE

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design Hotel Management System](solutions/Design-Hotel-Management-System.md) — Medium · State, Strategy, Observer

---

## Extra Practice (self-study)

- [ ] Add maintenance scheduling — block a room for a date range, not forever
- [ ] Add overbooking policy — allow 105% bookings with a walk list
- [ ] Add room upgrades — reassign a reservation to a higher type at check-in

## Tips
- Say **"reservation state and room status are different machines"** — that is the insight interviewers listen for
- Weekend pricing is a per-day function — resist "multiply by nights" shortcuts
- Housekeeping as an Observer keeps the front desk single-purpose

---

#lld #machine-coding #hotel #medium #practice