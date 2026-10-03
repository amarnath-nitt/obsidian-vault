# Thread-Safe Blocking Queue - Practice

## Key Concepts
- **Bounded FIFO with backpressure** — full blocks producers, empty blocks consumers, nobody spins
- One lock + **two conditions** (`notFull` / `notEmpty`), each the negation of a wait predicate
- Every state change **signals exactly the side it unblocks**

## Common Moves in LLD
1. **Circular buffer** — array + `head` + `count`, modulo indexing, never shifts
2. **`while (full) await()` / `while (empty) await()`** — park, don't spin
3. **Signal after mutation, under the same lock** — woken thread sees the fresh count
4. **`size()` under the lock** — a torn read is a wrong answer under concurrency

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Thread-Safe Blocking Queue](solutions/Thread-Safe-Blocking-Queue.md) — AlgoMaster · medium · Thread-safe structure — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/design-bounded-blocking-queue)

---

## Extra Practice (self-study)

- [ ] Reimplement with `synchronized` + `wait/notifyAll` — then argue why two `Condition`s wake fewer threads
- [ ] Add `tryEnqueue` with a timeout — it reuses the same predicates with `awaitNanos`

## Tips
- Say **"two conditions, each the negation of a wait predicate"** — the sentence that ends the question
- The `while`-not-`if` rule has a concrete story here: two woken dequeuers, one element
- Backpressure is the point: a full queue *slows producers*, it never drops or grows
