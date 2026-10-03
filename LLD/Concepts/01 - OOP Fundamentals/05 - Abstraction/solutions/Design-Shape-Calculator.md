# Design Shape Calculator (Abstraction)

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Topic:** Abstraction
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-shape-calculator)

### Problem

Design a shape calculator that computes the area of different shapes. The calculator must work with
any shape through a common **abstraction** — it should not contain a `switch` over concrete shape
types. Adding a new shape must not require changing the calculator.

### Approach

- Define an abstract **Shape** with `area()` and `name()`.
- Concrete shapes (`Circle`, `Rectangle`, `Triangle`) implement it.
- The calculator only sees `Shape`.

### Java Solution

```java
import java.util.List;

// Abstraction — the "what"
public abstract class Shape {
    public abstract double area();
    public abstract String name();
}

class Circle extends Shape {                 // "how"
    private final double radius;
    Circle(double radius) { this.radius = radius; }
    public double area()  { return Math.PI * radius * radius; }
    public String name()  { return "Circle"; }
}

class Rectangle extends Shape {
    private final double width, height;
    Rectangle(double width, double height) { this.width = width; this.height = height; }
    public double area()  { return width * height; }
    public String name()  { return "Rectangle"; }
}

class Triangle extends Shape {
    private final double base, height;
    Triangle(double base, double height) { this.base = base; this.height = height; }
    public double area()  { return 0.5 * base * height; }
    public String name()  { return "Triangle"; }
}

// The calculator depends only on the abstraction
public class ShapeCalculator {
    public double totalArea(List<Shape> shapes) {
        double total = 0;
        for (Shape s : shapes) total += s.area();      // polymorphic
        return total;
    }
}
```

**Usage**
```java
ShapeCalculator calc = new ShapeCalculator();
double total = calc.totalArea(List.of(new Circle(1), new Rectangle(2, 3)));
System.out.printf("%.2f%n", total);     // 9.14
```

### Design points
- **Abstraction hides detail** — the calculator has no idea how area is computed.
- **No `switch`** — adding `Square` needs only a new class.
- **Polymorphism** — `s.area()` dispatches to the right implementation.

**Complexity:** O(shapes) per calculation · Space O(1)

---
#oop #abstraction #lld #practice