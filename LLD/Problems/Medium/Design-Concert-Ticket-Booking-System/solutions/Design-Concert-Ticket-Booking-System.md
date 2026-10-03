# Design a Concert Ticket Booking System (Medium)

**Difficulty:** Medium · **Patterns:** State, Strategy, Observer
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design concert ticketing: tiered seats, temporary holds with expiry, payment confirmations, cancellations, and sold-out alerts.

**Functional**
- Hold seats per show; pay to confirm; cancel to release; expired holds auto-release.
- PENDING → CONFIRMED → CANCELLED; pricing by (tier, days to show); sold-out alerts per tier.

**Non-functional**
- Concurrent holds never double-sell a seat; expiry needs no user action.

### The failure, before

```java
// ❌ `if (seat.free) { seat.free = false; }` at "add to cart" time:
// an abandoned cart holds the seat forever, two tabs race the same check,
// and every price is a hardcoded if-chain per tier.
// if (seat.free) seat.free = false;   // hold == permanent lock; no expiry, no tiers.
```

### The Fix (after)

A booking that *is* the hold (`heldUntil`), tier pricing behind a strategy, and a sweep.

```java
import java.time.Clock;
import java.time.Duration;
import java.util.*;

enum Tier { GENERAL(1_500), SILVER(3_000), GOLD(6_000), VIP(12_000);
    final long base; Tier(long b) { base = b; } }

enum SeatStatus { FREE, HELD, SOLD }
enum BookingState { PENDING, CONFIRMED, CANCELLED }

class Seat {
    final String no; final Tier tier; SeatStatus status = SeatStatus.FREE;
    Seat(String no, Tier tier) { this.no = no; this.tier = tier; }
}

class Show {
    final String artist; final long startsAt;
    final Map<String, Seat> seats = new LinkedHashMap<>();
    final Map<Tier, Integer> soldPerTier = new EnumMap<>(Tier.class);
    Show(String artist, long startsAt) { this.artist = artist; this.startsAt = startsAt; }
    void addSeat(String no, Tier tier) { seats.put(no, new Seat(no, tier)); }
}

class Booking {
    final String id; final Show show; final List<Seat> seats; final String customer;
    BookingState state = BookingState.PENDING;
    long heldUntil;
    Booking(String id, Show show, List<Seat> seats, String customer) {
        this.id = id; this.show = show; this.seats = seats; this.customer = customer;
    }
}

interface PricingStrategy { long price(Tier tier, long daysToShow); }

class EarlyBird implements PricingStrategy {                 // 10% off when > 30 days out
    public long price(Tier tier, long daysToShow) {
        return daysToShow > 30 ? tier.base * 90 / 100 : tier.base;
    }
}

interface ShowObserver { void onSoldOut(Show show, Tier tier); }

class TicketService {
    private static final long HOLD_MS = 10 * 60_000;         // 10-minute hold
    private final Map<String, Show> shows = new LinkedHashMap<>();
    private final List<Booking> bookings = new ArrayList<>();
    private final List<ShowObserver> observers = new ArrayList<>();
    private Clock clock = Clock.systemUTC();
    private PricingStrategy pricing = new EarlyBird();
    private int seq = 0;

    void setClock(Clock c) { clock = c; }
    void addShow(Show s) { shows.put(s.artist, s); }
    void subscribe(ShowObserver o) { observers.add(o); }

    synchronized Booking hold(Show show, List<String> seatNos, String customer) {
        List<Seat> picked = new ArrayList<>();
        for (String no : seatNos) {
            Seat s = show.seats.get(no);
            if (s == null || s.status != SeatStatus.FREE)
                throw new IllegalStateException("Seat " + no + " is not free");
            picked.add(s);
        }
        picked.forEach(s -> s.status = SeatStatus.HELD);      // all-or-nothing
        Booking b = new Booking("B" + (++seq), show, picked, customer);
        b.heldUntil = clock.millis() + HOLD_MS;
        bookings.add(b);
        return b;
    }

    synchronized long pay(Booking b) {
        expire(b);
        if (b.state != BookingState.PENDING) throw new IllegalStateException("Booking is " + b.state);
        long days = Duration.ofMillis(b.show.startsAt - clock.millis()).toDays();
        long total = b.seats.stream()
                .mapToLong(no -> pricing.price(b.show.seats.get(no).tier, days)).sum();
        b.state = BookingState.CONFIRMED;
        b.seats.forEach(s -> s.status = SeatStatus.SOLD);
        b.seats.forEach(s -> b.show.soldPerTier.merge(s.tier, 1, Integer::sum));
        for (Tier tier : b.seats.stream().map(no -> b.show.seats.get(no).tier).distinct().toList()) {
            boolean anyInTier = b.show.seats.values().stream().anyMatch(s -> s.tier == tier);
            boolean soldOut = anyInTier && b.show.seats.values().stream()
                    .filter(s -> s.tier == tier)
                    .noneMatch(s -> s.status != SeatStatus.SOLD);
            if (soldOut) observers.forEach(o -> o.onSoldOut(b.show, tier));
        }
        return total;
    }

    synchronized long cancel(Booking b) {
        if (b.state == BookingState.CANCELLED) return 0;
        long refund = b.state == BookingState.CONFIRMED ? amountFor(b) : 0;
        b.state = BookingState.CANCELLED;
        b.seats.forEach(s -> s.status = SeatStatus.FREE);
        return refund;
    }

    synchronized void sweepExpired() { bookings.forEach(this::expire); }

    private void expire(Booking b) {
        if (b.state == BookingState.PENDING && clock.millis() > b.heldUntil) {
            b.state = BookingState.CANCELLED;
            b.seats.forEach(s -> s.status = SeatStatus.FREE);
        }
    }
    private long amountFor(Booking b) {
        long days = Duration.ofMillis(b.show.startsAt - clock.millis()).toDays();
        return b.seats.stream().mapToLong(no -> pricing.price(b.show.seats.get(no).tier, days)).sum();
    }
}
```

**Usage**
```java
TicketService svc = new TicketService();
Show show = new Show("A. R. Rahman", Instant.parse("2026-12-01T19:00:00Z").toEpochMilli());
show.addSeat("A1", Tier.VIP); show.addSeat("B1", Tier.GOLD);
svc.addShow(show);

Booking b = svc.hold(show, List.of("A1"), "Asha");   // PENDING, 10-min lease
svc.pay(b);                                          // seat A1 → SOLD, price applied
```

### Design points
- **The booking is the hold** — `heldUntil` on a PENDING booking; expire = CANCELLED + seats FREE.
- **Validate all, then mark** — no half-held rows; the failure mode is "nothing happened".
- **Pay re-checks expiry** — even if the sweep has not run, a stale hold cannot pay.
- **`synchronized` around the race** — hold/pay/cancel serialize; per-seat locks are the next step.

**Complexity:** hold/pay/cancel O(seats) · sweep O(bookings).

---
#lld #machine-coding #concert #medium #practice