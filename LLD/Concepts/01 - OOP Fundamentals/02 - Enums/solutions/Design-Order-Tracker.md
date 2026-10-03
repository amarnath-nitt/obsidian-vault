# Design Order Tracker (Enums)

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Topic:** Enums / State Management
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-order-tracker)

### Problem

Design an order tracker whose status is one of a fixed set — `PLACED`, `SHIPPED`, `DELIVERED`, and a
terminal `CANCELLED`. Only **legal transitions** are allowed (you cannot ship a cancelled order).
Model the status as an `enum` that knows the legal next states.

### Approach

- Use an enum with the status set and a `canTransitionTo` rule per status.
- The tracker exposes intent methods (`ship()`, `deliver()`, `cancel()`) that consult the enum.
- Illegal transitions are rejected.

### Java Solution

```java
public enum OrderStatus {
    PLACED, SHIPPED, DELIVERED, CANCELLED;

    /** Legal successors of each status. */
    public boolean canTransitionTo(OrderStatus next) {
        return switch (this) {
            case PLACED    -> next == SHIPPED   || next == CANCELLED;
            case SHIPPED   -> next == DELIVERED || next == CANCELLED;
            case DELIVERED -> false;                 // terminal
            case CANCELLED -> false;                 // terminal
        };
    }
}

public class OrderTracker {

    private final String orderId;
    private OrderStatus status = OrderStatus.PLACED;

    public OrderTracker(String orderId) { this.orderId = orderId; }

    public OrderStatus status() { return status; }

    /** Attempts a transition; returns true if it was legal. */
    public boolean transitionTo(OrderStatus next) {
        if (!status.canTransitionTo(next)) return false;
        status = next;
        return true;
    }

    public boolean ship()    { return transitionTo(OrderStatus.SHIPPED); }
    public boolean deliver() { return transitionTo(OrderStatus.DELIVERED); }
    public boolean cancel()  { return transitionTo(OrderStatus.CANCELLED); }

    public String describe() { return orderId + " is " + status; }
}
```

**Usage**
```java
OrderTracker order = new OrderTracker("ORD-1");
order.ship();             // true  → SHIPPED
order.cancel();           // true  → CANCELLED
order.deliver();          // false → terminal state, rejected
order.describe();         // "ORD-1 is CANCELLED"
```

### Design points
- **Enum owns the rules** — legal transitions live in `OrderStatus`, not scattered in callers.
- **Terminal states** — `DELIVERED`/`CANCELLED` accept nothing further.
- **Intent methods** — callers say `ship()`, never `setStatus(...)`.

**Complexity:** O(1) per transition · Space O(1)

---
#oop #enums #lld #practice