# Polymorphism — Concept

## What Is It?

**One interface, many forms.** A single call site runs different code depending on the actual object
— so you replace branching (`if`/`switch`) with dispatch.

| | |
|---|---|
| **Pillar** | Polymorphism |
| **One-liner** | One call site, many behaviours |

---

## Two flavours

| Kind | When | Example |
|------|------|---------|
| **Compile-time** (overloading) | same name, different parameter lists | `area(Shape)` / `area(Circle)` |
| **Runtime** (overriding) | subclass decides the implementation | `shape.area()` → `Circle.area()` |

Runtime polymorphism is the one that matters for LLD — it's the mechanism behind **OCP**,
**Strategy**, and most `switch`-elimination refactors.

---

## In Java

```java
// ❌ Branching grows with every new behaviour
double area(Shape s) {
    if (s.type == CIRCLE) return Math.PI * s.r * s.r;
    if (s.type == SQUARE) return s.side * s.side;
    ...
}

// ✅ Dispatch picks the right implementation
abstract class Shape { abstract double area(); }
class Circle extends Shape { double area() { return Math.PI * r * r; } }
class Square extends Shape { double area() { return side * side; } }

Shape s = new Circle();   // call site never changes as types are added
s.area();
```

---

## Notes

- Polymorphism is what makes **OCP** achievable: add a class, don't edit the client.
- The call site depends on an **abstraction**, never on the concrete type.
- Strategy is polymorphism applied to *behaviour* rather than to a type hierarchy.

---

## Common Mistakes

1. Runtime type-checking (`instanceof` chains) — that's a `switch` wearing a disguise.
2. Overloading mistaken for overriding (overload is compile-time only).
3. Designing hierarchies around *implementation* instead of *behaviour*.

---

## Related

- [[../00 - Index|OOP Fundamentals Index]]
- [[../../00 - Index|Concepts Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../../../Patterns/Behavioural/15 - Strategy/Concept|Strategy]] — polymorphism applied to behaviour

---

#oop #polymorphism #lld #concept
