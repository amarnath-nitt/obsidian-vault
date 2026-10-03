# Design an Order Processor (State)

**Source:** AlgoMaster · Low-Level Design Practice · **medium (premium)** · **Pattern:** State
🔗 [AlgoMaster index](https://algomaster.io/practice/low-level-design)

### Problem

An order moves through a lifecycle: **New → Paid → Shipped → Delivered**, with **Cancelled** as a
terminal branch. Which actions are legal depends on the current status (you cannot ship an unpaid
order, you cannot cancel a shipped order). Model the order as a **state machine** rather than a
status field with `if/else`.

### Approach — State

- **Context** = `Order` — holds a current `OrderState` and exposes intent methods.
- **States** = `NewState`, `PaidState`, `ShippedState`, `DeliveredState`, `CancelledState`.
- Illegal transitions throw; each state drives its own legal transitions.

### Java Solution

```java
interface OrderState {
    void pay(Order o);
    void ship(Order o);
    void deliver(Order o);
    void cancel(Order o);
}

class Order {
    private OrderState state = new NewState();
    private String status = "NEW";

    void setState(OrderState s, String name) { this.state = s; this.status = name; }
    public String status() { return status; }

    public void pay()     { state.pay(this); }
    public void ship()    { state.ship(this); }
    public void deliver() { state.deliver(this); }
    public void cancel()  { state.cancel(this); }
}

class NewState implements OrderState {
    public void pay(Order o)     { o.setState(new PaidState(), "PAID"); }
    public void ship(Order o)    { throw new IllegalStateException("Pay before shipping"); }
    public void deliver(Order o) { throw new IllegalStateException("Not shipped yet"); }
    public void cancel(Order o)  { o.setState(new CancelledState(), "CANCELLED"); }
}
class PaidState implements OrderState {
    public void pay(Order o)     { throw new IllegalStateException("Already paid"); }
    public void ship(Order o)    { o.setState(new ShippedState(), "SHIPPED"); }
    public void deliver(Order o) { throw new IllegalStateException("Not shipped yet"); }
    public void cancel(Order o)  { o.setState(new CancelledState(), "CANCELLED"); }
}
class ShippedState implements OrderState {
    public void pay(Order o)     { throw new IllegalStateException("Already paid"); }
    public void ship(Order o)    { throw new IllegalStateException("Already shipped"); }
    public void deliver(Order o) { o.setState(new DeliveredState(), "DELIVERED"); }
    public void cancel(Order o)  { throw new IllegalStateException("Cannot cancel a shipped order"); }
}
class DeliveredState implements OrderState {
    public void pay(Order o) {} public void ship(Order o) {}
    public void deliver(Order o) {} public void cancel(Order o) {}
}
class CancelledState implements OrderState {
    public void pay(Order o) {} public void ship(Order o) {}
    public void deliver(Order o) {} public void cancel(Order o) {}
}
```

**Usage**
```java
Order order = new Order();
order.pay();          // → PAID
order.ship();         // → SHIPPED
order.cancel();       // throws: "Cannot cancel a shipped order"
order.deliver();      // → DELIVERED
```

### Design points
- **Legal transitions enforced by the state** — the order never validates transitions itself.
- **Terminal states are no-ops** — `Delivered`/`Cancelled` ignore further events.
- **Table-driven alternative** — transitions can be declared as `Map<State, Map<Event, State>>`.

**Complexity:** O(1) per event · Space O(states)

---
#state #lld #practice