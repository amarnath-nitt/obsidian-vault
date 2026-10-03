# Processes vs Threads — Concept

## What Is It?

| | **Process** | **Thread** |
|---|---|---|
| **Definition** | an isolated address space with its own resources | a lightweight unit *inside* a process |
| **Memory** | private | **shared** with sibling threads |
| **Creation cost** | high (new address space) | low (shares the parent's) |
| **Communication** | IPC: pipes, sockets, shared memory, messages | direct — read/write the same heap |
| **Crash isolation** | one process crashing does not kill others | one thread crashing can kill the process |
| **Switching cost** | expensive (TLB / address-space switch) | cheaper |

---

## When to Use

> **Trigger keywords:** "isolation", "crash", "shared memory", "IPC", "overhead"

| Need | Choose |
|------|--------|
| Isolation, fault tolerance, true separation | **Process** |
| Cheap concurrency over shared state | **Thread** |
| Parallel CPU work with shared data | **Threads / thread pool** |
| Run untrusted or unstable code | **Process** |

---

## The key line

> **Threads share memory; processes do not.**

Sharing memory is exactly what makes threads *fast* — and exactly what makes them *dangerous*.
Every race condition, deadlock and visibility problem in this track exists **because** threads share
a heap.

```text
Process A            Process B
┌──────────────┐     ┌──────────────┐
│ heap (own)   │     │ heap (own)   │   ← separate; must use IPC
│ ┌──────────┐ │     │              │
│ │ Thread 1 │ │     │ Thread 1     │
│ │ Thread 2 │ │     │ Thread 2     │
│ └──────────┘ │     │              │
└──────────────┘     └──────────────┘
```

---

## Notes

- In Java, a thread is *green or OS-mapped* depending on the version, but every thread in a JVM
  shares the same heap — hence `synchronized`, `volatile`, `java.util.concurrent`.
- **Fork-join / parallelism** uses threads for shared-memory speed; **microservice isolation** uses processes.

---

## Common Mistakes

1. Saying "threads are just smaller processes" — the real difference is **memory sharing**.
2. Assuming threads are always faster — contended locks can make them slower than one thread.
3. Forgetting that a `ThreadLocal` is still per-*thread*, not per-process-isolated memory.

---

## Related

- [[../00 - Index|Concurrency Concepts Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../Thread-Lifecycle/Concept|Thread Lifecycle]]

---

#concurrency #lld #concept
