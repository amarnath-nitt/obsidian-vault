# Merge Intervals

**Difficulty:** Medium  
**Category:** Intervals  
**LeetCode Link:** [Merge Intervals](https://leetcode.com/problems/merge-intervals/)

---

## Approach: Sort and Merge

### Java Code
```java
class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        
        List<int[]> merged = new ArrayList<>();
        int[] current = intervals[0];
        
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] <= current[1]) {
                current[1] = Math.max(current[1], intervals[i][1]);
            } else {
                merged.add(current);
                current = intervals[i];
            }
        }
        merged.add(current);
        
        return merged.toArray(new int[merged.size()][]);
    }
}
```

### Complexity
- **Time:** O(n log n)
- **Space:** O(n)

---

## Tags
#intervals #sorting #medium #blind75

---

## Visualization

- Embed: `![](../assets/merge-intervals/step-1.svg)`
- Obsidian embed: `![[../assets/merge-intervals/step-1.svg]]`

<svg xmlns="http://www.w3.org/2000/svg" width="760" height="140">
    <style>text{font-family: Arial, sans-serif; font-size:13px}</style>
    <text x="20" y="28" fill="#222">Intervals sorted by start:</text>
    <g transform="translate(20,40)">
        <rect x="0" y="10" width="120" height="20" fill="#9ad0f5" stroke="#4b9be6"/>
        <rect x="80" y="10" width="160" height="20" fill="#bfe7c6" stroke="#57b86b"/>
        <rect x="260" y="10" width="80" height="20" fill="#ffd59e" stroke="#e29a2f"/>
        <text x="20" y="8" fill="#444">[1,4]  [2,6]  [8,10]</text>
    </g>
</svg>
