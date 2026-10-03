# Design a Recursive Accumulator (Reentrant Locks)

**Source:** AlgoMaster · Concurrency Practice · **medium** · **Topic:** Reentrant Locks
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/design-recursive-accumulator)

### Problem

```java
class RecursiveAccumulator {
    RecursiveAccumulator();
    void addRange(int n, LongConsumer onAdd);   // adds n + (n-1) + ... + 1, calling onAdd after each
    long getTotal();
}
```

**Guarantees:** `addRange` with `n <= 0` does nothing and does **not** invoke the callback; each
`addRange` is **one exclusive operation** (calls can't overlap, `getTotal` never observes a partial
range); the recursion re-acquires the **same** lock at each level; if the callback throws, the failure
propagates and the lock is released, while already-added values remain; instances are independent.

### The failure, before

```java
// ❌ Self-deadlock with a non-reentrant lock: the thread already owns it
void addRange(int n, ...) {
    lock.lock();
    addRecursively(n);      // calls lock.lock() again → hangs forever
    lock.unlock();
}
```

### The Fix (after)

```java
import java.util.concurrent.locks.ReentrantLock;
import java.util.function.LongConsumer;

public final class RecursiveAccumulator {
    private final ReentrantLock lock = new ReentrantLock();   // reentrant by construction
    private long total;

    public void addRange(int n, LongConsumer onAdd) {
        lock.lock();                                   // hold count = 1
        try {
            addRecursively(n, onAdd);                  // may re-enter — safe
        } finally {
            lock.unlock();                             // count returns to 0
        }
    }

    private void addRecursively(int n, LongConsumer onAdd) {
        if (n <= 0) return;                            // n <= 0 → nothing, no callback
        lock.lock();                                   // reentrant: same thread re-acquires
        try {
            total += n;                                // already holding the lock
            onAdd.accept(n);                           // callback AFTER each add
            addRecursively(n - 1, onAdd);
        } finally {
            lock.unlock();                             // balanced even if onAdd throws
        }
    }

    public long getTotal() {
        lock.lock();
        try { return total; } finally { lock.unlock(); }
    }
}
```

**Usage**
```java
RecursiveAccumulator acc = new RecursiveAccumulator();
acc.addRange(3, x -> System.out.print(x + " "));   // 3 2 1  (3 callback invocations)
acc.getTotal();                                    // 6
```

### Design points
- **Reentrancy removes the self-deadlock** — the recursive call takes a lock the same thread already
  owns; `ReentrantLock` counts holds instead of blocking.
- **The whole `addRange` is one critical section** — the outer `lock()`/`unlock()` spans the recursion,
  so a concurrent `getTotal()` sees only complete ranges.
- **Balanced `finally`** — if `onAdd` throws at depth 3, three `unlock()`s run and the lock is fully
  released; values added before the failure stay in `total`.
- **`n <= 0` guard before locking work** — no callback, no state change.
- **Instances independent** — the lock and `total` are per-object.

> **Cross-language note:** in Go, `sync.Mutex` is **not** reentrant — acquire once in `AddRange` and
> do the recursion in a private helper that assumes the lock is held.

**Complexity:** O(n) per `addRange` · Space O(n) for the recursion stack (or O(1) with an explicit loop).

---
#concurrency #reentrant #lld #practice
