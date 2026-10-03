# Design Restaurant Management System (Medium)

**Difficulty:** Medium · **Patterns:** State, Observer, Strategy
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design a restaurant: tables, menu, orders moving through the kitchen, and a bill with tax and tip.

**Functional**
- Seat parties; place orders with menu items; advance orders PLACED → PREPARING → READY → SERVED → PAID.
- Kitchen notified on new orders; bill = subtotal + tax (+ tip); paying frees the table.

**Non-functional**
- No skipped order states; one open order per table; tax rules pluggable.

### The failure, before

```java
// ❌ One `String status` per order plus a `boolean tableBusy` flag:
// states get skipped ("served" before "ready"), the kitchen polls every second,
// and the bill multiplies live menu prices — last week's order changes with today's menu.
// if (status.equals("ready")) status = "served";   // repeats, skips, and typos all pass
```

### The Fix (after)

Guarded order state machine + price snapshot + Observer kitchen + Strategy tax.

```java
import java.util.*;

enum TableStatus { FREE, OCCUPIED }
enum OrderState { PLACED, PREPARING, READY, SERVED, PAID }

class Table {
    final int number; final int seats; TableStatus status = TableStatus.FREE;
    Table(int number, int seats) { this.number = number; this.seats = seats; }
}

record MenuItem(String name, long price) {}

class Order {
    final int id; final Table table; final List<MenuItem> items = new ArrayList<>();
    private OrderState state = OrderState.PLACED;
    long tip;

    Order(int id, Table table) { this.id = id; this.table = table; }

    void add(MenuItem item) {
        if (state != OrderState.PLACED) throw new IllegalStateException("Kitchen already has it");
        items.add(item);                                        // snapshot: record, not reference
    }
    void advance() {
        state = switch (state) {
            case PLACED -> OrderState.PREPARING;
            case PREPARING -> OrderState.READY;
            case READY -> OrderState.SERVED;
            case SERVED -> OrderState.PAID;
            case PAID -> throw new IllegalStateException("Order already paid");
        };
    }
    long subtotal() { return items.stream().mapToLong(MenuItem::price).sum(); }
    OrderState state() { return state; }
}

interface TaxStrategy { long tax(long subtotal); }
class FlatTax implements TaxStrategy { public long tax(long s) { return s * 5 / 100; } }   // 5% GST

interface KitchenObserver { void onNewOrder(Order order); }

class Restaurant {
    private final Map<Integer, Table> tables = new LinkedHashMap<>();
    private final Map<String, MenuItem> menu = new LinkedHashMap<>();
    private final List<Order> orders = new ArrayList<>();
    private final List<KitchenObserver> kitchen = new ArrayList<>();
    private TaxStrategy tax = new FlatTax();
    private int seq = 0;

    void addTable(Table t) { tables.put(t.number, t); }
    void addMenuItem(MenuItem m) { menu.put(m.name(), m); }
    void setTax(TaxStrategy t) { tax = t; }
    void subscribe(KitchenObserver k) { kitchen.add(k); }

    void seatParty(Table table, int partySize) {
        if (table.status != TableStatus.FREE) throw new IllegalStateException("Table busy");
        if (partySize > table.seats) throw new IllegalStateException("Too small for " + partySize);
        table.status = TableStatus.OCCUPIED;
    }

    Order placeOrder(Table table, List<String> itemNames) {
        if (table.status != TableStatus.OCCUPIED) throw new IllegalStateException("Table not seated");
        boolean open = orders.stream().anyMatch(o -> o.table == table && o.state() != OrderState.PAID);
        if (open) throw new IllegalStateException("Table already has an open order");
        Order order = new Order(++seq, table);
        itemNames.forEach(n -> order.add(menu.get(n)));          // price snapshot inside add
        orders.add(order);
        kitchen.forEach(k -> k.onNewOrder(order));               // floor does not know the kitchen
        return order;
    }

    void advance(Order order) {
        order.advance();
        if (order.state() == OrderState.PAID) order.table.status = TableStatus.FREE;
    }

    long bill(Order order, long tip) {
        long subtotal = order.subtotal();
        return subtotal + tax.tax(subtotal) + tip;
    }
}
```

**Usage**
```java
Restaurant r = new Restaurant();
Table t7 = new Table(7, 4);
r.addTable(t7);
r.addMenuItem(new MenuItem("Paneer Tikka", 320));
r.addMenuItem(new MenuItem("Naan", 60));
r.subscribe(order -> System.out.println("Kitchen got order #" + order.id));

r.seatParty(t7, 3);
Order o = r.placeOrder(t7, List.of("Paneer Tikka", "Naan"));
r.advance(o); r.advance(o); r.advance(o); r.advance(o);      // …→ PAID, table FREE
System.out.println(r.bill(o, 50));                            // 380 + 5% + 50
```

### Design points
- **Guarded `advance()`** — the state machine is a switch; waiting, repeats, and skips all fail loudly.
- **Snapshot at add** — `MenuItem` records carry the price of the moment, so bills never mutate.
- **Kitchen decoupling** — the restaurant notifies `KitchenObserver`s; print, KDS, or both can subscribe.
- **Pay frees the table** — exactly one transition coupling the two machines, in exactly one place.

**Complexity:** placeOrder O(items) · advance O(1) · bill O(items).

---
#lld #machine-coding #restaurant #medium #practice