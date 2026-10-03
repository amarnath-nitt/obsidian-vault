# KISS — Concept

## What Is It?

**Keep It Simple, Stupid.** The simplest design that satisfies the requirement wins. Clever code is
a liability; obvious code is an asset — especially under interview pressure and in code you'll
re-read later.

| | |
|---|---|
| **Principle** | KISS — Keep It Simple |
| **One-liner** | The simplest design that works |

---

## When to Use

> **Trigger keywords:** "I had to read it three times", "clever one-liner", "nested ternaries", "spaghetti"

| Smell | Move |
|-------|------|
| Nested ternaries / double negatives | flatten with early returns |
| A comment explaining what the code does | rewrite so the code says it |
| More indirection than the problem needs | inline the single-use helper |

---

## In Java

```java
// ❌ Clever: a boolean inverting a boolean, redundant comparisons
boolean ok = !(blocked == true) ? (pw != null ? active == true : false) : false;

// ✅ Obvious: reads like the requirement
boolean ok = active && !blocked && hasPassword(user);
```

---

## Notes

- Simple ≠ naive. A simple solution still handles the real requirements and edge cases.
- **KISS and YAGNI reinforce each other** — both cut accidental complexity.
- Complexity is a *cost*; only pay it when the problem demands it.

---

## Common Mistakes

1. Mistaking "clever" for "good" — golfed expressions and trick overloads.
2. Adding indirection (factories, wrappers) that nothing currently needs.
3. Optimising readability away in favour of fewer lines.

---

## Related

- [[../00 - Index|Design Principles Index]]
- [[../../00 - Index|Concepts Index]]
- [[../../../00 - Index|LLD Main Index]]

---

#design-principles #kiss #lld #concept
