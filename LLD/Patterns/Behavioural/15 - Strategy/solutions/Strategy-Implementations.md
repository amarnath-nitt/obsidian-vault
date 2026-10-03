# Strategy — Implementations & Examples

**Pattern:** Strategy (Behavioural) · **Skill:** interchangeable algorithms selected at runtime

### Approach

- Define a **Strategy** interface for the variation point.
- Implement each algorithm as a **ConcreteStrategy**.
- Let the **Context** hold a strategy and delegate to it; choose the strategy at runtime.

### Java Solutions

**1. Payment Strategies**
```java
interface PaymentStrategy { void pay(double amount); }

class CreditCardPayment implements PaymentStrategy {
    private final String number;
    CreditCardPayment(String number) { this.number = number; }
    public void pay(double amount) { System.out.println("Paid " + amount + " via card " + number); }
}
class UpiPayment implements PaymentStrategy {
    private final String upiId;
    UpiPayment(String upiId) { this.upiId = upiId; }
    public void pay(double amount) { System.out.println("Paid " + amount + " via UPI " + upiId); }
}

class Checkout {                                       // Context
    private PaymentStrategy strategy;
    public void setStrategy(PaymentStrategy strategy) { this.strategy = strategy; }
    public void pay(double amount) {
        if (strategy == null) throw new IllegalStateException("No payment strategy set");
        strategy.pay(amount);
    }
}
// usage
Checkout checkout = new Checkout();
checkout.setStrategy(new UpiPayment("alice@upi"));
checkout.pay(499.0);
```

**2. Pricing / Discount Strategies**
```java
interface PricingStrategy { double price(double base); }

class NoDiscount       implements PricingStrategy { public double price(double b) { return b; } }
class PercentDiscount  implements PricingStrategy {
    private final double percent;
    PercentDiscount(double percent) { this.percent = percent; }
    public double price(double b) { return b * (1 - percent / 100); }
}
class FlatDiscount     implements PricingStrategy {
    private final double flat;
    FlatDiscount(double flat) { this.flat = flat; }
    public double price(double b) { return Math.max(0, b - flat); }
}
class Cart {
    private PricingStrategy pricing = new NoDiscount();
    public void setPricing(PricingStrategy p) { pricing = p; }
    public double total(double base) { return pricing.price(base); }
}
```

**3. Shipping Cost Strategies**
```java
interface ShippingStrategy { double cost(double weightKg); }
class StandardShipping implements ShippingStrategy { public double cost(double w) { return 5 + 1.0 * w; } }
class ExpressShipping  implements ShippingStrategy { public double cost(double w) { return 15 + 2.5 * w; } }
class SameDayShipping  implements ShippingStrategy { public double cost(double w) { return 30 + 5.0 * w; } }
```

**4. Functional (Lambda) Strategy**
```java
import java.util.*;
import java.util.function.*;

@FunctionalInterface
interface DiscountRule { double apply(double base); }

class Pricer {
    private DiscountRule rule = b -> b;                // default: no discount
    public void setRule(DiscountRule rule) { this.rule = rule; }
    public double finalPrice(double base) { return rule.apply(base); }
}
// usage — no new classes needed
Pricer pricer = new Pricer();
pricer.setRule(b -> b * 0.9);                          // 10% off
System.out.println(pricer.finalPrice(100));
```

**5. Strategy selected by a Factory (no `if/else` in the context)**
```java
import java.util.*;
import java.util.function.Supplier;

class StrategyRegistry {
    private static final Map<String, Supplier<PricingStrategy>> REGISTRY = new HashMap<>();
    static {
        REGISTRY.put("NONE",    NoDiscount::new);
        REGISTRY.put("PERCENT", () -> new PercentDiscount(10));
        REGISTRY.put("FLAT",    () -> new FlatDiscount(50));
    }
    static PricingStrategy of(String key) {
        Supplier<PricingStrategy> s = REGISTRY.get(key.toUpperCase());
        if (s == null) throw new IllegalArgumentException("Unknown pricing: " + key);
        return s.get();
    }
}
```

**6. Sorting with `Comparator` (JDK strategies)**
```java
record Item(String name, double price) {}
List<Item> items = new ArrayList<>(List.of(new Item("B", 20), new Item("A", 10)));
items.sort(Comparator.comparingDouble(Item::price));   // strategy 1
items.sort(Comparator.comparing(Item::name));          // strategy 2
```

**Complexity:** O(1) delegation per call · Space O(1) per strategy (stateless strategies are shareable)

**Design note:** moving selection into a **registry/factory** keeps the Context free of `if/else`, preserving Open/Closed.