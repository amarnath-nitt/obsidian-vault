---
solved: false
difficulty: Hard
pattern: Overlapping Intervals
lc_number: 759
date_solved: 
tags:
  - dsa
  - overlapping-intervals
  - hard
---
# Employee Free Time

[Problem Link](https://leetcode.com/problems/employee-free-time/)

## Problem Statement
We are given a list `schedule` of employees, which represents the working time for each employee.
Each employee has a list of non-overlapping `Intervals`, and these intervals are in sorted order.
Return the list of finite intervals representing **common, positive-length free time** for *all* employees, also in sorted order.

(Even though we are representing `Intervals` in the form `[x, y]`, the objects inside are `Intervals`, not lists or arrays. For example, `schedule[0][0].start = 1`, `schedule[0][0].end = 2`, and `schedule[0][0][0]` is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

## Approach
1.  Flatten all intervals from all employees into a single list.
2.  Sort the list by start time.
3.  Merge Overlapping Intervals. Any gap between merged intervals is a "free time".
    - Track `end` of the merged interval.
    - If next interval starts after `end`, then `[end, next.start]` is a free interval. Update `end` to `next.end`.
    - If next interval overlaps (starts before or at `end`), update `end` to `max(end, next.end)`.

## Time and Space Complexity
- **Time Complexity:** O(N log N) or O(N log K) if using a Heap, where N is total intervals.
- **Space Complexity:** O(N) to store flattened list.

## Code
```java
/*
// Definition for an Interval.
class Interval {
    public int start;
    public int end;

    public Interval() {}

    public Interval(int _start, int _end) {
        start = _start;
        end = _end;
    }
};
*/

class Solution {
    public List<Interval> employeeFreeTime(List<List<Interval>> schedule) {
        List<Interval> allIntervals = new ArrayList<>();
        
        // Flatten the schedule
        for (List<Interval> emp : schedule) {
            allIntervals.addAll(emp);
        }
        
        // Sort by start time
        Collections.sort(allIntervals, (a, b) -> a.start - b.start);
        
        List<Interval> result = new ArrayList<>();
        int end = allIntervals.get(0).end;
        
        for (int i = 1; i < allIntervals.size(); i++) {
            Interval current = allIntervals.get(i);
            
            if (current.start > end) {
                // Found a gap
                result.add(new Interval(end, current.start));
                end = current.end;
            } else {
                // Overlapping, extension
                end = Math.max(end, current.end);
            }
        }
        
        return result;
    }
}
```
