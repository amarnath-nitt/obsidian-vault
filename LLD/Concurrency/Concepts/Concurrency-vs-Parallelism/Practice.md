# Concurrency vs Parallelism - Practice

## Key Concepts
- **Concurrency** = structuring multiple tasks (interleaving) — a *design* problem
- **Parallelism** = executing simultaneously — a *hardware/scheduling* property
- One core ⇒ concurrent but not parallel; many cores ⇒ both

## Common Triggers in Interviews
| Trigger | Answer |
|---------|--------|
| "one core, many threads" | concurrent, **not** parallel |
| "why does this still race on 1 core?" | interleaving ≠ parallelism |
| "we need throughput on 8 cores" | parallelism — split the work |

---

## Exercises (self-study)

> No AlgoMaster exercise is tagged *Concurrency vs Parallelism* — this package is conceptual.
> The distinctions below are the classic screening-question answers.

- [ ] **Define both in one sentence each**, then give an example of concurrency without parallelism
- [ ] **Draw the two diagrams** — interleaved vs simultaneous — from memory
- [ ] **Classify these:** a Node.js event loop · `parallelStream()` · a 4-thread pool on a 2-core laptop · `synchronized` blocks
- [ ] **Answer the trap:** *"My program is single-core, so it can't have a race condition."* — refute it

---

## Extra Practice

- [ ] Run a 4-thread counter on a 1-core container and watch it still race
- [ ] Time a task split across 1 vs 4 threads and explain why the speedup is sub-linear

## Tips
- The distinction is a **screening question** — a crisp answer signals you know the theory
- Races are **concurrency** bugs; parallelism only makes them easier to reproduce
- Don't promise linear speedup — Amdahl's law caps it
