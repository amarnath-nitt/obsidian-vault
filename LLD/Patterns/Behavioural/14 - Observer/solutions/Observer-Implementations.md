# Observer — Implementations & Examples

**Pattern:** Observer (Behavioural) · **Skill:** broadcast state changes to dynamic subscribers

### Approach

- Define an **Observer** interface with `update(...)`.
- Keep a list of observers in the **Subject** with `attach` / `detach` / `notify`.
- Iterate over a **copy** of the list during notification.

### Java Solutions

**1. Stock Price Notifier**
```java
import java.util.*;
import java.util.concurrent.CopyOnWriteArrayList;

interface Observer { void update(String stock, double price); }

class StockMarket {                                    // Subject
    private final List<Observer> observers = new CopyOnWriteArrayList<>();
    public void subscribe(Observer o)   { observers.add(o); }
    public void unsubscribe(Observer o) { observers.remove(o); }
    public void setPrice(String stock, double price) {
        System.out.println("Price update: " + stock + " = " + price);
        for (Observer o : observers) o.update(stock, price);   // safe iteration
    }
}

class Investor implements Observer {
    private final String name;
    Investor(String name) { this.name = name; }
    public void update(String stock, double price) {
        System.out.println("  " + name + " alerted: " + stock + " -> " + price);
    }
}
// usage
StockMarket market = new StockMarket();
market.subscribe(new Investor("Alice"));
market.subscribe(new Investor("Bob"));
market.setPrice("ACME", 120.5);
```

**2. Order Event Bus (async dispatch)**
```java
import java.util.*;
import java.util.concurrent.*;

interface OrderListener { void onOrderPlaced(String orderId); }

class OrderService {                                   // Subject
    private final List<OrderListener> listeners = new CopyOnWriteArrayList<>();
    private final ExecutorService pool = Executors.newFixedThreadPool(4);

    public void register(OrderListener l) { listeners.add(l); }
    public void placeOrder(String orderId) {
        System.out.println("Order placed: " + orderId);
        for (OrderListener l : listeners) {
            pool.submit(() -> l.onOrderPlaced(orderId));   // async, isolated failures
        }
    }
    public void shutdown() { pool.shutdown(); }
}

class EmailNotifier implements OrderListener {
    public void onOrderPlaced(String id) { System.out.println("  Email sent for " + id); }
}
class InventoryUpdater implements OrderListener {
    public void onOrderPlaced(String id) { System.out.println("  Inventory decremented for " + id); }
}
```

**3. Pull Model**
```java
interface PullObserver { void update(); }              // no payload — observer pulls

class WeatherData {                                    // Subject
    private final List<PullObserver> observers = new ArrayList<>();
    private double temperature;
    void register(PullObserver o) { observers.add(o); }
    double getTemperature() { return temperature; }
    void setTemperature(double t) {
        this.temperature = t;
        observers.forEach(PullObserver::update);
    }
}
class Display implements PullObserver {
    private final WeatherData data;
    Display(WeatherData data) { this.data = data; }
    public void update() { System.out.println("  Display: " + data.getTemperature() + "°C"); }
}
```

**4. Topic-based Pub-Sub**
```java
import java.util.*;
import java.util.concurrent.*;

class EventBus {                                       // topic → subscribers
    private final Map<String, List<java.util.function.Consumer<String>>> topics = new ConcurrentHashMap<>();
    void subscribe(String topic, java.util.function.Consumer<String> handler) {
        topics.computeIfAbsent(topic, k -> new CopyOnWriteArrayList<>()).add(handler);
    }
    void publish(String topic, String payload) {
        topics.getOrDefault(topic, List.of()).forEach(h -> h.accept(payload));
    }
}
// usage
EventBus bus = new EventBus();
bus.subscribe("order.created", p -> System.out.println("Email: " + p));
bus.subscribe("order.created", p -> System.out.println("Analytics: " + p));
bus.publish("order.created", "ORD-1");
```

**Complexity:** notify O(n) in the number of observers · subscribe/unsubscribe O(1)

**Note:** use `CopyOnWriteArrayList` (or iterate over a snapshot) so an observer may safely add/remove itself during a notification without a `ConcurrentModificationException`.