# Concurrency Concepts — Index

The vocabulary and primitives behind every thread-safe design — **14 packages**.
Click the checkboxes (`- [ ]` / `- [x]`) to toggle completion status directly in Obsidian!

---

## 📋 Packages

### 🟢 Foundations
- [ ] **01. Concurrency 101** — [[Concurrency-101/Concept|Concept]] \| [[Concurrency-101/Practice|Practice]]
- [ ] **02. Concurrency vs Parallelism** — [[Concurrency-vs-Parallelism/Concept|Concept]] \| [[Concurrency-vs-Parallelism/Practice|Practice]]
- [ ] **03. Processes vs Threads** — [[Processes-vs-Threads/Concept|Concept]] \| [[Processes-vs-Threads/Practice|Practice]]
- [ ] **04. Thread Lifecycle & States** — [[Thread-Lifecycle/Concept|Concept]] \| [[Thread-Lifecycle/Practice|Practice]]

### 🟡 Shared State & Mutual Exclusion
- [ ] **05. Race Conditions & Critical Sections** — [[Race-Conditions/Concept|Concept]] \| [[Race-Conditions/Practice|Practice]]
- [ ] **06. Mutex (Mutual Exclusion)** — [[Mutex/Concept|Concept]] \| [[Mutex/Practice|Practice]]
- [ ] **07. Semaphores** — [[Semaphores/Concept|Concept]] \| [[Semaphores/Practice|Practice]]
- [ ] **08. Condition Variables** — [[Condition-Variables/Concept|Concept]] \| [[Condition-Variables/Practice|Practice]]

### 🟡 Locking Strategies
- [ ] **09. Coarse vs Fine-grained Locking** — [[Coarse-vs-Fine-Grained-Locking/Concept|Concept]] \| [[Coarse-vs-Fine-Grained-Locking/Practice|Practice]]
- [ ] **10. Reentrant Locks** — [[Reentrant-Locks/Concept|Concept]] \| [[Reentrant-Locks/Practice|Practice]]
- [ ] **11. Try-Lock & Timed Locking** — [[Try-Lock-and-Timed-Locking/Concept|Concept]] \| [[Try-Lock-and-Timed-Locking/Practice|Practice]]

### 🔴 Advanced
- [ ] **12. Compare-and-Swap (CAS)** — [[Compare-and-Swap/Concept|Concept]] \| [[Compare-and-Swap/Practice|Practice]]
- [ ] **13. Deadlock** — [[Deadlock/Concept|Concept]] \| [[Deadlock/Practice|Practice]]
- [ ] **14. Livelock** — [[Livelock/Concept|Concept]] \| [[Livelock/Practice|Practice]]

*9 AlgoMaster exercises across 14 packages; the four foundational packages are theory + self-study.*

---

## 🎯 How to choose

| Symptom | Primitive |
|---------|-----------|
| Lost update / result depends on interleaving | **Race Conditions** → mutex or atomic |
| Only one thread may be in a section | **Mutex** (`synchronized`, `ReentrantLock`) |
| Allow *N* concurrent callers | **Semaphore** |
| Wait until a predicate becomes true | **Condition Variable** |
| Contention is killing throughput | **Coarse vs fine-grained locking** |
| The same thread must re-acquire | **Reentrant Lock** |
| Give up if you can't get in | **Try-Lock / timed lock** |
| Lock-free read-modify-write | **CAS / atomics** |
| Threads blocked forever on each other | **Deadlock** |
| Threads busy but making no progress | **Livelock** |

---

## 🔗 Related

- [[../00 - Index|Concurrency Index]]
- [[../../00 - Index|LLD Main Index]]

---

#lld #concurrency #concepts
