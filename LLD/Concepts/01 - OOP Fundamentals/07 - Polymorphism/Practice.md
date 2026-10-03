# Polymorphism - Practice

## Key Concepts
- **One call site, many behaviours** — dispatch instead of branching
- **Runtime** polymorphism (overriding) is what powers OCP and Strategy
- Call sites must depend on an **abstraction**, never a concrete type

## Common Polymorphism Moves in LLD
1. **Kill the `switch`** — one implementation per case, dispatched
2. **Extract a strategy** — behaviour swapped at runtime
3. **Eliminate `instanceof` chains** — push the branch into the objects
4. **Reuse a base method** via `super` where behaviour is genuinely shared

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Design Notification Center](solutions/Design-Notification-Center.md) — AlgoMaster · easy · Polymorphism — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-notification-center)

### Medium
- [ ] [Design Discount Calculator](solutions/Design-Discount-Calculator-OOP.md) — AlgoMaster · medium · Polymorphism — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-discount-calculator)

---

## Extra Practice (self-study)

- [ ] Replace an `if/else` or `switch` chain with polymorphic dispatch
- [ ] Convert one runtime `instanceof` check into a virtual method call

## Tips
- Name **overriding vs overloading** — it's a common screening question
- Polymorphism is the mechanism; **OCP** is the benefit — say both
- A growing `switch` on the same value is polymorphism waiting to happen
