# Open/Closed — Concept

## What Is It?

Software entities should be **open for extension, closed for modification**: add new behaviour by
*adding* code, not by editing code that already works and is already tested.

| | |
|---|---|
| **Letter** | **O** |
| **Principle** | Open/Closed |
| **One-liner** | Extend by adding; don't edit what exists |

---

## When to Use

> **Trigger keywords:** "add a new type", "growing `switch`/`if-else`", "every new option touches the same method"

| Smell | Move |
|-------|------|
| Every new option extends an `if/else` chain | polymorphism or Strategy |
| Adding a rule means editing a stable function | extract a rule interface |
| Formats are handled by a `switch` on type | one writer per format |

---

## In Java

```java
// ❌ Every new shape edits this method
double area(Shape s) { if (s.type == CIRCLE) ... else if (s.type == SQUARE) ... }

// ✅ Add a new Shape subclass; nothing existing changes
abstract class Shape { abstract double area(); }
class Circle extends Shape { double area() { return Math.PI * r * r; } }
class Square extends Shape { double area() { return side * side; } }
```

**Variants that satisfy OCP:** Strategy, Template Method, Decorator, plug-in registries.

---

## Notes

- OCP is usually reached *after* you've seen a second variation — not before.
- The extension point is an **abstraction** (interface / abstract class), not a flag.
- Pair with **DIP**: the stable code depends on the abstraction, the new code implements it.

---

## Common Mistakes

1. Over-abstracting before there is a second variation (see also **YAGNI**).
2. "Extending" by adding a new `if` branch — that's still modification.
3. Building a plug-in framework nobody asked for.

---

## Related

- [[../00 - Index|SOLID Index]]
- [[../../00 - Index|Concepts Index]]
- [[../../../00 - Index|LLD Main Index]]

---

#solid #ocp #lld #concept
