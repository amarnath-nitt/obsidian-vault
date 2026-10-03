# Design a Menu System

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Composite
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-menu-system)

### Problem

Design an application menu that contains **items** and **sub-menus**, to arbitrary depth. The menu
should be able to render itself as text, report its total item count, and search for an item — all
by treating a single item and a whole sub-menu **uniformly**.

### Approach — Composite

- **Component** = `MenuComponent` (`render`, `count`).
- **Leaf** = `MenuItem`.
- **Composite** = `Menu` (holds children, recurses).
- Child management (`add`) lives only on the composite (**safe** variant).

### Java Solution

```java
import java.util.*;

interface MenuComponent {
    String render(String indent);
    int count();
    Optional<MenuItem> find(String label);
}

// Leaf
class MenuItem implements MenuComponent {
    private final String label;
    private final Runnable action;
    MenuItem(String label, Runnable action) { this.label = label; this.action = action; }

    public String render(String indent) { return indent + "• " + label + "\n"; }
    public int count()                  { return 1; }
    public Optional<MenuItem> find(String l) { return label.equals(l) ? Optional.of(this) : Optional.empty(); }

    String label() { return label; }
    void click()   { action.run(); }
}

// Composite
class Menu implements MenuComponent {
    private final String title;
    private final List<MenuComponent> children = new ArrayList<>();
    Menu(String title) { this.title = title; }

    Menu add(MenuComponent c) { children.add(c); return this; }

    public String render(String indent) {
        StringBuilder sb = new StringBuilder(indent + "▾ " + title + "\n");
        for (MenuComponent c : children) sb.append(c.render(indent + "  "));   // recursion
        return sb.toString();
    }
    public int count() {
        int total = 0;
        for (MenuComponent c : children) total += c.count();                   // recursion
        return total;
    }
    public Optional<MenuItem> find(String label) {                             // recursion
        for (MenuComponent c : children) {
            Optional<MenuItem> hit = c.find(label);
            if (hit.isPresent()) return hit;
        }
        return Optional.empty();
    }
}
```

**Usage**
```java
Menu root = new Menu("File")
        .add(new MenuItem("New", () -> {}))
        .add(new Menu("Export")
                .add(new MenuItem("PDF", () -> {}))
                .add(new MenuItem("CSV", () -> {})));
root.add(new MenuItem("Exit", () -> {}));

System.out.println(root.render(""));
System.out.println("Items: " + root.count());          // 4
root.find("CSV").ifPresent(MenuItem::click);
```

### Design points
- **Uniform treatment** — `render`/`count`/`find` work on a single item or a whole subtree.
- **Arbitrary depth** — recursion handles any nesting.
- **Safe variant** — only `Menu` can `add`, so leaves cannot be misused.

**Complexity:** O(n) per operation over the tree · Space O(depth) for recursion

---
#composite #lld #practice