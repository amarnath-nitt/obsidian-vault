# Non-Overlapping Intervals

**Difficulty:** Medium
**Category:** Intervals
**LeetCode Link:** [Non-Overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

---

## Problem Statement

Given an array of intervals, return the minimum number of intervals you need to remove to make the rest non-overlapping.

**Example:**
```
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1  (remove [1,3])
```

---

## Intuition

This is the classic "Activity Selection" greedy problem. To minimize removals, maximize the number of intervals we keep. Greedily keep intervals that end earliest — they leave the most room for future intervals. Sort by end time, and whenever an overlap is found, remove the interval with the later end time (i.e., keep the current one).

---

## Approach: Greedy — Sort by End Time

### Algorithm
1. Sort intervals by end time
2. Track `end` = end time of last kept interval
3. For each interval:
   - If `start >= end`: no overlap → keep it, update `end`
   - Else: overlap → remove it (increment count)

### Java Code
```java
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[1] - b[1]);

        int count = 0;
        int end = intervals[0][1];

        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < end) {
                count++; // Overlap — remove this interval
            } else {
                end = intervals[i][1]; // No overlap — keep it
            }
        }

        return count;
    }
}
```

### Step-by-Step Example
`[[1,2],[2,3],[3,4],[1,3]]` sorted by end: `[[1,2],[2,3],[1,3],[3,4]]`
```
end=2
[2,3]: 2 >= 2 → keep, end=3
[1,3]: 1 < 3  → overlap, count=1
[3,4]: 3 >= 3 → keep, end=4
Return 1
```

### Complexity Analysis
- **Time Complexity:** O(n log n) — sorting
- **Space Complexity:** O(1)

---

## Key Takeaways

1. **Greedy insight:** Always keep the interval that ends earliest — maximizes future space
2. **Sort by end time** (not start time) — key difference from Merge Intervals
3. **Equivalent to:** n - (max non-overlapping intervals we can keep)

---

## Tags
#intervals #greedy #medium #blind75
