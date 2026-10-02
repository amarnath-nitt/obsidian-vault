# Minimum Path Sum

**LeetCode 64** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/minimum-path-sum/)

### Problem
Find path from top-left to bottom-right with minimum sum.

### Java Solution

```java
class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length, n = grid[0].length;

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                if (i == 0) grid[i][j] += grid[i][j-1];
                else if (j == 0) grid[i][j] += grid[i-1][j];
                else grid[i][j] += Math.min(grid[i-1][j], grid[i][j-1]);
            }

        return grid[m-1][n-1];
    }
}
```

**Complexity:** Time O(m×n) · Space O(1) (in-place)

---
