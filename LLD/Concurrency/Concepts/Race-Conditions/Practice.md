# Race Conditions & Critical Sections - Practice

## Key Concepts
- **Race condition** = correctness depends on thread interleaving
- **Critical section** = the code that must run atomically
- The classic shapes: **lost update** and **check-then-act**
- Target property: **linearizability**

## Common Moves in LLD
1. **Find the shared mutable state first** — that's where the race lives
2. **Merge check and act** into one critical section
3. **Shrink the section** — release the lock before callbacks / I/O
4. **Prefer an atomic primitive** for counters (`AtomicInteger`)

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Design a Thread-Safe Inventory](solutions/Design-Thread-Safe-Inventory.md) — AlgoMaster · medium · Race Conditions — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/design-thread-safe-inventory)

---

## Extra Practice (self-study)

- [ ] Reproduce a lost update with 2 threads and 1,000,000 increments
- [ ] Find a check-then-act in your own codebase and make it atomic

## Tips
- Always open with *"what is the shared mutable state, and what is the invariant?"*
- **An intermittent pass is a failure** — say this in an interview
- The subtle part of the inventory problem is running the callback **outside** the lock while still guaranteeing it runs exactly once
