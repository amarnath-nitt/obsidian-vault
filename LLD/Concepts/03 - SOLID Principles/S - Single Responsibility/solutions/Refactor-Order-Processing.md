# Refactor Order Processing (Single Responsibility)

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Principle:** Single Responsibility
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/refactor-order-processing)

### Problem

An `OrderProcessor` currently validates the order, computes the total, saves it, and emails the
customer — four different reasons to change in one class. Refactor it so each concern lives in its own
class with a **single responsibility**.

### The Smell (before)

```java
// ❌ Four responsibilities in one class → four reasons to change
class OrderProcessor {
    void process(Order order) {
        if (order.items().isEmpty()) throw new IllegalArgumentException("empty");      // validation
        double total = order.items().stream().mapToDouble(Item::price).sum();          // pricing
        System.out.println("Saving order " + order.id());                              // persistence
        System.out.println("Emailing customer " + order.customerEmail());              // notification
    }
}
```

### The Fix (after)

```java
record Item(double price) {}
record Order(String id, String customerEmail, java.util.List<Item> items) {}

class OrderValidator {                         // one job: validate
    void validate(Order order) {
        if (order.items().isEmpty()) throw new IllegalArgumentException("Order has no items");
    }
}

class PricingService {                         // one job: price
    double total(Order order) {
        return order.items().stream().mapToDouble(Item::price).sum();
    }
}

class OrderRepository {                        // one job: persist
    void save(Order order) { System.out.println("Saving order " + order.id()); }
}

class OrderNotifier {                          // one job: notify
    void notifyCustomer(Order order, double total) {
        System.out.println("Emailed " + order.customerEmail() + " — total " + total);
    }
}

// The processor now only *coordinates* — it holds no business rules itself.
class OrderProcessor {
    private final OrderValidator validator;
    private final PricingService pricing;
    private final OrderRepository repository;
    private final OrderNotifier notifier;

    OrderProcessor(OrderValidator validator, PricingService pricing,
                   OrderRepository repository, OrderNotifier notifier) {
        this.validator = validator; this.pricing = pricing;
        this.repository = repository; this.notifier = notifier;
    }

    void process(Order order) {
        validator.validate(order);
        double total = pricing.total(order);
        repository.save(order);
        notifier.notifyCustomer(order, total);
    }
}
```

### Design points
- **One reason to change each** — changing the email template touches only `OrderNotifier`.
- **Testable in isolation** — each collaborator can be unit-tested / mocked separately.
- **Coordinator, not a god class** — `OrderProcessor` orchestrates but implements no rules.
- **Bonus: DIP** — the dependencies are injected rather than `new`ed internally.

**Complexity:** O(items) per order · Space O(1)

---
#solid #srp #lld #practice