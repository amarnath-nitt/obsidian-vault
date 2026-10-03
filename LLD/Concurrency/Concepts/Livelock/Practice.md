# Livelock - Practice

## Key Concepts
- **Running but making no progress** — busy CPU, zero throughput
- Distinct from **deadlock** (blocked, idle CPU) — the two are confused constantly
- Fix by **breaking the symmetry**: back-off, randomisation, priority, or a give-up limit

## Common Triggers in Interviews
| Symptom | Suspect |
|---------|---------|
| high CPU, no results | **livelock** |
| low CPU, threads stuck in `BLOCKED` | **deadlock** |
| one thread never runs while others do | **starvation** |

---

## Exercises (self-study)

> No AlgoMaster exercise is tagged *Livelock* — this package is conceptual and diagnostic.
> (CAS and try-lock code is where livelock usually hides.)

- [ ] **Tell the three apart** — deadlock vs livelock vs starvation, in one sentence each, with a CPU signature
- [ ] **Reproduce it** — two threads that always yield to each other; observe 100% CPU and no progress
- [ ] **Fix it with back-off** — add a *randomised* sleep and watch progress return
- [ ] **Fix it with priority** — decide deterministically which thread wins
- [ ] **Bound the retries** — add a give-up limit and turn infinite retry into a clean failure

---

## Extra Practice

- [ ] Write two CAS loops on the same variable and tune contention until they visibly starve each other
- [ ] Audit your code for unbounded `while(true)` retry loops without back-off

## Tips
- The **CPU signature** is your diagnostic tell: *deadlock = idle, livelock = hot*
- Randomised back-off beats fixed back-off — fixed delays can stay perfectly synchronised
- Livelock and **starvation** are cousins: livelock = nobody progresses, starvation = one is starved
