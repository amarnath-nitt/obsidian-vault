# Concurrency Problems — Index

Write the actual synchronization — the judge runs your class from several threads at once — **9 packages**.
Click the checkboxes (`- [ ]` / `- [x]`) to toggle completion status directly in Obsidian!

---

## 📋 Packages

### 🟢 Ordering classics
- [ ] **01. Print FooBar Alternately** — [[Print-FooBar-Alternately/Concept|Concept]] \| [[Print-FooBar-Alternately/Practice|Practice]]
- [ ] **02. Print Zero Even Odd** — [[Print-Zero-Even-Odd/Concept|Concept]] \| [[Print-Zero-Even-Odd/Practice|Practice]]
- [ ] **03. Fizz Buzz Multithreaded** — [[Fizz-Buzz-Multithreaded/Concept|Concept]] \| [[Fizz-Buzz-Multithreaded/Practice|Practice]]
- [ ] **04. Building H2O Molecule** — [[Building-H2O-Molecule/Concept|Concept]] \| [[Building-H2O-Molecule/Practice|Practice]]

### 🟡 Thread-safe data structures
- [ ] **05. Thread-Safe Cache with TTL** — [[Thread-Safe-Cache-with-TTL/Concept|Concept]] \| [[Thread-Safe-Cache-with-TTL/Practice|Practice]]
- [ ] **06. Concurrent HashMap** — [[Concurrent-HashMap/Concept|Concept]] \| [[Concurrent-HashMap/Practice|Practice]]
- [ ] **07. Thread-Safe Blocking Queue** — [[Thread-Safe-Blocking-Queue/Concept|Concept]] \| [[Thread-Safe-Blocking-Queue/Practice|Practice]]
- [ ] **08. Concurrent Bloom Filter** — [[Concurrent-Bloom-Filter/Concept|Concept]] \| [[Concurrent-Bloom-Filter/Practice|Practice]]

### 🔴 Algorithms
- [ ] **09. Multi-threaded Merge Sort** — [[Multithreaded-Merge-Sort/Concept|Concept]] \| [[Multithreaded-Merge-Sort/Practice|Practice]]

*9 AlgoMaster exercises — one per package.*

---

## 🎯 How to choose

| Problem family | The hard part |
|----------------|---------------|
| **Ordering classics** | a state variable + `while` predicate over a lock/condition |
| **Thread-safe structures** | linearizability under concurrent read-modify-write |
| **Algorithms** | bounding parallelism (worker budget) while preserving correctness |

---

## 🔗 Related

- [[../00 - Index|Concurrency Index]]
- [[../Concepts/00 - Index|Concurrency Concepts]]
- [[../Patterns/00 - Index|Concurrency Patterns]]
- [[../../00 - Index|LLD Main Index]]

---

#lld #concurrency #problems
