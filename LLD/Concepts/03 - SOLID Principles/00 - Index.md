# SOLID Principles — Index

The five SOLID principles — **SRP · OCP · LSP · ISP · DIP** — split into five packages.
Click the checkboxes (`- [ ]` / `- [x]`) to toggle completion status directly in Obsidian!

---

## 📚 Key Concepts

| Letter | Principle | One-liner |
|--------|-----------|-----------|
| **S** | Single Responsibility | A class should have **one reason to change** |
| **O** | Open/Closed | Open for **extension**, closed for **modification** |
| **L** | Liskov Substitution | Subtypes must be **substitutable** for their base type |
| **I** | Interface Segregation | No client forced to depend on methods it **doesn't use** |
| **D** | Dependency Inversion | Depend on **abstractions**, not concretions |

| Smell | Principle to apply |
|-------|--------------------|
| A class does "X **and** Y" | **SRP** — split it |
| Adding a feature means editing a growing `switch` | **OCP** — use polymorphism |
| A subclass throws on an inherited method | **LSP** — fix the hierarchy |
| An interface has methods some implementers stub out | **ISP** — split the interface |
| A class `new`s its collaborators directly | **DIP** — inject abstractions |

---

## 📋 Packages

### 🟢 Start here
- [ ] **S. Single Responsibility** (3) — [[S - Single Responsibility/Concept|Concept]] \| [[S - Single Responsibility/Practice|Practice]]
- [ ] **O. Open/Closed** (2) — [[O - Open Closed/Concept|Concept]] \| [[O - Open Closed/Practice|Practice]]

### 🟡 Contracts & interfaces
- [ ] **L. Liskov Substitution** (2) — [[L - Liskov Substitution/Concept|Concept]] \| [[L - Liskov Substitution/Practice|Practice]]
- [ ] **I. Interface Segregation** (3) — [[I - Interface Segregation/Concept|Concept]] \| [[I - Interface Segregation/Practice|Practice]]

### 🔴 Wiring
- [ ] **D. Dependency Inversion** (0 exercises) — [[D - Dependency Inversion/Concept|Concept]] \| [[D - Dependency Inversion/Practice|Practice]]

*10 AlgoMaster problems across 4 packages; DIP is theory + self-study (no dedicated AlgoMaster exercise yet).*

> **Remember:** SOLID is a set of *guidelines*, not laws. Apply a principle when you feel the
> corresponding **pain** — over-application creates more complexity than it removes.

---

## 🔗 Related

- [[../00 - Index|Concepts Index]]
- [[../../00 - Index|LLD Main Index]]

---

#lld #concepts #solid
