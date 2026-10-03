# Inheritance - Practice

## Key Concepts
- **Reuse via "is-a"** — `extends` for shared implementation, `implements` for shared contract
- **Favour composition** when it isn't a genuine is-a
- Every subtype must honour the base contract (**LSP**)

## Common Inheritance Moves in LLD
1. **Abstract base** for genuinely shared behaviour (`Vehicle`, `Notification`)
2. **Interface first** when only the contract is shared
3. **Convert to composition** when inheritance was only for code reuse
4. **Keep hierarchies shallow** — two levels is usually plenty

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Design Payment Methods](solutions/Design-Payment-Methods.md) — AlgoMaster · easy · Inheritance — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-payment-methods)

### Medium
- [ ] [Design Subscription Plans](solutions/Design-Subscription-Plans.md) — AlgoMaster · medium · Inheritance — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-subscription-plans)

---

## Extra Practice (self-study)

- [ ] Convert an inheritance hierarchy that should be composition
- [ ] Ask "is-a or has-a?" for every `extends` in your codebase

## Tips
- **Say the is-a sentence aloud**: "a Square *is a* Rectangle" — if it sounds wrong, don't inherit
- Inheritance brings **LSP** obligations — mention them
- Composition is the default advice; inheritance must earn its place
