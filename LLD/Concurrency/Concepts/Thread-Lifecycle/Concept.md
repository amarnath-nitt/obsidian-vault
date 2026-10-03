# Thread Lifecycle & States — Concept

## What Is It?

A Java thread moves through a fixed set of states (`Thread.State`). Knowing them lets you diagnose
*why* a program is stuck — the single most common concurrency debugging question.

```text
                start()
   NEW ─────────────────────► RUNNABLE ◄──────────────┐
                                    │                  │
                    blocked / waiting / timed waiting   │ notify(), unlock()
                                    │                  │
                                    ▼                  │
                               BLOCKED / WAITING / TIMED_WAITING
                                    
   RUNNABLE ──── run() returns ───► TERMINATED
```

| State | Meaning |
|-------|---------|
| **NEW** | created, `start()` not yet called |
| **RUNNABLE** | scheduled or ready to run (OS may or may not be giving it CPU) |
| **BLOCKED** | waiting to **enter a `synchronized`** block / acquire a monitor |
| **WAITING** | waiting for another thread to act (`wait()`, `join()`, `park()`) |
| **TIMED_WAITING** | same, with a timeout (`sleep(ms)`, `wait(ms)`) |
| **TERMINATED** | `run()` finished |

---

## When to Use

> **Trigger keywords:** "stuck", "hangs", "never wakes", "thread dump", "why is it BLOCKED"

| Symptom | Likely state | Cause |
|---------|--------------|-------|
| Many threads `BLOCKED` | BLOCKED | contention on one monitor |
| One thread `WAITING` forever | WAITING | missing `notify()` / lost signal |
| Everything fine but slow | RUNNABLE | workload, or lock convoy |
| Thread never started | NEW | `start()` never called (`run()` called directly instead) |

---

## The traps

```java
t.run();     // ❌ runs on the CALLER's thread — still one thread
t.start();   // ✅ starts a new thread which then calls run()
```

```java
// ❌ Spurious wakeups and lost notifications: always re-check in a loop
synchronized (lock) { lock.wait(); use(); }

// ✅
synchronized (lock) {
    while (!condition) lock.wait();   // predicate guards the wait
    use();
}
```

---

## Notes

- `sleep()` does **not** release monitors — `wait()` does. Mixing them up causes hangs.
- `BLOCKED` vs `WAITING`: BLOCKED is about a **lock**; WAITING is about **another thread's action**.
- A thread dump (`jstack`) showing thousands of `BLOCKED` on one monitor is the classic convoy signature.

---

## Common Mistakes

1. Calling `run()` instead of `start()` — no new thread.
2. `wait()` outside a `synchronized` block — `IllegalMonitorStateException`.
3. `wait()` without re-checking the predicate — missed/again-spurious wakeups.
4. `sleep()` while holding a lock — blocks everyone else for the sleep duration.

---

## Related

- [[../00 - Index|Concurrency Concepts Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../Condition-Variables/Concept|Condition Variables]]

---

#concurrency #threads #lld #concept
