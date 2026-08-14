# Insert Interval

**Difficulty:** Medium  
**Category:** Intervals  
**LeetCode Link:** [Insert Interval](https://leetcode.com/problems/insert-interval/)

---

## Approach: Three-Part Merge

### Java Code
```java
class Solution {
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
}
```

### Complexity
- **Time:** O(n)
- **Space:** O(n)

---

## Tags
#intervals #medium #blind75
