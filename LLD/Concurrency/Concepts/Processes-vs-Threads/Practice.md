# Processes vs Threads - Practice

## Key Concepts
- **Threads share memory; processes do not** — that single fact explains every race in this track
- Processes: isolated, expensive, IPC to communicate
- Threads: cheap, shared heap, must synchronize

## Common Triggers in Interviews
| Need | Choose |
|------|--------|
| isolation / fault tolerance | process |
| cheap concurrency over shared state | thread |
| run unstable or untrusted code | process |
| shared-memory parallelism | thread pool |

---

## Exercises (self-study)

> No AlgoMaster exercise is tagged *Processes vs Threads* — this package is conceptual.

- [ ] **Draw two processes and two threads each**, marking which memory is shared
- [ ] **Answer:** *"Why can a thread crash take down the whole process but a process usually can't?"*
- [ ] **Justify a design:** a web server handling 10k connections — processes or threads, and why?
- [ ] **List three forms of IPC** and say when each beats shared memory

---

## Extra Practice

- [ ] Start two processes that print a shared counter — observe they can't race without explicit shared memory
- [ ] Start two threads on a shared counter — observe the race

## Tips
- Lead with **memory sharing** — it's the distinction interviewers are checking for
- Pair it with the real trade-off: **isolation vs speed**
- "Threads are cheaper" is only half the answer; add *"but they share the heap"*
