# Deadlock - Practice

## Key Concepts
- **Circular wait** — every thread holds something and wants something someone else holds
- **Coffman's four conditions** — break any one and deadlock is impossible
- Prevention in practice: **global lock ordering** or **try-lock + back off**

## Common Moves in LLD
1. **Order the locks** — always `min(k1, k2)` before `max(k1, k2)`
2. **Acquire once for duplicates** — `(1, 1)` must not lock the same key twice with a non-reentrant lock
3. **Try-lock + retry** — can't get both? release and try again
4. **Never call out** while holding a lock if the callee might lock

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Design a Deadlock-Free Two-Key Executor](solutions/Design-Deadlock-Free-Two-Key-Executor.md) — AlgoMaster · medium · Deadlock — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/design-deadlock-free-two-key-executor)

---

## Extra Practice (self-study)

- [ ] Build a deliberate A→B / B→A deadlock and prove it with a thread dump
- [ ] Fix it with ordering, then fix it again with try-lock, and compare

## Tips
- Quote the four Coffman conditions — it's the fastest way to look rigorous
- The two-key contract: **"`(1,2)` and `(2,1)` must never deadlock"** → sort the keys
- Also handle **duplicate keys**: lock each distinct key exactly once
- The implementation must work with **non-reentrant** locks — so no `lock(); lock();` on the same key
