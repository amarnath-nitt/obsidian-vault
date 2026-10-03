# Refactor Shipping Desk (Law of Demeter)

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Principle:** Law of Demeter
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/refactor-shipping-desk)

### Problem

A shipping desk prepares labels by navigating deep chains:
`order.getCustomer().getAddress().getPostcode()` and `order.getItems().get(0).getProduct().getWeight()`.
Every hop is a coupling to an internal structure. Apply the **Law of Demeter**.

### The Smell (before)

```java
class ShippingDesk {
    String label(Order order) {
        String postcode  = order.getCustomer().getAddress().getPostcode();          // 3 hops
        double weightKg  = order.getItems().get(0).getProduct().getWeightKg();      // 3 hops
        String country   = order.getCustomer().getAddress().getCountry();           // 3 hops (chain repeated)
        return country + "-" + postcode + " (" + weightKg + "kg)";
    }
}
```

### The Fix (after)

Give `Order` the responsibility of answering questions about itself.

```java
record Address(String line1, String postcode, String country) {}
record Customer(String name, Address address) {}
record Product(String name, double weightKg) {}
record OrderItem(Product product, int quantity) {}

class Order {
    private final Customer customer;
    private final java.util.List<OrderItem> items;

    Order(Customer customer, java.util.List<OrderItem> items) {
        this.customer = customer; this.items = items;
    }

    // Delegating methods — the Order answers, callers don't reach through
    String shippingPostcode()  { return customer.address().postcode(); }
    String shippingCountry()   { return customer.address().country(); }
    double totalWeightKg()     { return items.stream().mapToDouble(i -> i.product().weightKg() * i.quantity()).sum(); }

    /** A value object capturing exactly what a label needs. */
    record ShippingInfo(String country, String postcode, double weightKg) {}
    ShippingInfo shippingInfo() {
        return new ShippingInfo(shippingCountry(), shippingPostcode(), totalWeightKg());
    }
}

class ShippingDesk {
    String label(Order order) {
        Order.ShippingInfo info = order.shippingInfo();            // one friend: the order
        return info.country() + "-" + info.postcode() + " (" + info.weightKg() + "kg)";
    }
}
```

### Design points
- **One friend** — the desk talks only to `Order`.
- **Delegating methods** — `Order` hides `Customer`, `Address`, and `Product`.
- **Value object** — `ShippingInfo` bundles what the label needs, so the desk holds no deep references.
- **Also fixes a bug** — `totalWeightKg` sums *all* items (the old code used only the first).

> **Law of Demeter:** don't reach through objects you didn't receive. Ask your immediate collaborator
> to do the work.

**Complexity:** O(items) per label · Space O(1)

---
#design-principles #law-of-demeter #lld #practice