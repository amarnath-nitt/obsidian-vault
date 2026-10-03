# Design a Traffic Light (State)

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Pattern:** State
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-state-traffic-light)

### Problem (contract)

Design the `Color` model used by a `TrafficLight` controller. The controller shows one colour at a
time and cycles **red → green → yellow → red**.

- `TrafficLight(String startColor)` starts on `RED`/`GREEN`/`YELLOW` (case-insensitive); an
  unrecognised value defaults to `RED`.
- `getColor()` returns the current colour's name.
- `getDuration()` returns the current duration: RED 30s, GREEN 25s, YELLOW 5s.
- `next()` advances one step and returns the new colour's name.
- `describe()` returns `"<COLOR> (<duration>s)"`, e.g. `"RED (30s)"`.
- Each colour must know **its own duration and its successor** — the cycle is not spelled out in the controller.

### Approach — State via an enum

- Model the colours as an **enum** whose members carry the duration and the next colour.
- The controller just asks the current colour for its successor.

### Java Solution

```java
enum Color {
    RED(30, null),          // successor wired after declaration
    GREEN(25, null),
    YELLOW(5, null);

    private final int duration;
    private Color next;

    Color(int duration, Color next) { this.duration = duration; }   // next set below

    static {                     // define the cycle once, alongside the colours
        RED.next = GREEN;
        GREEN.next = YELLOW;
        YELLOW.next = RED;
    }

    int duration() { return duration; }
    Color successor() { return next; }

    static Color from(String name) {
        for (Color c : values()) if (c.name().equalsIgnoreCase(name)) return c;
        return RED;              // unrecognised → default
    }
}

class TrafficLight {
    private Color color;

    TrafficLight(String startColor) { this.color = Color.from(startColor); }

    String getColor()   { return color.name(); }
    int getDuration()   { return color.duration(); }
    String describe()   { return color.name() + " (" + color.duration() + "s)"; }
    String next()       { color = color.successor(); return color.name(); }
}
```

**Usage**
```java
TrafficLight light = new TrafficLight("red");
System.out.println(light.describe());   // RED (30s)
System.out.println(light.next());        // GREEN
System.out.println(light.getDuration()); // 25

new TrafficLight("purple").getColor();   // "RED" (default)
```

### Design points
- **Enum modelling** — the colours are a closed set.
- **Cycle contained** — each colour knows its successor, so `TrafficLight.next` does no branching.
- **Unknown start defaulted** — invalid input is handled deliberately.

**Complexity:** O(1) per operation · Space O(1)

---
#state #lld #practice