# Abstraction — Concept

## What Is It?

Expose **what** an object does and hide **how** it does it. Callers depend on a small, stable
surface; the mechanism can change without touching them.

| | |
|---|---|
| **Pillar** | Abstraction |
| **One-liner** | Expose *what*, hide *how* |

---

## When to Use

> **Trigger keywords:** "the caller shouldn't care how", "swap the implementation", "hide the complexity"

| Trigger | Modelling Move |
|---------|----------------|
| Callers need only the outcome | interface / abstract class |
| Several implementations differ internally | one abstraction, many impls |
| A complex subsystem needs one entry point | **Facade** (see Patterns) |

---

## In Java

```java
// WHAT: the contract callers see
public interface PaymentMethod {
    void pay(double amount);
}

// HOW: hidden behind the contract
public class CreditCard implements PaymentMethod {
    public void pay(double amount) { /* tokenise, call acquirer, retry */ }
}
public class Upi implements PaymentMethod {
    public void pay(double amount) { /* build intent, poll status */ }
}
```

---

## Abstraction vs Encapsulation

| | Focus | Question it answers |
|---|-------|---------------------|
| **Abstraction** | the *interface* | *What* can you do with it? |
| **Encapsulation** | the *implementation* | *How* is it protected and changed? |

They complement each other: abstraction defines the surface, encapsulation protects what's behind it.

---

## Notes

- A **leaky abstraction** exposes internals (`getArrayList()`, raw SQL strings).
- Abstraction quality is measured by how little a caller must know.

---

## Common Mistakes

1. Interfaces that mirror implementation details.
2. Abstracting before a second implementation exists (**YAGNI**).
3. Confusing abstraction with "make it an interface" everywhere.

---

## Related

- [[../00 - Index|OOP Fundamentals Index]]
- [[../../00 - Index|Concepts Index]]
- [[../../../00 - Index|LLD Main Index]]

---

#oop #abstraction #lld #concept
