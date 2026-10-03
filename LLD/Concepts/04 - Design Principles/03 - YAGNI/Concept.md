# YAGNI — Concept

## What Is It?

**You Aren't Gonna Need It.** Don't build features, layers, or abstractions for hypothetical future
needs. Build what the requirement actually states *now*; refactor when the need is real.

| | |
|---|---|
| **Principle** | YAGNI — You Aren't Gonna Need It |
| **One-liner** | Don't build for imagined futures |

---

## When to Use

> **Trigger keywords:** "just in case", "for future extensibility", "configurable", "plug-in ready"

| Smell | Move |
|-------|------|
| An abstraction with exactly one implementation | inline it |
| Config options nobody sets | delete them |
| A framework built ahead of the second use case | build the simple version first |

---

## In Java

```java
// ❌ A plug-in framework "just in case" — only one payment type exists
PaymentProcessorFactory.build(DriverType.from(config)).charge(order);

// ✅ The simple version that satisfies today's requirement
if (order.method() == Method.CARD) cardGateway.charge(order);
```

---

## Notes

- YAGNI does **not** mean "no design". It means don't *pre-build* flexibility you can't justify.
- Tension with **OCP**: design *for* change (leave seams), don't *implement* change early.
- Speculative code is the most expensive code — it must be read, tested and maintained forever.

---

## Common Mistakes

1. Building a general engine for a single concrete case.
2. Confusing YAGNI with "no architecture" — structure still matters.
3. Keeping dead code "for later" instead of deleting it (version control remembers).

---

## Related

- [[../00 - Index|Design Principles Index]]
- [[../../00 - Index|Concepts Index]]
- [[../../../00 - Index|LLD Main Index]]

---

#design-principles #yagni #lld #concept
