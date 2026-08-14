# Non-overlapping Intervals

**Difficulty:** Medium  
**Category:** Intervals  
**LeetCode Link:** [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

---

## Approach: Greedy

### Java Code
```java
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[1] - b[1]);
        
        int count = 0;
        int end = intervals[0][1];
        
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < end) {
                count++;
            } else {
                end = intervals[i][1];
            }
        }
        
        return count;
    }
}
```

### Complexity
- **Time:** O(n log n)
- **Space:** O(1)

---

## Tags
#intervals #greedy #medium #blind75
