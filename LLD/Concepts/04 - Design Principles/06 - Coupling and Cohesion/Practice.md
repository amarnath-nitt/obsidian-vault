# Coupling & Cohesion - Practice

## Key Concepts
- **Low coupling between** modules — depend on interfaces, not concretions
- **High cohesion within** a module — one class, one job
- The two usually improve **together** when you introduce an abstraction

## Common Coupling/Cohesion Moves in LLD
1. **Extract an interface** where a `switch` selects concrete implementations
2. **Register implementations** — a map beats an `if/else` chain (also OCP)
3. **Split the god class** — routing, formatting and delivery become separate classes
4. **Move cross-cutting logic** (retry, logging) to one place instead of copying it

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Refactor Alert Router](solutions/Refactor-Alert-Router.md) — AlgoMaster · medium (premium) · Coupling & Cohesion — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/refactor-alert-router)
- [ ] [Refactor Payment Terminal](solutions/Refactor-Payment-Terminal.md) — AlgoMaster · medium (premium) · Coupling & Cohesion — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/refactor-payment-terminal)

---

## Extra Practice (self-study)

- [ ] Count how many classes you must edit to add one new type — that's your coupling score
- [ ] Move retry/logging out of N call sites into one place

## Tips
- Say both halves: **"high cohesion inside, low coupling between"**
- A `switch` over concrete types is simultaneously a **coupling and OCP** problem
- Test it with a **stub** behind the interface — if that's easy, coupling is low
