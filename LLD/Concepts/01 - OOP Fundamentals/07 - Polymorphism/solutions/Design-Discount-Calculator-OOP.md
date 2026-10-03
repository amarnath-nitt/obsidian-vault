# Design Discount Calculator (Polymorphism)

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Topic:** Polymorphism
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-discount-calculator)

### Problem

Design a price calculator that applies a **discount**. Discounts come in different shapes — none, a
percentage, or a flat amount. The calculator must apply **whichever** discount it is given through
**polymorphism**, without a `switch` over discount types.

### Approach

- Model `Discount` as an abstract base with `apply(total)` and `label()`.
- Subclasses implement the arithmetic.
- `PriceCalculator` takes a `Discount` and always calls the same two methods.

### Java Solution

```java
// Polymorphic base
public abstract class Discount {
    public abstract double apply(double total);
    public abstract String label();
}

class NoDiscount extends Discount {
    public double apply(double total) { return total; }
    public String label() { return "no discount"; }
}

class PercentageDiscount extends Discount {
    private final double percent;
    PercentageDiscount(double percent) { this.percent = percent; }
    public double apply(double total) { return total * (1 - percent / 100); }
    public String label() { return percent + "% off"; }
}

class FlatDiscount extends Discount {
    private final double amount;
    FlatDiscount(double amount) { this.amount = amount; }
    public double apply(double total) { return Math.max(0, total - amount); }
    public String label() { return "$" + amount + " off"; }
}

// Uses polymorphism — one call site, many behaviours
public class PriceCalculator {
    public String receipt(double subtotal, Discount discount) {
        double finalPrice = discount.apply(subtotal);       // dynamic dispatch
        return String.format("Subtotal $%.2f · %s · Total $%.2f",
                subtotal, discount.label(), finalPrice);
    }
}
```

**Usage**
```java
PriceCalculator calc = new PriceCalculator();
calc.receipt(100, new NoDiscount());            // Total $100.00
calc.receipt(100, new PercentageDiscount(10));  // Total $90.00
calc.receipt(100, new FlatDiscount(25));        // Total $75.00
```

### Design points
- **One interface, many forms** — `discount.apply(...)` dispatches at runtime.
- **No `switch` on type** — adding `BogoDiscount` needs only a new class.
- **Uniform call site** — the calculator treats every discount identically.

### OOP vs Strategy
This shows **polymorphism** in isolation. When the *choice* of discount also needs to be swappable
and selected from outside, the same idea is packaged as the **Strategy** pattern
(see [[../../../../Patterns/Behavioural/15 - Strategy/Concept|Strategy]]).

**Complexity:** O(1) per calculation · Space O(1)

---
#oop #polymorphism #lld #practice