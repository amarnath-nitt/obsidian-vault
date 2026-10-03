# Design Theme Factory

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Abstract Factory
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-factory-theme)

### Problem

A UI toolkit must render a **matching family** of widgets for a chosen theme. A light theme must not
mix a light button with a dark checkbox. Provide an **Abstract Factory** per theme so one choice
produces a consistent set of products.

### Approach

- `Button`, `Checkbox`, `TextField` — abstract products.
- `ThemeFactory` — declares `createButton()`, `createCheckbox()`, `createTextField()`.
- `LightThemeFactory` / `DarkThemeFactory` — one concrete factory per family.
- The client picks a factory **once** and builds the whole family from it.

### Java Solution

```java
// Abstract products
interface Button    { String render(); }
interface Checkbox  { String render(); }
interface TextField { String render(); }

// Light family
class LightButton    implements Button    { public String render() { return "◻ Light Button"; } }
class LightCheckbox  implements Checkbox  { public String render() { return "◻ Light Checkbox"; } }
class LightTextField implements TextField { public String render() { return "◻ Light TextField"; } }

// Dark family
class DarkButton    implements Button    { public String render() { return "◼ Dark Button"; } }
class DarkCheckbox  implements Checkbox  { public String render() { return "◼ Dark Checkbox"; } }
class DarkTextField implements TextField { public String render() { return "◼ Dark TextField"; } }

// Abstract factory
interface ThemeFactory {
    Button    createButton();
    Checkbox  createCheckbox();
    TextField createTextField();
}

class LightThemeFactory implements ThemeFactory {
    public Button    createButton()    { return new LightButton(); }
    public Checkbox  createCheckbox()  { return new LightCheckbox(); }
    public TextField createTextField() { return new LightTextField(); }
}
class DarkThemeFactory implements ThemeFactory {
    public Button    createButton()    { return new DarkButton(); }
    public Checkbox  createCheckbox()  { return new DarkCheckbox(); }
    public TextField createTextField() { return new DarkTextField(); }
}
```

**Client — consistent family, chosen once**
```java
class Screen {
    private final Button button;
    private final Checkbox checkbox;
    private final TextField field;

    Screen(ThemeFactory factory) {
        this.button   = factory.createButton();
        this.checkbox = factory.createCheckbox();
        this.field    = factory.createTextField();
    }
    String render() { return button.render() + " | " + checkbox.render() + " | " + field.render(); }
}

// usage
String ui = new Screen(new DarkThemeFactory()).render();
```

### Design points
- **Family consistency** — the factory guarantees all widgets share the theme.
- **Client knows only `ThemeFactory`** — swapping themes means passing a different factory.
- **Adding a theme** = one new factory class; **adding a widget** = a new method on the factory + every family.

**Complexity:** O(1) per product · Space O(1)

---
#abstract-factory #lld #practice