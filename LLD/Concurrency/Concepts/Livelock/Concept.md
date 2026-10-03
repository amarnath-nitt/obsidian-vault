# Livelock — Concept

## What Is It?

Threads are **actively running and repeatedly changing state** — yet **no one makes progress**.
Unlike deadlock (everyone is *blocked*), in a livelock everyone is *busy* and futile.

| | **Deadlock** | **Livelock** |
|---|---|---|
| Threads are | blocked / waiting | running / retrying |
| CPU usage | idle | **busy, spinning** |
| Cause | circular wait | endlessly reacting to each other |
| Classic fix | ordering / try-lock | back-off, randomised delay, priority |

---

## When to Use

> **Trigger keywords:** "keeps retrying", "CPU at 100%, nothing happens", "both step aside", "starving each other"

| Symptom | Suspect |
|---------|---------|
| High CPU, zero throughput | livelock |
| Two people dodging each other in a corridor, forever | livelock (the textbook image) |
| Threads blocked, low CPU | deadlock (not livelock) |

---

## Canonical example

```java
// ❌ Two courteous threads that always yield to each other
while (!myWork.isDone()) {
    if (otherLock.isHeldByOther()) {      // "after you"
        yield();                          // release, retry immediately
        continue;                         // → both keep yielding forever
    }
    doWork();
}
```

Also common: **two CAS loops that keep colliding** on the same variable, or two optimisers that
alternate and undo each other's work.

---

## The fix: introduce asymmetry or back-off

```java
// ✅ Randomised / exponential back-off: break the perfect symmetry
while (!myWork.isDone()) {
    if (otherLock.isHeldByOther()) {
        Thread.sleep(ThreadLocalRandom.current().nextInt(1, 10));  // wait a random while
        continue;
    }
    doWork();
}
```

Ways to break livelock:
1. **Back-off** (fixed, exponential, or **randomised**) — the most common.
2. **Priority / ordering** — one party is allowed to win.
3. **Give up after N attempts** — turn it into a bounded failure instead of infinite retry.

---

## Notes

- Livelock often appears **inside** lock-free code: optimistic retries that never land.
- It's related to **starvation** — one thread may be *mostly* starved while others progress; a
  livelock is when *nobody* progresses.
- Detection is hard: everything looks "busy". Look at throughput, not at thread states.

---

## Common Mistakes

1. Diagnosing "CPU pegged, nothing completes" as deadlock — deadlock leaves the CPU idle.
2. Unbounded retry loops with no back-off (in CAS or try-lock code).
3. Perfectly symmetric participants with no tie-breaker.
4. Assuming fairness is automatic — most locks/semaphores are **unfair**.

---

## Related

- [[../00 - Index|Concurrency Concepts Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../Deadlock/Concept|Deadlock]] · [[../Compare-and-Swap/Concept|CAS]]

---

#concurrency #livelock #lld #concept
