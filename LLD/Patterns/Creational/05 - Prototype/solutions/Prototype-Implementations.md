# Prototype — Implementations & Examples

**Pattern:** Prototype (Creational) · **Skill:** cloning objects (shallow vs deep)

### Approach

- Prefer a **copy constructor** in idiomatic Java; use `Cloneable` + `super.clone()` when you need the built-in mechanism.
- **Shallow** copies primitives safely but shares references.
- **Deep** copies clone nested mutable state (lists, maps, objects).

### Java Solutions

**1. Shallow copy — all primitives (safe)**
```java
final class Point {
    final int x, y;
    Point(int x, int y) { this.x = x; this.y = y; }
    Point(Point other) { this(other.x, other.y); }   // copy constructor
    @Override public String toString() { return "(" + x + "," + y + ")"; }
}
```

**2. Deep copy — `Order` with a mutable list**
```java
import java.util.*;

final class Item { final String name; Item(String n) { this.name = n; } }

final class Order {
    private final List<Item> items;
    Order(List<Item> items) { this.items = new ArrayList<>(items); }   // defensive copy in
    Order(Order other) { this.items = new ArrayList<>(other.items); }  // deep copy
    List<Item> items() { return List.copyOf(items); }
    void add(Item i) { items.add(i); }
    Order copy() { return new Order(this); }
}
```

**3. `Cloneable` + `clone()` (shallow then fix)**
```java
final class Shape implements Cloneable {
    String type;
    List<String> tags = new ArrayList<>();
    Shape(String type) { this.type = type; }

    @Override
    public Shape clone() {
        try {
            Shape copy = (Shape) super.clone();          // shallow
            copy.tags = new ArrayList<>(this.tags);      // fix the mutable field (deep)
            return copy;
        } catch (CloneNotSupportedException e) {
            throw new AssertionError(e);
        }
    }
}
```

**4. Prototype Registry**
```java
import java.util.*;

interface Prototype { Prototype copy(); }

class Document implements Prototype {
    String title, body;
    Document(String t, String b) { title = t; body = b; }
    private Document(Document o) { this.title = o.title; this.body = o.body; }
    public Document copy() { return new Document(this); }
    @Override public String toString() { return "[" + title + "] " + body; }
}

class PrototypeRegistry {
    private final Map<String, Prototype> registry = new HashMap<>();
    void register(String key, Prototype p) { registry.put(key, p); }
    Prototype get(String key) {
        Prototype p = registry.get(key);
        if (p == null) throw new IllegalArgumentException("No prototype: " + key);
        return p.copy();
    }
}
```

**5. Deep clone via serialisation (simple but slow)**
```java
@SuppressWarnings("unchecked")
static <T extends java.io.Serializable> T deepClone(T obj) {
    try (var bos = new java.io.ByteArrayOutputStream();
         var oos = new java.io.ObjectOutputStream(bos)) {
        oos.writeObject(obj);
        try (var ois = new java.io.ObjectInputStream(new java.io.ByteArrayInputStream(bos.toByteArray()))) {
            return (T) ois.readObject();
        }
    } catch (Exception e) {
        throw new RuntimeException(e);
    }
}
```

**Complexity:** shallow copy O(1) · deep copy O(size of object graph) · Space O(graph)

**Pitfall to mention:** `Object.clone()` bypasses constructors, so any validation in a constructor is skipped — prefer copy constructors for objects with invariants.