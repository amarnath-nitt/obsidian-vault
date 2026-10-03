# Design Ride-Sharing Service like Uber (Hard)

**Difficulty:** Hard · **Patterns:** State, Strategy, Observer
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design ride-hailing: request → nearest-driver match → trip lifecycle → fare with surge; driver availability, cancellations, atomic dispatch.

**Functional**
- Nearest available driver assigned atomically; REQUESTED → ASSIGNED → IN_PROGRESS → COMPLETED (cancel before pickup).
- Driver AVAILABLE → ON_TRIP → AVAILABLE; fare = base + per-km, surge as a multiplier.

**Non-functional**
- No driver double-assigned; matching and pricing are swappable strategies.

### The failure, before

```java
// ❌ `pickDriver()` then `driver.busy = true` as two separate steps:
// two concurrent requests pick the same driver; cancels forget to free the flag;
// and fare math is `12 * km + 30` inlined at the one call site.
// Driver d = nearestFree(); send(d, trip); d.busy = true;   // race window between the lines
```

### The Fix (after)

One atomic dispatch section + paired state machines + `FareStrategy` with surge wrapping base.

```java
import java.util.*;

record Location(double x, double y) {
    double distanceTo(Location o) { return Math.hypot(x - o.x, y - o.y); }
}

enum DriverStatus { AVAILABLE, ON_TRIP, OFFLINE }

class Driver {
    final String id; Location location; DriverStatus status = DriverStatus.AVAILABLE;
    Driver(String id, Location location) { this.id = id; this.location = location; }
}

class Rider {
    final String id;
    Rider(String id) { this.id = id; }
}

enum TripState { REQUESTED, ASSIGNED, IN_PROGRESS, COMPLETED, CANCELLED }

class Trip {
    final String id; final Rider rider; final Location pickup, dropoff;
    TripState state = TripState.REQUESTED;
    Driver driver; double km;

    Trip(String id, Rider rider, Location pickup, Location dropoff) {
        this.id = id; this.rider = rider; this.pickup = pickup; this.dropoff = dropoff;
    }
    void assign(Driver d) {
        require(TripState.REQUESTED, TripState.ASSIGNED);
        driver = d; d.status = DriverStatus.ON_TRIP;             // pair flips together
    }
    void start()    { require(TripState.ASSIGNED, TripState.IN_PROGRESS); }
    void complete(double km) {
        require(TripState.IN_PROGRESS, TripState.COMPLETED);
        this.km = km; driver.status = DriverStatus.AVAILABLE;    // driver freed here, once
    }
    void cancel() {
        if (state != TripState.REQUESTED && state != TripState.ASSIGNED)
            throw new IllegalStateException("Cannot cancel a " + state + " trip");
        if (driver != null) driver.status = DriverStatus.AVAILABLE;
        state = TripState.CANCELLED;
    }
    private void require(TripState from, TripState to) {
        if (state != from) throw new IllegalStateException(state + " → " + to);
        state = to;
    }
}

interface MatchingStrategy { Driver findDriver(List<Driver> drivers, Location pickup); }

class NearestDriver implements MatchingStrategy {
    public Driver findDriver(List<Driver> drivers, Location pickup) {
        return drivers.stream()
                .filter(d -> d.status == DriverStatus.AVAILABLE)
                .min(Comparator.comparingDouble(d -> d.location.distanceTo(pickup)))
                .orElseThrow(() -> new IllegalStateException("No drivers available"));
    }
}

interface FareStrategy { long fare(double km); }

class BaseFare implements FareStrategy {                          // ₹30 base + ₹12/km
    public long fare(double km) { return 30 + Math.round(12 * km); }
}

class SurgeFare implements FareStrategy {                         // surge wraps base
    private final FareStrategy base; private final int percent;
    SurgeFare(FareStrategy base, int percent) { this.base = base; this.percent = percent; }
    public long fare(double km) { return base.fare(km) * (100 + percent) / 100; }
}

class RideService {
    private final Map<String, Driver> drivers = new LinkedHashMap<>();
    private final Map<String, Trip> trips = new LinkedHashMap<>();
    private MatchingStrategy matching = new NearestDriver();
    private FareStrategy fares = new BaseFare();
    private int seq = 0;

    void addDriver(Driver d) { drivers.put(d.id, d); }
    void setMatching(MatchingStrategy m) { matching = m; }
    void setSurge(int percent) { fares = percent == 0 ? new BaseFare()
                                                      : new SurgeFare(new BaseFare(), percent); }

    synchronized Trip request(Rider rider, Location pickup, Location dropoff) {
        Driver d = matching.findDriver(new ArrayList<>(drivers.values()), pickup);
        Trip t = new Trip("T" + (++seq), rider, pickup, dropoff);
        t.assign(d);                                             // find + assign: one critical section
        trips.put(t.id, t);
        return t;
    }
    synchronized void start(Trip t) { t.start(); }
    synchronized long complete(Trip t) {
        t.complete(t.pickup.distanceTo(t.dropoff) * 1.3);        // 1.3: road factor over crow-flight
        return fares.fare(t.km);
    }
    synchronized void cancel(Trip t) { t.cancel(); }
}
```

**Usage**
```java
RideService svc = new RideService();
svc.addDriver(new Driver("d1", new Location(1, 1)));
svc.addDriver(new Driver("d2", new Location(9, 9)));
svc.setSurge(20);                                             // 1.2×

Rider asha = new Rider("r1");
Trip t = svc.request(asha, new Location(0, 0), new Location(8, 0));   // d1 assigned (nearest)
svc.start(t);
long paid = svc.complete(t);                                  // d1 free again
System.out.println(paid);                                     // (30 + 12×10.4) × 1.2 ≈ 185
```

### Design points
- **Dispatch is one atomic step** — filter, rank, and assign inside `synchronized`; the race window is gone.
- **Trip and driver states flip in pairs** — assignment marks ON_TRIP; completion/cancel mark AVAILABLE; nowhere else.
- **Surge decorates base** — `SurgeFare(BaseFare, 20)`; multipliers compose without conditionals.
- **Fare at completion** — km is a fact only at the end; pricing reads it once.

**Complexity:** request O(drivers) · start/complete O(1) · memory O(trips).

---
#lld #machine-coding #uber #hard #practice