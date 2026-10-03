# Single Responsibility — Concept

## What Is It?

A class should have **exactly one reason to change** — one job, one axis of change. When a class
does several unrelated things, a change to any one of them risks breaking the others.

| | |
|---|---|
| **Letter** | **S** |
| **Principle** | Single Responsibility |
| **One-liner** | One class, one job, one reason to change |

---

## When to Use

> **Trigger keywords:** "the class does X **and** Y", "god class", "unrelated changes break each other"

| Smell | Move |
|-------|------|
| You can describe a class with "and" | split it |
| Changing the report format breaks the save logic | separate presentation from persistence |
| A class mixes domain rules with I/O | pull the rules out |

---

## In Java

```java
// ❌ Invoice that also persists itself and prints itself — three reasons to change
class Invoice {
    void calculateTotal() {}
    void saveToDb() {}
    void print() {}
}

// ✅ Each concern in its own class
class Invoice           { double total() { ... } }        // the model
class InvoiceRepository { void save(Invoice i) {} }       // persistence
class InvoicePrinter    { void print(Invoice i) {} }      // presentation
```

---

## Notes

- SRP is about the **reason to change**, not "one method per class" or "one class per layer".
- Splitting by *technical layer* alone is not SRP — split by **who asks for the change**.
- Many small classes are fine; a facade can present them as one unit to callers.

---

## Common Mistakes

1. Splitting by technical layer instead of by reason to change.
2. Creating one-method micro-classes that lose cohesion.
3. Moving logic into "service" classes and leaving anemic models behind.

---

## Related

- [[../00 - Index|SOLID Index]]
- [[../../00 - Index|Concepts Index]]
- [[../../../00 - Index|LLD Main Index]]

---

#solid #srp #lld #concept
