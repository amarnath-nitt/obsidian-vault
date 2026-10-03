# Design Parking Lot - Practice

## Key Concepts
- **Floors → spots → ticket lifecycle** — park (allocate + ticket), unpark (fee + release)
- **Strategy for pricing + allocation** — hourly/flat/peak pricing, nearest/smallest-fit allocation
- **Singleton facade + synchronized entry/exit** — no double-booking under concurrency

## Common Moves in LLD
1. **Spot compatibility by type** — bike/car/truck spot only fits its vehicle type
2. **Ticket as the session** — entry time + vehicle + spot; fee derived from duration
3. **Pluggable pricing** — `PricingStrategy` interface; hourly now, flat/peak later
4. **Thread-safe park/unpark** — synchronized facade (or per-floor locks for throughput)

---

## Problems (self-study)

> No AlgoMaster exercise — this is the canonical Easy machine-coding problem. Implement the solution note below, then extend it.

- [ ] [Design Parking Lot](solutions/Design-Parking-Lot.md) — Easy · Singleton, Factory, Strategy

---

## Extra Practice (self-study)

- [ ] Add `FlatPricing` for events and `PeakPricing` — no changes to `ParkingLot`
- [ ] Add `SpotAllocationStrategy` (nearest-to-entrance) — no changes to `Floor`
- [ ] Replace synchronized methods with per-floor locks + `ConcurrentHashMap` tickets

## Tips
- Say **"ticket is the session"** — entry + vehicle + spot; everything derives from it
- Compatibility check first (`isFreeFor`), then occupy — never occupy-then-check
- Finish the happy path (park → unpark → fee) before extensions

---

#lld #machine-coding #parking-lot #easy #practice
