# Design Plugin System

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Factory Method
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-plugin-system-factory)

### Problem

Design a plugin system: the host loads a plugin **by name** and runs it, without the host knowing
the concrete plugin classes. New plugins must be addable without editing the host (Open/Closed).

### Approach

- `Plugin` — the product interface (`name()`, `execute(input)`).
- `PluginFactory` — the creator interface with a `create()` factory method.
- Each plugin ships **its own factory** — the class that knows how to build it.
- `PluginRegistry` maps a name → factory and hands back a fresh `Plugin` on demand.

### Java Solution

```java
// Product
interface Plugin {
    String name();
    void execute(String input);
}

class FormatterPlugin implements Plugin {
    public String name() { return "formatter"; }
    public void execute(String input) { System.out.println("formatted: " + input.trim()); }
}
class LinterPlugin implements Plugin {
    public String name() { return "linter"; }
    public void execute(String input) { System.out.println("linted: " + input); }
}
class CompressorPlugin implements Plugin {
    public String name() { return "compressor"; }
    public void execute(String input) { System.out.println("compressed len=" + input.length()); }
}

// Creator (factory method)
interface PluginFactory {
    Plugin create();
}
class FormatterPluginFactory  implements PluginFactory { public Plugin create() { return new FormatterPlugin(); } }
class LinterPluginFactory     implements PluginFactory { public Plugin create() { return new LinterPlugin(); } }
class CompressorPluginFactory implements PluginFactory { public Plugin create() { return new CompressorPlugin(); } }

// Registry: name -> creator
import java.util.*;

class PluginRegistry {
    private final Map<String, PluginFactory> factories = new HashMap<>();

    public void register(String name, PluginFactory factory) { factories.put(name, factory); }
    public boolean has(String name) { return factories.containsKey(name); }

    public Plugin load(String name) {
        PluginFactory factory = factories.get(name);
        if (factory == null) throw new IllegalArgumentException("Unknown plugin: " + name);
        return factory.create();                 // a fresh plugin each time
    }
}
```

**Usage**
```java
PluginRegistry registry = new PluginRegistry();
registry.register("formatter",  new FormatterPluginFactory());
registry.register("linter",     new LinterPluginFactory());
registry.register("compressor", new CompressorPluginFactory());

Plugin p = registry.load("formatter");
p.execute("  hello  ");                 // "formatted: hello"
```

### Why it works
- **Host depends only on `Plugin`** — it never references a concrete plugin class.
- **Adding a plugin = register a new factory** — no change to the host or registry code (OCP).
- **Fresh instance per `load`** — plugins are not accidentally shared.

**Complexity:** O(1) per lookup/create · Space O(plugins)

---
#factory-method #plugins #lld #practice