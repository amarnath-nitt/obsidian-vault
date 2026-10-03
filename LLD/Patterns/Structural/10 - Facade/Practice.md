# Facade Pattern - Practice

## Key Concepts
- **Facade** — one simplified interface over many subsystem classes
- **Subsystem** — the real workers, unchanged and still accessible
- **Delegation** — the facade orchestrates, it does not implement
- **Coarse-grained API** — one method hides a multi-step workflow
- **Coupling reduction** — clients depend on the facade, not the subsystem

## Common Facade Use Cases
1. **Home theater** — `watchMovie()` orchestrates projector/amp/dvd
2. **E-commerce checkout** — inventory + payment + shipping + notify
3. **Computer boot** — CPU + memory + disk sequence
4. **Library setup** — one `init()` hides configuration
5. **Compiler** — parse → analyse → optimise → emit behind `compile()`

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Control a Home Theater](solutions/Control-Home-Theater.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/control-home-theater)
- [ ] [Start a Computer](solutions/Start-Computer.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/start-computer)

---

## Extra Practice (self-study)

- [ ] Order checkout facade (inventory + payment + shipping + notify) — [reference code](solutions/Facade-Implementations.md)
- [ ] Media conversion facade (decode → convert → encode) — [reference code](solutions/Facade-Implementations.md)
- [ ] Layered facades (presentation → app → domain) — [reference code](solutions/Facade-Implementations.md)

---

## Tips
- **Delegate, never implement** — the facade contains orchestration, not rules
- Keep it **thin** and **coarse-grained** (one method = one workflow)
- Leave the **subsystem classes public** for power users
- Say it in interviews: "Facade simplifies N interfaces; Adapter converts one"