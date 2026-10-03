# Design a Timed Lock (Try-Lock & Timed Locking)

**Source:** AlgoMaster · Concurrency Practice · **medium** · **Topic:** Try-Lock and Timed Locking
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/design-timed-lock)

### Problem

```java
class TimedLock {
    TimedLock();
    boolean tryRun(Runnable task, long timeoutMillis);
}
```

**Guarantees:** acquire within `timeoutMillis`; if acquired — run `task`, release, return `true`;
if the timeout expires first — **do not execute** `task`, return `false`. Callbacks on the same
`TimedLock` must **never overlap**; `timeoutMillis == 0` must try **immediately without waiting**;
the lock is released if the callback **throws** (the failure propagates); instances are independent.

### The failure, before

```java
// ❌ 1) runs the task even when acquisition failed
//    2) leaks the lock if the task throws
//    3) busy-waits instead of parking
public boolean tryRun(Runnable task, long timeoutMillis) {
    while (!lock.tryLock()) { Thread.onSpinWait(); }   // spins
    task.run();                                        // always runs
    lock.unlock();                                     // skipped on exception
    return true;
}
```

### The Fix (after)

```java
import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.ReentrantLock;

public final class TimedLock {
    private final ReentrantLock lock = new ReentrantLock();

    public boolean tryRun(Runnable task, long timeoutMillis) throws InterruptedException {
        if (timeoutMillis < 0) throw new IllegalArgumentException("timeoutMillis >= 0");

        // Bounded wait — parks the thread; timeoutMillis == 0 means "try once, don't wait"
        if (!lock.tryLock(timeoutMillis, TimeUnit.MILLISECONDS)) {
            return false;                    // timed out → task is NOT executed
        }
        try {
            task.run();                      // callbacks never overlap: we hold the lock
            return true;
        } finally {
            lock.unlock();                   // released even if task throws
        }
    }
}
```

**Usage**
```java
TimedLock lock = new TimedLock();
lock.tryRun(taskA, 1000);   // true  — lock free, taskA runs exactly once
lock.tryRun(taskB, 0);      // false — taskB never runs while taskA owns the lock
```

### Design points
- **Timeout gates execution** — a failed acquisition returns `false` *before* touching the task, which
  is the heart of the contract.
- **`tryLock(timeout, unit)` parks** — no busy-wait; the thread sleeps until granted or expired.
- **Zero-timeout edge case falls out naturally** — `tryLock(0, …)` attempts once without waiting.
- **`finally { unlock(); }`** — a throwing callback cannot leak the lock (otherwise that `TimedLock`
  wedges permanently).
- **No overlap** — mutual exclusion is guaranteed by the lock itself, not by any flag in the class.
- **Instances independent** — the `ReentrantLock` is a per-object field.

**Complexity:** O(1) per call plus the (bounded) wait · Space O(1).

---
#concurrency #try-lock #lld #practice
