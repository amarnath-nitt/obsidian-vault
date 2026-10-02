# Aggressive Cows

**Problem:** Place C cows in N stalls (at positions). Maximize the minimum distance between any two cows.

### Approach (Binary Search on Answer)

- Binary search on the **minimum distance** (answer space: 1 to max_pos)
- For a given distance `d`, check if C cows can be placed with at least `d` apart
- Maximize valid `d`

### Java Solution

```java
public int aggressiveCows(int[] stalls, int c) {
    Arrays.sort(stalls);
    int lo = 1, hi = stalls[stalls.length-1] - stalls[0];

    while (lo < hi) {
        int mid = lo + (hi - lo + 1) / 2; // upper mid (maximize)
        if (canPlace(stalls, c, mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}

boolean canPlace(int[] stalls, int c, int minDist) {
    int count = 1, last = stalls[0];
    for (int i = 1; i < stalls.length; i++) {
        if (stalls[i] - last >= minDist) {
            count++;
            last = stalls[i];
            if (count == c) return true;
        }
    }
    return count >= c;
}
```

**Complexity:** Time O(n log(max_distance)) · Space O(1)

---
