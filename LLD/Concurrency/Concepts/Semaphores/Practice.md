# Semaphores - Practice

## Key Concepts
- A **count of permits** — acquire to enter, release to leave
- Guarantees **at most N** concurrent holders; a mutex is `N = 1`
- **Always release in `finally`** — a leaked permit shrinks capacity permanently

## Common Moves in LLD
1. **Throttle** — a limiter in front of a risky/limited resource
2. **Pool** — `N` permits for `N` connections or slots
3. **Gate** — `acquire()` up front, `release()` after the callback
4. **Never** release more than you acquire — permits accumulate

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Design a Concurrency Limiter With a Semaphore](solutions/Design-Concurrency-Limiter-With-A-Semaphore.md) — AlgoMaster · medium · Semaphores — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/design-concurrency-limiter-with-semaphore)

---

## Extra Practice (self-study)

- [ ] Build a 3-slot permit pool that admits 10 tasks with at most 3 running
- [ ] Deliberately drop a `release()` on an exception and watch capacity drain

## Tips
- Say **"permits, not threads"** — the semaphore counts permits, it doesn't track ownership
- The interview trap is the **exception path**: `acquire()` outside, `try/finally` around the body
- If the question is *"at most N at once"*, the answer is a semaphore
