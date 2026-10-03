# Dependency Inversion — Concept

## What Is It?

High-level modules should depend on **abstractions**, not on concrete low-level implementations —
and the details should be **injected**, not created internally.

| | |
|---|---|
| **Letter** | **D** |
| **Principle** | Dependency Inversion |
| **One-liner** | Depend on abstractions; inject the concretions |

---

## When to Use

> **Trigger keywords:** "hard to test", "new `MySqlDatabase()` inside a service", "can't swap the implementation"

| Smell | Move |
|-------|------|
| A service `new`s its collaborator | define an interface, inject it |
| Business logic depends on a concrete driver/SDK | invert: the abstraction lives with the high-level module |
| Tests need a real database to run | substitute a fake behind the same interface |

---

## In Java

```java
// ❌ OrderService is glued to a concrete database
class OrderService {
    private final MySqlDatabase db = new MySqlDatabase();
}

// ✅ Depend on an interface; inject the implementation
interface OrderRepository { void save(Order o); }

class OrderService {
    private final OrderRepository repo;
    OrderService(OrderRepository repo) { this.repo = repo; }   // injected
}
```

**This is also the definition of constructor injection** — the mechanism most interviews expect when
you say "DIP".

---

## Notes

- DIP is *not* the same as the Dependency Rule (clean architecture) but they overlap.
- The abstraction should usually live **with the high-level module** that needs it.
- Pair with **ISP**: a narrow interface is easier to satisfy and to fake in tests.

---

## Common Mistakes

1. "Inverting" into forty one-method interfaces nobody can navigate.
2. Creating an interface for every class (1:1 interfaces add nothing).
3. Hiding dependencies in a service locator instead of injecting them.

---

## Related

- [[../00 - Index|SOLID Index]]
- [[../../00 - Index|Concepts Index]]
- [[../../../00 - Index|LLD Main Index]]

---

#solid #dip #lld #concept
