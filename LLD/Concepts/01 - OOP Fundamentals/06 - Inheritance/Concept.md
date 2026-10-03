# Inheritance — Concept

## What Is It?

Inheritance is **reuse through an "is-a"** relationship: a subtype gets the base's state and
behaviour and may specialise it. It is powerful — and the most commonly over-applied OOP tool.

| | |
|---|---|
| **Pillar** | Inheritance |
| **One-liner** | Reuse via `extends` / `implements` — only for a true *is-a* |

---

## When to Use

> **Trigger keywords:** "is a kind of", "shares base behaviour", "reuse"

| Trigger | Move |
|---------|------|
| `Car` **is a** `Vehicle` with shared behaviour | `abstract class` + `extends` |
| Unrelated classes share only a contract | `interface` (not inheritance) |
| You're reusing code but it isn't a true *is-a* | **composition** instead |

---

## In Java

```java
abstract class Vehicle {
    abstract int capacity();
    void start() { /* shared */ }
}
class Car extends Vehicle { int capacity() { return 5; } }
class Bus  extends Vehicle { int capacity() { return 50; } }
```

---

## Inheritance vs Composition

```java
// ❌ Reuse by inheritance where it isn't an is-a
class Stack extends ArrayList<String> { ... }   // exposes add/remove — broken abstraction

// ✅ Reuse by composition — the Stack controls its own API
class Stack<T> { private final Deque<T> items = new ArrayDeque<>(); }
```

> **Favour composition over inheritance** — inheritance couples you to the base class's internals
> and is hard to change once published.

---

## Notes

- Inheritance forces **LSP**: every subtype must honour the base contract.
- Deep hierarchies are hard to reason about — keep them shallow.
- Use `abstract class` for shared *implementation*, `interface` for shared *contract*.

---

## Common Mistakes

1. Inheriting for code reuse when it isn't a true "is-a".
2. Deep hierarchies (`A extends B extends C extends D`).
3. Exposing base internals to subclasses (fragile base class problem).
4. Choosing inheritance by default before considering composition.

---

## Related

- [[../00 - Index|OOP Fundamentals Index]]
- [[../../00 - Index|Concepts Index]]
- [[../../../00 - Index|LLD Main Index]]

---

#oop #inheritance #lld #concept
