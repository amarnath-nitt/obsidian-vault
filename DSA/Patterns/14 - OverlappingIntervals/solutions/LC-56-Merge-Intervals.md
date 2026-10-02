---
solved: false
difficulty: Medium
pattern: Overlapping Intervals
lc_number: 56
date_solved: 
tags:
  - dsa
  - overlapping-intervals
  - medium
---
# Merge Intervals (LC 56)

**Difficulty**: Medium  
**Pattern**: Overlapping Intervals  
**LeetCode**: https://leetcode.com/problems/merge-intervals/

## Existing Solution
This problem is solved in Blind75: → [Solution](../../../LeetCode/Blind75/Intervals/Merge-Intervals.md)

## Problem Statement
Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals.

**Example:**
```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
```

## Approach 1: Brute Force

### Java Code
```java
class Solution {
    public int[][] merge(int[][] intervals) {
        List<int[]> merged = new ArrayList<>();
        boolean[] used = new boolean[intervals.length];
        
        for (int i = 0; i < intervals.length; i++) {
            if (used[i]) continue;
            
            int[] current = intervals[i].clone();
            used[i] = true;
            
            boolean changed = true;
            while (changed) {
                changed = false;
                for (int j = 0; j < intervals.length; j++) {
                    if (!used[j] && overlaps(current, intervals[j])) {
                        current[0] = Math.min(current[0], intervals[j][0]);
                        current[1] = Math.max(current[1], intervals[j][1]);
                        used[j] = true;
                        changed = true;
                    }
                }
            }
            merged.add(current);
        }
        
        return merged.toArray(new int[merged.size()][]);
    }
    
    private boolean overlaps(int[] a, int[] b) {
        return a[0] <= b[1] && b[0] <= a[1];
    }
}
```

### Complexity
- **Time**: O(n²)
- **Space**: O(n)

## Approach 2: Sort + Merge (Optimized)

### Java Code
```java
class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1) return intervals;
        
        // Sort by start time
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        
        List<int[]> merged = new ArrayList<>();
        int[] current = intervals[0];
        merged.add(current);
        
        for (int[] interval : intervals) {
            if (interval[0] <= current[1]) {
                // Overlapping, merge
                current[1] = Math.max(current[1], interval[1]);
            } else {
                // Non-overlapping, add new interval
                current = interval;
                merged.add(current);
            }
        }
        
        return merged.toArray(new int[merged.size()][]);
    }
}
```

### Complexity
- **Time**: O(n log n)
- **Space**: O(n)

## Key Takeaways
- Sort by start time enables linear merge
- Check overlap: `interval[0] <= current[1]`
- Update end: `max(current[1], interval[1])`
- Classic interval merging pattern
