# Implement Temperature Adapter

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Pattern:** Adapter
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/implement-temperature-adapter)

### Problem (contract)

A weather station understands one kind of thermometer: `getCelsius()` returning Celsius. A newly
purchased sensor reports **Fahrenheit** through a differently named method. Implement **only**
`FahrenheitSensorAdapter` so the station can treat both sensors identically.

- `FahrenheitSensorAdapter(sensor)` receives and stores a `FahrenheitSensor`.
- It implements the `Thermometer` contract.
- `getCelsius()` asks the wrapped sensor for its current Fahrenheit reading and returns
  `(F - 32) * 5 / 9`.
- The conversion happens **on every call** — do not cache the reading at construction.

### Approach

- **Object adapter** (composition): hold the `FahrenheitSensor` as a private field.
- Delegate to the adaptee and **translate the value** on each call.
- Use floating-point arithmetic so the result is not truncated.

### Java Solution

```java
// Target — what the station expects
interface Thermometer {
    double getCelsius();
}

// Adaptee — the vendor sensor with an incompatible API
class CelsiusSensor implements Thermometer {
    private double celsius;
    CelsiusSensor(double celsius) { this.celsius = celsius; }
    @Override public double getCelsius() { return celsius; }
}

class FahrenheitSensor {
    private double fahrenheit;
    FahrenheitSensor(double fahrenheit) { this.fahrenheit = fahrenheit; }
    double readFahrenheit() { return fahrenheit; }     // different method name
}

// Adapter — the only class you implement
class FahrenheitSensorAdapter implements Thermometer {

    private final FahrenheitSensor sensor;             // composition, not inheritance

    FahrenheitSensorAdapter(FahrenheitSensor sensor) { this.sensor = sensor; }

    @Override
    public double getCelsius() {
        double f = sensor.readFahrenheit();            // read live on each call
        return (f - 32) * 5.0 / 9.0;                   // floating-point conversion
    }
}
```

**Provided harness (do not modify)**
```java
class WeatherStation {
    private final java.util.List<Thermometer> sensors = new java.util.ArrayList<>();
    int addCelsiusSensor(double c)    { sensors.add(new CelsiusSensor(c)); return sensors.size() - 1; }
    int addFahrenheitSensor(double f) { sensors.add(new FahrenheitSensorAdapter(new FahrenheitSensor(f))); return sensors.size() - 1; }
    int sensorCount()                 { return sensors.size(); }
    double readCelsius(int i)         { return i < 0 || i >= sensors.size() ? Double.NaN : sensors.get(i).getCelsius(); }
    String reading(int i)             { return i < 0 || i >= sensors.size() ? "UNKNOWN" : sensors.get(i).getCelsius() + " C"; }
}
```

### Why it works
- **Composition over inheritance** — the adapter *holds* the sensor; it does not extend it.
- **On-demand conversion** — caching at construction would break when the sensor changes.
- **Only the adapter changes** — the station and the product classes are untouched.

**Complexity:** O(1) per read · Space O(1)

---
#adapter #lld #practice