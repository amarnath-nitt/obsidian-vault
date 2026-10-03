# YAGNI - Practice

## Key Concepts
- **Build what is required now** — not what a future requirement might want
- Speculative code is a **permanent cost** for a benefit that may never arrive
- Leave **seams** (interfaces where a real variation exists), don't pre-build the machinery

## Common YAGNI Moves in LLD
1. **Delete speculative abstractions** — one-implementation interfaces, unused factories
2. **Remove unused configuration** — no options nobody sets
3. **Collapse layers** — drop wrappers with a single caller
4. **Delete dead code** — version control is the archive

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Refactor Avatar Store](solutions/Refactor-Avatar-Store.md) — AlgoMaster · easy · YAGNI — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/refactor-avatar-store)
- [ ] [Refactor Password Checker](solutions/Refactor-Password-Checker.md) — AlgoMaster · easy · YAGNI — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/refactor-password-checker)

---

## Extra Practice (self-study)

- [ ] Delete a speculative abstraction nobody uses
- [ ] Count the config options in your app that are never set

## Tips
- YAGNI and **OCP** are in tension — say so in an interview; it shows judgement
- If you can't name the requirement that needs it, **don't build it**
- "Plug-in ready" with zero plug-ins is YAGNI's classic smell
