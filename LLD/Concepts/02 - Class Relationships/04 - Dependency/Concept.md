# Dependency — Concept

## What Is It?

A **temporary "uses-a"**: one class uses another only *during a method call* — typically as a
parameter or a local variable — and does **not** store a reference to it.

| | |
|---|---|
| **Relationship** | Dependency (`-->` dashed) |
| **One-liner** | A method temporarily uses another object; nothing is kept |

---

## When to Use

> **Trigger keywords:** "helper", "formatter", "calculates using", "passes to", "one-off"

| Trigger | Move |
|---------|------|
| A class uses a collaborator only inside one method | dependency (parameter) |
| The collaborator is stateless/does one job | dependency, not a field |
| You're tempted to store it "just in case" | keep it a dependency |

---

## In Java

```java
class AlertPreview {
    // the formatter is a parameter — used, not stored (dependency)
    String preview(String message, Formatter formatter) {
        return formatter.format(message);
    }
}
```

**The three "uses" relationships, weakest → strongest:**

| | Relationship | Lifetime |
|---|---|---|
| 1 | **Dependency** `-->` | used during a call, not stored |
| 2 | **Association** `—→` | stored, but peers are independent |
| 3 | **Aggregation / Composition** | stored *and* ownership applies |

---

## Notes

- Dependencies are the cheapest relationship — change one class without ripple effects.
- Turning a dependency into a stored field **strengthens** the relationship; do it deliberately.
- Constructor injection converts "dependency created internally" into "dependency injected" (**DIP**).

---

## Common Mistakes

1. Storing a collaborator as a field when it's only used once per call.
2. Ignoring dependencies in the class diagram — they still create compile-time coupling.
3. Confusing dependency (temporary) with association (stored).

---

## Related

- [[../00 - Index|Class Relationships Index]]
- [[../../00 - Index|Concepts Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../01 - Association/Concept|Association]]

---

#relationships #dependency #lld #concept
