# Design Shopping Cart (Encapsulation)

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Topic:** Encapsulation
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-shopping-cart)

### Problem

Design a `ShoppingCart` that holds line items (a product and a quantity). Callers add and remove
items and ask for the total. The cart must **encapsulate** its items — no caller may reach in and
mutate the internal collection, and quantities must stay valid.

### Approach

- Keep the items in a **private** map keyed by product id.
- Mutating operations validate quantities; queries return copies, never the live store.

### Java Solution

```java
import java.util.*;

public class ShoppingCart {

    public record LineItem(String productId, String name, double price, int quantity) {
        double subtotal() { return price * quantity; }
    }

    private final Map<String, LineItem> items = new LinkedHashMap<>();   // private state

    /** Adds a product, accumulating quantity if it is already in the cart. */
    public void add(String productId, String name, double price, int quantity) {
        if (quantity <= 0) throw new IllegalArgumentException("quantity must be > 0");
        if (price < 0)     throw new IllegalArgumentException("price must be >= 0");

        items.merge(productId,
                new LineItem(productId, name, price, quantity),
                (old, add) -> new LineItem(old.productId(), old.name(), old.price(),
                                           old.quantity() + add.quantity()));
    }

    /** Returns true if the product was present and is now fully removed. */
    public boolean remove(String productId) { return items.remove(productId) != null; }

    public double total() {
        double sum = 0;
        for (LineItem item : items.values()) sum += item.subtotal();
        return sum;
    }

    public int distinctProducts() { return items.size(); }

    /** A safe, read-only view of the cart contents. */
    public List<LineItem> items() { return List.copyOf(items.values()); }
}
```

**Usage**
```java
ShoppingCart cart = new ShoppingCart();
cart.add("P1", "Keyboard", 50.0, 1);
cart.add("P1", "Keyboard", 50.0, 2);   // accumulates → qty 3
cart.add("P2", "Mouse", 20.0, 1);

cart.total();               // 50*3 + 20 = 170.0
cart.items().size();        // 2
cart.remove("P2");          // true
```

### Design points
- **Encapsulation** — the map is private; `items()` returns an immutable snapshot.
- **Validating mutations** — quantity/price checked before state changes.
- **Accumulating adds** — `merge` folds duplicate products into one line.

**Complexity:** O(items) per total · Space O(items)

---
#oop #encapsulation #lld #practice