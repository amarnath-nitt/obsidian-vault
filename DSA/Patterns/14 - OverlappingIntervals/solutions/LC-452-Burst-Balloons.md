---
solved: false
difficulty: Medium
pattern: Overlapping Intervals
lc_number: 452
date_solved: 
tags:
  - dsa
  - overlapping-intervals
  - medium
---
# Minimum Number of Arrows to Burst Balloons (LC 452)

**Difficulty**: Medium  
**Pattern**: Overlapping Intervals  
**LeetCode**: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

## Problem Statement
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array `points` where `points[i] = [xstart, xend]`.
Arrows can be shot up directly vertically from different points along the x-axis. A balloon with `xstart` and `xend` is burst by an arrow shot at `x` if `xstart <= x <= xend`.
Return the minimum number of arrows that must be shot to burst all balloons.

**Example:**
```
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
```

## Approach: Greedy Sorting by End Time

### Intuition
Sort balloons by end time.
Shoot arrow at end of first balloon. This arrow bursts all overlapping balloons.
Skip all burst balloons. Repeat.
Equivalent to "Interval Scheduling" (max non-overlapping intervals, but here we count groups).

### Java Code
```java
class Solution {
    public int findMinArrowShots(int[][] points) {
        if (points.length == 0) return 0;
        
        // Sort by end time
        // Use Integer.compare to avoid overflow for large negative/positive values
        Arrays.sort(points, (a, b) -> Integer.compare(a[1], b[1]));
        
        int arrows = 1;
        int currentEnd = points[0][1];
        
        for (int i = 1; i < points.length; i++) {
            if (points[i][0] > currentEnd) {
                // No overlap, need new arrow
                arrows++;
                currentEnd = points[i][1];
            }
            // Overlapping balloons are automatically popped by arrow at currentEnd
        }
        
        return arrows;
    }
}
```

### Complexity
- **Time**: O(N log N)
- **Space**: O(log N) sorting

## Key Takeaways
- Sort by End Time -> Greedy choice
- `Integer.compare` for `int` subtraction safety
