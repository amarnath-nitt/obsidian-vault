# Interfaces — Concept

## What Is It?

An **interface** declares *what* a type can do without saying *how*. Unrelated classes can share the
contract, callers program against it, and implementations become swappable.

| | |
|---|---|
| **Construct** | `interface` |
| **One-liner** | A contract many types can fulfil — the basis of polymorphism |

---

## When to Use

> **Trigger keywords:** "swappable", "implement", "contract", "several kinds of"

| Trigger | Modelling Move |
|---------|----------------|
| Unrelated classes share a contract | `interface` |
| Related classes share partial implementation | `abstract class` |
| Behaviour must be swappable at runtime | interface + polymorphism (Strategy) |
| Tests need a substitute | interface + fake implementation |

---

## In Java

```java
public interface PaymentMethod {
    void pay(double amount);
    default boolean supportsRefund() { return false; }   // optional capability
}

class CreditCard implements PaymentMethod {
    public void pay(double amount) { /* card flow */ }
}
class Upi implements PaymentMethod {
    public void pay(double amount) { /* upi flow */ }
}

void checkout(PaymentMethod method, double amount) {   // caller depends on the contract
    method.pay(amount);
}
```

---

## Notes

- Interfaces are how you get **DIP** (depend on abstractions) and **ISP** (keep them small).
- Prefer **composition of small interfaces** over one fat interface.
- An interface with exactly one implementation *may* be speculative — see **YAGNI**.

---

## Common Mistakes

1. Fat interfaces that force stubs (**ISP**).
2. Interfaces that leak implementation (`getArrayList()`).
3. An interface per class — no variation, no benefit.
4. Using an interface only for "mockability" when constructor injection would do.

---

## Related

- [[../00 - Index|OOP Fundamentals Index]]
- [[../../00 - Index|Concepts Index]]
- [[../../../00 - Index|LLD Main Index]]

---

#oop #interfaces #lld #concept
