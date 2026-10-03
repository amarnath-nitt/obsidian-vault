# OOP Fundamentals — Index

Foundations of object-oriented modelling: **classes, enums, interfaces and the four pillars**, split into seven packages.
Click the checkboxes (`- [ ]` / `- [x]`) to toggle completion status directly in Obsidian!

---

## 📚 Key Concepts

- **Class** — blue print: fields (state) + methods (behaviour)
- **Object** — a runtime instance of a class
- **Encapsulation** — `private` fields, public behaviour
- **Abstraction** — interface / abstract class hides implementation
- **Inheritance** — reuse via `extends` / `implements`
- **Polymorphism** — compile-time (overloading) vs runtime (overriding)

---

## 📋 Packages

### 🟢 Modelling basics
- [ ] **01. Classes and Objects** (3) — [[01 - Classes and Objects/Concept|Concept]] \| [[01 - Classes and Objects/Practice|Practice]]
- [ ] **02. Enums** (2) — [[02 - Enums/Concept|Concept]] \| [[02 - Enums/Practice|Practice]]
- [ ] **03. Interfaces** (2) — [[03 - Interfaces/Concept|Concept]] \| [[03 - Interfaces/Practice|Practice]]

### 🟡 The Four Pillars
- [ ] **04. Encapsulation** (3) — [[04 - Encapsulation/Concept|Concept]] \| [[04 - Encapsulation/Practice|Practice]]
- [ ] **05. Abstraction** (2) — [[05 - Abstraction/Concept|Concept]] \| [[05 - Abstraction/Practice|Practice]]
- [ ] **06. Inheritance** (2) — [[06 - Inheritance/Concept|Concept]] \| [[06 - Inheritance/Practice|Practice]]
- [ ] **07. Polymorphism** (2) — [[07 - Polymorphism/Concept|Concept]] \| [[07 - Polymorphism/Practice|Practice]]

*16 AlgoMaster problems across 7 packages.*

---

## 🎯 How to choose

| Package | Use when… |
|---------|-----------|
| **Classes and Objects** | you're modelling a domain noun with state + behaviour |
| **Enums** | you have a fixed set of values that also carry behaviour |
| **Interfaces** | you need a swappable contract between caller and implementation |
| **Encapsulation** | you must protect invariants behind a small public API |
| **Abstraction** | clients should depend on *what* happens, not *how* |
| **Inheritance** | there is a genuine *is-a* with shared base behaviour |
| **Polymorphism** | one operation, several behaviours — replaces an `if/else` chain |

---

## 🔗 Related

- [[../00 - Index|Concepts Index]]
- [[../../00 - Index|LLD Main Index]]

---

#lld #concepts #oop-fundamentals
