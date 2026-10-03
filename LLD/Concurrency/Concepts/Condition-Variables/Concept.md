# Condition Variables — Concept

## What Is It?

A **condition variable** lets a thread **wait until a predicate becomes true**, by parking itself
until another thread signals that the state changed. It's how threads coordinate *progress*, not
just *mutual exclusion*.

| | |
|---|---|
| **Primitive** | Condition / `wait`–`notify` |
| **Guarantee** | wait until *someone else* changes shared state |
| **Java** | `Object.wait()/notifyAll()` inside `synchronized`, or `Condition` on a `ReentrantLock` |

---

## When to Use

> **Trigger keywords:** "wait until", "block until", "signal", "hand-off", "produced", "ready"

| Need | Tool |
|------|------|
| Wait until a flag/queue becomes ready | **condition variable** |
| Wait for a *count* of events | `CountDownLatch` |
| Wait for a *version/state change* that already happened | versioned signal (re-check predicate) |
| Just mutual exclusion | mutex — no condition needed |

---

## The four rules (this is the whole topic)

```java
// 1. Lock the monitor      2. Re-check in a loop      3. wait()          4. notify under the lock
synchronized (lock) {
    while (!condition) {          // NEVER 'if' — wakeups can be spurious
        lock.wait();              // releases the monitor and parks
    }
    // ... condition is now true, we hold the monitor
}

// producer, also under the same lock:
synchronized (lock) {
    state = NEW_VALUE;
    lock.notifyAll();             // wake everyone; each re-checks its own predicate
}
```

1. **Only inside the lock** — otherwise `IllegalMonitorStateException`.
2. **`while`, never `if`** — spurious wakeups and stale notifications are real.
3. **`wait()` releases the monitor** (unlike `sleep()`) — that's what lets the producer in.
4. **`notifyAll()` under the same lock** — changing state and signalling must be atomic together,
   or the waiter can wake, re-check, and miss it.

---

## The classic bug: signal loss

```java
// ❌ Producer signals before any waiter exists — the signal is gone forever
synchronized (lock) { ready = true; lock.notifyAll(); }

// waiter, later:
synchronized (lock) { while (!ready) lock.wait(); }   // waits forever if signal came first
```

**Fix:** make the condition *persistent state* (a version counter, a queue size, a flag) rather than
a one-shot event — so a waiter that arrives **after** the signal still sees it.

```java
// ✅ versioned: awaitNext(observed) returns immediately if the version already advanced
synchronized (lock) {
    while (version <= observed) lock.wait();
    return version;
}
```

---

## Notes

- `notify()` wakes one arbitrary waiter — if waiters wait on *different* predicates you **must**
  use `notifyAll()`.
- `ReentrantLock.newCondition()` gives you multiple named conditions on one lock — cleaner than
  several monitor objects.

---

## Common Mistakes

1. `if (!condition) wait();` — single check, missed wakeup on spurious return.
2. `wait()` outside `synchronized`.
3. `notify()` after releasing the lock (or never re-checking).
4. Treating a notification as durable when it isn't — signals are lost if nobody is listening.

---

## Related

- [[../00 - Index|Concurrency Concepts Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../Thread-Lifecycle/Concept|Thread Lifecycle]] · [[../../Patterns/Signaling-Pattern/Concept|Signaling Pattern]]

---

#concurrency #condition-variables #lld #concept
