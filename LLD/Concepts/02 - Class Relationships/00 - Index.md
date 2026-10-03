# Class Relationships — Index

The ways objects link to each other — **association, aggregation, composition and dependency**, split into four packages.
Click the checkboxes (`- [ ]` / `- [x]`) to toggle completion status directly in Obsidian!

---

## 📚 Key Concepts

- **Association** — peer link; both objects exist independently
- **Aggregation** — weak "has-a"; the part can outlive the whole
- **Composition** — strong "owns-a"; the part dies with the whole
- **Dependency** — temporary "uses-a" (method parameter / local)
- **Realization** — a class implements an interface
- **Lifetime test** — *"does the part survive the whole?"* decides aggregation vs composition

---

## 📋 Packages

- [ ] **01. Association** (2) — [[01 - Association/Concept|Concept]] \| [[01 - Association/Practice|Practice]]
- [ ] **02. Aggregation** (3) — [[02 - Aggregation/Concept|Concept]] \| [[02 - Aggregation/Practice|Practice]]
- [ ] **03. Composition** (3) — [[03 - Composition/Concept|Concept]] \| [[03 - Composition/Practice|Practice]]
- [ ] **04. Dependency** (1) — [[04 - Dependency/Concept|Concept]] \| [[04 - Dependency/Practice|Practice]]

*9 AlgoMaster problems across 4 packages.*

---

## 🎯 How to choose

| Package | Use when… |
|---------|-----------|
| **Association** | two peers reference each other but exist independently |
| **Aggregation** | a whole *has-a* reusable part that can outlive the whole |
| **Composition** | a whole *owns* an exclusive part that dies with the whole |
| **Dependency** | a method temporarily *uses* another object (parameter / local) |

> **Lifetime test:** *"does the part survive the whole?"* — yes → aggregation, no → composition.

---

## 🔗 Related

- [[../00 - Index|Concepts Index]]
- [[../../00 - Index|LLD Main Index]]

---

#lld #concepts #class-relationships
