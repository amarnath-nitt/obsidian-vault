# Merge Intervals

**Difficulty:** Medium
**Category:** Intervals
**LeetCode Link:** [Merge Intervals](https://leetcode.com/problems/merge-intervals/)

---

## Problem Statement

Given an array of intervals, merge all overlapping intervals and return the result.

**Example:**
```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
```

---

## Intuition

Sort intervals by start time. Then iterate — if the current interval overlaps with the last merged interval (current start ≤ last end), extend the last interval's end. Otherwise, start a new merged interval.

---

## Approach: Sort and Merge

### Algorithm
1. Sort intervals by start time
2. Initialize result with the first interval
3. For each subsequent interval:
   - If it overlaps with last in result (`current[0] <= last[1]`): extend last's end
   - Else: add current as new interval

### Java Code
```java
class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

        List<int[]> merged = new ArrayList<>();
        int[] current = intervals[0];

        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] <= current[1]) {
                current[1] = Math.max(current[1], intervals[i][1]);
            } else {
                merged.add(current);
                current = intervals[i];
            }
        }
        merged.add(current);

        return merged.toArray(new int[merged.size()][]);
    }
}
```

### Step-by-Step Example
`[[1,3],[2,6],[8,10],[15,18]]` after sort:
```
current = [1,3]
[2,6]: 2 <= 3 → extend → current = [1,6]
[8,10]: 8 > 6 → add [1,6], current = [8,10]
[15,18]: 15 > 10 → add [8,10], current = [15,18]
add [15,18]
Result: [[1,6],[8,10],[15,18]]
```

### Complexity Analysis
- **Time Complexity:** O(n log n) — dominated by sorting
- **Space Complexity:** O(n) — output list

---

## Key Takeaways

1. **Sort first:** Sorting by start time ensures overlapping intervals are adjacent
2. **Overlap condition:** `current[0] <= last[1]`
3. **Extend end:** Take `max` of both ends when merging

---

## Tags
#intervals #sorting #medium #blind75
