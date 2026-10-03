# KISS - Practice

## Key Concepts
- **The simplest design that satisfies the requirement wins**
- Complexity must **earn** its place
- Readable beats short — **obvious code is an asset**

## Common KISS Moves in LLD
1. **Flatten control flow** — early returns instead of nested conditionals
2. **Name the values** — constants and well-named locals replace magic numbers
3. **Inline single-use helpers** that only add a hop
4. **Delete redundant comparisons** — `== true`, `== false`, double negatives

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Refactor Delivery Fee](solutions/Refactor-Delivery-Fee.md) — AlgoMaster · easy · KISS — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/refactor-delivery-fee)
- [ ] [Refactor Login Guard](solutions/Refactor-Login-Guard.md) — AlgoMaster · easy · KISS — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/refactor-login-guard)

---

## Extra Practice (self-study)

- [ ] Rewrite one nested-ternary expression with early returns
- [ ] Delete a redundant `== true` comparison across your codebase

## Tips
- If you need a **comment** to explain a boolean, the boolean is too clever
- Behaviour must stay identical — KISS changes the *expression*, not the *rule*
- Pair with **YAGNI**: both remove accidental complexity
