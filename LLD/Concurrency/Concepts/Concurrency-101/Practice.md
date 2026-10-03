# Concurrency 101 - Practice

## Key Concepts
- **Concurrency** = progress on multiple tasks by interleaving; **parallelism** = actually running at the same instant
- **Race condition** — the result depends on thread interleaving
- **Critical section** — code that must run atomically
- **Atomicity · Visibility · Ordering** — the three things concurrency correctnes needs

## Common Triggers in Interviews
| Trigger | Response |
|---------|----------|
| Shared mutable state across threads | protect with a lock / atomic |
| Producer → consumer hand-off | blocking queue / condition variable |
| Limit concurrent resource use | semaphore / thread pool |
| Read-heavy, rare writes | read-write lock |
| Simple counter / flag | `AtomicInteger` / `volatile` |

---

## Exercises (self-study)

> AlgoMaster has no "Concurrency 101" exercise — this package is the shared vocabulary the
> other 13 concept packages build on. Work these, then move to Race Conditions and Mutex.

- [ ] **Explain the lost update** — draw the `counter++` read/modify/write interleaving and show why two threads produce 1 instead of 2
- [ ] **Fix it three ways** — `synchronized`, `ReentrantLock`, and `AtomicInteger`
- [ ] **Vocabulary drill** — define atomicity, visibility and ordering without notes, with one example of each failing
- [ ] **Name the primitive** — for each of: bounded buffer, N-slot gate, wait-for-a-flag, exclusive write: name the primitive you'd reach for

---

## Extra Practice

- [ ] Write a 20-line counter with two threads that must end at exactly 2,000,000
- [ ] Reproduce a race deliberately, then fix it — seeing the intermittent failure teaches more than reading about it

## Tips
- **Say the vocabulary** — atomicity, visibility, ordering, happens-before
- An intermittent pass is a **failed** test, not a flaky one
- Always start thread-safety answers with *"what is the shared mutable state?"*
