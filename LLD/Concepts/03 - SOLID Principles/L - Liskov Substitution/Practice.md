# Liskov Substitution - Practice

## Key Concepts
- **Substitutability** — a subtype must drop in wherever the base type is used
- **Behavioural subtyping** — same contract, same meaning, no surprises
- Fix a broken hierarchy with a **better abstraction**, not a bigger base class

## Common LSP Moves in LLD
1. **Detect the thrower** — a subtype that throws on an inherited method is the classic smell
2. **Split the hierarchy** — separate types instead of forcing a shared mutable base
3. **Prefer immutable siblings** — `Rectangle` and `Square` as separate final types
4. **Re-check contracts** — preconditions must not strengthen, postconditions must not weaken

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Repair a Payment Contract](solutions/Repair-Payment-Contract.md) — AlgoMaster · easy · LSP — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/repair-payment-contract)

### Medium
- [ ] [Repair a Document Contract](solutions/Repair-Document-Contract.md) — AlgoMaster · medium · LSP — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/repair-document-contract)

---

## Extra Practice (self-study)

- [ ] Find a subtype that throws on an inherited method and redesign it
- [ ] Rewrite a `Square extends Rectangle` hierarchy without inheritance

## Tips
- Say **"behavioural subtyping"** — it signals you know LSP is about contracts, not syntax
- When LSP breaks, ask whether the shared base class should exist at all
- LSP is the reason **composition over inheritance** is the default advice
