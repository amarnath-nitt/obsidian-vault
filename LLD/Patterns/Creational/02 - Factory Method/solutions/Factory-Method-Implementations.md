# Factory Method — Implementations & Examples

**Pattern:** Factory Method (Creational) · **Skill:** decoupling object creation from usage

### Approach

- **Simple Factory** — one class with a type→product `switch`; simplest, not OCP.
- **Factory Method (GoF)** — a `Creator` abstraction with subclasses that decide the product.
- **Registered Factory** — a `Map<Type, Supplier<Product>>` so new products need no edits (OCP).

### Java Solutions

**1. Simple Factory — Shapes**
```java
interface Shape { double area(); }

class Circle implements Shape {
    private final double r;
    Circle(double r) { this.r = r; }
    public double area() { return Math.PI * r * r; }
}
class Rectangle implements Shape {
    private final double w, h;
    Rectangle(double w, double h) { this.w = w; this.h = h; }
    public double area() { return w * h; }
}

class ShapeFactory {
    static Shape create(String type) {
        return switch (type.toLowerCase()) {
            case "circle"    -> new Circle(1);
            case "rectangle" -> new Rectangle(2, 3);
            default -> throw new IllegalArgumentException("Unknown shape: " + type);
        };
    }
}
```

**2. Notification Factory (Product + Factory)**
```java
interface Notification { void send(String to, String msg); }
class EmailNotification implements Notification {
    public void send(String to, String m) { System.out.println("Email→" + to + ": " + m); }
}
class SmsNotification implements Notification {
    public void send(String to, String m) { System.out.println("SMS→" + to + ": " + m); }
}
class PushNotification implements Notification {
    public void send(String to, String m) { System.out.println("Push→" + to + ": " + m); }
}

enum Channel { EMAIL, SMS, PUSH }

class NotificationFactory {
    static Notification create(Channel c) {
        return switch (c) {
            case EMAIL -> new EmailNotification();
            case SMS   -> new SmsNotification();
            case PUSH  -> new PushNotification();
        };
    }
}
```

**3. GoF Factory Method (Creator hierarchy)**
```java
interface Button { String label(); }
class WindowsButton implements Button { public String label() { return "Windows Button"; } }
class HtmlButton    implements Button { public String label() { return "HTML Button"; } }

interface Dialog {
    Button createButton();                       // ← the factory method
    default void show() { System.out.println("Opening " + createButton().label()); }
}
class WindowsDialog implements Dialog { public Button createButton() { return new WindowsButton(); } }
class WebDialog     implements Dialog { public Button createButton() { return new HtmlButton(); } }
```

**4. Registered Factory (OCP)**
```java
import java.util.*;
import java.util.function.Supplier;

interface Payment { void pay(double amount); }
class CreditCardPayment implements Payment { public void pay(double a) { System.out.println("Card " + a); } }
class UpiPayment        implements Payment { public void pay(double a) { System.out.println("UPI " + a); } }

class PaymentFactory {
    private static final Map<String, Supplier<Payment>> REGISTRY = new HashMap<>();
    static {
        register("CARD", CreditCardPayment::new);
        register("UPI", UpiPayment::new);
    }
    static void register(String key, Supplier<Payment> ctor) { REGISTRY.put(key, ctor); }
    static Payment create(String key) {
        Supplier<Payment> ctor = REGISTRY.get(key.toUpperCase());
        if (ctor == null) throw new IllegalArgumentException("Unknown payment: " + key);
        return ctor.get();
    }
}
```

**Complexity:** creation O(1) (switch / map lookup) · Space O(1) per created object

**Note:** the factory returns the **interface**; callers never reference a concrete type. Adding a payment method = one `register(...)` line, no edits elsewhere.