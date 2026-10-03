# Encapsulation - Practice

## Key Concepts
- **Hide state, expose behaviour** — private fields, meaningful methods
- Invariants are enforced at **one choke point**
- Returning the internal mutable collection breaks encapsulation too

## Common Encapsulation Moves in LLD
1. **Privatise fields** and add methods that validate before mutating
2. **Return copies / unmodifiable views** — `List.copyOf(items)`
3. **Move logic in** — the class owns the rule, not the caller
4. **Remove setter bloat** — expose only the operations the domain needs

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Design Bank Account](solutions/Design-Bank-Account.md) — AlgoMaster · easy · Encapsulation — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-bank-account)
- [ ] [Design Temperature Sensor](solutions/Design-Temperature-Sensor.md) — AlgoMaster · easy · Encapsulation — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-temperature-sensor)

### Medium
- [ ] [Design Shopping Cart](solutions/Design-Shopping-Cart.md) — AlgoMaster · medium · Encapsulation — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-shopping-cart)

---

## Extra Practice (self-study)

- [ ] Find a public mutable field and make its class own the invariant
- [ ] Replace a getter that hands out an internal list with an unmodifiable copy

## Tips
- Name the **invariant** you're protecting — that's the interview answer
- Encapsulation is the mechanism behind **SRP** at the field level
- Getters/setters alone are not encapsulation; **guarding the change** is
