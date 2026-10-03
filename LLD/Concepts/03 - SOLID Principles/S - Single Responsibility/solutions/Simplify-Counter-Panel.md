# Simplify a Counter Panel (Single Responsibility)

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Principle:** Single Responsibility
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/simplify-counter-panel)

### Problem

A `CounterPanel` holds the count, formats it for display, and handles increment/decrement requests —
three responsibilities tangled together. Refactor so the **counter state**, the **formatting**, and the
**input handling** each live separately.

### The Smell (before)

```java
// ❌ State + formatting + input handling in one class
class CounterPanel {
    private int count = 0;

    String onIncrementClicked() {                 // input handling + state + formatting
        count++;
        return "Count: " + count + (count == 1 ? " item" : " items");
    }
    String onDecrementClicked() {
        if (count > 0) count--;
        return "Count: " + count + (count == 1 ? " item" : " items");
    }
    String render() { return "[" + count + "]"; }   // a third format, same class
}
```

### The Fix (after)

```java
// 1. State — the only thing that knows the count and its rules
class Counter {
    private int value = 0;
    void increment()          { value++; }
    void decrement()          { if (value > 0) value--; }   // rule lives here
    int value()               { return value; }
}

// 2. Formatting — the only thing that knows how to render a count
class CounterFormatter {
    String label(int count) { return "Count: " + count + (count == 1 ? " item" : " items"); }
    String badge(int count) { return "[" + count + "]"; }
}

// 3. Input handling — the only thing that translates UI events into counter actions
class CounterPanel {
    private final Counter counter;
    private final CounterFormatter formatter;

    CounterPanel(Counter counter, CounterFormatter formatter) {
        this.counter = counter; this.formatter = formatter;
    }

    String onIncrementClicked() { counter.increment(); return formatter.label(counter.value()); }
    String onDecrementClicked() { counter.decrement(); return formatter.label(counter.value()); }
    String render()             { return formatter.badge(counter.value()); }
}
```

**Usage**
```java
CounterPanel panel = new CounterPanel(new Counter(), new CounterFormatter());
panel.onIncrementClicked();   // "Count: 1 item"
panel.onDecrementClicked();   // "Count: 0 items"
panel.render();               // "[0]"
```

### Design points
- **Three responsibilities, three classes** — state, formatting, and event handling.
- **Rules live with state** — "never below zero" belongs to `Counter`.
- **Formatting is reusable** — `CounterFormatter` can serve any view.
- **Testable** — you can unit-test `Counter` and `CounterFormatter` without any UI.

**Complexity:** O(1) per operation · Space O(1)

---
#solid #srp #lld #practice