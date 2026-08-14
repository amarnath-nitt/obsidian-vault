# Meeting Rooms

**Difficulty:** Easy (Premium)  
**Category:** Intervals  
**LeetCode Link:** [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)

---

## Problem Statement

Given an array of meeting time intervals where `intervals[i] = [start_i, end_i]`, determine if a person could attend all meetings.

**Example 1:**
```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
```

**Example 2:**
```
Input: intervals = [[7,10],[2,4]]
Output: true
```

**Constraints:**
- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i < end_i <= 10^6`

---

## Intuition

If any two meetings overlap, the person cannot attend all meetings. Sort by start time and check for overlaps.

---

## Approach: Sort and Check

### Algorithm
1. Sort intervals by start time
2. Check if any meeting ends after the next one starts
3. If yes, there's an overlap → return false

### Java Code
```java
class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        if (intervals.length <= 1) return true;
        
        // Sort by start time
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        
        // Check for overlaps
        for (int i = 0; i < intervals.length - 1; i++) {
            if (intervals[i][1] > intervals[i + 1][0]) {
                return false;  // Overlap found
            }
        }
        
        return true;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n log n) - Sorting
- **Space Complexity:** O(1) - In-place sorting

---

## Tags
#intervals #sorting #easy #blind75
