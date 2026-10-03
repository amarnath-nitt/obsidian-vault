# Design an Order Processor (Template Method)

**Source:** AlgoMaster · Low-Level Design Practice · **medium (premium)** · **Pattern:** Template Method
🔗 [AlgoMaster index](https://algomaster.io/practice/low-level-design)

### Problem

Processing orders follows a fixed sequence — **validate → price → reserve → confirm** — but the
pricing and reservation logic differs by order type (physical, digital, subscription). Keep the
sequence in one place and let each order type provide its own steps.

### Approach — Template Method

- `OrderProcessor` defines the `final` `process(order)` sequence.
- Abstract steps: `validate()`, `price()`, `reserve()`, `confirm()`.
- A `postProcess()` hook allows optional extra work.

### Java Solution

```java
abstract class OrderProcessor {
    // Template method — the fixed workflow
    final String process(String orderId, double amount) {
        if (!validate(orderId)) return "INVALID";
        double total = price(amount);
        reserve(orderId);
        confirm(orderId, total);
        postProcess(orderId);                        // optional hook
        return "OK:" + total;
    }

    protected abstract boolean validate(String orderId);
    protected abstract double price(double amount);
    protected abstract void reserve(String orderId);
    protected abstract void confirm(String orderId, double total);
    protected void postProcess(String orderId) { /* default: nothing */ }
}

class PhysicalOrderProcessor extends OrderProcessor {
    protected boolean validate(String id)         { return id != null && !id.isBlank(); }
    protected double price(double amount)         { return amount + 5.0; }        // + shipping
    protected void reserve(String id)             { System.out.println("Reserved stock for " + id); }
    protected void confirm(String id, double t)   { System.out.println("Confirmed " + id + " total " + t); }
}
class DigitalOrderProcessor extends OrderProcessor {
    protected boolean validate(String id)         { return id != null && !id.isBlank(); }
    protected double price(double amount)         { return amount; }              // no shipping
    protected void reserve(String id)             { System.out.println("Generated license for " + id); }
    protected void confirm(String id, double t)   { System.out.println("Emailed download link for " + id + " total " + t); }
    @Override protected void postProcess(String id){ System.out.println("Logged digital sale " + id); }
}
```

**Usage**
```java
System.out.println(new PhysicalOrderProcessor().process("ORD-1", 100));  // OK:105.0
System.out.println(new DigitalOrderProcessor().process("ORD-2", 100));   // OK:100.0
```

### Design points
- **One workflow** — `process` is `final`; subclasses cannot reorder or skip steps.
- **Varying steps abstract** — pricing/reservation differ per order type.
- **Hook for extras** — `postProcess` runs only if a subclass overrides it.

### Note on ambiguity
AlgoMaster has both a **State** and a **Template Method** variant of "Order Processor". Here the
focus is the **fixed processing workflow**; the State variant models the order's *lifecycle*.

**Complexity:** O(steps) per order · Space O(1)

---
#template-method #lld #practice