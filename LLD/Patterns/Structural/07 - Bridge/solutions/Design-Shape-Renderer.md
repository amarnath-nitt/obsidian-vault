# Design a Shape Renderer

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Bridge
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-shape-renderer)

### Problem

A drawing tool supports several **shapes** (circle, square) that can each be drawn by several
**renderers** (vector, raster). Without care this becomes a cartesian explosion of classes
(`VectorCircle`, `RasterCircle`, `VectorSquare`, …). Design it so shapes and renderers **vary
independently**.

### Approach — Bridge

- **Abstraction** = `Shape` (holds a `Renderer`).
- **RefinedAbstractions** = `Circle`, `Square`.
- **Implementor** = `Renderer` (vector / raster).
- Two hierarchies joined by composition → `N + M` classes instead of `N × M`.

### Java Solution

```java
// Implementor — the low-level "how to draw" dimension
interface Renderer {
    String render(String shape);
}
class VectorRenderer implements Renderer {
    public String render(String shape) { return "Draw " + shape + " as vector lines"; }
}
class RasterRenderer implements Renderer {
    public String render(String shape) { return "Draw " + shape + " as pixels"; }
}

// Abstraction — the high-level "what to draw" dimension
abstract class Shape {
    protected final Renderer renderer;          // ← the bridge
    protected Shape(Renderer renderer) { this.renderer = renderer; }
    abstract String draw();
}

class Circle extends Shape {
    Circle(Renderer r) { super(r); }
    String draw() { return renderer.render("Circle"); }
}
class Square extends Shape {
    Square(Renderer r) { super(r); }
    String draw() { return renderer.render("Square"); }
}
```

**Usage — mix any shape with any renderer**
```java
Shape vectorCircle = new Circle(new VectorRenderer());
Shape rasterSquare = new Square(new RasterRenderer());

System.out.println(vectorCircle.draw());   // Draw Circle as vector lines
System.out.println(rasterSquare.draw());   // Draw Square as pixels
```

**Class-count comparison**

| Approach | Circle/Square × Vector/Raster |
|----------|-------------------------------|
| Inheritance explosion | 4 classes (`VectorCircle`, `RasterCircle`, …) |
| **Bridge** | 2 + 2 = **4** now, but **+1 shape = 1 class** instead of 2, **+1 renderer = 1 class** instead of 2 |

### Design points
- **Two dimensions, two hierarchies** — shapes and renderers change for different reasons.
- **Composition holds the variation** — `Shape` *has a* `Renderer`, it does not extend one.
- **Extensible both ways** — add `Triangle` or `SVGRenderer` without touching the other side.

**Complexity:** O(1) per draw · Space O(1)

---
#bridge #lld #practice