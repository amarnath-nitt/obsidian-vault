# Design a Route Planner

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Pattern:** Strategy
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-route-planner)

### Problem

A navigation app computes a route between two points. Users can choose a **preference** — fastest,
shortest, cheapest, or most scenic — and each preference applies a different algorithm/weighting. The
planner should not contain a growing `switch` over preferences.

### Approach — Strategy

- `RoutingStrategy` — the interface (`route(from, to)`).
- Concrete strategies: `FastestRoute`, `ShortestRoute`, `CheapestRoute`, `ScenicRoute`.
- `Navigator` holds a strategy and delegates; the user can switch preference at any time.

### Java Solution

```java
interface RoutingStrategy {
    String route(String from, String to);
}

class FastestRoute implements RoutingStrategy {
    public String route(String from, String to) { return "Fastest: " + from + " → highway → " + to; }
}
class ShortestRoute implements RoutingStrategy {
    public String route(String from, String to) { return "Shortest: " + from + " → direct → " + to; }
}
class CheapestRoute implements RoutingStrategy {
    public String route(String from, String to) { return "Cheapest: " + from + " → toll-free → " + to; }
}
class ScenicRoute implements RoutingStrategy {
    public String route(String from, String to) { return "Scenic: " + from + " → coast road → " + to; }
}

class Navigator {
    private RoutingStrategy strategy;

    Navigator(RoutingStrategy strategy) { this.strategy = strategy; }
    public void setStrategy(RoutingStrategy strategy) { this.strategy = strategy; }
    public String plan(String from, String to) { return strategy.route(from, to); }
}
```

**Usage**
```java
Navigator nav = new Navigator(new FastestRoute());
System.out.println(nav.plan("Home", "Office"));   // Fastest: ...

nav.setStrategy(new ScenicRoute());
System.out.println(nav.plan("Home", "Office"));   // Scenic: ...
```

**Choosing the strategy from user input (registry, no `switch`)**
```java
import java.util.*;
import java.util.function.Supplier;

class RoutingStrategies {
    private static final Map<String, Supplier<RoutingStrategy>> REGISTRY = Map.of(
        "fastest",  FastestRoute::new,
        "shortest", ShortestRoute::new,
        "cheapest", CheapestRoute::new,
        "scenic",   ScenicRoute::new
    );
    static RoutingStrategy of(String preference) {
        Supplier<RoutingStrategy> s = REGISTRY.get(preference.toLowerCase());
        if (s == null) throw new IllegalArgumentException("Unknown preference: " + preference);
        return s.get();
    }
}
```

### Design points
- **Algorithm isolated** — each routing preference is a class, not a branch in `Navigator`.
- **Runtime change** — the user can switch preference mid-session.
- **Registry** — selection logic lives outside the context, preserving Open/Closed.

**Complexity:** O(1) per plan (algorithm-specific cost lives inside the strategy) · Space O(1)

---
#strategy #lld #practice