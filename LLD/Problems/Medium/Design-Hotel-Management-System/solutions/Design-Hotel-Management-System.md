# Design Hotel Management System (Medium)

**Difficulty:** Medium · **Patterns:** State, Strategy, Observer
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design a hotel: rooms by type, date-range reservations, check-in/check-out, room status lifecycle, housekeeping on checkout, and per-night pricing.

**Functional**
- Search by type + dates; reserve, check in, check out; checkout bills every night.
- Room status AVAILABLE → OCCUPIED → CLEANING → AVAILABLE; MAINTENANCE blocks booking.

**Non-functional**
- No double-booking; pricing and housekeeping plug in without touching the front desk.

### The failure, before

```java
// ❌ `room.booked = true` toggled by hand, `room.clean` as a second flag,
// bill = nights * flatRate (no weekends), housekeeping called inline and forgotten on cancel.
room.booked = true;  // which dates? overlapping? cleaning? flags drift apart.
```

### The Fix (after)

Overlap ledger for reservations + a room-status state machine + Observer housekeeping.

```java
import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.*;

class DateRange {
    final LocalDate start, end;                              // [start, end)
    DateRange(LocalDate s, LocalDate e) {
        if (!e.isAfter(s)) throw new IllegalArgumentException("end must be after start");
        start = s; end = e;
    }
    boolean overlaps(DateRange o) { return start.isBefore(o.end) && o.start.isBefore(end); }
    long nights() { return ChronoUnit.DAYS.between(start, end); }
}

enum RoomType { STANDARD(80), DELUXE(140), SUITE(250);
    final int base; RoomType(int b) { base = b; } }

enum RoomStatus { AVAILABLE, OCCUPIED, CLEANING, MAINTENANCE }

class Room {
    final String no; final RoomType type; RoomStatus status = RoomStatus.AVAILABLE;
    Room(String no, RoomType type) { this.no = no; this.type = type; }
}

enum ReservationState { RESERVED, CHECKED_IN, CHECKED_OUT, CANCELLED }

class Reservation {
    final Room room; final String guest; final DateRange dates;
    private ReservationState state = ReservationState.RESERVED;
    Reservation(Room r, String g, DateRange d) { room = r; guest = g; dates = d; }

    void checkIn()  { require(ReservationState.RESERVED, ReservationState.CHECKED_IN); }
    void checkOut() { require(ReservationState.CHECKED_IN, ReservationState.CHECKED_OUT); }
    void cancel()   { require(ReservationState.RESERVED, ReservationState.CANCELLED); }
    private void require(ReservationState from, ReservationState to) {
        if (state != from) throw new IllegalStateException(state + " → " + to);
        state = to;
    }
    boolean blocks(Room r, DateRange d) {
        return room == r && state != ReservationState.CANCELLED && dates.overlaps(d);
    }
    ReservationState state() { return state; }
}

interface PricingStrategy { long rate(RoomType type, LocalDate day); }

class WeekendPricing implements PricingStrategy {            // Fri/Sat +50%
    public long rate(RoomType type, LocalDate day) {
        boolean weekend = day.getDayOfWeek() == DayOfWeek.FRIDAY
                       || day.getDayOfWeek() == DayOfWeek.SATURDAY;
        return weekend ? type.base * 150 / 100 : type.base;
    }
}

interface RoomObserver { void onCheckOut(Room room); }

class Housekeeping implements RoomObserver {
    public void onCheckOut(Room room) { room.status = RoomStatus.CLEANING; }
}

class Hotel {
    private final Map<String, Room> rooms = new LinkedHashMap<>();
    private final List<Reservation> ledger = new ArrayList<>();
    private final List<RoomObserver> observers = new ArrayList<>();
    private PricingStrategy pricing = new WeekendPricing();

    void addRoom(Room r) { rooms.put(r.no, r); }
    void setPricing(PricingStrategy p) { pricing = p; }
    void subscribe(RoomObserver o) { observers.add(o); }

    List<Room> search(RoomType type, DateRange dates) {
        List<Room> out = new ArrayList<>();
        for (Room r : rooms.values())
            if (r.type == type && r.status != RoomStatus.MAINTENANCE
                    && ledger.stream().noneMatch(res -> res.blocks(r, dates)))
                out.add(r);
        return out;
    }

    Reservation reserve(Room room, String guest, DateRange dates) {
        if (ledger.stream().anyMatch(res -> res.blocks(room, dates)))
            throw new IllegalStateException("Room " + room.no + " taken for those dates");
        Reservation res = new Reservation(room, guest, dates);
        ledger.add(res);
        return res;
    }

    void checkIn(Reservation res)  { res.checkIn();  res.room.status = RoomStatus.OCCUPIED; }
    void checkOut(Reservation res) {
        long bill = bill(res);
        res.checkOut();
        res.room.status = RoomStatus.AVAILABLE;
        observers.forEach(o -> o.onCheckOut(res.room));      // housekeeping takes it from here
        System.out.println(res.guest + " owed " + bill);
    }

    long bill(Reservation res) {
        long total = 0;
        for (LocalDate d = res.dates.start; d.isBefore(res.dates.end); d = d.plusDays(1))
            total += pricing.rate(res.room.type, d);
        return total;
    }
    void finishCleaning(Room room) { room.status = RoomStatus.AVAILABLE; }
}
```

**Usage**
```java
Hotel hotel = new Hotel();
Room r101 = new Room("101", RoomType.STANDARD);
hotel.addRoom(r101);
hotel.subscribe(new Housekeeping());
DateRange stay = new DateRange(LocalDate.of(2026, 10, 9), LocalDate.of(2026, 10, 12));  // Fri–Mon
Reservation res = hotel.reserve(r101, "Asha", stay);
hotel.checkIn(res);        // room → OCCUPIED
hotel.checkOut(res);       // bill printed; room → CLEANING via observer
```

### Design points
- **Two machines, one room** — reservation state and room status both transition at check-in/out, but only the ledger decides availability.
- **Per-day pricing** — summing a rate function over the range makes weekends/seasons trivial; no special-case math.
- **Housekeeping decoupled** — the hotel knows nothing about cleaning schedules; an Observer flips the room and the next check-in can reject a dirty room.
- **MAINTENANCE blocks quietly** — a status filter in search keeps broken rooms out without reservation logic knowing why.

**Complexity:** search O(rooms × ledger) · reserve O(ledger) · bill O(nights).

---
#lld #machine-coding #hotel #medium #practice