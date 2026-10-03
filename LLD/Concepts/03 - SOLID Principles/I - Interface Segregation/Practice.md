# Interface Segregation - Practice

## Key Concepts
- **Clients depend only on what they use** — no fat interfaces
- Split by **client/role**, not by implementer
- Small interfaces also make **DIP** easier (easier to satisfy, easier to fake in tests)

## Common ISP Moves in LLD
1. **Find the stubbers** — any `UnsupportedOperationException` means the interface is too fat
2. **Extract role interfaces** — `Readable`, `Writable`, `Chargeable`
3. **Let classes implement several small roles** instead of one big one
4. **Push optional operations down** to a separate extension interface

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Refactor Plugin Lifecycle Hooks](solutions/Refactor-Plugin-Lifecycle-Hooks.md) — AlgoMaster · easy · ISP — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/refactor-plugin-lifecycle-hooks)

### Medium
- [ ] [Refactor an Office Device Interface](solutions/Refactor-Office-Device-Interface.md) — AlgoMaster · medium · ISP — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/refactor-office-device-interface)
- [ ] [Narrow Report Dependencies](solutions/Narrow-Report-Dependencies.md) — AlgoMaster · medium · ISP — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/narrow-report-dependencies)

---

## Extra Practice (self-study)

- [ ] Split one fat interface in your codebase into role interfaces
- [ ] Count the `UnsupportedOperationException`s in a project — each is an ISP smell

## Tips
- The giveaway is an implementer that **throws** for methods it never supports
- Say **"role interfaces"** — it shows you split by client, not at random
- ISP and **DIP** often land together: a narrow interface is easy to depend on
