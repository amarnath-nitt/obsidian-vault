# Design Temperature Sensor (Encapsulation)

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Topic:** Encapsulation
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-temperature-sensor)

### Problem

Design a `TemperatureSensor` that records readings over time. The sensor keeps a running minimum and
maximum, and rejects readings outside a valid physical range. Callers record values and ask for
aggregates — they never manipulate the internal history directly.

### Approach

- Keep the readings and aggregates **private**.
- Validate each recorded value; reject out-of-range readings.
- Expose only derived queries (`count`, `min`, `max`, `average`).

### Java Solution

```java
public class TemperatureSensor {

    private static final double MIN_VALID = -100.0;
    private static final double MAX_VALID =  100.0;

    private int count;
    private double sum;
    private double min = Double.POSITIVE_INFINITY;
    private double max = Double.NEGATIVE_INFINITY;

    /** Records a reading; throws if it is outside the valid range. */
    public void record(double celsius) {
        if (celsius < MIN_VALID || celsius > MAX_VALID) {
            throw new IllegalArgumentException("reading out of range: " + celsius);
        }
        count++;
        sum += celsius;
        min = Math.min(min, celsius);
        max = Math.max(max, celsius);
    }

    public int count()   { return count; }
    public double min()  { return count == 0 ? Double.NaN : min; }
    public double max()  { return count == 0 ? Double.NaN : max; }
    public double average() { return count == 0 ? Double.NaN : sum / count; }
}
```

**Usage**
```java
TemperatureSensor sensor = new TemperatureSensor();
sensor.record(20.0);
sensor.record(25.5);
sensor.record(18.0);

sensor.min();        // 18.0
sensor.max();        // 25.5
sensor.average();    // 21.1666...
sensor.record(500);  // throws - out of range
```

### Design points
- **State hidden** — the aggregate fields are private; callers see only results.
- **Validation at the boundary** — out-of-range readings never enter the state.
- **Running aggregates** — min/max/sum updated incrementally (no stored history needed).

**Complexity:** O(1) per record/query · Space O(1)

---
#oop #encapsulation #lld #practice