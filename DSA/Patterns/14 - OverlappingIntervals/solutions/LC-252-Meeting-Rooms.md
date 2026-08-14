# Meeting Rooms (LC 252)

**Difficulty**: Easy  
**Pattern**: Overlapping Intervals  
**LeetCode**: https://leetcode.com/problems/meeting-rooms/

## Problem Statement
Given an array of meeting time intervals where `intervals[i] = [starti, endi]`, determine if a person could attend all meetings.

**Example:**
```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
```

## Approach: Sorting

### Intuition
Sort intervals by start time.
Check if any interval starts before the previous one ends.
If `intervals[i][0] < intervals[i-1][1]`, then impossible.

### Java Code
```java
class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < intervals[i-1][1]) {
                return false;
            }
        }
        
        return true;
    }
}
```

### Complexity
- **Time**: O(N log N)
- **Space**: O(log N) sorting

## Key Takeaways
- Basic overlap check
