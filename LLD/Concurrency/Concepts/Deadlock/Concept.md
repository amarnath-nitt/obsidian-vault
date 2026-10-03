# Deadlock — Concept

## What Is It?

**Deadlock:** two or more threads are blocked forever, each waiting for a resource the others hold.
Nothing progresses; nothing errors — the program just *hangs*.

### Coffman's four conditions (all four must hold)

| # | Condition | In practice |
|---|-----------|-------------|
| 1 | **Mutual exclusion** | a resource can be held by only one thread |
| 2 | **Hold and wait** | a thread holds one lock while waiting for another |
| 3 | **No preemption** | a lock can't be taken away — only released voluntarily |
| 4 | **Circular wait** | A waits for B, B waits for A (…环) |

**Break any one** and deadlock is impossible.

---

## The canonical example

```java
// ❌ Two threads, opposite acquisition order → circular wait
// Thread 1: lock(A); lock(B);      Thread 2: lock(B); lock(A);
```

```text
Thread 1 holds A ──► wants B
Thread 2 holds B ──► wants A
        (neither can proceed → deadlock)
```

---

## The fixes (break one condition)

```java
// FIX 1 — Global ordering (breaks circular wait): always acquire the smaller key first
int first  = Math.min(k1, k2);
int second = Math.max(k1, k2);
lock(first).lock();
try {
    lock(second).lock();          // same key → acquire only once
    try { task.run(); }
    finally { unlock(second); }
} finally { unlock(first); }
```

```java
// FIX 2 — Try-lock + back off (breaks hold-and-wait):
if (lockA.tryLock()) {
    try {
        if (lockB.tryLock()) { try { work(); } finally { lockB.unlock(); } }
    } finally { lockA.unlock(); }
}   // couldn't get both → release and retry later
```

Other strategies: **acquire all locks up front**, or **timeout and release everything**.

---

## Notes

- Deadlock is **silent** — no exception. Diagnose with a thread dump: look for a *cycle* in
  `BLOCKED` threads.
- Consistent **lock ordering across the whole codebase** is the cheapest prevention.
- **Lock ordering is a design rule, not a local one** — a helper that locks without knowing the
  global order reintroduces the cycle.

---

## Common Mistakes

1. Two locks acquired in different orders in two code paths.
2. Holding a lock while calling out to unknown/untrusted code (which may want another lock).
3. Nested locks with no documented ordering.
4. Assuming "it never happened in testing" — deadlock is timing-dependent.

---

## Related

- [[../00 - Index|Concurrency Concepts Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../Mutex/Concept|Mutex]] · [[../Try-Lock-and-Timed-Locking/Concept|Try-Lock]] · [[../Livelock/Concept|Livelock]]

---

#concurrency #deadlock #lld #concept
