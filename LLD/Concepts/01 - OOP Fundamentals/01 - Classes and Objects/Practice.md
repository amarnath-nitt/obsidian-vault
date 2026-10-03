# Classes & Objects - Practice

## Key Concepts
- **Class** = blueprint (fields + methods); **Object** = runtime instance
- Design by **state, behaviour, invariants**
- Keep behaviour **with** the data it operates on

## Common Moves in LLD
1. **Name the domain nouns** — `Car`, `Book`, `StepTracker`, not `Manager`
2. **Model the state you must remember** — nothing more
3. **Guard invariants in the class itself** — reject bad input at the boundary
4. **Use a `record`** for immutable values (`Money`, `Coordinates`)

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Design Car Class](solutions/Design-Car-Class.md) — AlgoMaster · easy · Classes and Objects — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-car-class)
- [ ] [Design Library Book Class](solutions/Design-Library-Book.md) — AlgoMaster · easy · Classes and Objects — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-library-book)

### Medium
- [ ] [Design Step Tracker Class](solutions/Design-Step-Tracker.md) — AlgoMaster · medium · Classes and Objects — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-step-tracker)

---

## Extra Practice (self-study)

- [ ] Model a small `ParkingLot` with `Ticket` and `Vehicle` classes
- [ ] Rewrite an anemic data class so its behaviour lives with its state

## Tips
- In the interview, **draw the classes first**, then the methods
- Say the **invariant** out loud — it shows you design for correctness
- If you can't name the class with a domain noun, model it again
