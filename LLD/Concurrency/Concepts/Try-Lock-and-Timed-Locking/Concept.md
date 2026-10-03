# Try-Lock & Timed Locking — Concept

## What Is It?

Instead of blocking **indefinitely** when a lock is busy, a thread can **probe** it:

| Call | Behaviour |
|------|-----------|
| `lock()` | block until acquired |
| `tryLock()` | **non-blocking** — `true` if acquired now, `false` otherwise |
| `tryLock(timeout, unit)` | wait *up to* the timeout, then give up |
| `lockInterruptibly()` | block, but abort on interrupt |

**Why:** turning an unbounded wait into a bounded one lets you back off, retry, degrade, or fail fast.

---

## When to Use

> **Trigger keywords:** "give up", "timeout", "skip if busy", "try again later", "avoid blocking", "deadline"

| Need | Move |
|------|------|
| Do the work only if the lock is free *right now* | `tryLock()` |
| Wait a bounded time then degrade | `tryLock(timeout)` |
| Cancellable wait | `lockInterruptibly()` |
| Plain exclusion, no give-up semantics | `lock()` / `synchronized` |

---

## In Java

```java
public final class TimedLock {
    private final ReentrantLock lock = new ReentrantLock();

    /** Returns true if the task ran within the timeout; false if we gave up. */
    public boolean tryRun(Runnable task, long timeoutMillis) throws InterruptedException {
        if (!lock.tryLock(timeoutMillis, TimeUnit.MILLISECONDS)) {
            return false;                       // timed out → task is NOT executed
        }
        try {
            task.run();                         // lock held for the callback
            return true;
        } finally {
            lock.unlock();                      // released even if the task throws
        }
    }
}
```

`timeoutMillis == 0` means *"try once, don't wait at all"* — `tryLock()` is exactly that.

---

## Notes

- **Never busy-wait** to emulate a timeout — use `tryLock(timeout)` so the thread parks.
- A timed lock that gives up must leave the system in a **valid** state (nothing half-done).
- Try-lock is also a **deadlock-avoidance** technique: if you can't get both locks, release and retry.

---

## Common Mistakes

1. Running the task anyway after a failed `tryLock` — the timeout must gate execution.
2. Forgetting `unlock()` when the task throws.
3. Polling with `sleep()` instead of `tryLock(timeout)` — wastes CPU and isn't precise.
4. Returning `true` when nothing ran — callers must be able to trust the boolean.

---

## Related

- [[../00 - Index|Concurrency Concepts Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../Mutex/Concept|Mutex]] · [[../Deadlock/Concept|Deadlock]]

---

#concurrency #try-lock #lld #concept
