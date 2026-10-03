# Bridge — Implementations & Examples

**Pattern:** Bridge (Structural) · **Skill:** decoupling two independent hierarchies

### Approach

- Identify the **two orthogonal dimensions** (e.g. shape × renderer).
- Make the **low-level** dimension an interface (`Implementor`).
- Have the **high-level** abstraction hold an `Implementor` field and delegate to it.

### Java Solutions

**1. Shape × Renderer**
```java
interface Renderer { String render(String shape); }             // Implementor
class VectorRenderer implements Renderer {                     // ConcreteImplementor
    public String render(String shape) { return "Draw " + shape + " as vector lines"; }
}
class RasterRenderer implements Renderer {
    public String render(String shape) { return "Draw " + shape + " as pixels"; }
}

abstract class Shape {                                         // Abstraction
    protected final Renderer renderer;                         // ← the bridge
    protected Shape(Renderer renderer) { this.renderer = renderer; }
    abstract String draw();
}
class Circle extends Shape {                                   // RefinedAbstraction
    Circle(Renderer r) { super(r); }
    String draw() { return renderer.render("Circle"); }
}
class Square extends Shape {
    Square(Renderer r) { super(r); }
    String draw() { return renderer.render("Square"); }
}

// usage — mix any shape with any renderer
new Circle(new VectorRenderer()).draw();   // Draw Circle as vector lines
new Square(new RasterRenderer()).draw();   // Draw Square as pixels
```

**2. Remote × Device**
```java
interface Device { void turnOn(); void setVolume(int v); }     // Implementor
class Tv implements Device {
    public void turnOn() { System.out.println("TV on"); }
    public void setVolume(int v) { System.out.println("TV volume " + v); }
}
class Radio implements Device {
    public void turnOn() { System.out.println("Radio on"); }
    public void setVolume(int v) { System.out.println("Radio volume " + v); }
}

abstract class Remote {                                        // Abstraction
    protected final Device device;
    protected Remote(Device d) { this.device = d; }
    abstract void on();
}
class BasicRemote extends Remote {                             // RefinedAbstraction
    BasicRemote(Device d) { super(d); }
    void on() { device.turnOn(); }
}
class AdvancedRemote extends Remote {
    AdvancedRemote(Device d) { super(d); }
    void on() { device.turnOn(); device.setVolume(20); }
}
```

**3. Message × Channel**
```java
interface Channel { void deliver(String text); }               // Implementor
class EmailChannel implements Channel { public void deliver(String t) { System.out.println("Email: " + t); } }
class SmsChannel   implements Channel { public void deliver(String t) { System.out.println("SMS: " + t); } }

abstract class Message {
    protected final Channel channel;
    protected Message(Channel c) { channel = c; }
    abstract void send();
}
class TextMessage extends Message {
    private final String text;
    TextMessage(Channel c, String text) { super(c); this.text = text; }
    void send() { channel.deliver(text); }
}
class AlertMessage extends Message {
    AlertMessage(Channel c) { super(c); }
    void send() { channel.deliver("⚠ ALERT"); }
}
```

**Complexity:** O(1) delegation per call · Space O(1) per bridged object

**Why it matters:** with 3 shapes and 3 renderers, inheritance needs **9** classes; Bridge needs **3 + 3 = 6**. Add a 4th shape → **1** new class instead of **3**.