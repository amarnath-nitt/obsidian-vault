# Visitor — Implementations & Examples

**Pattern:** Visitor (Behavioural) · **Skill:** adding operations to a stable type hierarchy

### Approach

- Give every element an `accept(Visitor)` that calls the matching `visitX(this)`.
- Declare a `visitX()` per element type on the **Visitor**.
- Implement each operation as a **ConcreteVisitor**; elements never change for a new operation.

### Java Solutions

**1. Shape Visitor (area + export)**
```java
interface Visitor {
    void visit(Circle c);
    void visit(Rectangle r);
}

interface Shape { void accept(Visitor v); }

class Circle implements Shape {
    final double r; Circle(double r) { this.r = r; }
    public void accept(Visitor v) { v.visit(this); }
}
class Rectangle implements Shape {
    final double w, h; Rectangle(double w, double h) { this.w = w; this.h = h; }
    public void accept(Visitor v) { v.visit(this); }
}

class AreaVisitor implements Visitor {
    double total = 0;
    public void visit(Circle c)    { total += Math.PI * c.r * c.r; }
    public void visit(Rectangle r) { total += r.w * r.h; }
}
class ExportVisitor implements Visitor {
    public void visit(Circle c)    { System.out.println("<circle r=\"" + c.r + "\"/>"); }
    public void visit(Rectangle r) { System.out.println("<rect w=\"" + r.w + "\" h=\"" + r.h + "\"/>"); }
}

// usage — same elements, different operations
List<Shape> shapes = List.of(new Circle(1), new Rectangle(2, 3));
AreaVisitor area = new AreaVisitor();
shapes.forEach(s -> s.accept(area));
System.out.println("Area = " + area.total);
```

**2. Expression AST (evaluate + print)**
```java
interface ExprVisitor<R> {
    R visitNumber(NumberExpr n);
    R visitAdd(AddExpr a);
}
interface Expr { <R> R accept(ExprVisitor<R> v); }

class NumberExpr implements Expr {
    final int value; NumberExpr(int v) { value = v; }
    public <R> R accept(ExprVisitor<R> v) { return v.visitNumber(this); }
}
class AddExpr implements Expr {
    final Expr left, right; AddExpr(Expr l, Expr r) { left = l; right = r; }
    public <R> R accept(ExprVisitor<R> v) { return v.visitAdd(this); }
}

class Evaluator implements ExprVisitor<Integer> {
    public Integer visitNumber(NumberExpr n) { return n.value; }
    public Integer visitAdd(AddExpr a) {
        return a.left.accept(this) + a.right.accept(this);   // recursion
    }
}
class Printer implements ExprVisitor<String> {
    public String visitNumber(NumberExpr n) { return String.valueOf(n.value); }
    public String visitAdd(AddExpr a) {
        return "(" + a.left.accept(this) + " + " + a.right.accept(this) + ")";
    }
}
// usage
Expr expr = new AddExpr(new NumberExpr(3), new AddExpr(new NumberExpr(4), new NumberExpr(5)));
System.out.println(expr.accept(new Evaluator()));   // 12
System.out.println(expr.accept(new Printer()));     // (3 + (4 + 5))
```

**3. Composite + Visitor (file tree size)**
```java
interface NodeVisitor<R> {
    R visit(FileNode f);
    R visit(FolderNode d);
}
interface FsNode { <R> R accept(NodeVisitor<R> v); }

class FileNode implements FsNode {
    final long bytes; FileNode(long b) { bytes = b; }
    public <R> R accept(NodeVisitor<R> v) { return v.visit(this); }
}
class FolderNode implements FsNode {
    final List<FsNode> children = new java.util.ArrayList<>();
    FolderNode add(FsNode n) { children.add(n); return this; }
    public <R> R accept(NodeVisitor<R> v) { return v.visit(this); }
}

class TotalSizeVisitor implements NodeVisitor<Long> {
    public Long visit(FileNode f)   { return f.bytes; }
    public Long visit(FolderNode d) {                        // recurse into children
        long total = 0;
        for (FsNode c : d.children) total += c.accept(this);
        return total;
    }
}
```

**4. Cart Item Pricing (per-type operation)**
```java
interface CartVisitor {
    double visit(Book b);
    double visit(Electronics e);
}
interface CartItem { double accept(CartVisitor v); }

class Book { final double price; final double weightKg; Book(double p, double w) { price = p; weightKg = w; } }
class Electronics { final double price; Electronics(double p) { price = p; } }

class PriceVisitor implements CartVisitor {
    public double visit(Book b)        { return b.price * 0.9; }   // books discounted 10%
    public double visit(Electronics e) { return e.price * 1.18; }  // electronics + tax
}
```

**Complexity:** O(n) over the structure per operation · Space O(depth) recursion

**Design note:** adding a new **operation** (e.g. a `DiscountVisitor`) touches **no** element class; adding a new **element type** (e.g. `Triangle`) would force a new `visit` method on **every** visitor — the key trade-off.