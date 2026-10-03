# Signaling Pattern - Practice

## Key Concepts
- **Wait until another thread signals** — and make the signal *durable state*, not an event
- `while (!condition) wait()` + **advance state and `notifyAll()` under the same lock**
- `CountDownLatch` = this pattern specialised to fire once

## Common Moves in LLD
1. **Turn counter** — a `step` field guards whose turn it is
2. **Version stamp** — late waiters still observe progress (see Condition Variables)
3. **Latch** — one-shot release for N waiters
4. **`notifyAll()`** whenever waiters may have different predicates

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Print in Order](solutions/Print-In-Order.md) — AlgoMaster · easy · Signaling — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/print-in-order)

### Medium
- [ ] [Design an Auto-Reset Signal](solutions/Design-An-Auto-Reset-Signal.md) — AlgoMaster · medium (premium) · Signaling — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/design-auto-reset-signal)

---

## Extra Practice (self-study)

- [ ] Implement `first/second/third` ordering with a counter and `notifyAll()`
- [ ] Build an auto-reset event: signal releases one waiter, then resets itself

## Tips
- The ordering problems reduce to **one state field + one wait loop** — say that upfront
- **Signal-before-wait is the classic trap**: always persist the fact that it happened
- "Advance the state and notify under the same lock" is the sentence that wins the question
