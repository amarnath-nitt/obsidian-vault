# Design Stock Price Alerts

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Observer
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-stock-alerts)

### Problem

A stock feed reports price changes. Traders register **alerts** — for example "notify me when AAPL
crosses above 200". Each alert reacts to the relevant price updates, and alerts can be added or
removed at any time.

### Approach — Observer

- **Subject** = `StockMarket` (`setPrice`).
- **Observer** = `PriceAlert` — each alert holds the stock symbol and its own condition.
- The market notifies only the alerts registered for the symbol.

### Java Solution

```java
import java.util.*;
import java.util.concurrent.CopyOnWriteArrayList;

interface PriceObserver {
    void onPrice(String symbol, double price);
}

// A configurable threshold alert
class PriceAlert implements PriceObserver {
    private final String symbol;
    private final double threshold;
    private final boolean notifyAbove;      // true: alert when price > threshold
    private boolean triggered = false;

    PriceAlert(String symbol, double threshold, boolean notifyAbove) {
        this.symbol = symbol; this.threshold = threshold; this.notifyAbove = notifyAbove;
    }

    @Override
    public void onPrice(String symbol, double price) {
        if (!this.symbol.equals(symbol)) return;                 // ignore other symbols
        boolean hit = notifyAbove ? price > threshold : price < threshold;
        if (hit && !triggered) {
            triggered = true;
            System.out.println("🔔 " + symbol + " " + (notifyAbove ? "above" : "below")
                    + " " + threshold + " (now " + price + ")");
        } else if (!hit) {
            triggered = false;                                   // re-arm for next crossing
        }
    }
}

// Subject — per-symbol subscriber lists
class StockMarket {
    private final Map<String, List<PriceObserver>> observers = new HashMap<>();

    public void subscribe(String symbol, PriceObserver o) {
        observers.computeIfAbsent(symbol, k -> new CopyOnWriteArrayList<>()).add(o);
    }
    public void unsubscribe(String symbol, PriceObserver o) {
        List<PriceObserver> list = observers.get(symbol);
        if (list != null) list.remove(o);
    }

    public void setPrice(String symbol, double price) {
        System.out.println(symbol + " = " + price);
        for (PriceObserver o : observers.getOrDefault(symbol, List.of())) {
            o.onPrice(symbol, price);
        }
    }
}
```

**Usage**
```java
StockMarket market = new StockMarket();
market.subscribe("AAPL", new PriceAlert("AAPL", 200, true));    // above 200
market.subscribe("AAPL", new PriceAlert("AAPL", 150, false));   // below 150

market.setPrice("AAPL", 180);   // no alert
market.setPrice("AAPL", 205);   // "🔔 AAPL above 200.0 (now 205.0)"
```

### Design points
- **Selective notification** — observers are keyed by symbol, so alerts only see relevant updates.
- **Self-contained condition** — each alert owns its symbol, threshold and direction.
- **Edge-triggered** — `triggered` fires once per crossing, avoiding repeated spam.

**Complexity:** O(observers for symbol) per update · Space O(observers)

---
#observer #lld #practice