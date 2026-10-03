# Design Online Shopping System like Amazon (Hard)

**Difficulty:** Hard · **Patterns:** State, Strategy, Observer
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design e-commerce core: catalogue search, cart, checkout with inventory reservation, order lifecycle, cancellations with restock, discounts.

**Functional**
- Cart per user; checkout reserves stock all-or-nothing; CREATED → PAID → SHIPPED → DELIVERED; cancel restores stock.
- Discount strategies; restock observers.

**Non-functional**
- Available = on-hand − reserved never goes negative under concurrent checkouts.

### The failure, before

```java
// ❌ `if (stock > 0) stock--;` at "add to cart" time: carts hold stock nobody paid for,
// two checkouts pass the same check and stock goes negative, and cancel forgets
// the difference between reserved and shipped stock.
// if (stock > 0) stock--;   // carts are not orders; the number lies.
```

### The Fix (after)

An `Inventory` with an explicit **reserved** layer + a guarded order state machine + strategies.

```java
import java.util.*;

class Product {
    final String sku, name; final long price;
    Product(String sku, String name, long price) { this.sku = sku; this.name = name; this.price = price; }
}

class Inventory {
    private final Map<String, Integer> onHand = new HashMap<>();
    private final Map<String, Integer> reserved = new HashMap<>();
    private final List<StockObserver> observers = new ArrayList<>();

    void restock(String sku, int qty) {
        onHand.merge(sku, qty, Integer::sum);
        observers.forEach(o -> o.onRestock(sku));
    }
    void subscribe(StockObserver o) { observers.add(o); }
    synchronized int available(String sku) {
        return onHand.getOrDefault(sku, 0) - reserved.getOrDefault(sku, 0);
    }
    synchronized void reserve(Map<String, Integer> items) {          // all-or-nothing
        for (Map.Entry<String, Integer> e : items.entrySet())
            if (available(e.getKey()) < e.getValue())
                throw new IllegalStateException("Out of stock: " + e.getKey());
        items.forEach((sku, qty) -> reserved.merge(sku, qty, Integer::sum));
    }
    synchronized void commit(Map<String, Integer> items) {           // payment: reservation becomes sale
        items.forEach((sku, qty) -> {
            reserved.merge(sku, -qty, Integer::sum);
            onHand.merge(sku, -qty, Integer::sum);
        });
    }
    synchronized void release(Map<String, Integer> items) {          // cancelled before payment
        items.forEach((sku, qty) -> reserved.merge(sku, -qty, Integer::sum));
    }
    synchronized void restockItems(Map<String, Integer> items) {     // cancelled after payment
        items.forEach((sku, qty) -> onHand.merge(sku, qty, Integer::sum));
    }
}

interface StockObserver { void onRestock(String sku); }

class Cart {
    final Map<String, Integer> items = new LinkedHashMap<>();
    void add(String sku, int qty) { items.merge(sku, qty, Integer::sum); }
    void remove(String sku) { items.remove(sku); }
}

enum OrderState { CREATED, PAID, SHIPPED, DELIVERED, CANCELLED }

class Order {
    final String id; final Map<String, Integer> items; final long subtotal;
    private OrderState state = OrderState.CREATED;
    Order(String id, Map<String, Integer> items, long subtotal) {
        this.id = id; this.items = Map.copyOf(items); this.subtotal = subtotal;
    }
    void pay()     { require(OrderState.CREATED, OrderState.PAID); }
    void ship()    { require(OrderState.PAID, OrderState.SHIPPED); }
    void deliver() { require(OrderState.SHIPPED, OrderState.DELIVERED); }
    void cancel()  {
        if (state != OrderState.CREATED && state != OrderState.PAID)
            throw new IllegalStateException("Cannot cancel a " + state + " order");
        state = OrderState.CANCELLED;
    }
    private void require(OrderState from, OrderState to) {
        if (state != from) throw new IllegalStateException(state + " → " + to);
        state = to;
    }
    OrderState state() { return state; }
}

interface DiscountStrategy { long discount(long subtotal); }
class NoDiscount implements DiscountStrategy { public long discount(long s) { return 0; } }
class PercentOff implements DiscountStrategy {
    private final int percent;
    PercentOff(int percent) { this.percent = percent; }
    public long discount(long s) { return s * percent / 100; }
}

class ShoppingService {
    private final Map<String, Product> catalogue = new LinkedHashMap<>();
    private final Map<String, Cart> carts = new HashMap<>();
    private final Map<String, Order> orders = new LinkedHashMap<>();
    private final Inventory inventory = new Inventory();
    private DiscountStrategy discounts = new NoDiscount();
    private int seq = 0;

    void addProduct(Product p, int qty) { catalogue.put(p.sku, p); inventory.restock(p.sku, qty); }
    void subscribe(StockObserver o) { inventory.subscribe(o); }
    void setDiscounts(DiscountStrategy d) { discounts = d; }
    Cart cartOf(String userId) { return carts.computeIfAbsent(userId, k -> new Cart()); }

    synchronized Order checkout(String userId) {
        Cart cart = cartOf(userId);
        if (cart.items.isEmpty()) throw new IllegalStateException("Cart is empty");
        inventory.reserve(cart.items);                              // throws → nothing reserved
        long subtotal = cart.items.entrySet().stream()
                .mapToLong(e -> catalogue.get(e.getKey()).price * e.getValue()).sum();
        Order order = new Order("O" + (++seq), cart.items, subtotal);
        orders.put(order.id, order);
        cart.items.clear();
        return order;
    }

    long pay(Order order) {
        inventory.commit(order.items);                              // reservation → sale
        order.pay();
        return order.subtotal - discounts.discount(order.subtotal);
    }
    void ship(Order order)    { order.ship(); }
    void deliver(Order order) { order.deliver(); }

    void cancel(Order order) {
        OrderState s = order.state();
        if (s != OrderState.CREATED && s != OrderState.PAID)
            throw new IllegalStateException("Cannot cancel a " + s + " order");
        if (s == OrderState.CREATED) inventory.release(order.items);      // not yet sold
        else inventory.restockItems(order.items);                         // sold: back on shelf
        order.cancel();
    }
}
```

**Usage**
```java
ShoppingService shop = new ShoppingService();
shop.addProduct(new Product("SKU-1", "Mechanical Keyboard", 4_500), 5);
shop.setDiscounts(new PercentOff(10));

shop.cartOf("u1").add("SKU-1", 2);
Order o = shop.checkout("u1");          // 2 units reserved; available drops from 5 → 3
long paid = shop.pay(o);                // committed: on-hand 5 → 3
shop.ship(o); shop.deliver(o);

shop.cartOf("u2").add("SKU-1", 1);
Order o2 = shop.checkout("u2");
shop.cancel(o2);                        // CREATED → reservation released; available back to 2
```

### Design points

- **Reserved ≠ on-hand** — checkout reserves, payment commits; every cancel branch knows which one to undo.
- **All-or-nothing reserve** — the check loop runs before any reservation write; no partial holds.
- **State graph in `Order`** — pay/ship/deliver/cancel each guard their from-state; illegal jumps cannot compile a story.
- **Inventory notifies, carts listen** — back-in-stock alerts fall out of restock events, no polling.

**Complexity:** checkout O(items) · pay O(items) · available O(1).

---
#lld #machine-coding #amazon #hard #practice