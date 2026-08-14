# Insert Interval (LC 57)

**Difficulty**: Medium  
**Pattern**: Overlapping Intervals  
**LeetCode**: https://leetcode.com/problems/insert-interval/

## Problem Statement
You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]` represent the start and the end of the `i`th interval and `intervals` is sorted in ascending order by `start_i`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

**Example:**
```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

## Approach: Iterative Merge

### Intuition
Iterate through the sorted intervals. There are three cases for each current interval:
1. Current ends before new interval starts -> Add current to result.
2. Current starts after new interval ends -> Add new interval (if not added) and current to result.
3. Overlap -> Merge current and new interval (`min(start)`, `max(end)`).

### Java Code
```java
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<>();
        int i = 0;
        int n = intervals.length;
        
        // Add all intervals that come before the new interval
        while (i < n && intervals[i][1] < newInterval[0]) {
            result.add(intervals[i]);
            i++;
        }
        
        // Merge all overlapping intervals
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            i++;
        }
        result.add(newInterval);
        
        // Add remaining intervals
        while (i < n) {
            result.add(intervals[i]);
            i++;
        }
        
        return result.toArray(new int[result.size()][]);
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(n) for result

## Key Takeaways
- Three-phase strategy: Before overlap, During overlap (merge), After overlap.
- Handle edge cases where new interval is first or last.
- Since input is sorted, linear scan is sufficient.
