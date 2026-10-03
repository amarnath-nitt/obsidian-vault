# Design Car Rental System (Medium)

**Difficulty:** Medium · **Patterns:** State, Strategy
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design a car rental: fleet by type + branch, date-range availability, reservations (reserve → pick up → return), and pluggable pricing.

**Functional**
- Search available cars by type + branch + date range; reserve, pick up, and return.
- Reservation lifecycle RESERVED → ACTIVE → COMPLETED (or CANCELLED before pickup).
- Quote prices by car type and rental duration.

**Non-functional**
- Two overlapping reservations for one car must be impossible; pricing plugs in without fleet changes.

### The failure, before

```java
// ❌ `boolean isRented` on the car — a car gets double-booked for *different weeks*
// the moment two reservations sit outside "today", and price math is hardcoded everywhere.
if (!car.isRented) { car.isRented = true; book(); }   // date ranges never compared
```

### The Fix (after)

Half-open `DateRange` + overlap checks over a reservation ledger + Strategy pricing.

```java
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.*;

class DateRange {
    final LocalDate start, end;                      // [start, end) — end exclusive
    DateRange(LocalDate s, LocalDate e) {
        if (!e.isAfter(s)) throw new IllegalArgumentException("end must be after start");
        start = s; end = e;
    }
    boolean overlaps(DateRange o) { return start.isBefore(o.end) && o.start.isBefore(end); }
    long days() { return ChronoUnit.DAYS.between(start, end); }
}

enum CarType {
    ECONOMY(30), SUV(55), LUXURY(95);
    final int perDay;
    CarType(int perDay) { this.perDay = perDay; }
}

class Car {
    final String id; final CarType type; final String branch;
    Car(String id, CarType type, String branch) { this.id = id; this.type = type; this.branch = branch; }
}

class Customer { final String id, license; Customer(String id, String l) { this.id = id; license = l; } }

enum ReservationState { RESERVED, ACTIVE, COMPLETED, CANCELLED }

class Reservation {
    final String id; final Car car; final Customer customer; final DateRange dates;
    private ReservationState state = ReservationState.RESERVED;
    Reservation(String id, Car c, Customer cu, DateRange d) { this.id = id; car = c; customer = cu; dates = d; }

    void pickUp()   { require(ReservationState.RESERVED, ReservationState.ACTIVE); }
    void complete() { require(ReservationState.ACTIVE, ReservationState.COMPLETED); }
    void cancel()   { require(ReservationState.RESERVED, ReservationState.CANCELLED); }
    private void require(ReservationState from, ReservationState to) {
        if (state != from) throw new IllegalStateException(state + " → " + to);
        state = to;
    }
    boolean holds(Car c, DateRange r) {
        return car == c && state != ReservationState.CANCELLED
            && state != ReservationState.COMPLETED && dates.overlaps(r);
    }
    ReservationState state() { return state; }
}

interface PricingStrategy { long quote(CarType type, long days); }

class StandardPricing implements PricingStrategy {                // 7+ days → 10% off
    public long quote(CarType type, long days) {
        long base = type.perDay * days;
        return days >= 7 ? base * 90 / 100 : base;
    }
}

class CarRentalSystem {
    private final Map<String, Car> cars = new LinkedHashMap<>();
    private final List<Reservation> ledger = new ArrayList<>();
    private PricingStrategy pricing = new StandardPricing();
    private int seq = 0;

    void addCar(Car c) { cars.put(c.id, c); }
    void setPricing(PricingStrategy p) { pricing = p; }

    List<Car> search(CarType type, String branch, DateRange dates) {
        List<Car> out = new ArrayList<>();
        for (Car c : cars.values())
            if (c.type == type && c.branch.equals(branch)
                    && ledger.stream().noneMatch(r -> r.holds(c, dates)))
                out.add(c);
        return out;
    }

    Reservation reserve(Car car, Customer customer, DateRange dates) {
        if (ledger.stream().anyMatch(r -> r.holds(car, dates)))
            throw new IllegalStateException("Car " + car.id + " not free for " + dates.start + ".." + dates.end);
        Reservation r = new Reservation("R" + (++seq), car, customer, dates);
        ledger.add(r);
        return r;
    }

    long quote(CarType type, DateRange dates) { return pricing.quote(type, dates.days()); }
}
```

**Usage**
```java
CarRentalSystem sys = new CarRentalSystem();
sys.addCar(new Car("C1", CarType.SUV, "BLR-HSR"));
DateRange week = new DateRange(LocalDate.of(2026, 10, 5), LocalDate.of(2026, 10, 12));
Reservation r = sys.reserve(sys.search(CarType.SUV, "BLR-HSR", week).get(0),
                            new Customer("u1", "KA-123"), week);
r.pickUp(); r.complete();                       // C1 free again after completion
System.out.println(sys.quote(CarType.SUV, week));   // 55 * 7 * 90% = 346
```

### Design points
- **No `isRented` flag** — one reservation ledger; `holds(...)` answers every availability question.
- **Half-open ranges compose** — back-to-back rentals (`end == nextStart`) do not collide.
- **State guards on transitions** — pickup only from RESERVED, complete only from ACTIVE; illegal moves throw.
- **Pricing is pure** — `quote(type, days)` touches no state; seasonal/extras strategies swap in cleanly.

**Complexity:** search O(fleet × ledger) worst case · reserve O(ledger) · quote O(1).

---
#lld #machine-coding #car-rental #medium #practice