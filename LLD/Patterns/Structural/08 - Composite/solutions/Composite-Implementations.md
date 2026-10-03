# Composite — Implementations & Examples

**Pattern:** Composite (Structural) · **Skill:** treating leaves and trees uniformly

### Approach

- Define a **Component** interface with the operations the client cares about.
- **Leaf** implements it directly; **Composite** implements it and **delegates/aggregates** over a list of children.
- Recursion happens automatically when a Composite calls the same method on each child.

### Java Solutions

**1. File System (File + Folder)**
```java
import java.util.*;

abstract class Node {
    private final String name;
    protected Node(String name) { this.name = name; }
    public String getName() { return name; }
    public abstract long size();
}

class File extends Node {
    private final long bytes;
    File(String name, long bytes) { super(name); this.bytes = bytes; }
    public long size() { return bytes; }
}

class Folder extends Node {
    private final List<Node> children = new ArrayList<>();
    Folder(String name) { super(name); }
    public Folder add(Node n) { children.add(n); return this; }     // safe: only Folder can add
    public long size() {
        long total = 0;
        for (Node c : children) total += c.size();                 // recursion
        return total;
    }
}
// usage
Folder root = new Folder("root")
        .add(new File("a.txt", 100))
        .add(new Folder("docs").add(new File("b.md", 250)));
System.out.println(root.size());   // 350
```

**2. Menu with Sub-menus**
```java
interface MenuComponent { String name(); double price(); }

class MenuItem implements MenuComponent {
    private final String name; private final double price;
    MenuItem(String n, double p) { name = n; price = p; }
    public String name() { return name; }
    public double price() { return price; }
}
class Menu implements MenuComponent {
    private final String name; private final List<MenuComponent> items = new ArrayList<>();
    Menu(String n) { name = n; }
    public Menu add(MenuComponent c) { items.add(c); return this; }
    public String name() { return name; }
    public double price() {
        double sum = 0;
        for (MenuComponent c : items) sum += c.price();
        return sum;
    }
}
```

**3. Organization Compensation**
```java
abstract class Employee {
    private final String name; protected final double salary;
    protected Employee(String name, double salary) { this.name = name; this.salary = salary; }
    public abstract double totalCompensation();
}
class Developer extends Employee {
    Developer(String n, double s) { super(n, s); }
    public double totalCompensation() { return salary; }
}
class Manager extends Employee {
    private final List<Employee> reports = new ArrayList<>();
    Manager(String n, double s) { super(n, s); }
    public Manager add(Employee e) { reports.add(e); return this; }
    public double totalCompensation() {
        double total = salary;
        for (Employee e : reports) total += e.totalCompensation();  // recursion
        return total;
    }
}
```

**4. Transparent Variant (child ops on Component)**
```java
abstract class Component {
    public void add(Component c)    { throw new UnsupportedOperationException(); }
    public void remove(Component c) { throw new UnsupportedOperationException(); }
    public abstract String render();
}
class Leaf extends Component { public String render() { return "leaf"; } }
class Branch extends Component {
    private final List<Component> kids = new ArrayList<>();
    @Override public void add(Component c) { kids.add(c); }
    public String render() {
        StringBuilder sb = new StringBuilder("branch(");
        for (Component c : kids) sb.append(c.render()).append(" ");
        return sb.append(")").toString();
    }
}
```

**Complexity:** aggregate operation O(n) over the whole tree · Space O(depth) stack for recursion

**Design note:** throw `UnsupportedOperationException` only in the **transparent** variant; the **safe** variant avoids it entirely.