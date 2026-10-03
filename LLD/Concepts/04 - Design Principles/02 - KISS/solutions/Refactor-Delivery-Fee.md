# Refactor Delivery Fee (KISS)

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Principle:** KISS
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/refactor-delivery-fee)

### Problem

A delivery-fee calculation has grown needlessly complex — flags, nested ternaries, and "clever"
one-liners make a simple rule hard to read. Apply **KISS**: express the rule plainly.

### The Smell (before)

```java
class DeliveryFee {
    double fee(double distanceKm, boolean isMember, boolean isPriority, boolean isWeekend) {
        return distanceKm <= 0 ? 0
             : (isMember
                 ? (isWeekend ? (isPriority ? 0.0 : 2.0) : (isPriority ? 1.0 : 3.0))
                 : (isWeekend ? (isPriority ? 4.0 : 6.0) : (isPriority ? 3.5 : 5.0)))
               + Math.max(0, distanceKm - 5) * 0.5;
    }
}
```

### The Fix (after)

Plain, readable rule with early returns and named values.

```java
class DeliveryFee {

    private static final double BASE_FEE = 5.0;
    private static final int FREE_DISTANCE_KM = 5;
    private static final double PER_EXTRA_KM = 0.5;

    double fee(double distanceKm, boolean isMember, boolean isPriority, boolean isWeekend) {
        if (distanceKm <= 0) return 0;

        double base = BASE_FEE;
        if (isWeekend) base += 1.0;
        if (isMember)  base -= 2.0;
        if (isPriority) base += 1.5;

        base = Math.max(0, base);                        // never negative
        double extraDistance = Math.max(0, distanceKm - FREE_DISTANCE_KM) * PER_EXTRA_KM;
        return base + extraDistance;
    }
}
```

### Design points
- **Readable control flow** — separate `if`s instead of nested ternaries.
- **Named constants** — `BASE_FEE`, `FREE_DISTANCE_KM` document the rule.
- **Obvious intent** — each line adds one surcharge; easy to change and test.
- **Same behaviour** — the rule is preserved; only the *expression* is simplified.

> **KISS principle:** the simplest design that satisfies the requirement wins. Clever code is a
> liability; obvious code is an asset.

**Complexity:** O(1) · Space O(1)

---
#design-principles #kiss #lld #practice