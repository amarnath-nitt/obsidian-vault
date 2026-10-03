# Classes & Objects — Concept

## What Is It?

A **class** is a blueprint: fields (state) + methods (behaviour). An **object** is a runtime
instance of that blueprint. Almost every LLD interview starts by deciding *which nouns become
classes* and *which verbs become their methods*.

| | |
|---|---|
| **Construct** | Class / Object |
| **One-liner** | Bundle the state with the behaviour that operates on it |

---

## When to Use

> **Trigger keywords:** "entity", "role", "model", "track", "has a …"

| Trigger | Modelling Move |
|---------|----------------|
| A **noun** with data + actions | Create a **class** with fields + methods |
| A **fixed set** of options (status, type) | Use an **enum** |
| A value with no identity, only contents | Use a **record** (value object) |
| Two classes share a **contract** | Define an **interface** |

---

## In Java

```java
public class BankAccount {
    private final String id;
    private double balance;                      // state

    public void deposit(double amount) {         // behaviour guarding its own state
        if (amount <= 0) throw new IllegalArgumentException("amount > 0");
        balance += amount;
    }
    public double getBalance() { return balance; }
}
```

**Design a class by asking three questions:**
1. What **state** must it remember?
2. What **behaviour** may change that state — and who else may change it?
3. What **invariants** must always hold?

---

## Notes

- Keep **behaviour with the data it needs** — avoid anemic models full of getters/setters.
- Prefer a **meaningful name** from the domain: `Ride`, `Driver`, `Invoice` — not `Manager2`.
- A class should be describable in **one short sentence** without the word "and".

---

## Common Mistakes

1. **Anemic models** — pure data holders; the logic leaks into "manager" services.
2. **God classes** — one class does everything (see **SRP**).
3. **Public mutable fields** — breaks encapsulation; use private + methods.
4. **Naming by mechanism** rather than domain (`DataHolder`, `Helper2`).

---

## Related

- [[../00 - Index|OOP Fundamentals Index]]
- [[../../00 - Index|Concepts Index]]
- [[../../../00 - Index|LLD Main Index]]

---

#oop #classes #lld #concept
