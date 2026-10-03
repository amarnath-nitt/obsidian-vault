# Signaling Pattern — Concept

## What Is It?

One thread must **wait until another thread has signalled** that something happened. The hard part is
that the signal may arrive **before** anyone is waiting — so a correct design makes the signal
*durable state*, not a one-shot event.

| | |
|---|---|
| **Pattern** | Signaling / rendezvous |
| **Core** | a flag, version, or queue + a `while (!condition) wait()` loop |
| **Java** | `wait/notifyAll`, `Condition`, `CountDownLatch`, `CompletableFuture` |

---

## When to Use

> **Trigger keywords:** "in this order", "after X finishes", "wait until notified", "one-shot", "happens-before"

| Need | Tool |
|------|------|
| Fixed ordering of a few one-shot calls | state counter + `wait` loop |
| A signal that may fire *early* | **versioned / persisted** condition |
| Exactly one release, many waiters | `CountDownLatch` |
| Reusable signalling (reset + wait) | `Semaphore`, `CyclicBarrier`, auto-reset event |

---

## The shape

```java
public final class Foo {
    private final Object lock = new Object();
    private int step = 0;                 // durable state: 0 → 1 → 2

    public void first(Runnable r)  { signal(0, 1, r); }
    public void second(Runnable r) { signal(1, 2, r); }
    public void third(Runnable r)  { signal(2, 3, r); }

    private void signal(int from, int to, Runnable r) {
        synchronized (lock) {
            while (step != from) {        // WAIT until it is our turn
                try { lock.wait(); } catch (InterruptedException e) { Thread.currentThread().interrupt(); return; }
            }
            r.run();                      // do our part
            step = to;                    // advance the durable state
            lock.notifyAll();             // wake everyone — they re-check their own predicate
        }
    }
}
```

**Why it works:** `step` is *state*, so a thread that arrives late still sees the progress. A bare
`notify()` with no state would be lost forever if nobody was waiting.

---

## Notes

- **`notifyAll()`, not `notify()`** — several waiters may be parked on different predicates.
- **Always re-check in `while`** — spurious wakeups and "not my turn yet" both need a second check.
- **Advance state and notify under the same lock** — otherwise a waiter can wake between them.
- A `CountDownLatch` is this pattern specialised to *fire once*.

---

## Common Mistakes

1. One-shot notification with no persistent state → **signal lost** if it fires early.
2. `if` instead of `while` → missed wakeup.
3. `notify()` when waiters wait on different predicates → one wakes, the other sleeps forever.
4. Signalling outside the lock → the woken thread re-checks stale state.

---

## Related

- [[../00 - Index|Concurrency Patterns Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../../Concepts/Condition-Variables/Concept|Condition Variables]]

---

#concurrency #signaling #lld #concept
