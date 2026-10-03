# Try-Lock & Timed Locking - Practice

## Key Concepts
- **Bounded waiting instead of unbounded blocking** — `tryLock()` / `tryLock(timeout)`
- A failed try-lock must **not** execute the work
- Also a **deadlock-avoidance** tool: can't get both → release, back off, retry

## Common Moves in LLD
1. **Fail fast** — `tryLock()` and return `false` if busy
2. **Degrade** — `tryLock(timeout)`, then serve a stale/simplified answer
3. **Deadlock avoidance** — acquire in order, or take-and-release instead of holding two
4. **Always `finally { unlock(); }`** — the task may throw

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Design a Timed Lock](solutions/Design-Timed-Lock.md) — AlgoMaster · medium · Try-Lock and Timed Locking — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/design-timed-lock)

---

## Extra Practice (self-study)

- [ ] Wrap any lock in a `tryRun(task, timeout)` that returns a boolean
- [ ] Convert a blocking wait into a try-lock with a graceful fallback

## Tips
- The contract to quote: **"if the timeout expires, do not execute the task and return `false`"**
- `tryLock(0, …)` == `tryLock()` — worth saying; it shows you know the zero-timeout edge case
- The judge checks that callbacks **never overlap** and that a throwing task still releases the lock
