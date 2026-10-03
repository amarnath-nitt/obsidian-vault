# Design Ride-Sharing Service like Uber - Practice

## Key Concepts
- **Matching is atomic** — find + assign under one lock; otherwise the same driver wins two requests
- **Two state machines move together** — trip (REQUESTED→…) and driver (AVAILABLE→ON_TRIP→AVAILABLE) flip in pairs
- **Surge wraps base** — a `SurgeFare` decorating `BaseFare`; pricing policy changes without touching trips

## Common Moves in LLD
1. **Filter, then rank** — available drivers only; `min` by distance; throw when none
2. **Cancel does bookkeeping** — free the driver if assigned; nothing else to unwind pre-pickup
3. **Distance is the dispatcher's currency** — a pluggable metric (`Location.distanceTo`) keeps matching honest
4. **Fare computed at completion** — km is known then; pricing never guesses

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design Ride-Sharing Service like Uber](solutions/Design-Ride-Sharing-Service.md) — Hard · State, Strategy, Observer

---

## Extra Practice (self-study)

- [ ] Add driver acceptance with timeout — fall back to the next nearest on expiry
- [ ] Add zone-based surge — per-zone multipliers over the base fare
- [ ] Add driver ratings — average over completed trips; matching strategy could prefer 4.8+

## Tips
- Say **"dispatch = filter + rank + assign, one critical section"** — concurrency answered in one breath
- Show the cancel path — unfinished trips are where the states leak
- Surge as a wrapper, not an if — pricing stays composable

---

#lld #machine-coding #uber #hard #practice