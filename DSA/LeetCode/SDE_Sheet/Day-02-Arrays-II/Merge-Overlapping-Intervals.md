# Merge Overlapping Intervals

**LeetCode 56** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/merge-intervals/)

### Problem
Given a list of intervals, merge all overlapping intervals.

### Approach

1. **Sort** intervals by start time
2. Iterate and compare current interval's start with last merged interval's end:
   - If `current.start <= last.end` → merge by extending end: `Math.max(last.end, current.end)`
   - Else → add a new interval

### Java Solution

```java
class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        List<int[]> merged = new ArrayList<>();

        for (int[] interval : intervals) {
            if (merged.isEmpty() || merged.get(merged.size()-1)[1] < interval[0]) {
                merged.add(interval);
            } else {
                merged.get(merged.size()-1)[1] =
                    Math.max(merged.get(merged.size()-1)[1], interval[1]);
            }
        }
        return merged.toArray(new int[0][]);
    }
}
```

**Complexity:** Time O(n log n) · Space O(n)

---
