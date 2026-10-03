# Mutex (Mutual Exclusion) — Concept

## What Is It?

A **mutex** guarantees that **only one thread** is inside a critical section at a time. Everything in
the section is observed as a single atomic step by every other thread.

| | |
|---|---|
| **Primitive** | Mutex / mutual exclusion lock |
| **Guarantee** | at most one holder in the critical section |
| **Java** | `synchronized`, `ReentrantLock` |

---

## When to Use

> **Trigger keywords:** "only one at a time", "critical section", "exclusive", "protect this state"

| Need | Tool |
|------|------|
| Simple mutual exclusion, no timeout/fairness | `synchronized` |
| Need `tryLock`, timeouts, fairness, interruptibility | `ReentrantLock` |
| Counter / flag only | atomic (no lock needed) |
| N-way exclusion | `Semaphore(1)` is a mutex too — but prefer a lock for 1 |

---

## The two Java forms

```java
// ✅ Idiomatic: block-scoped, cannot forget to unlock
synchronized (lock) {          // acquires THIS object's monitor
    if (stock < qty) return false;
    stock -= qty;
}                              // releases on exit, including exceptions
```

```java
// ✅ Explicit: needed for tryLock / timeout / fairness
private final ReentrantLock lock = new ReentrantLock();   // private final!

lock.lock();
try {
    // critical section
} finally {
    lock.unlock();             // MUST be in finally — or a throw leaks the lock
}
```

---

## Rules that actually matter

1. **Lock on a `private final` object** — never on `this` or a publicly reachable object; otherwise
   callers can lock you out (or in).
2. **Unlock in `finally`** — a thrown exception must not leak the lock.
3. **Hold it as briefly as possible** — no I/O, no callbacks, no `sleep()` inside.
4. **Consistent ordering** — every thread acquires multiple locks in the same order (see **Deadlock**).
5. **Keep the invariant inside** — locking method A but not method B that touches the same field is
   not protection.

---

## Notes

- `ReentrantLock` is **reentrant**: the owner can lock again (needed for recursion — see **Reentrant Locks**).
- A mutex gives **mutual exclusion**, not visibility magic — but mutual exclusion *does* create
  happens-before edges, so writes are visible to the next acquirer.
- `synchronized` locks are unfair by default; `ReentrantLock` can be configured either way.

---

## Common Mistakes

1. Locking on `this` or a `String` literal (interned!) — use a `private final Object`.
2. Forgetting `unlock()` on an exception path.
3. Synchronizing one method but leaving another path to the same state unsynchronized.
4. Locking far too much — a big critical section is a throughput bug.

---

## Related

- [[../00 - Index|Concurrency Concepts Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../Race-Conditions/Concept|Race Conditions]] · [[../Reentrant-Locks/Concept|Reentrant Locks]] · [[../Deadlock/Concept|Deadlock]]

---

#concurrency #mutex #lld #concept
