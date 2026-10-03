# Design an Elevator System (Medium)

**Difficulty:** Medium · **Patterns:** State, Strategy, Singleton
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design an elevator system: N cars, external (floor, direction) + internal requests, LOOK scheduling, swappable dispatch policy.

**Functional**
- External and internal requests can arrive at any time; no request is lost and no stop is queued twice.
- Cars sweep all stops in one direction before reversing (LOOK); operator can take a car out of service.

**Non-functional**
- Dispatch policy is swappable without touching car logic; the simulation advances on discrete ticks.

### The failure, before

```java
// ❌ A single car with List<Integer> queue + FCFS: it zig-zags between floors,
// reverses in the wrong direction, duplicates stops, and one car is always chosen.
public void move() { Integer next = queue.remove(0); current = next; }   // nearest? direction? no.
```

### The Fix (after)

Two sorted stop sets per car (LOOK) + a fleet dispatcher behind a strategy.

```java
import java.util.*;

enum Dir { UP, DOWN, IDLE }

class Elevator {
    private int floor = 0;
    private Dir dir = Dir.IDLE;
    private final NavigableSet<Integer> up = new TreeSet<>();                              // ascending
    private final NavigableSet<Integer> down = new TreeSet<>(Comparator.reverseOrder());   // descending

    void request(int target) {
        if (target > floor) up.add(target);
        else if (target < floor) down.add(target);
        if (dir == Dir.IDLE) dir = target > floor ? Dir.UP : target < floor ? Dir.DOWN : Dir.IDLE;
    }

    void step() {
        Integer next = dir == Dir.UP ? up.pollFirst() : dir == Dir.DOWN ? down.pollFirst() : null;
        if (next == null) {                                     // sweep exhausted → reverse if work remains
            if (dir == Dir.UP) dir = down.isEmpty() ? Dir.IDLE : Dir.DOWN;
            else if (dir == Dir.DOWN) dir = up.isEmpty() ? Dir.IDLE : Dir.UP;
            return;
        }
        floor = next;                                           // doors open at `next` — boarding happens here
    }

    int floor() { return floor; }
    Dir dir() { return dir; }
    boolean busy() { return !up.isEmpty() || !down.isEmpty(); }
}

interface DispatchStrategy {
    Elevator select(List<Elevator> cars, int floor, Dir dir);
}

class NearestCar implements DispatchStrategy {
    public Elevator select(List<Elevator> cars, int floor, Dir dir) {
        Elevator best = cars.get(0);
        int bestCost = Integer.MAX_VALUE;
        for (Elevator car : cars) {
            int cost = Math.abs(car.floor() - floor) + (car.busy() ? 10 : 0);   // idle cars win ties
            if (cost < bestCost) { bestCost = cost; best = car; }
        }
        return best;
    }
}

class ElevatorSystem {                                          // Singleton dispatcher
    private static final ElevatorSystem INSTANCE = new ElevatorSystem(3);
    private final List<Elevator> cars = new ArrayList<>();
    private DispatchStrategy strategy = new NearestCar();

    private ElevatorSystem(int n) { for (int i = 0; i < n; i++) cars.add(new Elevator()); }
    static ElevatorSystem get() { return INSTANCE; }

    void setStrategy(DispatchStrategy s) { strategy = s; }
    void request(int floor, Dir dir) { strategy.select(cars, floor, dir).request(floor); }
    void stepAll() { cars.forEach(Elevator::step); }
    List<Elevator> cars() { return cars; }
}
```

**Usage**
```java
ElevatorSystem sys = ElevatorSystem.get();
sys.request(5, Dir.UP);      // lobby panel: floor 5, going up
sys.request(2, Dir.DOWN);    // floor 2, going down
sys.stepAll(); sys.stepAll(); sys.stepAll();   // keep ticking; cars serve stops in sweep order
```

### Design points
- **Two sets, one sweep** — up ascending + down descending give LOOK for free; the `TreeSet` dedupes repeated requests.
- **Reversal lives in `step()`** — a car only flips when its current sweep is exhausted and work remains.
- **Idle cars win ties** — a busy-car penalty balances the fleet with no global bookkeeping.
- **One dispatcher, N cars** — external requests only meet the system; cars hold no opinion about each other.

**Complexity:** request O(log S) · step O(log S) · dispatch O(N) — S = queued stops, N = cars.

---
#lld #machine-coding #elevator #medium #practice