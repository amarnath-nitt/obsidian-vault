# Overlapping Intervals - Practice Notes

## Pattern Overview
Problems involving intervals that may overlap, merge, or need to be scheduled.

## Key Concepts
- **Sort by start time**: Most common approach
- **Merge overlapping**: Check if current overlaps with previous
- **Time Complexity**: O(n log n) due to sorting

## Template Code

### Merge Intervals
```java
public int[][] merge(int[][] intervals) {
    Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
    List<int[]> result = new ArrayList<>();
    
    int[] current = intervals[0];
    for (int i = 1; i < intervals.length; i++) {
        if (intervals[i][0] <= current[1]) {
            // Overlapping - merge
            current[1] = Math.max(current[1], intervals[i][1]);
        } else {
            // No overlap - add current and move to next
            result.add(current);
            current = intervals[i];
        }
    }
    result.add(current);
    return result.toArray(new int[result.size()][]);
}
```

### Insert Interval
```java
public int[][] insert(int[][] intervals, int[] newInterval) {
    List<int[]> result = new ArrayList<>();
    int i = 0;
    
    // Add all intervals before newInterval
    while (i < intervals.length && intervals[i][1] < newInterval[0]) {
        result.add(intervals[i++]);
    }
    
    // Merge overlapping intervals
    while (i < intervals.length && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
        newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
        i++;
    }
    result.add(newInterval);
    
    // Add remaining intervals
    while (i < intervals.length) {
        result.add(intervals[i++]);
    }
    
    return result.toArray(new int[result.size()][]);
}
```

## Practice Problems

### Easy
- [ ] [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) (LC 252) → [Solution](solutions/LC-252-Meeting-Rooms.md)

### Medium
- [ ] [Merge Intervals](https://leetcode.com/problems/merge-intervals/) (LC 56) → [Solution](solutions/LC-56-Merge-Intervals.md)
- [ ] [Insert Interval](https://leetcode.com/problems/insert-interval/) (LC 57) → [Solution](solutions/LC-57-Insert-Interval.md)
- [ ] [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) (LC 435) → [Solution](solutions/LC-435-Non-overlapping-Intervals.md)
- [ ] [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) (LC 253) → [Solution](solutions/LC-253-Meeting-Rooms-II.md)
- [ ] [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) (LC 452) → [Solution](solutions/LC-452-Burst-Balloons.md)

### Hard
- [ ] [Employee Free Time](https://leetcode.com/problems/employee-free-time/) (LC 759) → [Solution](solutions/LC-759-Employee-Free-Time.md)

## Reference
[LeetCode Pattern Guide](https://lnkd.in/gzzfpkkq)
