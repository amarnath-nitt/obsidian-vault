# Dependency - Practice

## Key Concepts
- **Temporary "uses-a"** — used during a call, never stored
- The **weakest** of the "uses" relationships: lowest coupling
- Constructor injection turns an internal dependency into an injected one (**DIP**)

## Common Dependency Moves in LLD
1. **Pass it in** — `preview(message, formatter)` instead of a field
2. **Keep collaborators stateless** where possible, so they're easy to reuse
3. **Promote deliberately** — only store it if you genuinely need it across calls
4. **Draw the dashed arrow** `-->` on the class diagram

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Design Alert Preview](solutions/Design-Alert-Preview.md) — AlgoMaster · easy · Dependency — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-alert-preview)

---

## Extra Practice (self-study)

- [ ] Find a field that's only used in one method and turn it into a parameter
- [ ] Draw dependency vs association arrows for three classes in your project

## Tips
- Say **"temporary, passed as a parameter, not stored"** — that's the whole definition
- Dependency is the **lowest-coupling** option — reach for it first
- Ranking them (dependency → association → aggregation → composition) is a great interview answer
