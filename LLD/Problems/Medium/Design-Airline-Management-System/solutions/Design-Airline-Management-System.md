# Design Airline Management System (Medium)

**Difficulty:** Medium · **Patterns:** State, Strategy, Observer
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design an airline booking flow: search flights, hold seats with expiry, confirm with payment, cancel with policy-based refunds.

**Functional**
- Search by route + date; hold seats (temporary); confirm with payment; cancel with refund.
- PENDING → CONFIRMED → CANCELLED; expired holds auto-cancel and free seats.

**Non-functional**
- No seat is double-sold; expired holds release automatically; pricing/refund are pluggable.

### The failure, before

```java
// ❌ `seat.booked = true` permanently: no hold, no expiry, no class pricing —
// two checkout tabs both confirm the same seat; an abandoned cart blocks it forever.
// if (!seat.booked) { seat.booked = true; charge(card); }
```

### The Fix (after)

Seat holds with a TTL on a booking state machine + Strategy pricing/refunds.

```java
import java.time.Clock;
import java.time.Duration;
import java.util.*;

enum SeatClass { ECONOMY, BUSINESS, FIRST }
enum SeatStatus { FREE, HELD, BOOKED }
enum BookingState { PENDING, CONFIRMED, CANCELLED }

class Seat {
    final String no; final SeatClass cls; SeatStatus status = SeatStatus.FREE;
    Seat(String no, SeatClass cls) { this.no = no; this.cls = cls; }
}

class Flight {
    final String id, origin, dest; final long departAt;
    final Map<String, Seat> seats = new LinkedHashMap<>();
    Flight(String id, String o, String d, long departAt) { this.id = id; origin = o; dest = d; this.departAt = departAt; }
    void addSeat(String no, SeatClass cls) { seats.put(no, new Seat(no, cls)); }
}

class Booking {
    final String id; final Flight flight; final List<Seat> seats; final String passenger;
    BookingState state = BookingState.PENDING;
    long heldUntil;
    Booking(String id, Flight f, List<Seat> s, String p) { this.id = id; flight = f; seats = s; passenger = p; }
}

interface PricingStrategy { long fare(Flight flight, SeatClass cls); }

class DemandPricing implements PricingStrategy {             // closer to departure → pricier
    private final Clock clock;
    DemandPricing(Clock clock) { this.clock = clock; }
    public long fare(Flight flight, SeatClass cls) {
        long base = switch (cls) { case ECONOMY -> 5_000; case BUSINESS -> 12_000; case FIRST -> 20_000; };
        long days = Duration.ofMillis(flight.departAt - clock.millis()).toDays();
        return days < 3 ? base * 150 / 100 : base;
    }
}

interface RefundPolicy { long refund(Booking booking, long now); }

class TieredRefund implements RefundPolicy {                 // >48h full, ≤48h half
    public long refund(Booking b, long now) {
        long msToDepart = b.flight.departAt - now;
        return msToDepart > 48 * 3_600_000L ? FULL_FARE : FULL_FARE / 2;
    }
    static final long FULL_FARE = 5_000;                     // simplified: flat reference fare
}

class BookingService {
    private static final long HOLD_MS = 15 * 60_000;         // 15-minute hold
    private final Map<String, Flight> flights = new LinkedHashMap<>();
    private final Map<String, Booking> bookings = new LinkedHashMap<>();
    private Clock clock = Clock.systemUTC();
    private PricingStrategy pricing = new DemandPricing(clock);
    private RefundPolicy refunds = new TieredRefund();
    private int seq = 0;

    void setClock(Clock c) { clock = c; pricing = new DemandPricing(c); }
    void addFlight(Flight f) { flights.put(f.id, f); }
    List<Flight> search(String origin, String dest, long dayStart, long dayEnd) {
        return flights.values().stream()
                .filter(f -> f.origin.equals(origin) && f.dest.equals(dest)
                          && f.departAt >= dayStart && f.departAt < dayEnd)
                .toList();
    }

    Booking hold(Flight flight, List<String> seatNos, String passenger) {
        List<Seat> picked = new ArrayList<>();
        for (String no : seatNos) {
            Seat s = flight.seats.get(no);
            if (s == null || s.status != SeatStatus.FREE) throw new IllegalStateException("Seat " + no + " not free");
            picked.add(s);
        }
        picked.forEach(s -> s.status = SeatStatus.HELD);      // all-or-nothing: validated first
        Booking b = new Booking("B" + (++seq), flight, picked, passenger);
        b.heldUntil = clock.millis() + HOLD_MS;
        bookings.put(b.id, b);
        return b;
    }

    long confirm(Booking b) {
        expireHold(b);
        if (b.state != BookingState.PENDING) throw new IllegalStateException("Booking is " + b.state);
        b.state = BookingState.CONFIRMED;
        b.seats.forEach(s -> s.status = SeatStatus.BOOKED);
        return b.seats.stream().mapToLong(s -> pricing.fare(b.flight, s.cls)).sum();
    }

    long cancel(Booking b) {
        if (b.state == BookingState.CANCELLED) return 0;
        long refund = b.state == BookingState.CONFIRMED ? refunds.refund(b, clock.millis())
                                                        : 0;           // unpaid hold: nothing to refund
        b.state = BookingState.CANCELLED;
        b.seats.forEach(s -> s.status = SeatStatus.FREE);
        return refund;
    }

    void sweepExpired() { bookings.values().forEach(this::expireHold); }

    private void expireHold(Booking b) {
        if (b.state == BookingState.PENDING && clock.millis() > b.heldUntil) {
            b.state = BookingState.CANCELLED;
            b.seats.forEach(s -> s.status = SeatStatus.FREE);
        }
    }
}
```

**Usage**
```java
BookingService svc = new BookingService();
svc.setClock(Clock.fixed(Instant.parse("2026-10-03T10:00:00Z"), ZoneOffset.UTC));
Flight ai = new Flight("AI-501", "BLR", "DEL", Instant.parse("2026-10-10T06:00:00Z").toEpochMilli());
ai.addSeat("12A", SeatClass.ECONOMY);
svc.addFlight(ai);
Booking b = svc.hold(ai, List.of("12A"), "Asha");   // PENDING, held 15 min
long fare = svc.confirm(b);                          // seat 12A → BOOKED
long refund = svc.cancel(b);                         // >48h out → full refund; seat free again
```

### Design points
- **A hold is a booking with `heldUntil`** — one state machine, not a separate hold subsystem.
- **All-or-nothing holds** — seats are validated before any is marked HELD; nobody gets half a row.
- **Expiry is checked at confirm and swept periodically** — stale state can never confirm.
- **Refund math is policy** — `RefundPolicy` takes the booking + now; tiers change without touching the flow.

**Complexity:** hold O(seats) · confirm O(seats) · search O(flights).

---
#lld #machine-coding #airline #medium #practice