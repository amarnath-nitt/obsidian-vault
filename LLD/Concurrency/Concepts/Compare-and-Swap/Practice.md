# Compare-and-Swap (CAS) - Practice

## Key Concepts
- **CAS** = *if unchanged since I read it, swap it* — one atomic instruction
- **Lock-free**: optimistic **retry loop** instead of blocking
- Watch for **ABA** (version stamps) and **live-lock** (endless collisions)

## Common Moves in LLD
1. **Counter** — `AtomicInteger.incrementAndGet()` is a CAS loop
2. **Max / min / best-effort update** — read → compare → CAS → retry
3. **Publish-once** — CAS from `null` to a value, exactly one winner
4. **Give up and use a lock** if the critical section is long

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Design an Atomic Maximum With Compare-and-Swap](solutions/Design-Atomic-Maximum-With-Compare-And-Swap.md) — AlgoMaster · medium (premium) · CAS — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/design-atomic-maximum-with-compare-and-swap)

---

## Extra Practice (self-study)

- [ ] Implement `accumulateMax` as a CAS loop and prove no update is lost
- [ ] Demonstrate ABA with an `AtomicReference` and fix it with a stamp

## Tips
- The formula to say out loud: **"read, decide, CAS, retry if it changed"**
- Name the **ABA** problem unprompted — it's the standard follow-up question
- Contrast honestly: CAS wins on *brief* contention; a lock wins when the critical section is long
