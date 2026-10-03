# Enums — Concept

## What Is It?

An **enum** models a *closed set of constants* — and, uniquely, it can carry **behaviour** with
them. It replaces magic strings like `"PENDING"` with a type the compiler checks.

| | |
|---|---|
| **Construct** | `enum` |
| **One-liner** | A closed set of values, each with its own behaviour |

---

## When to Use

> **Trigger keywords:** "status", "type", "kind", "the same string in ten places"

| Trigger | Modelling Move |
|---------|----------------|
| A fixed set of options (`PENDING`, `SHIPPED`, `DONE`) | `enum`, never a string |
| Each option behaves differently | enum **methods** (or a `switch` over the enum) |
| A value must be serialisable/stable | enum name is the wire format |

---

## In Java

```java
public enum TicketStatus {
    OPEN     { boolean canClose() { return true; } },
    CLOSED   { boolean canClose() { return false; } },
    CANCELLED{ boolean canClose() { return false; } };

    abstract boolean canClose();
}

// Exhaustive switching — the compiler warns when you add a new constant
String label(TicketStatus s) {
    return switch (s) {
        case OPEN -> "Open";
        case CLOSED -> "Closed";
        case CANCELLED -> "Cancelled";
    };
}
```

---

## Notes

- Enums can have fields, constructors and methods — use that for per-constant behaviour.
- An exhaustive `switch` over an enum is **safe**: the compiler catches missing cases.
- `null` is rarely the right enum value — prefer an explicit `UNKNOWN` constant.

---

## Common Mistakes

1. Magic strings / integers instead of an enum (no type safety, typos at runtime).
2. An enum with a dozen unrelated methods — cohesion lost.
3. Storing database ids in the enum name and then renaming constants.

---

## Related

- [[../00 - Index|OOP Fundamentals Index]]
- [[../../00 - Index|Concepts Index]]
- [[../../../00 - Index|LLD Main Index]]

---

#oop #enums #lld #concept
