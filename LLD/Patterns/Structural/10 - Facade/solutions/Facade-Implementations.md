# Facade — Implementations & Examples

**Pattern:** Facade (Structural) · **Skill:** hiding subsystem complexity behind one API

### Approach

- Identify a **multi-step workflow** that callers keep repeating.
- Keep each subsystem class as-is.
- Add a **Facade** whose methods orchestrate several subsystem calls in order.

### Java Solutions

**1. Home Theater Facade**
```java
class Amplifier    { void on() { System.out.println("Amp on"); }  void off() { System.out.println("Amp off"); }  void setVolume(int v) { System.out.println("Volume " + v); } }
class DvdPlayer    { void on() { System.out.println("DVD on"); }  void off() { System.out.println("DVD off"); }  void play(String m) { System.out.println("Playing " + m); } void stop() { System.out.println("DVD stop"); } }
class Projector    { void on() { System.out.println("Projector on"); } void off() { System.out.println("Projector off"); } }
class Lights       { void dim(int v) { System.out.println("Lights " + v + "%"); } }

class HomeTheaterFacade {
    private final Amplifier amp; private final DvdPlayer dvd;
    private final Projector projector; private final Lights lights;
    HomeTheaterFacade(Amplifier a, DvdPlayer d, Projector p, Lights l) {
        amp = a; dvd = d; projector = p; lights = l;
    }
    void watchMovie(String movie) {
        lights.dim(10);
        projector.on();
        amp.on(); amp.setVolume(5);
        dvd.on(); dvd.play(movie);
    }
    void endMovie() {
        dvd.stop(); dvd.off();
        amp.off(); projector.off();
        lights.dim(100);
    }
}
```

**2. Order Checkout Facade**
```java
class InventoryService { boolean reserve(String sku) { System.out.println("Reserved " + sku); return true; } }
class PaymentService   { boolean charge(double amount) { System.out.println("Charged " + amount); return true; } }
class ShippingService  { void schedule(String addr) { System.out.println("Ship to " + addr); } }
class NotificationService { void notifyUser(String msg) { System.out.println("Notify: " + msg); } }

record CheckoutResult(boolean success, String message) {}

class CheckoutFacade {
    private final InventoryService inventory = new InventoryService();
    private final PaymentService payment = new PaymentService();
    private final ShippingService shipping = new ShippingService();
    private final NotificationService notify = new NotificationService();

    CheckoutResult checkout(String sku, double amount, String address) {
        if (!inventory.reserve(sku))         return new CheckoutResult(false, "Out of stock");
        if (!payment.charge(amount))          return new CheckoutResult(false, "Payment failed");
        shipping.schedule(address);
        notify.notifyUser("Order confirmed for " + sku);
        return new CheckoutResult(true, "Order placed");
    }
}
// usage — one call replaces five subsystem interactions
new CheckoutFacade().checkout("SKU-1", 49.99, "221B Baker Street");
```

**3. Computer Boot Facade**
```java
class Cpu    { void freeze() { System.out.println("CPU freeze"); }  void jump(long p) { System.out.println("CPU jump " + p); } void execute() { System.out.println("CPU execute"); } }
class Memory { void load(long p, String d) { System.out.println("Mem load " + d); } }
class HardDrive { String read(long l, int s) { return "boot-sector"; } }

class ComputerFacade {
    private final Cpu cpu = new Cpu();
    private final Memory memory = new Memory();
    private final HardDrive hd = new HardDrive();
    private static final long BOOT_ADDRESS = 0L;
    private static final int BOOT_SECTOR = 512;

    void start() {
        cpu.freeze();
        memory.load(BOOT_ADDRESS, hd.read(BOOT_ADDRESS, BOOT_SECTOR));
        cpu.jump(BOOT_ADDRESS);
        cpu.execute();
    }
}
```

**Complexity:** O(k) for a workflow of k subsystem calls · Space O(1) extra

**Design note:** the facade reduces the **number of collaborators** a client must know, which shrinks the client's coupling and simplifies testing (the subsystem can be mocked behind the facade).