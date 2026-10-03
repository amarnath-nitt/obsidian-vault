# Producer-Consumer Pattern - Practice

## Key Concepts
- **Bounded buffer** decouples producers from consumers and applies **back-pressure**
- **Two conditions** on one lock: `notFull` and `notEmpty`
- **Close semantics** are the real test: drain, then fail — never drop, never hang

## Common Moves in LLD
1. **`while (full) notFull.await()`** on put — the producer blocks when the buffer is full
2. **`while (empty) notEmpty.await()`** on take — the consumer waits for work
3. **Signal the other side** after every mutation
4. **`close()`** — wake *everyone*; producers fail, consumers drain

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Design a Closable Bounded Queue](solutions/Design-A-Closable-Bounded-Queue.md) — AlgoMaster · medium · Producer-Consumer — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/design-closable-bounded-queue)

---

## Extra Practice (self-study)

- [ ] Build a bounded buffer with two `Condition`s and prove back-pressure works
- [ ] Add `close()` and test all five shutdown rules

## Tips
- The closable-queue contract has **five explicit rules** — memorise them (drain, no-item, blocked
  producer fails, post-close fails immediately, idempotent)
- Never busy-wait: the judge checks you **don't spin**
- "One lock, two conditions" is the phrase that shows you know the pattern properly
