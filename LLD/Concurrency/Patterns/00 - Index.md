# Concurrency Patterns — Index

Recurring shapes for coordinating threads — **4 packages**.
Click the checkboxes (`- [ ]` / `- [x]`) to toggle completion status directly in Obsidian!

---

## 📋 Packages

- [ ] **01. Signaling Pattern** — [[Signaling-Pattern/Concept|Concept]] \| [[Signaling-Pattern/Practice|Practice]] · *2 exercises*
- [ ] **02. Thread Pool Pattern** — [[Thread-Pool-Pattern/Concept|Concept]] \| [[Thread-Pool-Pattern/Practice|Practice]] · *1 exercise*
- [ ] **03. Producer-Consumer Pattern** — [[Producer-Consumer-Pattern/Concept|Concept]] \| [[Producer-Consumer-Pattern/Practice|Practice]] · *1 exercise*
- [ ] **04. Reader-Writer Pattern** — [[Reader-Writer-Pattern/Concept|Concept]] \| [[Reader-Writer-Pattern/Practice|Practice]] · *2 exercises*

*6 AlgoMaster exercises across 4 packages.*

---

## 🎯 How to choose

| Pattern | Use when… |
|---------|-----------|
| **Signaling** | one thread must wait until another has *signalled* (often stateful / versioned) |
| **Thread Pool** | you need bounded, reusable workers instead of one thread per task |
| **Producer-Consumer** | one side produces, the other consumes, and the buffer is bounded |
| **Reader-Writer** | reads are frequent and can share; writes must be exclusive |

---

## 🔗 Related

- [[../00 - Index|Concurrency Index]]
- [[../Concepts/00 - Index|Concurrency Concepts]]
- [[../../00 - Index|LLD Main Index]]

---

#lld #concurrency #patterns
