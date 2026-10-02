# Insert Interval

**Difficulty:** Medium
**Category:** Intervals
**LeetCode Link:** [Insert Interval](https://leetcode.com/problems/insert-interval/)

---

## Problem Statement

Given a sorted list of non-overlapping intervals and a new interval, insert the new interval and merge if necessary.

**Example:**
```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
```

---

## Intuition

The intervals are already sorted. Process in three phases:
1. Add all intervals that end before the new interval starts (no overlap)
2. Merge all intervals that overlap with the new interval (expand bounds)
3. Add all remaining intervals after the new interval

---

## Approach: Three-Phase Linear Scan

### Algorithm
1. Add all intervals where `end < newInterval[0]`
2. While `start <= newInterval[1]`: expand `newInterval` bounds
3. Add merged `newInterval`, then add remaining

### Java Code
```java
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<>();
        int i = 0;

        // Phase 1: before new interval
        while (i < intervals.length && intervals[i][1] < newInterval[0]) {
            result.add(intervals[i++]);
        }

        // Phase 2: merge overlapping
        while (i < intervals.length && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            i++;
        }
        result.add(newInterval);

        // Phase 3: after new interval
        while (i < intervals.length) result.add(intervals[i++]);

        return result.toArray(new int[result.size()][]);
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## Key Takeaways

1. **Three phases:** Before / overlapping / after
2. **Overlap condition:** `intervals[i][0] <= newInterval[1]`
3. **No sorting needed:** Input is already sorted

---

## Tags
#intervals #medium #blind75
