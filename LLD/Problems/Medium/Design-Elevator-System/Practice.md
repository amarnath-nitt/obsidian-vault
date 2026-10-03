# Design an Elevator System - Practice

## Key Concepts
- **LOOK, not FCFS** — each car keeps up-stops ascending and down-stops descending; it finishes the sweep before reversing
- **Dispatch is a Strategy** — nearest-car with a busy penalty; scan/zone policies plug in behind one interface
- **Time is a tick** — `step()` moves one floor per call; the simulation is deterministic and testable

## Common Moves in LLD
1. **Two stop sets per car** — ascending `TreeSet` for up, descending for down; `request(f)` inserts, `step()` polls
2. **Idle cars win ties** — dispatch cost = distance (+ penalty when busy); no ghost assignments pile up
3. **Doors as part of a step** — boarding happens at the stop the car polls; keep it inside the sweep
4. **Operator ops isolated** — out-of-service removes a car from dispatch; the sweep never changes

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design an Elevator System](solutions/Design-Elevator-System.md) — Medium · State, Strategy, Singleton

---

## Extra Practice (self-study)

- [ ] Add door-open states — doors stay open N ticks before the sweep resumes
- [ ] Add a capacity limit — full cars skip new boardings
- [ ] Add emergency mode — every car returns to ground in one sweep

## Tips
- Say **"LOOK with two sorted sets"** — that one phrase is the whole scheduling answer
- Tick first, dispatch second — interviewers poke at "two requests to the same car at once"
- Ask N cars / M floors before coding — the bounds shape the design

---

#lld #machine-coding #elevator #medium #practice