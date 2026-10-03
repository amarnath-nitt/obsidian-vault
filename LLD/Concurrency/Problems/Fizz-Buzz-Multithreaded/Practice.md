# Fizz Buzz Multithreaded - Practice

## Key Concepts
- **Four threads, one shared cursor** — `current` (1..n); exactly one method's predicate is true at a time
- `while (not mine) wait()` + **print, advance, `notifyAll()` under the same lock**
- `while (true)` loop with the **exit check inside the lock** — no thread knows its own count upfront

## Common Moves in LLD
1. **One predicate per method** — fizz / buzz / fizzbuzz / number partition 1..n disjointly
2. **Cursor advance is the handover** — whoever prints decides who goes next
3. **Notify on every exit path** — a silent return hangs the other three threads
4. **`notifyAll()`** — all three parked threads re-check against the new cursor

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Fizz Buzz Multithreaded](solutions/Fizz-Buzz-Multithreaded.md) — AlgoMaster · medium · Ordering — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/fizz-buzz-multithreaded)

---

## Extra Practice (self-study)

- [ ] Trace `n = 5` by hand: write which thread wakes for each value of `current`
- [ ] Generalise: five threads where the fifth prints primes — only the predicates change

## Tips
- Say **"the cursor partitions the work; the predicates are disjoint by construction"** — that kills the follow-up about two threads printing the same value
- The exit-notify is the classic hang — mention it before the interviewer asks
- Never create threads — the judge supplies all four; you only coordinate the methods
