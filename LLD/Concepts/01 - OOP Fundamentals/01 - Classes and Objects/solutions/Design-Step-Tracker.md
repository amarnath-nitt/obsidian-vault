# Design Step Tracker Class

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Topic:** Classes and Objects
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-step-tracker)

### Problem

Design a `StepTracker` that records the number of steps a user takes each day and reports
aggregates. The tracker owns its data — callers add steps and ask questions; they never touch the
internal store directly.

### Approach

- Keep a `Map<LocalDate, Integer>` of daily steps **private**.
- Provide `addSteps` (accumulating per day) and read-only queries.
- Compute aggregates on demand so the class stays small.

### Java Solution

```java
import java.time.LocalDate;
import java.util.*;

public class StepTracker {

    private final Map<LocalDate, Integer> stepsByDay = new HashMap<>();

    /** Adds steps to the given day (accumulates if called more than once for that day). */
    public void addSteps(LocalDate day, int steps) {
        if (steps < 0) throw new IllegalArgumentException("steps must be >= 0");
        stepsByDay.merge(day, steps, Integer::sum);
    }

    public int stepsOn(LocalDate day) { return stepsByDay.getOrDefault(day, 0); }

    public int totalSteps() {
        int total = 0;
        for (int s : stepsByDay.values()) total += s;
        return total;
    }

    public int bestDay() {
        int best = 0;
        for (int s : stepsByDay.values()) best = Math.max(best, s);
        return best;
    }

    public double averagePerDay() {
        return stepsByDay.isEmpty() ? 0.0 : (double) totalSteps() / stepsByDay.size();
    }

    public int daysTracked() { return stepsByDay.size(); }
}
```

**Usage**
```java
StepTracker tracker = new StepTracker();
tracker.addSteps(LocalDate.of(2026, 1, 1), 5000);
tracker.addSteps(LocalDate.of(2026, 1, 1), 2000);   // same day → 7000
tracker.addSteps(LocalDate.of(2026, 1, 2), 3000);

tracker.stepsOn(LocalDate.of(2026, 1, 1));   // 7000
tracker.totalSteps();                        // 10000
tracker.bestDay();                           // 7000
tracker.averagePerDay();                     // 5000.0
```

### Design points
- **Encapsulated store** — the map is private; callers use methods.
- **Accumulating writes** — `merge` handles multiple additions per day.
- **Derived queries** — aggregates computed from state, no duplicate bookkeeping.

**Complexity:** O(days) per aggregate · Space O(days)

---
#oop #classes #lld #practice