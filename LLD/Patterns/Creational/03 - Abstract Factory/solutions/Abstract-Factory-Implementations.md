# Abstract Factory — Implementations & Examples

**Pattern:** Abstract Factory (Creational) · **Skill:** creating consistent families of objects

### Approach

- Define an **AbstractFactory** with one `create*()` per product type.
- Provide a **ConcreteFactory** per family (Light/Dark, AWS/GCP).
- The client picks a factory **once** and builds the whole family from it.

### Java Solutions

**1. Light / Dark UI Family**
```java
interface Button   { void render(); }
interface Checkbox { void render(); }

class LightButton   implements Button   { public void render() { System.out.println("◻ Light Button"); } }
class DarkButton    implements Button   { public void render() { System.out.println("◼ Dark Button"); } }
class LightCheckbox implements Checkbox { public void render() { System.out.println("◻ Light Checkbox"); } }
class DarkCheckbox  implements Checkbox { public void render() { System.out.println("◼ Dark Checkbox"); } }

interface UiFactory {
    Button createButton();
    Checkbox createCheckbox();
}
class LightFactory implements UiFactory {
    public Button createButton()     { return new LightButton(); }
    public Checkbox createCheckbox() { return new LightCheckbox(); }
}
class DarkFactory implements UiFactory {
    public Button createButton()     { return new DarkButton(); }
    public Checkbox createCheckbox() { return new DarkCheckbox(); }
}

// client — consistent family, chosen once
class Application {
    private final Button button;
    private final Checkbox checkbox;
    Application(UiFactory factory) {
        this.button = factory.createButton();
        this.checkbox = factory.createCheckbox();
    }
    void paint() { button.render(); checkbox.render(); }
}

// usage
new Application(new DarkFactory()).paint();
```

**2. Furniture Kit (Chair + Sofa + CoffeeTable)**
```java
interface Chair       { String style(); }
interface Sofa        { String style(); }
interface CoffeeTable { String style(); }

class ModernChair       implements Chair       { public String style() { return "modern chair"; } }
class ModernSofa        implements Sofa        { public String style() { return "modern sofa"; } }
class ModernCoffeeTable implements CoffeeTable { public String style() { return "modern table"; } }
class VictorianChair       implements Chair       { public String style() { return "victorian chair"; } }
class VictorianSofa        implements Sofa        { public String style() { return "victorian sofa"; } }
class VictorianCoffeeTable implements CoffeeTable { public String style() { return "victorian table"; } }

interface FurnitureFactory {
    Chair createChair(); Sofa createSofa(); CoffeeTable createCoffeeTable();
}
class ModernFactory implements FurnitureFactory {
    public Chair createChair()             { return new ModernChair(); }
    public Sofa createSofa()               { return new ModernSofa(); }
    public CoffeeTable createCoffeeTable() { return new ModernCoffeeTable(); }
}
class VictorianFactory implements FurnitureFactory {
    public Chair createChair()             { return new VictorianChair(); }
    public Sofa createSofa()               { return new VictorianSofa(); }
    public CoffeeTable createCoffeeTable() { return new VictorianCoffeeTable(); }
}
```

**3. Factory-of-Factories (registry)**
```java
import java.util.*;
import java.util.function.Supplier;

class UiFactoryRegistry {
    private static final Map<String, Supplier<UiFactory>> FAMILIES = new HashMap<>();
    static {
        FAMILIES.put("LIGHT", LightFactory::new);
        FAMILIES.put("DARK",  DarkFactory::new);
    }
    static UiFactory of(String theme) {
        Supplier<UiFactory> f = FAMILIES.get(theme.toUpperCase());
        if (f == null) throw new IllegalArgumentException("Unknown theme: " + theme);
        return f.get();
    }
}
```

**4. Repository Suite (SQL vs NoSQL)**
```java
interface UserRepo    { String find(long id); }
interface OrderRepo   { String list(); }
interface DataFactory { UserRepo users(); OrderRepo orders(); }

class SqlUserRepo  implements UserRepo  { public String find(long id) { return "SQL user " + id; } }
class SqlOrderRepo implements OrderRepo { public String list() { return "SQL orders"; } }
class SqlFactory   implements DataFactory {
    public UserRepo users()  { return new SqlUserRepo(); }
    public OrderRepo orders() { return new SqlOrderRepo(); }
}

class NoSqlUserRepo  implements UserRepo  { public String find(long id) { return "NoSQL user " + id; } }
class NoSqlOrderRepo implements OrderRepo { public String list() { return "NoSQL orders"; } }
class NoSqlFactory   implements DataFactory {
    public UserRepo users()  { return new NoSqlUserRepo(); }
    public OrderRepo orders() { return new NoSqlOrderRepo(); }
}
```

**Complexity:** creation O(1) per product · Space O(1) per created object

**Trade-off to state in interviews:** adding a **family** (new theme/backend) is a single new factory; adding a **product** (e.g. `createSlider()`) forces edits to the abstract factory and **every** concrete factory.