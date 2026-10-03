# Compare-and-Swap (CAS) — Concept

## What Is It?

**CAS** is a single atomic CPU instruction: *"if the value is still what I expect, set it to this;
otherwise tell me it changed."* It is the foundation of **lock-free** code — you retry instead of
blocking.

```text
CAS(&value, expected, newValue):
    atomically:  if (value == expected) { value = newValue; return true; }
                  else                  {                    return false; }
```

| | |
|---|---|
| **Primitive** | atomic read-modify-write |
| **Guarantee** | no lock; no lost update; progress without blocking |
| **Java** | `AtomicInteger`, `AtomicReference`, `VarHandle` |
| **Under the hood** | `lock cmpxchg` / LL-SC |

---

## The CAS loop

```java
private final AtomicReference<Integer> max = new AtomicReference<>();

/** Atomically store the larger of the current value and candidate. */
void accumulateMax(int candidate) {
    while (true) {
        Integer cur = max.get();                 // 1. read
        if (cur != null && cur >= candidate) return;   // 2. already big enough
        if (max.compareAndSet(cur, candidate)) return; // 3. swap only if unchanged
        // else: someone else won this round → loop and retry
    }
}
```

**Properties**
- **Atomic** — the read-and-swap is one instruction; no other thread can interleave.
- **Optimistic** — it never blocks; it *retries*.
- **Obstruction-free at worst** — if another thread keeps interfering, you spin.

---

## When to Use

> **Trigger keywords:** "without locking", "atomic", "counter", "increment", "lock-free", "optimistic"

| Need | Tool |
|------|------|
| Counter / increment | `AtomicInteger.incrementAndGet()` (a CAS loop) |
| Compare-and-update with a custom rule | CAS loop |
| Long critical section | a **lock** — CAS loops only pay off when contention is brief |

---

## Notes

- **ABA problem** — the value goes `A → B → A`; a naive CAS sees "unchanged". Fix with a versioned
  stamp (`AtomicStampedReference`).
- **CAS is not free** — under heavy contention a lock can outperform a spinning CAS loop.
- **Live-lock risk** — two threads can keep colliding and neither finishes promptly.

---

## Common Mistakes

1. Reading into a local, doing work, then CAS-ing **without** checking the result.
2. Forgetting to **retry** when CAS returns `false`.
3. Using CAS for long operations (the loop just spins).
4. Ignoring ABA when the *identity* of the value matters, not just its bits.

---

## Related

- [[../00 - Index|Concurrency Concepts Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../Race-Conditions/Concept|Race Conditions]] · [[../Livelock/Concept|Livelock]]

---

#concurrency #cas #lock-free #lld #concept
