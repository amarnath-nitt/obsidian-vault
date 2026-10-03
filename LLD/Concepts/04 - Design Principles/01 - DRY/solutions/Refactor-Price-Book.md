# Refactor Price Book (DRY)

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Principle:** DRY
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/refactor-price-book)

### Problem

A checkout prices items by looking up hard-coded numbers scattered across the codebase. The same
price is written in multiple places (a "price book" hidden in the code), so a price change can leave
the system inconsistent. Apply **DRY** by giving prices a single source of truth.

### The Smell (before)

```java
class Checkout {
    double total(String sku, int qty) {
        double price;
        if (sku.equals("COFFEE")) price = 3.50;       // magic number
        else if (sku.equals("TEA")) price = 2.75;     // magic number
        else price = 0;
        return price * qty;
    }
}
class Receipt {
    double linePrice(String sku) {
        if (sku.equals("COFFEE")) return 3.50;        // duplicated magic number
        if (sku.equals("TEA"))    return 2.75;        // duplicated magic number
        return 0;
    }
}
```

### The Fix (after)

```java
import java.util.*;

// The single source of truth for prices
final class PriceBook {
    private static final Map<String, Double> PRICES = Map.of(
        "COFFEE", 3.50,
        "TEA",    2.75,
        "CAKE",   4.25
    );

    private PriceBook() {}

    static double priceOf(String sku) {
        Double price = PRICES.get(sku);
        if (price == null) throw new IllegalArgumentException("Unknown SKU: " + sku);
        return price;
    }
}
```

```java
class Checkout {
    double total(String sku, int qty) { return PriceBook.priceOf(sku) * qty; }
}
class Receipt {
    double linePrice(String sku) { return PriceBook.priceOf(sku); }
}
```

### Design points
- **Single source of truth** — prices live in exactly one map.
- **Change once** — updating a price edits `PriceBook` only.
- **No magic numbers** — every lookup goes through a named, validating method.
- **Fail fast** — an unknown SKU raises a clear error instead of silently pricing at `0`.

**Complexity:** O(1) per lookup · Space O(SKUs)

---
#design-principles #dry #lld #practice