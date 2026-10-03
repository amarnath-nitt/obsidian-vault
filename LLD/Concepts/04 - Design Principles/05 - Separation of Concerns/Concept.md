# Separation of Concerns — Concept

## What Is It?

Each module should address **one concern** and hide it from the others. In LLD the usual concerns
are: HTTP/parsing, domain rules, persistence, and presentation.

| | |
|---|---|
| **Principle** | Separation of Concerns (SoC) |
| **One-liner** | One module, one concern |

---

## When to Use

> **Trigger keywords:** "one class does everything", "parsing + rules + SQL together", "can't test without the database"

| Smell | Move |
|-------|------|
| A service parses, validates, persists and renders | split into parser / validator / repo / writer |
| Business rules live inside a controller | move rules to a domain service |
| Tests need a real DB or HTTP stack | isolate the concern behind an interface |

---

## In Java

```java
// ❌ Four concerns tangled in one method
class OrderHandler {
    void handle(String raw) {
        String[] c = raw.split(",");            // parsing
        if (c.length != 3) return;              // validation
        db.execute("insert ...");               // persistence
        System.out.println(toJson(c));          // presentation
    }
}

// ✅ One concern per collaborator, orchestrated thinly
Order o = parser.parse(raw);
validator.validate(o);
repository.save(o);
return writer.write(o);
```

---

## Notes

- SoC is the **architectural** parent of **SRP** (class level) and of layering.
- The coordinator between concerns should hold **no rules of its own**.
- Persistence is nearly always worth isolating behind a repository interface (also **DIP**).

---

## Common Mistakes

1. Splitting so finely that every class is a one-liner (over-fragmentation).
2. Leaving a "god coordinator" that still contains domain logic.
3. Putting domain rules in the HTTP layer "just for now".

---

## Related

- [[../00 - Index|Design Principles Index]]
- [[../../00 - Index|Concepts Index]]
- [[../../../00 - Index|LLD Main Index]]

---

#design-principles #separation-of-concerns #lld #concept
