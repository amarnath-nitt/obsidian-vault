# Law of Demeter - Practice

## Key Concepts
- **Talk to friends, not strangers** — no reaching through returned objects
- Fix chains with **delegating methods** on the object you already hold
- A **value object** can bundle exactly what a caller needs

## Common Demeter Moves in LLD
1. **Find the chains** — grep for `get...().get...().get...()`
2. **Add a delegating method** — `project.leadEmail()` instead of four hops
3. **Return a value object** — `order.shippingInfo()` instead of three separate chains
4. **Reduce coupling** — the caller no longer knows the internal graph

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Refactor Climate Console](solutions/Refactor-Climate-Console.md) — AlgoMaster · easy · Law of Demeter — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/refactor-climate-console)

### Medium
- [ ] [Refactor Project Dashboard](solutions/Refactor-Project-Dashboard.md) — AlgoMaster · medium · Law of Demeter — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/refactor-project-dashboard)
- [ ] [Refactor Shipping Desk](solutions/Refactor-Shipping-Desk.md) — AlgoMaster · medium · Law of Demeter — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/refactor-shipping-desk)

---

## Extra Practice (self-study)

- [ ] Grep your codebase for three-deep getter chains and break them
- [ ] Replace a chain with a single delegating method on the object you hold

## Tips
- The interview answer is **"I'd add a delegating method so the caller talks to one object"**
- Demeter violations are also **coupling** violations — say both
- A delegating method often fixes **encapsulation** problems too
