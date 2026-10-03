# Association — Concept

## What Is It?

A **peer link** between two objects that both exist independently. Neither owns the other, and
neither's lifetime depends on it — they simply *know about* or *use* each other.

| | |
|---|---|
| **Relationship** | Association (`-->`) |
| **One-liner** | A peer link; both objects exist independently |

---

## When to Use

> **Trigger keywords:** "links", "enrols", "follows", "references", "registry"

| Trigger | Move |
|---------|------|
| Two entities are meaningful on their own | association |
| The link itself carries data (dates, role) | model the link as its own class |
| The link is many-to-many | an **association class** (`Enrollment`) |

---

## In Java

```java
class Student { final String id; Student(String id) { this.id = id; } }
class Course  { final String code; Course(String code) { this.code = code; } }

// The link is first-class — it can carry its own data
class Enrollment {
    private final Student student;
    private final Course  course;
    private final LocalDate enrolledOn;

    Enrollment(Student s, Course c, LocalDate d) {
        this.student = s; this.course = c; this.enrolledOn = d;
    }
}
```

---

## Notes

- Association is the **weakest** of the "has-a" family — no ownership, no shared lifetime.
- When the relationship has attributes of its own (`role`, `since`, `grade`), it deserves a class.
- Weaker than **aggregation** (shared part) which is weaker than **composition** (owned part).

---

## Common Mistakes

1. Modelling a rich relationship as a bare `List<Student>` and losing its data.
2. Adding ownership semantics where none exist.
3. Omitting the relationship class in a class diagram — the relationships *are* the design.

---

## Related

- [[../00 - Index|Class Relationships Index]]
- [[../../00 - Index|Concepts Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../../02 - Class Relationships/02 - Aggregation/Concept|Aggregation]] · [[../../02 - Class Relationships/03 - Composition/Concept|Composition]]
---

#relationships #association #lld #concept
