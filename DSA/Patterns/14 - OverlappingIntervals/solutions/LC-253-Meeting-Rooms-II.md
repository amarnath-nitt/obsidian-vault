# Meeting Rooms II (LC 253)

**Difficulty**: Medium  
**Pattern**: Overlapping Intervals / Heap  
**LeetCode**: https://leetcode.com/problems/meeting-rooms-ii/

## Problem Statement
Given an array of meeting time intervals where `intervals[i] = [starti, endi]`, return the minimum number of conference rooms required.

**Example:**
```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
```

## Approach 1: Min-Heap

### Intuition
Sort meetings by start time.
Use Min-Heap to track end times of meetings currently in rooms.
Min-Heap top tells us the earliest a room becomes free.
For new meeting:
- If `start >= heap.peek()`: Room is free. Pop (re-use room), push new end time.
- Else: Need new room. Push new end time.
Heap size is result.

### Java Code
```java
class Solution {
    public int minMeetingRooms(int[][] intervals) {
        if (intervals.length == 0) return 0;
        
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]); // Sort by start
        
        PriorityQueue<Integer> endTimes = new PriorityQueue<>(); // Min-Heap of end times
        endTimes.offer(intervals[0][1]);
        
        for (int i = 1; i < intervals.length; i++) {
            // If room becomes free before current meeting starts
            if (intervals[i][0] >= endTimes.peek()) {
                endTimes.poll();
            }
            endTimes.offer(intervals[i][1]);
        }
        
        return endTimes.size();
    }
}
```

### Complexity
- **Time**: O(N log N)
- **Space**: O(N)

## Key Takeaways
- Sort by Start Time, Heap for End Times
