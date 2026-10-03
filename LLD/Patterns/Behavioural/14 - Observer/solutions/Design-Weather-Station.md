# Design a Weather Station

**Source:** AlgoMaster · Low-Level Design Practice · **medium (premium)** · **Pattern:** Observer
🔗 [AlgoMaster index](https://algomaster.io/practice/low-level-design)

### Problem

A weather station measures temperature, humidity and pressure. Several displays must update whenever
a reading changes. Support both the **push** model (the station sends the data) and the **pull** model
(displays query the station on notification).

### Approach — Observer

- **Subject** = `WeatherData` (`register`, `remove`, `measurementsChanged`).
- Observers implement a common `update()` (pull) or `update(data)` (push) callback.

### Java Solution

```java
import java.util.*;
import java.util.concurrent.CopyOnWriteArrayList;

// ---------- Pull model ----------
interface PullObserver {
    void update();                       // observer asks the subject for data
}

class WeatherData {
    private final List<PullObserver> observers = new CopyOnWriteArrayList<>();
    private double temperature, humidity, pressure;

    public void register(PullObserver o) { observers.add(o); }
    public void remove(PullObserver o)   { observers.remove(o); }

    public void setMeasurements(double t, double h, double p) {
        this.temperature = t; this.humidity = h; this.pressure = p;
        measurementsChanged();
    }
    private void measurementsChanged() {
        for (PullObserver o : observers) o.update();     // signal only
    }

    public double getTemperature() { return temperature; }
    public double getHumidity()    { return humidity; }
    public double getPressure()    { return pressure; }
}

class ConditionsDisplay implements PullObserver {
    private final WeatherData data;
    ConditionsDisplay(WeatherData data) { this.data = data; this.data.register(this); }
    @Override public void update() {
        System.out.printf("Conditions: %.1f°C, %.1f%% humidity%n", data.getTemperature(), data.getHumidity());
    }
}

// ---------- Push model ----------
record WeatherReading(double temperature, double humidity, double pressure) {}

interface PushObserver {
    void update(WeatherReading reading);     // subject sends the payload
}

class WeatherStation {
    private final List<PushObserver> observers = new CopyOnWriteArrayList<>();
    public void register(PushObserver o) { observers.add(o); }
    public void setMeasurements(double t, double h, double p) {
        WeatherReading reading = new WeatherReading(t, h, p);
        for (PushObserver o : observers) o.update(reading);
    }
}

class StatisticsDisplay implements PushObserver {
    private double maxTemp = Double.NEGATIVE_INFINITY;
    @Override public void update(WeatherReading r) {
        maxTemp = Math.max(maxTemp, r.temperature());
        System.out.println("Max temp so far: " + maxTemp);
    }
}
```

**Usage**
```java
// pull
WeatherData data = new WeatherData();
new ConditionsDisplay(data);
data.setMeasurements(25.0, 65.0, 1013.0);

// push
WeatherStation station = new WeatherStation();
station.register(new StatisticsDisplay());
station.setMeasurements(25.0, 65.0, 1013.0);
```

### Design points
- **Push vs pull** — push couples observers to a payload type but is simpler; pull keeps observers
  flexible (they fetch what they need).
- **Decoupled** — the station knows only the observer interface.
- **Safe notify** — `CopyOnWriteArrayList` avoids `ConcurrentModificationException`.

**Complexity:** O(n) per change · Space O(n)

---
#observer #lld #practice