# Design a Versioned Signal (Condition Variables)

**Source:** AlgoMaster · Concurrency Practice · **medium** · **Topic:** Condition Variables
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/design-versioned-signal)

### Problem

```java
class VersionedSignal {
    VersionedSignal();          // version starts at 0
    int currentVersion();
    void signal();              // version++, wake every waiter that may now proceed
    int awaitNext(int observedVersion) throws InterruptedException;
                                      // wait until version > observedVersion; return current
}
```

**Guarantees:** if the version is **already greater**, `awaitNext` returns **immediately** — signals
are *persistent*, so a signal that happens before a waiter starts is **not lost**. Every waiter must
**re-check** after waking (wakeups can be spurious; one notification may not advance the version far
enough for every waiter).

### The failure, before

```java
// ❌ one-shot notification: if the signal fires before anyone waits, it is gone forever
synchronized void signal() { notified = true; notifyAll(); }
synchronized int awaitNext(int observed) throws InterruptedException {
    if (!notified) wait();        // 'if' + non-durable flag → missed wakeup
    return version;
}
```

### The Fix (after)

Store the progress as a **monotonic version number** — a waiter compares against the version *it
observed*, so a signal that already happened satisfies it without ever being "delivered".

```java
public final class VersionedSignal {
    private final Object lock = new Object();
    private int version = 0;

    public int currentVersion() {
        synchronized (lock) { return version; }
    }

    public void signal() {
        synchronized (lock) {
            version++;                          // state change...
            lock.notifyAll();                   // ...and wake, atomically together
        }
    }

    public int awaitNext(int observedVersion) throws InterruptedException {
        synchronized (lock) {
            while (version <= observedVersion) {  // re-check EVERY wakeup
                lock.wait();                      // releases the monitor while parked
            }
            return version;                       // already > observed → returns at once
        }
    }
}
```

**Usage**
```java
VersionedSignal signal = new VersionedSignal();
int observed = signal.currentVersion();          // 0
// another thread:  signal.signal();             // version → 1
signal.awaitNext(observed);                      // returns 1 immediately, even if the
                                                 // signal fired before we started waiting
```

### Design points
- **State, not events** — the version *is* the record of every past signal, so nothing is lost.
- **`while`, not `if`** — a spurious wakeup, or a notification that didn't advance past
  `observedVersion`, must park again.
- **Signal and increment inside one `synchronized` block** — otherwise a waiter can wake between the
  two and re-check a stale version.
- **`notifyAll()`** — several waiters may share the same predicate, and one bump may serve all of them.
- **Immediate return when already satisfied** — the `while` condition is false on entry, so no wait.
- **`awaitNext` declares `throws InterruptedException`** — `wait()` throws a checked exception, so
  cancellation propagates to the caller instead of being silently swallowed.

**Complexity:** O(waiters) per `signal()` (all are woken and re-check) · Space O(1).

---
#concurrency #condition-variables #lld #practice
