# Reentrant Locks — Concept

## What Is It?

A **reentrant (recursive) lock** can be acquired **again by the thread that already holds it**,
without deadlocking. It counts acquisitions and only unlocks when the count reaches zero.

| | |
|---|---|
| **Property** | reentrancy / recursion safety |
| **Why it matters** | a method that locks and then calls a helper that also locks |
| **Java** | `ReentrantLock`, and `synchronized` (also reentrant) |

---

## When to Use

> **Trigger keywords:** "recursive", "nested calls to a locked method", "self-deadlock", "already holds the lock"

| Situation | Need |
|-----------|------|
| A locked method calls another locked method on the **same** object | reentrant lock |
| Recursive algorithm (accumulating a range, tree walk) under one lock | reentrant lock |
| Language/runtime whose mutex is **NOT** reentrant (Go's `sync.Mutex`) | acquire **once**, recurse in a private helper |
| You must not allow re-entry | a non-reentrant lock / ownership check |

---

## In Java

```java
public final class RecursiveAccumulator {
    private final ReentrantLock lock = new ReentrantLock();
    private long total;

    public void addRange(int n, LongConsumer onAdd) {
        lock.lock();                       // hold count = 1
        try {
            addRecursively(n, onAdd);      // helper may lock again — safe, count = 2
        } finally {
            lock.unlock();                 // count = 1
        }
    }

    private void addRecursively(int n, LongConsumer onAdd) {
        if (n <= 0) return;
        lock.lock();                       // reentrant: same thread, already owns it
        try {
            total += n;
            onAdd.accept(n);
            addRecursively(n - 1, onAdd);  // recursion under the same lock
        } finally {
            lock.unlock();
        }
    }

    public long getTotal() {
        lock.lock();
        try { return total; } finally { lock.unlock(); }
    }
}
```

**Contrast — a non-reentrant mutex (Go):**
```go
func (a *Accumulator) AddRange(n int, onAdd func(int)) {
    a.mu.Lock()                // acquire ONCE
    a.addRec(n, onAdd)         // private helper assumes the lock is already held
    a.mu.Unlock()
}
```
Calling `a.mu.Lock()` again in the same goroutine would **deadlock**.

---

## Notes

- Reentrancy **prevents self-deadlock**, it does not make the code thread-safe by itself.
- The unlock count must still balance: every `lock()` needs exactly one `lock()`'s worth of `unlock()`.
- `synchronized` is reentrant too — that's why a synchronized method may call another one.

---

## Common Mistakes

1. Assuming every language's mutex is reentrant — Go's is the classic counter-example.
2. Locking, unlocking, and re-locking in a pattern where another thread can interleave (breaks the
   atomicity you thought you had).
3. Forgetting that the lock is **still held** during the callback — nested work under the lock
   widens your critical section.

---

## Related

- [[../00 - Index|Concurrency Concepts Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../Mutex/Concept|Mutex]] · [[../Deadlock/Concept|Deadlock]]

---

#concurrency #reentrant #lld #concept
