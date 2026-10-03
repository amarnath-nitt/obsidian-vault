# Semaphores — Concept

## What Is It?

A **semaphore** holds a count of **permits**. A thread must acquire a permit to proceed and release
it when done — so at most *N* threads can be in a section at once.

| | |
|---|---|
| **Primitive** | Semaphore (Dijkstra's `P()` / `V()`) |
| **Guarantee** | at most **N** concurrent holders |
| **Java** | `java.util.concurrent.Semaphore` |
| **Mutex =** | a semaphore with `N = 1` |

---

## When to Use

> **Trigger keywords:** "at most N", "limit", "concurrency limiter", "connection pool", "throttle"

| Need | Tool |
|------|------|
| Only one thread at a time | mutex (`synchronized`) |
| **At most N** at a time | **semaphore** |
| N identical resources (connections, slots) | semaphore |
| Release N waiters at once | `CountDownLatch` / barrier (not a semaphore) |

---

## In Java

```java
public class ConcurrencyLimiter {
    private final Semaphore permits;

    public ConcurrencyLimiter(int maxConcurrent) {
        this.permits = new Semaphore(maxConcurrent);
    }

    public void run(Runnable task) throws InterruptedException {
        permits.acquire();                 // blocks until a permit is free
        try {
            task.run();                    // at most maxConcurrent callbacks overlap
        } finally {
            permits.release();             // ALWAYS release — even if task throws
        }
    }
}
```

---

## Rules that matter

1. **Release in `finally`** — a throwing task that leaks a permit permanently shrinks capacity.
2. **Acquire then release in pairs** — never `acquire()` without a matching `release()`.
3. **Permits are reusable** — release returns one to the pool; there is no "end of life".
4. **Separate instances ⇒ separate pools** — two limiters don't share permits.
5. **Don't use a semaphore as a mutex unless N=1** — and even then a lock is clearer.

---

## Notes

- `acquire()` is interruptible; `tryAcquire(timeout)` gives you a give-up path (see **Try-Lock**).
- A semaphore counts **permits**, not threads — it doesn't know who holds what.
- Unbounded `release()` beyond the initial count is possible (permits accumulate) — usually a bug.

---

## Common Mistakes

1. Forgetting `release()` on the exception path — capacity slowly drains to zero.
2. Releasing more times than acquired — silently allowing more than N concurrent.
3. Using a semaphore where a mutex or a thread pool is the right shape.

---

## Related

- [[../00 - Index|Concurrency Concepts Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../Mutex/Concept|Mutex]] · [[../../Patterns/Thread-Pool-Pattern/Concept|Thread Pool Pattern]]

---

#concurrency #semaphore #lld #concept
