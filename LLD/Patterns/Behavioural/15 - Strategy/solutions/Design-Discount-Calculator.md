# Design a Discount Calculator

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Pattern:** Strategy
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-strategy-discount-calculator)

### Problem

A checkout applies a **discount** to an order total. Discounts come in different forms — no discount,
a **percentage** off, a **flat** amount off, or a **buy-one-get-one** style rule. The checkout should
apply whichever discount policy is configured, and new policies must be addable without editing the
checkout.

### Approach — Strategy

- `DiscountStrategy` — the algorithm interface (`apply(total)`).
- Concrete strategies: `NoDiscount`, `PercentageDiscount`, `FlatDiscount`, `BuyNGetOneFree`.
- `Checkout` holds a strategy and delegates to it; the strategy is swappable at runtime.

### Java Solution

```java
import java.util.function.DoubleUnaryOperator;

interface DiscountStrategy {
    double apply(double total);
}

class NoDiscount implements DiscountStrategy {
    public double apply(double total) { return total; }
}
class PercentageDiscount implements DiscountStrategy {
    private final double percent;
    PercentageDiscount(double percent) { this.percent = percent; }
    public double apply(double total) { return total * (1 - percent / 100); }
}
class FlatDiscount implements DiscountStrategy {
    private final double amount;
    FlatDiscount(double amount) { this.amount = amount; }
    public double apply(double total) { return Math.max(0, total - amount); }
}
class BuyNGetOneFree implements DiscountStrategy {
    private final int n;
    BuyNGetOneFree(int n) { this.n = n; }
    public double apply(double total) { return total * (n + 1) / (n + 2); } // rough bogo approximation
}

class Checkout {
    private DiscountStrategy strategy = new NoDiscount();   // sensible default

    public void setStrategy(DiscountStrategy strategy) { this.strategy = strategy; }
    public double total(double subtotal) { return strategy.apply(subtotal); }
}
```

**Usage**
```java
Checkout checkout = new Checkout();

System.out.println(checkout.total(100));                 // 100.0 (no discount)
checkout.setStrategy(new PercentageDiscount(10));
System.out.println(checkout.total(100));                 // 90.0  (10% off)
checkout.setStrategy(new FlatDiscount(25));
System.out.println(checkout.total(100));                 // 75.0  (flat 25 off)

// a lambda is a Strategy too
DoubleUnaryOperator membersOnly = t -> t * 0.8;
System.out.println(new Checkout() {{ setStrategy(membersOnly::apply); }}.total(100));
```

### Design points
- **One variation point** — the discount rule is the only thing that changes.
- **Open/Closed** — add a `SeasonalDiscount` class without touching `Checkout`.
- **Runtime selection** — swap the discount per order or per user.

**Complexity:** O(1) per calculation · Space O(1)

---
#strategy #lld #practice