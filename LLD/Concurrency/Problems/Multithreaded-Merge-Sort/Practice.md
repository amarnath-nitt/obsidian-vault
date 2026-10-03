# Multi-threaded Merge Sort - Practice

## Key Concepts
- **Bounded fork-join** — a `Semaphore(maxThreads - 1)` budget gates every fork
- **`tryAcquire`, never blocking acquire** — no capacity means *sequential now*, not *wait*
- `onMerge` fires **exactly once before every merge** (`n-1` times) on all paths

## Common Moves in LLD
1. **Permit-gated fork** — left half on a new thread, right half inline, `join` before merging
2. **Sequential fallback** — both halves inline when the budget is empty
3. **`release()` in `finally`** — the budget never leaks, sorts stay reusable
4. **Caller counts as a worker** — the semaphore holds `maxThreads - 1`, not `maxThreads`

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Multi-threaded Merge Sort](solutions/Multithreaded-Merge-Sort.md) — AlgoMaster · medium · Parallel algorithm — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/design-parallel-merge-sorter)

---

## Extra Practice (self-study)

- [ ] Run with `maxThreads = 1` — prove the trace is identical to sequential merge sort with `n-1` callbacks
- [ ] Leak test: throw mid-sort and show the next `sort()` still forks (permits were repaid)

## Tips
- Say **"tryAcquire means the fallback is sequential work, not waiting"** — the design's key sentence
- The `n-1` callback count is path-independent — state it before the interviewer derives it
- Join-before-merge is the correctness line; the budget is the resource line
