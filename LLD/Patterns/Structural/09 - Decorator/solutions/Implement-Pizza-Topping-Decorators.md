# Implement Pizza Topping Decorators

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Pattern:** Decorator
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/implement-pizza-topping-decorators)

### Problem

A pizza has a base price and a description. **Toppings** (cheese, olives, mushrooms) can be added in
any combination, and each adds its own cost and updates the description. Support **any combination**
without creating a class per combination.

### Approach — Decorator

- **Component** = `Pizza` (`description`, `cost`).
- **ConcreteComponent** = `Margherita` base.
- **Decorator** = abstract `ToppingDecorator` holding a wrapped `Pizza`.
- **ConcreteDecorators** = `Cheese`, `Olives`, `Mushrooms`.

### Java Solution

```java
// Component
interface Pizza {
    String description();
    double cost();
}

// ConcreteComponent
class Margherita implements Pizza {
    public String description() { return "Margherita"; }
    public double cost()        { return 6.00; }
}

// Decorator base
abstract class ToppingDecorator implements Pizza {
    protected final Pizza inner;
    protected ToppingDecorator(Pizza inner) { this.inner = inner; }
    public String description() { return inner.description(); }
    public double cost()        { return inner.cost(); }
}

// Concrete decorators
class Cheese extends ToppingDecorator {
    Cheese(Pizza p) { super(p); }
    public String description() { return super.description() + " + cheese"; }
    public double cost()        { return super.cost() + 1.50; }
}
class Olives extends ToppingDecorator {
    Olives(Pizza p) { super(p); }
    public String description() { return super.description() + " + olives"; }
    public double cost()        { return super.cost() + 0.75; }
}
class Mushrooms extends ToppingDecorator {
    Mushrooms(Pizza p) { super(p); }
    public String description() { return super.description() + " + mushrooms"; }
    public double cost()        { return super.cost() + 1.00; }
}
```

**Usage — stack any combination**
```java
Pizza pizza = new Mushrooms(new Olives(new Cheese(new Margherita())));
System.out.println(pizza.description() + " = $" + pizza.cost());
// Margherita + cheese + olives + mushrooms = $9.25
```

### Why Decorator (and not inheritance)
- **2ⁿ combinations** would need `2ⁿ` subclasses; decorators need only **n** classes.
- Each topping is **composed at runtime**, so combos are built dynamically.
- **Order is preserved** — the description reflects nesting order.

**Complexity:** O(depth) per `cost()`/`description()` · Space O(depth)

---
#decorator #lld #practice