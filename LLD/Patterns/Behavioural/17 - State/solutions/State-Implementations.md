# State — Implementations & Examples

**Pattern:** State (Behavioural) · **Skill:** changing behaviour with an object's lifecycle

### Approach

- Define a **State** interface with the behaviours the context exposes.
- Implement one **ConcreteState** per lifecycle state; each triggers its own transitions.
- The **Context** holds a current state and delegates all behaviour to it.

### Java Solutions

**1. Traffic Light**
```java
interface LightState { void next(TrafficLight light); String color(); }

class RedState implements LightState {
    public void next(TrafficLight light) { light.setState(new GreenState()); }
    public String color() { return "RED"; }
}
class GreenState implements LightState {
    public void next(TrafficLight light) { light.setState(new YellowState()); }
    public String color() { return "GREEN"; }
}
class YellowState implements LightState {
    public void next(TrafficLight light) { light.setState(new RedState()); }
    public String color() { return "YELLOW"; }
}

class TrafficLight {
    private LightState state = new RedState();
    void setState(LightState s) { state = s; }
    void next() { state.next(this); }
    String color() { return state.color(); }
}
```

**2. Order Lifecycle**
```java
interface OrderState {
    void pay(Order o); void ship(Order o); void deliver(Order o); void cancel(Order o);
}

class Order {
    OrderState state = new NewState();
    void setState(OrderState s) { state = s; System.out.println("Order → " + s.getClass().getSimpleName()); }
    public void pay()     { state.pay(this); }
    public void ship()    { state.ship(this); }
    public void deliver() { state.deliver(this); }
    public void cancel()  { state.cancel(this); }
}

class NewState implements OrderState {
    public void pay(Order o)     { o.setState(new PaidState()); }
    public void ship(Order o)    { throw new IllegalStateException("Pay first"); }
    public void deliver(Order o) { throw new IllegalStateException("Ship first"); }
    public void cancel(Order o)  { o.setState(new CancelledState()); }
}
class PaidState implements OrderState {
    public void pay(Order o)     { throw new IllegalStateException("Already paid"); }
    public void ship(Order o)    { o.setState(new ShippedState()); }
    public void deliver(Order o) { throw new IllegalStateException("Ship first"); }
    public void cancel(Order o)  { o.setState(new CancelledState()); }
}
class ShippedState implements OrderState {
    public void pay(Order o)     { throw new IllegalStateException("Already paid"); }
    public void ship(Order o)    { throw new IllegalStateException("Already shipped"); }
    public void deliver(Order o) { o.setState(new DeliveredState()); }
    public void cancel(Order o)  { throw new IllegalStateException("Cannot cancel shipped order"); }
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

**3. Vending Machine**
```java
interface VendingState { void insertCoin(int cents); void selectItem(); }

class VendingMachine {
    private int balance = 0;
    private VendingState state = new IdleState();
    void setState(VendingState s) { state = s; }
    void insertCoin(int c) { balance += c; state.insertCoin(c); }
    void selectItem() { state.selectItem(); }
    int balance() { return balance; }
    void reset() { balance = 0; }
}

class IdleState implements VendingState {
    public void insertCoin(int c) { System.out.println("coin accepted"); /* move to HasMoney via machine.setState */ }
    public void selectItem() { System.out.println("insert coin first"); }
}
class HasMoneyState implements VendingState {
    public void insertCoin(int c) { System.out.println("added coin"); }
    public void selectItem() { System.out.println("dispensing item"); }
}
```

**4. Table-Driven State Machine**
```java
import java.util.*;

enum State { NEW, PAID, SHIPPED }
enum Event { PAY, SHIP }

class StateMachine {
    private static final Map<State, Map<Event, State>> TABLE = Map.of(
        State.NEW,   Map.of(Event.PAY, State.PAID),
        State.PAID,  Map.of(Event.SHIP, State.SHIPPED)
    );
    private State current = State.NEW;
    void fire(Event e) {
        State next = Optional.ofNullable(TABLE.get(current))
                             .map(m -> m.get(e)).orElse(null);
        if (next == null) throw new IllegalStateException("Illegal: " + current + " + " + e);
        current = next;
    }
    State current() { return current; }
}
```

**Complexity:** `O(1)` per event · Space O(number of states)

**Design note:** expose **intent methods** (`pay`, `ship`) rather than a raw status setter — the context should not let callers force invalid states.