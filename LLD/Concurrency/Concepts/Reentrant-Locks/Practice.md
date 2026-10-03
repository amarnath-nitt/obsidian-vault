# Reentrant Locks - Practice

## Key Concepts
- A thread that **already holds** the lock can take it again — no self-deadlock
- It's a **hold counter**: every `lock()` needs a matching `unlock()`
- Reentrancy ≠ thread-safety — it only removes the recursion hazard

## Common Moves in LLD
1. **Recursive work under one lock** — accumulate by recursing while holding the lock
2. **Locked method calling locked method** — `synchronized`/`ReentrantLock` handle it
3. **Non-reentrant runtime?** — lock once at the top, recurse through a private helper
4. **Mind the width** — a callback running under the lock widens the critical section

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Design a Recursive Accumulator](solutions/Design-Recursive-Accumulator.md) — AlgoMaster · medium · Reentrant Locks — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/design-recursive-accumulator)

---

## Extra Practice (self-study)

- [ ] Write a recursive sum that locks at every level and prove it doesn't self-deadlock
- [ ] Port it to a non-reentrant mutex and restructure with a private helper

## Tips
- The problem statement **tells you the implementation shape**: *"recursively calls the locked
  operation… languages with reentrant locks may acquire again at each level"*
- Quote the **Go contrast** — it proves you know reentrancy isn't universal
- "Each `addRange` is one exclusive operation; `getTotal` never sees a partial range" is the invariant
