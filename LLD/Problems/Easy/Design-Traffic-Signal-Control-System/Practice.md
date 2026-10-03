# Design Traffic Signal Control System - Practice

## Key Concepts
- **Phases own the cycle** — each phase sets its colours, counts down, hands off to the next
- **All-red clearance between greens** — the safety invariant; never skip it
- **Overrides are states** — emergency hold and night flashing suspend/resume the cycle

## Common Moves in LLD
1. **Controller holds signals, phases hold rules** — colours mutate only in `onEnter`
2. **Inject the tick** — timer in prod, manual `tick()` in tests
3. **Pedestrian as a flag** — consumed by the next phase, not acted on mid-green
4. **Emergency captures resume point** — hold remembers where to return

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design Traffic Signal Control System](solutions/Design-Traffic-Signal-Control-System.md) — Easy · State

---

## Extra Practice (self-study)

- [ ] Add protected left-turn arrow — a sub-phase inside each green
- [ ] Add sensor mode — green extends while cars detected, up to a max
- [ ] Add coordinated corridor — two controllers phase-locked with an offset

## Tips
- Say **"exactly one green, always through all-red"** — the invariant is the design
- Draw the 5-phase cycle before coding — it is the whole answer
- Night/emergency are states, not flags — say why out loud

---

#lld #machine-coding #traffic-signal #easy #practice
