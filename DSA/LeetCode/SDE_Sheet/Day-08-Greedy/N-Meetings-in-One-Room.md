# N Meetings in One Room

**Problem:** Given start and end times of N meetings, find the maximum number of meetings that can be held in one room.

### Approach (Activity Selection — Earliest Finish Time)

1. Sort meetings by **end time**
2. Greedily pick a meeting if its **start time > last meeting's end time**

> **Why earliest finish?** By finishing early, we leave maximum room for future meetings.

### Java Solution

```java
import java.util.Arrays;

public class NMeetings {
    static int maxMeetings(int[] start, int[] end) {
        int n = start.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Arrays.sort(idx, (a, b) -> end[a] - end[b]); // sort by end time

        int count = 1, lastEnd = end[idx[0]];
        for (int i = 1; i < n; i++) {
            if (start[idx[i]] > lastEnd) {
                count++;
                lastEnd = end[idx[i]];
            }
        }
        return count;
    }
}
```

**Complexity:** Time O(n log n) · Space O(n)

---
