# Design a Concurrency Limiter With a Semaphore (Semaphores)

**Source:** AlgoMaster · Concurrency Practice · **medium** · **Topic:** Semaphores
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/design-concurrency-limiter-with-semaphore)

### Problem

```java
class ConcurrencyLimiter {
    ConcurrencyLimiter(int maxConcurrent);
    void run(Runnable task);   // blocks for a permit, runs, releases
}
```

**Guarantees:** at most `maxConcurrent` callbacks executing at once; a caller with no available
permit **blocks**; permits are **reusable** across any number of calls; the permit is released even
if the callback **throws** (the original failure propagates); separate instances have **independent**
permit pools.

### The failure, before

```java
// ❌ permit leaked on the exception path — capacity shrinks every time a task throws
public void run(Runnable task) {
    permits.acquire();
    task.run();          // if this throws, release() never runs
    permits.release();
}
```

After a few throwing tasks the limiter admits nobody — silently, and only under load.

### The Fix (after)

```java
import java.util.concurrent.Semaphore;

public final class ConcurrencyLimiter {
    private final Semaphore permits;

    public ConcurrencyLimiter(int maxConcurrent) {
        if (maxConcurrent < 1) throw new IllegalArgumentException("maxConcurrent >= 1");
        this.permits = new Semaphore(maxConcurrent);
    }

    public void run(Runnable task) throws InterruptedException {
        permits.acquire();               // 1. wait for a permit (blocks / interruptible)
        try {
            task.run();                  // 2. at most maxConcurrent of these overlap
        } finally {
            permits.release();           // 3. ALWAYS returned, even on throw
        }
    }
}
```

**Usage**
```java
ConcurrencyLimiter limiter = new ConcurrencyLimiter(2);
// four threads:
limiter.run(slowTask);   // at most two slowTask callbacks overlap at any instant
```

### Design points
- **Acquire / release pairing is enforced by `try`-`finally`** — the invariant survives any exception.
- **The permit is the capacity** — `new Semaphore(N)` creates the pool; `release()` returns one permit,
  it does not create a thread.
- **Independent instances** — each `ConcurrencyLimiter` owns its own `Semaphore`, so pools don't leak
  across limiters.
- **Blocking, not spinning** — `acquire()` parks the thread; no busy-wait.
- **Interruptible** — a waiting caller can be cancelled, satisfying the "must not busy-wait" contract.

**Complexity:** O(1) amortised per call · Space O(1) — cost is contention on the permit queue.

---
#concurrency #semaphore #lld #practice
