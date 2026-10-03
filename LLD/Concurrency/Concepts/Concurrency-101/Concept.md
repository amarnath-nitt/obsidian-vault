# Concurrency 101 — Concept

## What Is It?

**Concurrency** is the ability of a program to make progress on **multiple tasks**, interleaving their execution. In LLD interviews, concurrency is a normal follow-up after your single-threaded design: *"now make it thread-safe."* You must be able to explain **why** a race exists and **which primitive** fixes it.

---

## When to Use

> **Trigger keywords:** "multiple threads", "simultaneously", "shared state", "thread-safe", "lock", "atomic"

| Trigger | Response |
|---------|----------|
| **Shared mutable state** across threads | protect with a lock / atomic |
| **Producer → consumer** hand-off | blocking queue / condition variable |
| **Limit concurrent resource use** | semaphore / thread pool |
| **Read-heavy, rare writes** | read-write lock |
| **Simple counter / flag** | `AtomicInteger` / `volatile` |

---

## Core Vocabulary

| Term | Meaning |
|------|---------|
| **Process** | Isolated address space; heavy to create |
| **Thread** | Lightweight unit *within* a process; shares memory |
| **Race condition** | Result depends on thread interleaving |
| **Critical section** | Code that must run atomically |
| **Atomicity** | An operation that completes wholly or not at all |
| **Visibility** | A write by one thread being seen by another (`volatile`) |
| **Ordering** | Preventing compiler/CPU reordering (`happens-before`) |
| **Deadlock** | Threads blocked forever waiting on each other |
| **Livelock** | Threads active but making no progress |

---

## The Race Condition, Visualised

```java
// counter starts at 0; two threads each do ++ 1,000,000 times
counter++;   // NOT atomic — it is: read → add → write
```

```
Thread A: read 0 ──┐
Thread B: read 0 ──┼─► both read 0
Thread A: write 1
Thread B: write 1   ← lost update! final = 1, expected = 2
```

**Fix options:** `synchronized`, `ReentrantLock`, or `AtomicInteger.incrementAndGet()` (CAS loop, lock-free).

---

## Synchronization Primitives (Java)

| Primitive | Use | Java |
|-----------|-----|------|
| `synchronized` | mutual exclusion, reentrant | `synchronized (obj) {}` |
| `ReentrantLock` | explicit lock, `tryLock`, fairness | `java.util.concurrent.locks` |
| `Semaphore` | allow **N** permits | `Semaphore(3)` |
| `CountDownLatch` | wait for N events | one-shot gate |
| `CyclicBarrier` | N threads rendezvous | reusable barrier |
| `AtomicX` | lock-free read-modify-write | `AtomicInteger`, `AtomicReference` |
| `volatile` | visibility + ordering (not atomicity) | `volatile int flag` |
| BlockingQueue | safe producer-consumer | `ArrayBlockingQueue` |

---

## Common Mistakes

1. **Assuming `++` is atomic** — it is not; use `AtomicInteger`.
2. **Using `volatile` for compound actions** — `volatile` gives visibility, not atomicity.
3. **Locking on the wrong object** — lock on a `private final` monitor, not a publicly reachable one.
4. **Holding a lock while doing I/O** — kills throughput; shrink the critical section.
5. **Inconsistent lock ordering** — the classic cause of **deadlock**.
6. **Forgotten `wait` loop** — always `while (!condition) wait();` to guard against spurious wakeups.

---

## Related Patterns

- [[../../Patterns/Producer-Consumer-Pattern/Concept|Producer-Consumer Pattern]]
- [[../Deadlock/Concept|Deadlock]]
- [[../Compare-and-Swap/Concept|Compare-and-Swap (CAS)]]

---

#concurrency #threads #lld #concept