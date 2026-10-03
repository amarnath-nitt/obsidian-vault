# Design Online Food Delivery Service like Swiggy (Hard)

**Difficulty:** Hard · **Patterns:** State, Strategy, Observer
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design food delivery: restaurants + menus, cart and order placement, kitchen/delivery lifecycle, nearest-agent dispatch, distance fees, and tracking.

**Functional**
- PLACED → CONFIRMED → PREPARING → OUT_FOR_DELIVERY → DELIVERED; cancel before dispatch frees the agent.
- Nearest available agent assigned atomically; fee by restaurant→customer distance; observers see every transition.

**Non-functional**
- No agent on two deliveries at once; menu prices snapshot at placement.

### The failure, before

```java
// ❌ Status as free strings (`"confirmed"`, `"Confirmed"`, `"CONF"`) checked with equals
// across modules: the kitchen can "deliver" before dispatch, cancels forget to free the agent,
// and the tracking screen polls the order table every second.
// if (order.status.equals("out")) { order.status = "delivered"; agent.free = true; }  // sometimes.
```

### The Fix (after)

An `OrderState` machine with guarded transitions + atomic nearest-agent dispatch + observer fan-out.

```java
import java.util.*;

record Location(double x, double y) {
    double distanceTo(Location o) { return Math.hypot(x - o.x, y - o.y); }
}

record MenuItem(String name, long price) {}

class Restaurant {
    final String id, name; final Location location;
    final Map<String, MenuItem> menu = new LinkedHashMap<>();
    Restaurant(String id, String name, Location location) {
        this.id = id; this.name = name; this.location = location;
    }
    void addItem(MenuItem item) { menu.put(item.name(), item); }
}

class Cart {
    final Map<String, Integer> items = new LinkedHashMap<>();
    void add(String item, int qty) { items.merge(item, qty, Integer::sum); }
    void remove(String item) { items.remove(item); }
}

enum OrderState { PLACED, CONFIRMED, PREPARING, OUT_FOR_DELIVERY, DELIVERED, CANCELLED }
enum AgentStatus { AVAILABLE, ON_DELIVERY }

class DeliveryAgent {
    final String id; Location location; AgentStatus status = AgentStatus.AVAILABLE;
    DeliveryAgent(String id, Location location) { this.id = id; this.location = location; }
}

class Order {
    final String id, restaurantId; final Location dropoff;
    final Map<String, Integer> items; final long itemTotal;
    private OrderState state = OrderState.PLACED;
    private DeliveryAgent agent;

    Order(String id, String restaurantId, Location dropoff, Map<String, Integer> items, long itemTotal) {
        this.id = id; this.restaurantId = restaurantId; this.dropoff = dropoff;
        this.items = Map.copyOf(items); this.itemTotal = itemTotal;
    }
    void advance(OrderState to) {                                   // the full legal graph, one place
        OrderState expected = switch (to) {
            case CONFIRMED -> OrderState.PLACED;
            case PREPARING -> OrderState.CONFIRMED;
            case OUT_FOR_DELIVERY -> OrderState.PREPARING;
            case DELIVERED -> OrderState.OUT_FOR_DELIVERY;
            default -> throw new IllegalStateException("Cannot advance to " + to);
        };
        if (state != expected) throw new IllegalStateException(state + " → " + to);
        state = to;
    }
    void assign(DeliveryAgent a) {
        if (state != OrderState.PREPARING) throw new IllegalStateException("Not ready to dispatch");
        a.status = AgentStatus.ON_DELIVERY;
        agent = a;
    }
    void complete() {
        if (agent != null) agent.status = AgentStatus.AVAILABLE;    // agent freed exactly here
        advance(OrderState.DELIVERED);
    }
    void cancel() {
        if (state == OrderState.OUT_FOR_DELIVERY || state == OrderState.DELIVERED)
            throw new IllegalStateException("Too late to cancel — food is on the way");
        if (agent != null) agent.status = AgentStatus.AVAILABLE;
        state = OrderState.CANCELLED;
    }
    OrderState state() { return state; }
}

interface AssignmentStrategy { DeliveryAgent assign(List<DeliveryAgent> agents, Location restaurant); }

class NearestAgent implements AssignmentStrategy {
    public DeliveryAgent assign(List<DeliveryAgent> agents, Location restaurant) {
        return agents.stream()
                .filter(a -> a.status == AgentStatus.AVAILABLE)
                .min(Comparator.comparingDouble(a -> a.location.distanceTo(restaurant)))
                .orElseThrow(() -> new IllegalStateException("No agents available"));
    }
}

interface FeeStrategy { long fee(double km); }
class DistanceFee implements FeeStrategy { public long fee(double km) { return 20 + Math.round(8 * km); } }

interface OrderObserver { void onUpdate(Order order, OrderState state); }

class FoodDeliveryService {
    private final Map<String, Restaurant> restaurants = new LinkedHashMap<>();
    private final Map<String, Order> orders = new LinkedHashMap<>();
    private final List<DeliveryAgent> agents = new ArrayList<>();
    private final List<OrderObserver> observers = new ArrayList<>();
    private AssignmentStrategy assignment = new NearestAgent();
    private FeeStrategy fees = new DistanceFee();
    private int seq = 0;

    void addRestaurant(Restaurant r) { restaurants.put(r.id, r); }
    void addAgent(DeliveryAgent a) { agents.add(a); }
    void subscribe(OrderObserver o) { observers.add(o); }

    Order placeOrder(String restaurantId, Cart cart, Location dropoff) {
        Restaurant r = restaurants.get(restaurantId);
        long total = 0;
        for (Map.Entry<String, Integer> e : cart.items.entrySet()) {
            MenuItem item = r.menu.get(e.getKey());
            if (item == null) throw new IllegalStateException("Not on the menu: " + e.getKey());
            total += item.price() * e.getValue();                   // price snapshot
        }
        Order order = new Order("O" + (++seq), restaurantId, dropoff, cart.items, total);
        orders.put(order.id, order);
        notify(order);
        return order;
    }

    synchronized void confirm(Order order)  { order.advance(OrderState.CONFIRMED); notify(order); }
    synchronized void prepare(Order order)  { order.advance(OrderState.PREPARING); notify(order); }

    synchronized DeliveryAgent dispatch(Order order) {
        DeliveryAgent agent = assignment.assign(new ArrayList<>(agents), restaurants.get(order.restaurantId).location);
        order.assign(agent);
        order.advance(OrderState.OUT_FOR_DELIVERY);
        notify(order);
        return agent;
    }
    synchronized long deliver(Order order) {
        order.complete();
        notify(order);
        double km = restaurants.get(order.restaurantId).location.distanceTo(order.dropoff);
        return order.itemTotal + fees.fee(km);
    }
    synchronized void cancel(Order order) { order.cancel(); notify(order); }

    private void notify(Order order) {
        OrderState snapshot = order.state();
        observers.forEach(o -> o.onUpdate(order, snapshot));
    }
}
```

