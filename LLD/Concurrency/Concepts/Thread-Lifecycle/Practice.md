# Thread Lifecycle & States - Practice

## Key Concepts
- Six states: `NEW · RUNNABLE · BLOCKED · WAITING · TIMED_WAITING · TERMINATED`
- **BLOCKED = lock** · **WAITING = another thread's action**
- `sleep()` keeps the monitor; `wait()` releases it

## Common Triggers in Interviews
| Symptom | State | Cause |
|---------|-------|-------|
| threads piled up | BLOCKED | contention on one monitor |
| never wakes | WAITING | missing `notify()` / lost signal |
| nothing new happens | NEW | `run()` called instead of `start()` |

---

## Exercises (self-study)

> No AlgoMaster exercise is tagged *Thread Lifecycle* — this package is conceptual and diagnostic.

- [ ] **Draw the state diagram** from memory, marking what triggers each transition
- [ ] **`run()` vs `start()`** — explain what happens in each case and which one creates a thread
- [ ] **Diagnose:** a dump shows 40 threads `BLOCKED` on `Object@1a2b`. What is wrong, and what would you change?
- [ ] **`sleep()` vs `wait()`** — table: releases lock? needs monitor? static? wakes on `notify()`?
- [ ] **Fix the wait:** rewrite `synchronized(l){ l.wait(); }` correctly

---

## Extra Practice

- [ ] Write a program that puts a thread into `WAITING`, then never notifies it — take a thread dump and read it
- [ ] Trigger a `BLOCKED` convoy (many threads, one lock) and observe it in a dump

## Tips
- **"BLOCKED is about locks, WAITING is about signals"** — a crisp distinction interviewers look for
- Always wait inside `while (!condition)`, never `if`
- A thread dump is your first tool when someone says *"it hangs"*
