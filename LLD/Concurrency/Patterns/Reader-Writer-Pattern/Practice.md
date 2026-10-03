# Reader-Writer Pattern - Practice

## Key Concepts
- **Reads share, writes exclude** — many readers OR one writer, never both
- **Reader-preference starves writers**; count `waitingWriters` to prevent it
- **Run the callback outside the lock** — or readers serialise each other

## Common Moves in LLD
1. **Two conditions** — `canRead` and `canWrite` on one lock
2. **Counter the readers** — the last one out signals the writers
3. **Queue the writers** — `waitingWriters++` gates new readers
4. **`signalAll()` for readers**, `signal()` for the next writer

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Design a Read-Write Coordinator](solutions/Design-A-Read-Write-Coordinator.md) — AlgoMaster · medium · Read-Write Lock — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/design-read-write-coordinator)

### Hard
- [ ] [Readers-Writers Problem](solutions/Readers-Writers-Problem.md) — AlgoMaster · hard · Readers-Writers — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/readers-writers-problem)

---

## Extra Practice (self-study)

- [ ] Implement reader-preference, watch writers starve, then add the waiting-writer counter
- [ ] Read a config-heavy service and decide if a read-write lock would help

## Tips
- The **hard** variant explicitly demands **writer preference** — *"once a writer is waiting, readers
  that arrive later must wait"*
- Say **"callbacks run outside the lock"** — it's in both contracts and is easy to miss
- The paired invariant: *last reader out signals a writer; writer out signals all readers*
