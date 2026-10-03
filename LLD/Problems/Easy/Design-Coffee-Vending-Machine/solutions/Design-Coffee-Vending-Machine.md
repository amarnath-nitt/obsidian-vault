# Design Coffee Vending Machine (Easy)

**Difficulty:** Easy · **Patterns:** Factory, State
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design a coffee machine: recipes from ingredient containers, payment, atomic brew, refill, low alerts.

**Functional**
- **Recipes**: espresso, latte, cappuccino — each with ingredient map + price.
- **Select** only if ingredients suffice; **pay**; **brew** deducts atomically; **cancel** refunds.
- Operator **refills** containers; machine flags **low** ingredients.

**Non-functional**
- New recipes via factory registration; no partial brews.

### The failure, before

```java
// ❌ switch-on-string recipes with inline ingredient math —
// latte deducts milk but fails on beans: half-brewed cup, money kept.
switch (choice) { case "latte": milk -= 2; beans -= 1; ... }
```

### The Fix (after)

`RecipeFactory` + containers with atomic `takeAll` + small state machine.

```java
import java.util.*;

class Recipe {
    final String code, name; final int price; final Map<String, Integer> needs;
    Recipe(String code, String name, int price, Map<String, Integer> needs) {
        this.code = code; this.name = name; this.price = price; this.needs = Map.copyOf(needs);
    }
}

class RecipeFactory {
    private final Map<String, Recipe> recipes = new HashMap<>();
    RecipeFactory() {
        register(new Recipe("E", "Espresso",   30, Map.of("water", 1, "beans", 2)));
        register(new Recipe("L", "Latte",      50, Map.of("water", 1, "beans", 2, "milk", 2)));
        register(new Recipe("C", "Cappuccino", 60, Map.of("water", 1, "beans", 2, "milk", 3)));
    }
    public void register(Recipe r) { recipes.put(r.code, r); }   // new drink = one line
    public Recipe create(String code) {
        Recipe r = recipes.get(code);
        if (r == null) throw new IllegalArgumentException("Bad code");
        return r;
    }
}

class IngredientContainer {
    private final String name; private int level; private final int capacity;
    IngredientContainer(String name, int capacity) { this.name = name; this.capacity = capacity; this.level = capacity; }
    public int level() { return level; }
    public boolean low() { return level * 4 < capacity; }   // < 25%
    public void refill() { level = capacity; }
    void take(int n) {
        if (level < n) throw new IllegalStateException(name + " insufficient");
        level -= n;
    }
}

class CoffeeMachine {
    private final RecipeFactory factory = new RecipeFactory();
    private final Map<String, IngredientContainer> bins = new HashMap<>();
    private int inserted = 0;

    CoffeeMachine() {
        bins.put("water", new IngredientContainer("water", 20));
        bins.put("milk",  new IngredientContainer("milk", 20));
        bins.put("beans", new IngredientContainer("beans", 20));
    }
    public void insert(int v) { inserted += v; }
    public void cancel() { System.out.println("Refunded " + inserted); inserted = 0; }

    public synchronized String brew(String code) {
        Recipe r = factory.create(code);
        for (var e : r.needs.entrySet())                        // 1. validate ALL
            if (bins.get(e.getKey()).level() < e.getValue())
                throw new IllegalStateException("Insufficient " + e.getKey());
        if (inserted < r.price) throw new IllegalStateException("Need " + r.price);
        for (var e : r.needs.entrySet()) bins.get(e.getKey()).take(e.getValue());  // 2. deduct ALL
        int change = inserted - r.price; inserted = 0;
        return "Brewed " + r.name + ", change " + change;        // 3. dispense
    }
    public void refillAll() { bins.values().forEach(IngredientContainer::refill); }
    public List<String> low() {
        List<String> out = new ArrayList<>();
        bins.forEach((k, v) -> { if (v.low()) out.add(k); });
        return out;
    }
}
```

**Usage**
```java
CoffeeMachine m = new CoffeeMachine();
m.insert(60); System.out.println(m.brew("C"));  // Brewed Cappuccino, change 0
```

### Design points
- **Validate-all, then deduct-all** — the two loops are the atomicity; no half-brew exists.
- **Factory owns the menu** — mocha = one `register`, brewer untouched.
- **Containers bound the domain** — `take` throws below zero; `low()` warns at 25%.
- **Synchronized brew** — one cup at a time per machine; check-and-deduct can't interleave.

**Complexity:** brew O(ingredients) · Space O(recipes + bins).

---
#lld #machine-coding #coffee-machine #easy #practice
