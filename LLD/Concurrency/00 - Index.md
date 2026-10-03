# Concurrency & Multi-threading — Index

Threads, synchronization primitives, and concurrency patterns — a favourite LLD interview topic.
Click the checkboxes (`- [ ]` / `- [x]`) to toggle completion status directly in Obsidian!

---

## 🗂️ Groups

### 🧠 Concepts (14)
- Entry point: [[Concepts/00 - Index|Concepts Index]]
- **Concurrency 101 · Concurrency vs Parallelism · Processes vs Threads · Thread Lifecycle · Race Conditions · Mutex · Semaphores · Condition Variables · Locking · Reentrant Locks · Try-Lock · CAS · Deadlock · Livelock**
- The vocabulary and primitives behind every thread-safe design

### 🧩 Patterns (4)
- Entry point: [[Patterns/00 - Index|Patterns Index]]
- **Signaling · Thread Pool · Producer-Consumer · Reader-Writer**
- Recurring shapes for coordinating threads

### 💻 Problems (9)
- Entry point: [[Problems/00 - Index|Problems Index]]
- **FooBar · Zero Even Odd · Fizz Buzz · H2O · TTL Cache · Concurrent HashMap · Blocking Queue · Bloom Filter · Merge Sort**
- Write the actual synchronization; the judge runs it from several threads at once

*24 AlgoMaster concurrency exercises across 27 packages — all from [AlgoMaster · Concurrency Practice](https://algomaster.io/practice/concurrency).*

---

## 🧭 Key Primitives at a Glance

| Primitive | Purpose | Java Type |
|-----------|---------|-----------|
| Mutex / Lock | Only one thread in a critical section | `synchronized`, `ReentrantLock` |
| Semaphore | Allow N concurrent permits | `java.util.concurrent.Semaphore` |
| Condition | Wait for a predicate to become true | `Condition`, `wait/notify` |
| Atomic | Lock-free read-modify-write | `AtomicInteger`, `CAS` |
| Barrier / Latch | Coordinate a fixed number of threads | `CountDownLatch`, `CyclicBarrier` |

---

## 🔗 Related

- [[../Concepts/00 - Index|LLD Concepts Index]]
- [[../Patterns/00 - Index|Design Patterns Index]]
- [[../00 - Index|LLD Main Index]]

---

#lld #concurrency
