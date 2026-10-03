# Design Parking Lot (Easy)

**Difficulty:** Easy · **Patterns:** Singleton, Factory, Strategy
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design a multi-floor parking lot: vehicles park in compatible spots, a ticket is issued on entry, a fee is computed on exit.

**Functional**
- A lot has multiple **floors**, each with **parking spots** of different **types** (bike / car / truck).
- A **vehicle** can be parked if a compatible spot is free; a **ticket** is issued on entry.
- On exit, a **fee** is computed from duration + vehicle type and the spot is released.

**Non-functional**
- Pluggable **pricing** (hourly, flat, peak) and **spot-allocation** strategies.
- Multi-threaded entry/exit must not double-book a spot.

### The failure, before

```java
// ❌ One giant class: pricing hardcoded, spot search inline, no thread safety —
// a second bike takes the same spot while the first ticket is still open.
public double parkAndCharge(String plate) { /* ... 200 lines ... */ return fee; }
```

### The Fix (after)

Facade (`ParkingLot`) + `Floor`/`Spot`/`Ticket` entities + `PricingStrategy` interface.

```java
import java.time.Duration;
import java.time.LocalDateTime;
import java.util.*;

enum VehicleType { BIKE, CAR, TRUCK }

abstract class Vehicle {
    private final String plate;
    private final VehicleType type;
    protected Vehicle(String plate, VehicleType type) { this.plate = plate; this.type = type; }
    public String getPlate() { return plate; }
    public VehicleType getType() { return type; }
}
class Bike  extends Vehicle { public Bike(String p)  { super(p, VehicleType.BIKE); } }
class Car   extends Vehicle { public Car(String p)   { super(p, VehicleType.CAR); } }
class Truck extends Vehicle { public Truck(String p) { super(p, VehicleType.TRUCK); } }

class ParkingSpot {
    private final String id;
    private final VehicleType type;
    private boolean free = true;
    ParkingSpot(String id, VehicleType type) { this.id = id; this.type = type; }
    boolean isFreeFor(VehicleType t) { return free && type == t; }
    void occupy()  { free = false; }
    void release() { free = true; }
    public String getId() { return id; }
}

class Floor {
    private final int level;
    private final List<ParkingSpot> spots = new ArrayList<>();
    Floor(int level) { this.level = level; }
    void addSpot(ParkingSpot s) { spots.add(s); }
    ParkingSpot findSpot(VehicleType t) {
        return spots.stream().filter(s -> s.isFreeFor(t)).findFirst().orElse(null);
    }
}

class Ticket {
    private final String id;
    private final Vehicle vehicle;
    private final ParkingSpot spot;
    private final LocalDateTime entry = LocalDateTime.now();
    private LocalDateTime exit;
    Ticket(String id, Vehicle v, ParkingSpot s) { this.id = id; this.vehicle = v; this.spot = s; }
    void close() { exit = LocalDateTime.now(); }
    long hours() {
        LocalDateTime end = (exit == null) ? LocalDateTime.now() : exit;
        return Math.max(1, Duration.between(entry, end).toHours());
    }
    public String getId() { return id; }
    public ParkingSpot getSpot() { return spot; }
    public Vehicle getVehicle() { return vehicle; }
}

interface PricingStrategy { double calculate(Ticket t); }
class HourlyPricing implements PricingStrategy {
    private static final Map<VehicleType, Double> RATE =
        Map.of(VehicleType.BIKE, 10.0, VehicleType.CAR, 20.0, VehicleType.TRUCK, 40.0);
    public double calculate(Ticket t) { return RATE.get(t.getVehicle().getType()) * t.hours(); }
}

class ParkingLot {
    private static volatile ParkingLot instance;
    private final List<Floor> floors = new ArrayList<>();
    private final Map<String, Ticket> active = new HashMap<>();
    private final PricingStrategy pricing = new HourlyPricing();

    private ParkingLot() {}
    public static ParkingLot getInstance() {
        if (instance == null) {
            synchronized (ParkingLot.class) {
                if (instance == null) instance = new ParkingLot();
            }
        }
        return instance;
    }

    public void addFloor(Floor f) { floors.add(f); }
    public void addSpot(int level, ParkingSpot s) { floors.get(level).addSpot(s); }

    public synchronized Ticket park(Vehicle v) {
        for (Floor f : floors) {
            ParkingSpot s = f.findSpot(v.getType());
            if (s != null) {
                s.occupy();
                Ticket t = new Ticket(UUID.randomUUID().toString(), v, s);
                active.put(t.getId(), t);
                return t;
            }
        }
        throw new IllegalStateException("No spot available for " + v.getType());
    }

    public synchronized double unpark(Ticket t) {
        t.close();
        t.getSpot().release();
        active.remove(t.getId());
        return pricing.calculate(t);
    }
}
```

**Usage**
```java
ParkingLot lot = ParkingLot.getInstance();
// lot.addFloor(new Floor(0)); lot.addSpot(0, new ParkingSpot("C1", VehicleType.CAR));
// Ticket t = lot.park(new Car("KA-01-AB-1234"));
// double fee = lot.unpark(t);
```

### Design points
- **Ticket is the session** — entry + vehicle + spot; fee derives from duration, nothing stored twice.
- **Compatibility before occupancy** — `isFreeFor` gates `occupy`; no take-backs.
- **Strategy for pricing** — hourly now, flat/peak later, `ParkingLot` untouched.
- **Synchronized facade** — park/unpark are atomic; per-floor locks + `ConcurrentHashMap` when throughput matters.

**Complexity:** park / unpark O(floors × spots) naive scan → O(floors) with a free-spot index → O(1) with a per-type free-spot queue.

---
#lld #machine-coding #parking-lot #easy #practice
