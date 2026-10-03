# Implement a Pizza Builder and Director

**Source:** AlgoMaster · Low-Level Design Practice · **hard (premium)** · **Pattern:** Builder + Director
🔗 [AlgoMaster problem (premium)](https://algomaster.io/practice/low-level-design)

### Problem

Build a `Pizza` two ways:

1. **Builder** — a fluent API for a custom pizza (size, crust, cheese, toppings).
2. **Director** — encapsulates *recipes* (Margherita, Pepperoni) that drive the builder through a
   fixed sequence of steps, so the same steps produce different pizzas.

### Approach

- `Pizza` is immutable; `Pizza.Builder` is the fluent builder.
- `PizzaDirector` holds a `Pizza.Builder` and exposes `makeMargherita()`, `makePepperoni()`.
- `build()` validates the required `size`.

### Java Solution

```java
import java.util.*;

public final class Pizza {

    private final String size;
    private final String crust;
    private final boolean cheese;
    private final List<String> toppings;

    private Pizza(Builder b) {
        this.size = b.size;
        this.crust = b.crust;
        this.cheese = b.cheese;
        this.toppings = List.copyOf(b.toppings);
    }

    @Override public String toString() {
        return size + " " + crust + (cheese ? " cheese" : "") + " pizza with " + toppings;
    }

    public static Builder builder() { return new Builder(); }

    public static final class Builder {
        private String size;
        private String crust = "regular";
        private boolean cheese;
        private final List<String> toppings = new ArrayList<>();

        public Builder size(String s)       { this.size = s; return this; }
        public Builder crust(String c)      { this.crust = c; return this; }
        public Builder cheese()             { this.cheese = true; return this; }
        public Builder addTopping(String t) { toppings.add(t); return this; }

        public Pizza build() {
            if (size == null || size.isBlank()) throw new IllegalStateException("size is required");
            return new Pizza(this);
        }
    }
}
```

**Director**
```java
public final class PizzaDirector {

    private final Pizza.Builder builder;

    public PizzaDirector(Pizza.Builder builder) { this.builder = builder; }

    public Pizza makeMargherita() {
        return builder.size("medium").crust("thin").cheese()
                      .addTopping("tomato").addTopping("basil")
                      .build();
    }

    public Pizza makePepperoni() {
        return builder.size("large").crust("regular").cheese()
                      .addTopping("pepperoni").addTopping("oregano")
                      .build();
    }
}
```

**Usage**
```java
Pizza custom     = Pizza.builder().size("small").addTopping("olives").build();
Pizza margherita = new PizzaDirector(Pizza.builder()).makeMargherita();
```

### Design points
- **Builder vs Director** — the Builder exposes the steps; the Director knows a *recipe* (a reusable
  sequence) and drives the builder.
- **Same steps, different pizzas** — the Director hard-codes the order; the builder stays generic.
- **Fresh builder per recipe** — pass a new `Pizza.builder()` so state never leaks between builds.

**Complexity:** O(toppings) · Space O(toppings)

---
#builder #director #lld #practice