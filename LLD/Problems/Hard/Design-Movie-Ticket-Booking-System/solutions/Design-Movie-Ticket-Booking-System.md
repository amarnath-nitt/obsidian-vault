# Design Movie Ticket Booking System (Hard)

**Difficulty:** Hard · **Patterns:** State, Strategy
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design movie ticketing: shows with seat maps, seat locks with expiry, payments, cancellations, and time-based seat pricing.

**Functional**
- Lock seats per show (TTL); pay to confirm; cancel to release; expired locks auto-release and expire bookings.
- Pricing by category and show time; booking states PENDING → CONFIRMED → CANCELLED/EXPIRED.

**Non-functional**
- No seat locked or sold twice under concurrency; expiry needs no user action.

### The failure, before

```java
// ❌ `if (!seat.sold) { seat.sold = true; }` during "select": selection is permanent,
// abandoned carts block seats forever, and two customers race the same check —
// the second overwrites the first silently.
// if (!seat.sold) seat.sold = true;   // select == buy; no TTL, no race handling.
```

### The Fix (after)

A `SeatLockManager` that owns locks + sold sets, a PENDING booking holding a lock token, and a sweep.

```java
import java.time.Clock;
import java.util.*;

enum SeatCategory { REGULAR, PREMIUM, RECLINER }
enum BookingState { PENDING, CONFIRMED, CANCELLED, EXPIRED }

class Seat {
    final String no; final SeatCategory category;
    Seat(String no, SeatCategory category) { this.no = no; this.category = category; }
}

class Show {
    final String id, movie, screen; final long startsAt;
    final Map<String, Seat> seats = new LinkedHashMap<>();
    Show(String id, String movie, String screen, long startsAt) {
        this.id = id; this.movie = movie; this.screen = screen; this.startsAt = startsAt;
    }
    void addSeat(String no, SeatCategory category) { seats.put(no, new Seat(no, category)); }
}

record Lock(String token, List<String> seatNos, long expiresAt) {}

class SeatLockManager {
    static final long HOLD_MS = 8 * 60_000;                      // 8-minute hold
    private final Map<String, String> lockedBy = new HashMap<>();      // seat → token
    private final Map<String, Lock> locks = new HashMap<>();           // token → lock
    private final Set<String> sold = new HashSet<>();
    private int seq = 0;

    synchronized Lock lock(List<String> seatNos, long nowMs) {
        sweep(nowMs);
        for (String no : seatNos)
            if (lockedBy.containsKey(no) || sold.contains(no))
                throw new IllegalStateException("Seat unavailable: " + no);
        Lock lock = new Lock("L" + (++seq), List.copyOf(seatNos), nowMs + HOLD_MS);
        locks.put(lock.token(), lock);
        lock.seatNos().forEach(no -> lockedBy.put(no, lock.token()));
        return lock;
    }

    synchronized void confirm(Lock lock, long nowMs) {
        sweep(nowMs);
        if (!locks.containsKey(lock.token()))
            throw new IllegalStateException("Lock expired — reselect seats");
        lock.seatNos().forEach(no -> { lockedBy.remove(no); sold.add(no); });
        locks.remove(lock.token());
    }

    synchronized void release(Lock lock) {
        lock.seatNos().forEach(lockedBy::remove);
        locks.remove(lock.token());
    }

    synchronized void sweep(long nowMs) {                        // lazily reclaim expired holds
        List<Lock> expired = locks.values().stream().filter(l -> l.expiresAt() <= nowMs).toList();
        expired.forEach(this::release);
    }
    synchronized boolean isSold(String seatNo) { return sold.contains(seatNo); }
}

interface PricingStrategy { long price(SeatCategory category, long startsAt, long now); }

class MatineePricing implements PricingStrategy {                // prime time (18:00+) costs +30%
    public long price(SeatCategory category, long startsAt, long now) {
        long base = switch (category) { case REGULAR -> 150; case PREMIUM -> 250; case RECLINER -> 400; };
        long hour = (startsAt / 3_600_000L) % 24;                // demo clock: hours since epoch
        return hour >= 18 ? base * 130 / 100 : base;
    }
}

class Booking {
    final String id, showId; final List<String> seats; final Lock lock;
    BookingState state = BookingState.PENDING;
    Booking(String id, String showId, List<String> seats, Lock lock) {
        this.id = id; this.showId = showId; this.seats = seats; this.lock = lock;
    }
}

class MovieBookingService {
    private final Map<String, Show> shows = new LinkedHashMap<>();
    private final Map<String, SeatLockManager> lockManagers = new HashMap<>();
    private final Map<String, Booking> bookings = new LinkedHashMap<>();
    private PricingStrategy pricing = new MatineePricing();
    private Clock clock = Clock.systemUTC();
    private int seq = 0;

    void addShow(Show show) { shows.put(show.id, show); lockManagers.put(show.id, new SeatLockManager()); }
    void setClock(Clock c) { clock = c; }
    void setPricing(PricingStrategy p) { pricing = p; }

    Booking book(String showId, List<String> seatNos) {
        Lock lock = lockManagers.get(showId).lock(seatNos, clock.millis());
        Booking b = new Booking("B" + (++seq), showId, seatNos, lock);
        bookings.put(b.id, b);
        return b;
    }

    long pay(String bookingId) {
        Booking b = bookings.get(bookingId);
        if (b.state != BookingState.PENDING) throw new IllegalStateException("Booking is " + b.state);
        lockManagers.get(b.showId).confirm(b.lock, clock.millis());   // throws if the lock died
        b.state = BookingState.CONFIRMED;
        Show show = shows.get(b.showId);
        return b.seats.stream()
                .mapToLong(no -> pricing.price(show.seats.get(no).category, show.startsAt, clock.millis()))
                .sum();
    }

    void cancel(String bookingId) {
        Booking b = bookings.get(bookingId);
        if (b.state == BookingState.PENDING) lockManagers.get(b.showId).release(b.lock);
        if (b.state == BookingState.CONFIRMED || b.state == BookingState.PENDING)
            b.state = BookingState.CANCELLED;                        // (refund policy: extension point)
    }

    void sweepExpired() {
        lockManagers.values().forEach(m -> m.sweep(clock.millis()));
        bookings.values().stream()
                .filter(b -> b.state == BookingState.PENDING && b.lock.expiresAt() <= clock.millis())
                .forEach(b -> b.state = BookingState.EXPIRED);
    }
}
```

**Usage**
```java
MovieBookingService svc = new MovieBookingService();
Show show = new Show("S1", "Interstellar", "Screen 3", 20 * 3_600_000L);   // 8 PM show
show.addSeat("A1", SeatCategory.PREMIUM);
show.addSeat("A2", SeatCategory.PREMIUM);
svc.addShow(show);

Booking b = svc.book("S1", List.of("A1", "A2"));   // both seats locked, 8 minutes
long total = svc.pay(b.id);                        // 250 × 2 × 1.3 = 650
System.out.println(total);
```

### Design points
- **Locks are first-class data** — seat → token and token → expiry; the sweep is three lines and needs no user.
- **Confirm goes through the lock** — a dead lock means no sale; payment can never resurrect an expired hold.
- **Sold ⊥ locked** — confirm moves seats to `sold`; cancel only frees locks; the two states never blur.
- **Pricing is (category, show, now)** — a pure function; matinee/prime-time swaps change one class.

**Complexity:** book O(seats) · pay O(seats) · sweep O(locks).

---
#lld #machine-coding #movie-tickets #hard #practice