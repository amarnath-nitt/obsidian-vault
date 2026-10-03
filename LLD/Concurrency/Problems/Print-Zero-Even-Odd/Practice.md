# Print Zero Even Odd - Practice

## Key Concepts
- **Three threads, one shared cursor** — `current` (1..n) plus a `zeroTurn` flag
- Each number-side predicate has **two clauses**: number side's turn AND cursor parity is mine
- `while` + **flip both state fields and `notifyAll()` under the same lock**

## Common Moves in LLD
1. **Two state fields** — `zeroTurn` forces the `0`; `current` picks even vs odd
2. **Loop bounds encode the contract** — zero runs `n` times, even/odd only their own values
3. **Only the number side advances the cursor** — zero never touches `current`
4. **`notifyAll()`** — the other two waiters re-check their own two-clause predicate

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Print Zero Even Odd](solutions/Print-Zero-Even-Odd.md) — AlgoMaster · medium · Ordering — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/print-zero-even-odd)

---

## Extra Practice (self-study)

- [ ] Trace `n = 2` by hand: `zero,odd,zero,even` — write the `(zeroTurn, current)` pair before each print
- [ ] Reimplement with three semaphores (`zeroSem(1)`, `evenSem(0)`, `oddSem(0)`)

## Tips
- State the invariant first: **"zero, then the cursor value, then zero, …"**
- The interview follow-up is always *"what if a fourth thread prints multiples of 3?"* — answer: the cursor predicate gains a clause, the shape doesn't change
- Never create threads — the judge supplies all three; you only coordinate the methods
