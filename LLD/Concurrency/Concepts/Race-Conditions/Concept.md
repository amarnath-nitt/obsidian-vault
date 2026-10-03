# Race Conditions & Critical Sections — Concept

## What Is It?

A **race condition** exists when the correctness of a program depends on the *uncontrolled
interleaving* of threads. A **critical section** is the stretch of code that must execute as if it
were atomic.

| | |
|---|---|
| **Bug** | Race condition |
| **The code at risk** | Critical section |
| **The fix** | Make the critical section atomic — lock, atomic, or single-threaded hand-off |

---

## When to Use

> **Trigger keywords:** "lost update", "check-then-act", "sometimes wrong", "intermittent", "oversell"

| Smell | Move |
|-------|------|
| `if (map.containsKey(k)) map.put(k, v)` | atomic `computeIfAbsent` |
| read → modify → write on shared state | lock the whole sequence |
| "it passed, then failed on the next run" | classic race — treat every pass as a failure |
| counter, balance, stock, size | atomic or mutex |

---

## The lost update, visualised

```java
counter++;   // NOT one step — it is:  READ → ADD → WRITE
```

```text
Thread A: read 0 ────┐
Thread B: read 0 ────┼──► both read 0
Thread A: write 1
Thread B: write 1            ← lost update!  final = 1, expected = 2
```

**Check-then-act** is the same disease at a larger grain:

```java
// ❌ Two threads both pass the check, then both act → oversell
if (stock >= qty) { stock -= qty; onPurchased.run(); }

// ✅ The check and the act must be ONE critical section
synchronized (this) {
    if (stock < qty) return false;
    stock -= qty;
}
onPurchased.run();   // callback OUTSIDE the lock — see below
```

---

## Notes

- **Linearizability** is the standard you're aiming for: each operation appears to take effect
  atomically at some instant between start and end.
- **Keep the critical section small** — but never split a check from its act.
- Callbacks/I/O inside a lock destroy throughput; run them after releasing where the contract allows.

---

## Common Mistakes

1. Locking the wrong object (a public or shared monitor).
2. Making the critical section atomic but leaving the *check* outside it.
3. Treating an intermittent pass as success.
4. Synchronizing individual methods while the real invariant spans two of them.

---

## Related

- [[../00 - Index|Concurrency Concepts Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../Mutex/Concept|Mutex]] · [[../Compare-and-Swap/Concept|CAS]]

---

#concurrency #race-condition #lld #concept
