# Design a Widget Palette

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Prototype
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-widget-palette)

### Problem

A UI builder offers a **palette** of pre-configured widgets (a styled button, a labelled input, a
card). Dropping a widget onto the canvas should produce a **copy** of the palette template — with its
own position and state — rather than re-creating the configuration each time.

### Approach

- A `Prototype` interface with `clone()`.
- A `WidgetPalette` registry maps a template name → prototype.
- `stamp(name, x, y)` looks up the prototype, **clones** it, and places the copy at `(x, y)`.

### Java Solution

```java
import java.util.*;

interface Prototype { Prototype clone(); }

class Widget implements Prototype {

    private final String kind;          // "button", "input", "card"
    private final String style;         // styling shared from the template
    private final Map<String, String> config;
    private int x, y;                   // instance state

    Widget(String kind, String style, Map<String, String> config) {
        this.kind = kind;
        this.style = style;
        this.config = config;
    }

    void placeAt(int x, int y) { this.x = x; this.y = y; }
    void set(String key, String value) { config.put(key, value); }

    @Override
    public Widget clone() {
        // new widget, deep-copied config so instances are independent
        return new Widget(kind, style, new HashMap<>(config));
    }

    @Override public String toString() {
        return kind + "[" + style + ", " + config + "] at (" + x + "," + y + ")";
    }
}

class WidgetPalette {
    private final Map<String, Widget> templates = new HashMap<>();

    void register(String name, Widget template) { templates.put(name, template); }
    boolean has(String name) { return templates.containsKey(name); }

    Widget stamp(String name, int x, int y) {
        Widget template = templates.get(name);
        if (template == null) throw new IllegalArgumentException("Unknown widget: " + name);
        Widget copy = template.clone();        // ← prototype copy
        copy.placeAt(x, y);
        return copy;
    }
}
```

**Usage**
```java
WidgetPalette palette = new WidgetPalette();
palette.register("primaryButton",
        new Widget("button", "primary", new HashMap<>(Map.of("label", "Submit"))));

Widget a = palette.stamp("primaryButton", 10, 20);
Widget b = palette.stamp("primaryButton", 10, 80);
a.set("label", "Save");                 // only edits copy "a"

System.out.println(a);  // button[primary, {label=Save}]   at (10,20)
System.out.println(b);  // button[primary, {label=Submit}] at (10,80)
```

### Design points
- **Templates configured once** — restyling a template re-uses the same object graph shape.
- **Deep-copied config** — editing one dropped widget never mutates the template or its siblings.
- **Registry + clone** — the palette is a cache of prototypes, so new widgets are cheap.

**Complexity:** O(config) per clone · Space O(config) per widget

---
#prototype #ui #lld #practice