# Liskov Substitution — Concept

## What Is It?

Subtypes must be **substitutable** for their base type: wherever the base is expected, a subclass
instance must work without callers noticing — no crashes, no changed meaning, no surprises.

| | |
|---|---|
| **Letter** | **L** |
| **Principle** | Liskov Substitution |
| **One-liner** | Subclasses honour the base contract |

---

## When to Use

> **Trigger keywords:** "subclass throws `UnsupportedOperationException`", "works for A but not B", "broken hierarchy"

| Smell | Move |
|-------|------|
| An inherited method throws / is a no-op | the subtype isn't really a subtype |
| A subclass weakens a precondition or silently changes results | fix the abstraction |
| `Square extends Rectangle` breaks setters | model them as separate immutable types |

---

## In Java

```java
// ❌ Square breaks Rectangle's setters (width and height are coupled)
class Rectangle {
    void setWidth(int w) { ... }
    void setHeight(int h) { ... }
}
class Square extends Rectangle {
    void setWidth(int w) { super.setWidth(w); super.setHeight(w); }  // surprise!
}

// ✅ A common immutable abstraction both can honour
abstract class Shape { abstract int area(); }
final class Rectangle extends Shape { Rectangle(int w, int h) {...} int area() {...} }
final class Square    extends Shape { Square(int s) {...}        int area() {...} }
```

**Barbara Liskov's rule:** don't strengthen preconditions, don't weaken postconditions, preserve
invariants, and don't change throwing behaviour in a subtype.

---

## Notes

- LSP is about **behavioural** subtyping, not just `extends` compiling.
- When a hierarchy violates LSP, the fix is usually a **better abstraction** — or composition.
- A subtype that can't honour the contract should **not** inherit from it.

---

## Common Mistakes

1. Subclassing for code reuse when it is not a true "is-a".
2. Making a subtype that throws on part of the inherited API.
3. Silently changing results for the same inputs (e.g. different discount rules behind one method).

---

## Related

- [[../00 - Index|SOLID Index]]
- [[../../00 - Index|Concepts Index]]
- [[../../../00 - Index|LLD Main Index]]

---

#solid #lsp #lld #concept
