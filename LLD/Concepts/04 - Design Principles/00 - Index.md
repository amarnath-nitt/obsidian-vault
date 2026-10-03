# Design Principles — Index

Pragmatic principles beyond SOLID — **DRY · KISS · YAGNI · Law of Demeter · Separation of Concerns · Coupling & Cohesion** — split into six packages.
Click the checkboxes (`- [ ]` / `- [x]`) to toggle completion status directly in Obsidian!

---

## 📚 Key Concepts

- **DRY** — one authoritative home for each piece of knowledge
- **KISS** — the simplest design that works
- **YAGNI** — don't build for imagined futures
- **Law of Demeter** — talk to friends, not strangers
- **Separation of Concerns** — one module, one concern
- **Coupling & Cohesion** — low coupling between, high cohesion within
- **Composing Objects** — prefer composition over inheritance

---

## 📋 Packages

### 🟢 Quick wins
- [ ] **01. DRY** (2) — [[01 - DRY/Concept|Concept]] \| [[01 - DRY/Practice|Practice]]
- [ ] **02. KISS** (2) — [[02 - KISS/Concept|Concept]] \| [[02 - KISS/Practice|Practice]]
- [ ] **03. YAGNI** (2) — [[03 - YAGNI/Concept|Concept]] \| [[03 - YAGNI/Practice|Practice]]

### 🟡 Structure
- [ ] **04. Law of Demeter** (3) — [[04 - Law of Demeter/Concept|Concept]] \| [[04 - Law of Demeter/Practice|Practice]]
- [ ] **05. Separation of Concerns** (2) — [[05 - Separation of Concerns/Concept|Concept]] \| [[05 - Separation of Concerns/Practice|Practice]]

### 🔴 Architecture
- [ ] **06. Coupling and Cohesion** (2) — [[06 - Coupling and Cohesion/Concept|Concept]] \| [[06 - Coupling and Cohesion/Practice|Practice]]

*13 AlgoMaster problems across 6 packages.*

---

## 🎯 How to choose

| Principle | Smell | Fix |
|-----------|-------|-----|
| **DRY** | the same rule is written in several places | give each piece of knowledge one home |
| **KISS** | clever nested logic for a simple rule | early returns, named constants, obvious flow |
| **YAGNI** | speculative abstractions nobody asked for | delete them; add complexity when required |
| **Law of Demeter** | `a.getB().getC().doSomething()` chains | add delegating methods; talk to one friend |
| **Separation of Concerns** | one class parses, validates and persists | split into parser / validator / repository |
| **Coupling & Cohesion** | a change ripples across many classes | depend on interfaces; one module, one purpose |

---

## 🔗 Related

- [[../00 - Index|Concepts Index]]
- [[../../00 - Index|LLD Main Index]]

---

#lld #concepts #design-principles
