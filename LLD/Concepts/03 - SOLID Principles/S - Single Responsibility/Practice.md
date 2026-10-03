# Single Responsibility - Practice

## Key Concepts
- **One reason to change** — a class has a single axis of change
- **Split by responsibility**, not by layer
- Keep **domain rules** with the domain objects; keep I/O at the edges

## Common SRP Moves in LLD
1. **Extract persistence** — a model that calls SQL gets a repository
2. **Extract presentation** — a model that formats output gets a printer/serializer
3. **Extract validation** — a model that both stores and validates gets a validator
4. **Keep orchestration thin** — a service coordinates, it doesn't compute

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Refactor Order Processing](solutions/Refactor-Order-Processing.md) — AlgoMaster · easy · SRP — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/refactor-order-processing)

### Medium
- [ ] [Simplify a Counter Panel](solutions/Simplify-Counter-Panel.md) — AlgoMaster · medium · SRP — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/simplify-counter-panel)

### Hard
- [ ] [Refactor Member Signup](solutions/Refactor-Member-Signup.md) — AlgoMaster · hard · SRP — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/refactor-member-signup)

---

## Extra Practice (self-study)

- [ ] Find a class you can describe with "and" and split it
- [ ] Move all persistence out of your domain objects into repositories

## Tips
- Name the **responsibility** when you justify a split in an interview
- If two changes always land together, they belong in the same class
- SRP is the class-level version of **Separation of Concerns**
