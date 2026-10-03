# Design Traffic Light (Enums)

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Topic:** Enums / State Management
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-traffic-light)

### Problem (contract)

Design the `Color` model for a `TrafficLight` controller that cycles **red → green → yellow → red**.

- `TrafficLight(String startColor)` — accepts `RED`/`GREEN`/`YELLOW` (case-insensitive);
  an unrecognised value defaults to `RED`.
- `getColor()` — the current colour's name.
- `getDuration()` — RED 30s, GREEN 25s, YELLOW 5s.
- `next()` — advance one step, return the new colour's name.
- `describe()` — `"<COLOR> (<duration>s)"`, e.g. `"RED (30s)"`.

Each colour knows **its own duration and successor** — the cycle is not spelled out in the controller.

### Approach

- Use an **enum** for the closed set of colours.
- Attach `duration` and the `next` colour to each constant (intrinsic behaviour in the enum).
- The controller merely asks the current colour for its successor.

### Java Solution

```java
public enum Color {
    RED(30), GREEN(25), YELLOW(5);

    private final int duration;
    private Color next;

    Color(int duration) { this.duration = duration; }   // successor wired in the static block

    static {
        RED.next = GREEN;
        GREEN.next = YELLOW;
        YELLOW.next = RED;          // the cycle is defined once, beside the colours
    }

    public int duration()  { return duration; }
    public Color successor() { return next; }

    public static Color from(String name) {
        for (Color c : values()) {
            if (c.name().equalsIgnoreCase(name)) return c;
        }
        return RED;                 // unrecognised → default
    }
}

public class TrafficLight {
    private Color color;

    public TrafficLight(String startColor) { this.color = Color.from(startColor); }

    public String getColor()   { return color.name(); }
    public int getDuration()   { return color.duration(); }
    public String describe()   { return color.name() + " (" + color.duration() + "s)"; }
    public String next()       { color = color.successor(); return color.name(); }
}
```

**Usage**
```java
TrafficLight light = new TrafficLight("red");
light.describe();        // "RED (30s)"
light.next();            // "GREEN"
light.getDuration();     // 25
new TrafficLight("purple").getColor();   // "RED" (default)
```

### Design points
- **Enum, not strings** — a closed set of colours with no magic values.
- **Cycle contained** — `next()` performs no branching; each colour knows its successor.
- **Deliberate default** — unknown input resolves to `RED`.

**Complexity:** O(1) per operation · Space O(1)

---
#oop #enums #lld #practice