# Abstraction - Practice

## Key Concepts
- **Expose what, hide how** — callers depend on a small stable surface
- Distinct from **encapsulation**: abstraction is the interface, encapsulation protects the body
- Leaky abstractions expose internals — keep them out of the contract

## Common Abstraction Moves in LLD
1. **Define the outcome** (`export(events)`) before the mechanism (CSV, JSON, S3)
2. **One abstraction, many implementations** — swap without touching callers
3. **Facade a subsystem** behind a single readable API
4. **Reject leaky signatures** — no `getArrayList()`, no raw driver types

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Design Shape Calculator](solutions/Design-Shape-Calculator.md) — AlgoMaster · easy · Abstraction — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-shape-calculator)

### Medium
- [ ] [Design Event Exporter](solutions/Design-Event-Exporter.md) — AlgoMaster · medium · Abstraction — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-event-exporter)

---

## Extra Practice (self-study)

- [ ] Describe an interface purely in terms of outcomes, with no implementation nouns
- [ ] Find a leaky abstraction in your codebase and hide the detail

## Tips
- Say **"abstraction vs encapsulation"** — distinguishing them is a strong signal
- Abstraction is the mechanism behind **OCP** and **DIP**
- If a caller must know *how*, the abstraction isn't finished
