# Design a Keyed Task Executor (Coarse vs Fine-grained Locking)

**Source:** AlgoMaster · Concurrency Practice · **medium** · **Topic:** Coarse-grained vs Fine-grained Locking
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/design-keyed-task-executor)

### Problem

```java
class KeyedTaskExecutor {
    KeyedTaskExecutor(int keyCount);                 // keys 0 .. keyCount-1
    void execute(int key, Runnable task);            // exclusive access to THAT key
}
```

**Guarantees:** tasks with the **same key never overlap**; tasks on **different keys are independent
and may run at the same time**; the key's lock is held for the callback's **entire execution**; if the
task throws, the lock is **still released** and the original failure propagates; different executor
instances are independent.

### The failure, before

```java
// ❌ Coarse-grained: one lock for every key
class KeyedTaskExecutor {
    private final Lock lock = new ReentrantLock();
    void execute(int key, Runnable task) {
        lock.lock();
        try { task.run(); } finally { lock.unlock(); }
    }
}
```

Correct, but key `0` blocks key `1` for no reason — every task in the system serialises on one
monitor. Throughput collapses as keyCount grows.

### The Fix (after)

Fine-grained: **one lock per key**.

```java
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public final class KeyedTaskExecutor {
    private final Lock[] keyLocks;

    public KeyedTaskExecutor(int keyCount) {
        if (keyCount < 1) throw new IllegalArgumentException("keyCount >= 1");
        keyLocks = new Lock[keyCount];
        for (int i = 0; i < keyCount; i++) {
            keyLocks[i] = new ReentrantLock();     // built up-front — no lock-creation race
        }
    }

    public void execute(int key, Runnable task) {
        if (key < 0 || key >= keyLocks.length) throw new IndexOutOfBoundsException("key");
        Lock lock = keyLocks[key];
        lock.lock();
        try {
            task.run();                            // held for the whole callback
        } finally {
            lock.unlock();                         // released even if task throws
        }
    }
}
```

**Usage**
```java
KeyedTaskExecutor executor = new KeyedTaskExecutor(3);
// Thread 1: executor.execute(1, taskA);
// Thread 2: executor.execute(1, taskB);   → taskA and taskB NEVER overlap
// Thread 3: executor.execute(0, taskC);   → taskC runs concurrently with both
```

### Design points
- **Per-key exclusion, global parallelism** — `keyLocks[key]` means unrelated keys share nothing.
- **Lock table built in the constructor** — no unsynchronised lazy creation (that would race itself).
- **Held for the whole callback** — the lock is acquired before `task.run()` and released after it
  returns, satisfying "must never overlap".
- **`finally` releases** — a throwing task can't leak the lock and wedge that key forever.
- **Independent instances** — the `keyLocks` array is per-executor.

> **Trade-off stated out loud:** fine-grained costs one lock object per key and requires careful
> ordering if a task ever needs *two* keys — that's exactly where **deadlock** comes from.

**Complexity:** O(1) per `execute` · Space O(keyCount) for the lock table.

---
#concurrency #locking #lld #practice
