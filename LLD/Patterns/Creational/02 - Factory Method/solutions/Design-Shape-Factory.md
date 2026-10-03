# Design Shape Factory

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Pattern:** Factory Method
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-shape-factory)

### Problem (contract)

A drawing tool can already measure and describe any `Shape`. It must **not** scatter
`new Circle(...)`, `new Rectangle(...)`, `new Triangle(...)` through its workflow — Factory Method
gives that construction decision a clear home.

Complete the creator family:

- `ShapeCreator` — abstract creator; declares `kind()` and the factory method `createShape()`.
- `build()` — creates a **fresh** shape via `createShape()` and increments this creator's count.
- `measure()` — builds a shape and returns its area.
- `describeShape()` — builds a shape and returns `"<Name> with area: <area>"` (area to **2 decimals**).
- `builtCount()` — how many shapes this creator has built.
- `CircleCreator` (radius 5), `RectangleCreator` (4×6), `TriangleCreator` (base 3, height 8) supply the
  concrete factory methods and lower-case names `"circle"`, `"rectangle"`, `"triangle"`.
- The supplied `ShapeWorks` context must work unmodified.

### Approach

- One abstract creator holding the **shared, counted** construction path (`build`).
- `measure` / `describeShape` both call `build`, so **every request makes a new shape**.
- Concrete creators override only `createShape()` — no shared logic duplicated.

### Java Solution

```java
// Products (provided)
interface Shape { double area(); }
class Circle    implements Shape { private final double r;   Circle(double r)      { this.r = r; }
    public double area() { return Math.PI * r * r; } }
class Rectangle implements Shape { private final double w, h; Rectangle(double w, double h) { this.w = w; this.h = h; }
    public double area() { return w * h; } }
class Triangle  implements Shape { private final double b, h; Triangle(double b, double h)  { this.b = b; this.h = h; }
    public double area() { return 0.5 * b * h; } }

// Creator family (this is the part you implement)
abstract class ShapeCreator {
    private int count = 0;

    abstract String kind();
    protected abstract Shape createShape();          // ← the factory method

    Shape build() {                                  // single counted construction path
        count++;
        return createShape();
    }
    double measure() { return build().area(); }
    String describeShape() {
        Shape s = build();
        return String.format("%s with area: %.2f", s.getClass().getSimpleName(), s.area());
    }
    int builtCount() { return count; }
}

class CircleCreator    extends ShapeCreator { String kind() { return "circle"; }
    protected Shape createShape() { return new Circle(5); } }
class RectangleCreator extends ShapeCreator { String kind() { return "rectangle"; }
    protected Shape createShape() { return new Rectangle(4, 6); } }
class TriangleCreator  extends ShapeCreator { String kind() { return "triangle"; }
    protected Shape createShape() { return new Triangle(3, 8); } }
```

**Supplied context (do not modify)**
```java
class ShapeWorks {
    private final java.util.Map<String, ShapeCreator> creators = new java.util.LinkedHashMap<>();
    private ShapeCreator active;
    ShapeWorks() {
        creators.put("circle",    new CircleCreator());
        creators.put("rectangle", new RectangleCreator());
        creators.put("triangle",  new TriangleCreator());
        active = creators.get("circle");
    }
    String currentCreator() { return active.kind(); }
    boolean use(String name) {
        ShapeCreator c = creators.get(name);
        if (c == null) return false;
        active = c; return true;
    }
    String describe() { return active.describeShape(); }
    double area()     { return active.measure(); }
}
```

### Why it works
- **Fresh shape per request** — `describe()`/`area()` each call `build()` → the count always grows.
- **Count owned by `build`** — no subclass can bypass the single counted path.
- **Unknown creator is a no-op** — `ShapeWorks.use` returns `false` and keeps the current creator.

**Complexity:** O(1) per shape · Space O(1)

---
#factory-method #lld #practice