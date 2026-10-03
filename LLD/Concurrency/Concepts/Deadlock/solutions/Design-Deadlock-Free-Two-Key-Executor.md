# Design a Deadlock-Free Two-Key Executor (Deadlock)

**Source:** AlgoMaster · Concurrency Practice · **medium** · **Topic:** Deadlock
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/design-deadlock-free-two-key-executor)

### Problem

```java
class TwoKeyTaskExecutor {
    TwoKeyTaskExecutor(int keyCount);                                  // keys 0 .. keyCount-1
    void execute(int firstKey, int secondKey, Runnable task);          // hold BOTH keys
}
```

**Guarantees:** callbacks **must not overlap** if their key pairs share either key; disjoint key
pairs run **concurrently**; keys may be given in **any order** — `(1, 2)` and `(2, 1)` must never
deadlock; if both arguments are the **same key**, acquire it **only once**; must work with
**non-reentrant** locks; if the task throws, **both** locks are released and the failure propagates.

### The deadlock, before

```java
// ❌ Each caller takes its own first key → circular wait
void execute(int k1, int k2, Runnable task) {
    lock(k1).lock();                 // T1: takes 1, wants 3
    lock(k2).lock();                 // T2: takes 3, wants 1   → both blocked forever
    try { task.run(); } finally { unlock(k2); unlock(k1); }
}
```

`execute(1, 3, A)` on thread 1 and `execute(3, 1, B)` on thread 2 produce exactly this cycle.

### The Fix (after)

**Break circular wait with a global ordering** — always acquire the *smaller* key first.

```java
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public final class TwoKeyTaskExecutor {
    private final Lock[] keyLocks;

    public TwoKeyTaskExecutor(int keyCount) {
        if (keyCount < 1) throw new IllegalArgumentException("keyCount >= 1");
        keyLocks = new Lock[keyCount];
        for (int i = 0; i < keyCount; i++) keyLocks[i] = new ReentrantLock();
    }

    public void execute(int firstKey, int secondKey, Runnable task) {
        checkKey(firstKey); checkKey(secondKey);

        // Global ordering: sort the keys, and dedupe when both are the same
        int first  = Math.min(firstKey, secondKey);
        int second = Math.max(firstKey, secondKey);
        boolean distinct = first != second;             // same key → lock ONCE only

        keyLocks[first].lock();
        try {
            if (distinct) keyLocks[second].lock();      // never double-lock one key
            try {
                task.run();                             // holds both keys for the callback
            } finally {
                if (distinct) keyLocks[second].unlock();
            }
        } finally {
            keyLocks[first].unlock();                   // released even on exception
        }
    }

    private void checkKey(int key) {
        if (key < 0 || key >= keyLocks.length) throw new IndexOutOfBoundsException("key");
    }
}
```

**Usage**
```java
TwoKeyTaskExecutor exec = new TwoKeyTaskExecutor(4);
// Thread 1: exec.execute(1, 3, taskA);
// Thread 2: exec.execute(3, 1, taskB);   → both acquire 1 BEFORE 3 → no cycle, both finish
// Thread 3: exec.execute(0, 1, taskC);   → disjoint from {1,3}? no — shares 1, so it waits
exec.execute(2, 2, taskD);               → same key → locked once (works with non-reentrant locks)
```

### Design points
- **Global lock ordering breaks Coffman's "circular wait"** — with `min` first everywhere, a cycle
  is impossible, so one of the four deadlock conditions is gone.
- **Dedupe (`first != second`)** — locking the same non-reentrant lock twice in one thread would
  self-deadlock; we acquire it exactly once.
- **Nested `finally` blocks** — the inner unlock only runs if the second lock was taken, and the
  outer unlock always runs; a throwing task releases both.
- **Disjoint key pairs still parallel** — sharing nothing means no unnecessary blocking.
- **Per-instance lock table** — instances are independent.

> **Alternative:** `tryLock` with back-off also works (breaks *hold-and-wait*), but needs a retry
> loop and can starve under load. Ordering is simpler and deterministic.

**Complexity:** O(1) per call · Space O(keyCount).

---
#concurrency #deadlock #lld #practice
