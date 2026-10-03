# Enums - Practice

## Key Concepts
- **Closed set of constants** with optional per-value **behaviour**
- Replaces magic strings with compiler-checked types
- An exhaustive `switch` over an enum is checked by the compiler

## Common Enum Moves in LLD
1. **Replace a status string** — `OrderStatus.PENDING` instead of `"PENDING"`
2. **Move behaviour onto the constant** — `OPEN.canClose()` reads well
3. **Switch exhaustively** — adding a constant forces you to handle it
4. **Use `UNKNOWN`** instead of `null` for "unrecognised"

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Design Traffic Light](solutions/Design-Traffic-Light.md) — AlgoMaster · easy · Enums — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-traffic-light)

### Medium
- [ ] [Design Order Tracker](solutions/Design-Order-Tracker.md) — AlgoMaster · medium · Enums — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-order-tracker)

---

## Extra Practice (self-study)

- [ ] Convert a magic-string status into an enum with behaviour
- [ ] Add a new constant and watch the compiler demand you handle it

## Tips
- Enum + behaviour is a **mini State/Strategy** — a nice interview talking point
- Say **"closed set"** — it's the reason an enum beats a boolean or a string
- Never let `null` stand in for a known state
