# Design Computer Workshop (Composition)

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Relationship:** Composition
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-computer-workshop)

### Problem

Design a workshop that assembles **computers** from **components** (CPU, RAM, disk). A component is
installed into one specific computer and is meaningless outside it — installing it elsewhere would
require physically moving it. The computer **owns** its components (composition).

### Approach — Composition

- `Component` instances are created **for** a computer and belong exclusively to it.
- `Computer` exposes `install(...)` that creates and owns components.
- A `Workshop` assembles computers.

### Java Solution

```java
import java.util.*;

public class Computer {

    private final String model;
    private final List<Component> components = new ArrayList<>();   // owned, exclusive

    public Computer(String model) { this.model = model; }

    /** Creates a component owned by this computer — not shared. */
    public void install(String type, String spec) {
        components.add(new Component(type, spec));
    }

    public String model() { return model; }
    public int componentCount() { return components.size(); }
    public List<String> specs() {
        List<String> out = new ArrayList<>();
        for (Component c : components) out.add(c.type() + ":" + c.spec());
        return out;
    }
}

/** Exclusively owned by a Computer (constructor is package-private). */
class Component {
    private final String type;
    private final String spec;
    Component(String type, String spec) { this.type = type; this.spec = spec; }
    String type() { return type; }
    String spec() { return spec; }
}

public class Workshop {

    private final List<Computer> built = new ArrayList<>();

    /** Assembles a computer from a spec sheet, creating its owned components. */
    public Computer assemble(String model, Map<String, String> parts) {
        Computer computer = new Computer(model);
        parts.forEach(computer::install);       // components created inside the computer
        built.add(computer);
        return computer;
    }

    public List<String> builtModels() {
        List<String> models = new ArrayList<>();
        for (Computer c : built) models.add(c.model());
        return models;
    }
}
```

**Usage**
```java
Workshop workshop = new Workshop();
Computer pc = workshop.assemble("Workstation", Map.of(
        "CPU", "8-core", "RAM", "32GB", "Disk", "1TB SSD"));

pc.componentCount();   // 3
pc.specs();            // [CPU:8-core, RAM:32GB, Disk:1TB SSD]
```

### Why Composition
- **Exclusive ownership** — a component belongs to exactly one computer.
- **Lifetime bound** — destroying the computer destroys its components.
- **Created internally** — `install` is the only way a component comes into being.
- **Not shareable** — you cannot move the RAM into another machine.

**Complexity:** O(parts) per assembly · Space O(parts)

---
#oop #composition #lld #practice