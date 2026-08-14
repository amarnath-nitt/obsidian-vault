# Meeting Rooms II

**Difficulty:** Medium (Premium)  
**Category:** Intervals  
**LeetCode Link:** [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)

---

## Problem Statement

Given an array of meeting time intervals where `intervals[i] = [start_i, end_i]`, return the minimum number of conference rooms required.

**Example:**
```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
```

**Constraints:**
- `1 <= intervals.length <= 10^4`
- `0 <= start_i < end_i <= 10^6`

---

## Intuition

The minimum number of rooms needed equals the maximum number of overlapping meetings at any point in time.

---

## Approach: Min Heap

### Algorithm
1. Sort intervals by start time
2. Use min heap to track end times of ongoing meetings
3. For each meeting, remove ended meetings from heap
4. Add current meeting's end time to heap
5. Max heap size is the answer

### Java Code
```java
class Solution {
    public int minMeetingRooms(int[][] intervals) {
        if (intervals.length == 0) return 0;
        
        // Sort by start time
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        
        // Min heap to track end times
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        heap.offer(intervals[0][1]);
        
        for (int i = 1; i < intervals.length; i++) {
            // If earliest ending meeting has ended, remove it
            if (intervals[i][0] >= heap.peek()) {
                heap.poll();
            }
            
            // Add current meeting's end time
            heap.offer(intervals[i][1]);
        }
        
        return heap.size();
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n log n) - Sorting + heap operations
- **Space Complexity:** O(n) - Heap storage

---

## Tags
#intervals #heap #sorting #medium #blind75
