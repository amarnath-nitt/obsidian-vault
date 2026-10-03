# Design Subscription Plans (Inheritance)

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Topic:** Inheritance
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-subscription-plans)

### Problem

Design subscription plans — a **Free**, **Premium**, and **Enterprise** tier. All plans share common
behaviour (price formatting, a `describe()` summary) but differ in limits and cost. Use **inheritance**
so shared logic lives in one base class.

### Approach

- `SubscriptionPlan` (abstract) holds the plan name and shared helpers.
- Subclasses define the varying values (`monthlyCost`, `maxProjects`, `maxStorageGb`).
- A `final summary()` in the base reuses the subclass values.

### Java Solution

```java
public abstract class SubscriptionPlan {

    protected final String name;
    protected SubscriptionPlan(String name) { this.name = name; }

    public abstract double monthlyCost();
    public abstract int maxProjects();
    public abstract int maxStorageGb();

    public boolean supportsProjects(int count) { return count <= maxProjects(); }

    /** Shared summary reused by every plan (is-a). */
    public final String summary() {
        return name + " — $" + String.format("%.2f", monthlyCost())
                + "/mo, " + maxProjects() + " projects, " + maxStorageGb() + " GB";
    }

    public String name() { return name; }
}

class FreePlan extends SubscriptionPlan {
    FreePlan() { super("Free"); }
    public double monthlyCost() { return 0.0; }
    public int maxProjects()    { return 1; }
    public int maxStorageGb()   { return 1; }
}

class PremiumPlan extends SubscriptionPlan {
    PremiumPlan() { super("Premium"); }
    public double monthlyCost() { return 19.99; }
    public int maxProjects()    { return 20; }
    public int maxStorageGb()   { return 100; }
}

class EnterprisePlan extends SubscriptionPlan {
    private final int seats;
    EnterprisePlan(int seats) { super("Enterprise"); this.seats = seats; }
    public double monthlyCost() { return 49.99 * seats; }
    public int maxProjects()    { return Integer.MAX_VALUE; }
    public int maxStorageGb()   { return 1000; }
    public int seats()          { return seats; }
}
```

**Usage**
```java
SubscriptionPlan plan = new PremiumPlan();
plan.summary();               // "Premium — $19.99/mo, 20 projects, 100 GB"
plan.supportsProjects(10);    // true

new FreePlan().supportsProjects(5);   // false
```

### Design points
- **Shared code in the base** — `summary()` and `supportsProjects()` are inherited.
- **Varying data in subclasses** — limits and cost overridden per plan.
- **`final summary()`** — subclasses cannot break the shared format.
- **Correct is-a** — a `PremiumPlan` *is-a* `SubscriptionPlan`.

**Complexity:** O(1) per query · Space O(1)

---
#oop #inheritance #lld #practice