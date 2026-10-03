# Coarse vs Fine-grained Locking — Concept

## What Is It?

A **locking-strategy** choice about how *much* of the system one lock covers.

| | **Coarse-grained** | **Fine-grained** |
|---|---|---|
| **Lock covers** | a whole object / whole structure | one bucket, one key, one shard |
| **Contention** | low (few locks) | high (many locks) |
| **Parallelism** | low — everything queues on one lock | high — unrelated work proceeds |
| **Complexity** | simple; one lock to reason about | must lock/unlock many, ordering matters |
| **Risk** | throughput ceiling (convoy) | **deadlock**, lock leaks, partial updates |

**Rule of thumb:** start coarse, measure, then split only where the profiler shows contention.

---

## When to Use

> **Trigger keywords:** "contention", "throughput", "one lock is the bottleneck", "per-key", "striping"

| Symptom | Move |
|---------|------|
| One monitor has a long `BLOCKED` queue | split it — finer granularity |
| Correctness is getting hard to reason about | you've gone too fine |
| Many short operations on unrelated data | per-key / striped locks |
| Operations touch the whole structure anyway | coarse is fine |

---

## In Java

```java
// ❌ Coarse: every operation on every key waits for one lock
class Executor {
    private final Lock lock = new ReentrantLock();
    void execute(int key, Runnable task) { lock.lock(); try { task.run(); } finally { lock.unlock(); } }
}

// ✅ Fine: one lock per key — key 0 and key 1 never contend
class KeyedTaskExecutor {
    private final Lock[] keyLocks;                 // keyCount independent locks

    KeyedTaskExecutor(int keyCount) {
        keyLocks = new Lock[keyCount];
        for (int i = 0; i < keyCount; i++) keyLocks[i] = new ReentrantLock();
    }

    void execute(int key, Runnable task) {
        Lock lock = keyLocks[key];
        lock.lock();
        try { task.run(); } finally { lock.unlock(); }   // released even on throw
    }
}
```

Other common strategies: **striped locking** (hash into N locks — `ConcurrentHashMap`), **sharding**,
and **optimistic** reads with validation on write.

---

## Notes

- Fine-grained locks require **consistent acquisition order** or you invite deadlock.
- The win only materialises if threads actually hit **different** keys — measure before/after.
- `ConcurrentHashMap` is striped locking made concrete: independent segments/bins.

---

## Common Mistakes

1. Going fine-grained before measuring — complexity with no payoff.
2. Locking per-key but still touching shared state outside those locks.
3. Creating locks lazily in an unsynchronized way (races while building the lock table).
4. Forgetting to release per-key locks on the exception path.

---

## Related

- [[../00 - Index|Concurrency Concepts Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../Mutex/Concept|Mutex]] · [[../Deadlock/Concept|Deadlock]]

---

#concurrency #locking #lld #concept
