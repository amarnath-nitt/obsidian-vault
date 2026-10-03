# Thread Pool Pattern - Practice

## Key Concepts
- **Fixed, long-lived workers** + a task queue — bounded resource, task reuse
- `submit()` must **accept, not execute**; `shutdown()` must **drain, then join**
- **Run callbacks outside the pool's lock** — or a task can't submit a task

## Common Moves in LLD
1. **Bounded worker count** — `workerCount` threads created once
2. **Blocking queue** — workers park when idle, wake when work arrives
3. **Idempotent shutdown** — stop intake, drain accepted work, join workers
4. **Exactly-once** — `offer() == true` is the acceptance point

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Hard
- [ ] [Design a Thread Pool](solutions/Design-A-Thread-Pool.md) — AlgoMaster · hard · Thread Pool — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/design-thread-pool)

---

## Extra Practice (self-study)

- [ ] Build a fixed pool with `workerCount` threads and a `BlockingQueue`
- [ ] Add `shutdown()` and prove every accepted task still runs

## Tips
- The three contract clauses to quote: **"runs outside the internal lock"**, **"never inline"**,
  **"shutdown is idempotent and drains"**
- The subtle bug is workers **exiting when the queue is briefly empty** — they must drain first
- A callback that calls `submit()` is the test for whether you held the lock too long
