# Interface Segregation — Concept

## What Is It?

No client should be forced to depend on methods it **doesn't use**. Many small, focused interfaces
beat one fat interface that every implementer has to stub out.

| | |
|---|---|
| **Letter** | **I** |
| **Principle** | Interface Segregation |
| **One-liner** | Small, role-specific interfaces |

---

## When to Use

> **Trigger keywords:** "fat interface", "implementers stub out methods", "`UnsupportedOperationException`", "change one client breaks another"

| Smell | Move |
|-------|------|
| Implementers throw / no-op most methods | split into role interfaces |
| A change to one method forces every implementer to recompile | segregate by client |
| One interface mixes unrelated capabilities | one interface per capability |

---

## In Java

```java
// ❌ One printer interface forces every device to implement everything
interface MultiFunctionDevice { void print(); void scan(); void fax(); }
class SimplePrinter implements MultiFunctionDevice {
    public void print() {}
    public void scan()  { throw new UnsupportedOperationException(); }   // stub
    public void fax()   { throw new UnsupportedOperationException(); }   // stub
}

// ✅ Split — devices implement only what they support
interface Printer { void print(); }
interface Scanner { void scan(); }
class SimplePrinter implements Printer { public void print() {} }
```

---

## Notes

- **Cohesion of the interface** still matters — don't shatter it into one-method fragments nobody can navigate.
- Clients should depend on the **smallest interface that serves them** (this also helps **DIP**).
- Role interfaces (`Readable`, `Writable`, `Chargeable`) read well in interviews.

---

## Common Mistakes

1. Making interfaces so small they lose cohesion and navigation becomes painful.
2. Splitting by *implementer* instead of by *client*.
3. Keeping one god interface and adding `default` methods to paper over it.

---

## Related

- [[../00 - Index|SOLID Index]]
- [[../../00 - Index|Concepts Index]]
- [[../../../00 - Index|LLD Main Index]]

---

#solid #isp #lld #concept
