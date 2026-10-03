# Design Plugin Editor

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Topic:** Interfaces
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-plugin-editor)

### Problem

Design an editor that runs a series of **plugins** over a piece of text. Each plugin transforms the
text in some way. The editor must not know the concrete plugin classes — it should depend only on a
**plugin interface**, so new plugins can be added without changing the editor.

### Approach

- Define a `Plugin` interface (`name()`, `transform(input)`).
- The editor holds a list of `Plugin` references and applies them in order.
- Concrete plugins (`UpperCasePlugin`, `ReversePlugin`, …) implement the interface.

### Java Solution

```java
import java.util.*;

// The contract the editor depends on
public interface Plugin {
    String name();
    String transform(String input);
}

// Concrete plugins
class UpperCasePlugin implements Plugin {
    public String name() { return "uppercase"; }
    public String transform(String input) { return input.toUpperCase(); }
}
class ReversePlugin implements Plugin {
    public String name() { return "reverse"; }
    public String transform(String input) { return new StringBuilder(input).reverse().toString(); }
}
class TrimPlugin implements Plugin {
    public String name() { return "trim"; }
    public String transform(String input) { return input.strip(); }
}

// The editor knows only the interface
public class Editor {
    private final List<Plugin> plugins = new ArrayList<>();

    public void register(Plugin plugin) { plugins.add(plugin); }

    public String run(String text) {
        String result = text;
        for (Plugin plugin : plugins) {
            result = plugin.transform(result);       // polymorphic dispatch
        }
        return result;
    }

    public List<String> pluginNames() {
        List<String> names = new ArrayList<>();
        for (Plugin p : plugins) names.add(p.name());
        return names;
    }
}
```

**Usage**
```java
Editor editor = new Editor();
editor.register(new TrimPlugin());
editor.register(new UpperCasePlugin());
editor.register(new ReversePlugin());

editor.run("  hello  ");      // "OLLEH"
```

### Design points
- **Program to an interface** — `Editor` never references a concrete plugin.
- **Polymorphism** — `plugin.transform(...)` resolves at runtime.
- **Open/Closed** — add a `CensorPlugin` without editing `Editor`.

**Complexity:** O(plugins × text) per run · Space O(text)

---
#oop #interfaces #lld #practice