# Design an Auto-Reset Signal (Signaling)

**Source:** AlgoMaster · Concurrency Practice · **medium (premium)** · **Pattern:** Signaling
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/design-auto-reset-signal)

### Problem

Implement an **auto-reset event**: a waiter blocks until a signal arrives; the signal **releases
exactly one waiter and then resets itself**, so the next waiter blocks again until the following
signal.

**Shape of the contract:**
- `signal()` — releases one waiting thread (if any) and returns to the unsignalled state
- `wait()` — blocks until a signal; the signal is *consumed* by this waiter
- A signal with **no waiter** must not be remembered as a permanently set flag (auto-reset semantics)
  unless the problem's stated variant says otherwise — read the contract carefully

### The design

```java
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public final class AutoResetSignal {
    private final ReentrantLock lock = new ReentrantLock();
    private final Condition changed = lock.newCondition();
    private boolean set = false;            // durable state for the CURRENT signal

    /** Release one waiter, then immediately reset. */
    public void signal() {
        lock.lock();
        try {
            set = true;                     // state change...
            changed.signal();               // ...release one waiter, atomically together
            // auto-reset: the waiter that wakes consumes `set`
        } finally {
            lock.unlock();
        }
    }

    /** Wait until signalled; consume the signal so the next waiter blocks again. */
    public void await() throws InterruptedException {
        lock.lock();
        try {
            while (!set) changed.await();   // re-check every wakeup
            set = false;                    // CONSUME — this is the auto-reset
        } finally {
            lock.unlock();
        }
    }
}
```

### Design points
- **`set` is real state** — a signal arriving before anyone waits is still observable by the first
  waiter (no lost wakeup).
- **`while (!set)`** — spurious wakeups and non-consumers re-park correctly.
- **Consume on wake** — clearing `set` inside the lock is what makes it *auto*-reset: the next
  `await()` blocks again.
- **Signal and state under one lock** — otherwise a waiter can wake between them and see stale state.
- **`Condition` over `wait/notify`** — one lock, a named condition, and it composes with
  `tryLock`/timeouts if needed.

> **Follow-up:** *why not `Semaphore(1)`?* — a semaphore with one permit behaves like an auto-reset
> event, but the event also carries the "already set" state transition explicitly, which is what
> most contracts test.

**Complexity:** O(waiters) per `signal()` · Space O(1).

---
#concurrency #signaling #lld #practice