**Usage**
```java
FoodDeliveryService svc = new FoodDeliveryService();
Restaurant dosa = new Restaurant("r1", "Dosa Corner", new Location(2, 2));
dosa.addItem(new MenuItem("Masala Dosa", 120));
svc.addRestaurant(dosa);
svc.addAgent(new DeliveryAgent("a1", new Location(1, 1)));
svc.addAgent(new DeliveryAgent("a2", new Location(9, 9)));
svc.subscribe((order, state) -> System.out.println(order.id + " → " + state));

Cart cart = new Cart();
cart.add("Masala Dosa", 2);
Order o = svc.placeOrder("r1", cart, new Location(8, 0));
svc.confirm(o); svc.prepare(o); svc.dispatch(o);            // a1 assigned (nearest)
long total = svc.deliver(o);                                // items 240 + fee for ~6.3 km
System.out.println(total);                                  // 240 + 20 + 8×6.3 ≈ 310
```

### Design points
- **One guarded graph** — `advance(to)` maps every legal from-state; wrong order of operations cannot compile a lie.
- **Dispatch is atomic and nearest-based** — filter available, rank by distance, assign, flip status — inside one lock.
- **Agent freed exactly once** — in `complete()` and in `cancel()`; no other path touches `AgentStatus`.
- **Tracking = observer fan-out** — every transition notifies; UI reads a snapshot, never polls.

**Complexity:** place O(items) · dispatch O(agents) · deliver O(1).

---
#lld #machine-coding #swiggy #hard #practice