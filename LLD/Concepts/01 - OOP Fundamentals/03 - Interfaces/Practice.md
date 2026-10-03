# Interfaces - Practice

## Key Concepts
- **Declare what, hide how** — callers depend on the contract
- The gateway to **polymorphism**, **DIP** and **ISP**
- Keep interfaces **small and role-based**

## Common Interface Moves in LLD
1. **Extract a contract** where a `switch` picks concrete classes
2. **Inject through the interface** so implementations are swappable
3. **Fake it in tests** — an in-memory implementation behind the same interface
4. **Use `default` methods** sparingly for genuinely optional capabilities

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Design Plugin Editor](solutions/Design-Plugin-Editor.md) — AlgoMaster · easy · Interfaces — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-plugin-editor)

### Medium
- [ ] [Design Input Validator](solutions/Design-Input-Validator.md) — AlgoMaster · medium · Interfaces — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-input-validator)

---

## Extra Practice (self-study)

- [ ] Define an interface and two implementations for a swappable behaviour
- [ ] Program a method against an interface, then swap the implementation

## Tips
- **Name the contract as a verb-role**: `Validatable`, `Chargeable`, `Renderable`
- If you can't name two real implementations, question the interface (YAGNI)
- Interfaces are the mechanism behind **OCP** — say that in an interview
