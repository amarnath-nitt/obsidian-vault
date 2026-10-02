---
solved: false
difficulty: Medium
pattern: Overlapping Intervals
lc_number: 435
date_solved: 
tags:
  - dsa
  - overlapping-intervals
  - medium
---
# Non-overlapping Intervals (LC 435)

**Difficulty**: Medium  
**Pattern**: Overlapping Intervals / Greedy  
**LeetCode**: https://leetcode.com/problems/non-overlapping-intervals/

## Problem Statement
Given an array of intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

**Example:**
```
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
```

## Approach: Greedy (Sort by End Time)

### Intuition
To keep the maximum number of intervals (which minimizes removals), we should always pick the interval that ends earliest. This leaves as much room as possible for subsequent intervals.
1. Sort by end time.
2. Iterate: if current start < prev end, it overlaps -> remove current (increment count).
3. Else, update prev end to current end.

### Java Code
```java
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if (intervals.length == 0) return 0;
        
        // Sort by end time
        Arrays.sort(intervals, (a, b) -> a[1] - b[1]);
        
        int end = intervals[0][1];
        int removed = 0;
        
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < end) {
                // Overlap found, remove current interval (greedy choice: keep the one ending earlier)
                removed++;
            } else {
                // No overlap, update end time
                end = intervals[i][1];
            }
        }
        
        return removed;
    }
}
```

### Complexity
- **Time**: O(n log n) due to sorting
- **Space**: O(1) or O(log n) for sort

## Key Takeaways
- Classic Greedy interval problem (Interval Scheduling)
- Sort by **End Time** is crucial
- Counting removals is equivalent to finding max non-overlapping set (N - max_set)
