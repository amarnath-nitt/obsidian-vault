# Encapsulation — Concept

## What Is It?

Hide the internal state behind a small, controlled public API — and let **methods on the class**
be the only way to change it. The point is not `private` syntax; it's keeping **invariants true**.

| | |
|---|---|
| **Pillar** | Encapsulation |
| **One-liner** | Hide state, expose behaviour |

---

## When to Use

> **Trigger keywords:** "public field", "anyone can set", "invalid state", "getters and setters everywhere"

| Smell | Move |
|-------|------|
| `public double balance;` | make it private; add `deposit()` |
| Callers set fields directly | the class validates and applies the change |
| Data class with only getters/setters | move the behaviour in |

---

## In Java

```java
// ❌ Anyone can put the account into an invalid state
public class BankAccount {
    public double balance;
}

// ✅ State is private; only validated methods change it
public class BankAccount {
    private double balance;

    public void deposit(double amount) {
        if (amount <= 0) throw new IllegalArgumentException("amount > 0");
        balance += amount;
    }
    public void withdraw(double amount) {
        if (amount > balance) throw new IllegalStateException("insufficient funds");
        balance -= amount;
    }
    public double getBalance() { return balance; }   // read-only view
}
```

---

## Notes

- Encapsulation is what makes **invariants enforceable** — one choke point for every change.
- Returning **unmodifiable views / copies** preserves it (`List.copyOf(...)`).
- Getters that hand out the internal mutable list break encapsulation just as badly as a public field.

---

## Common Mistakes

1. Public mutable fields (or public final fields holding mutable objects).
2. Getters/setters with no logic — the class stops owning its own rules (**anemic model**).
3. Exposing internal collections so callers can mutate them.
4. Confusing encapsulation with "private everything" — the API still needs to be usable.

---

## Related

- [[../00 - Index|OOP Fundamentals Index]]
- [[../../00 - Index|Concepts Index]]
- [[../../../00 - Index|LLD Main Index]]

---

#oop #encapsulation #lld #concept
