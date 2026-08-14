# Minimum Path Sum (LC 64)

**Difficulty**: Medium  
**Pattern**: Dynamic Programming  
**LeetCode**: https://leetcode.com/problems/minimum-path-sum/

## Problem Statement
Given a `m x n` grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

**Example:**
```
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7 (1→3→1→1→1)
```

## Approach: 2D DP

### Intuition
`dp[i][j]` = min path sum to reach `(i, j)`.
`dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])`.
Handle boundaries (first row/col) carefully.

### Java Code
```java
class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        
        // Use input grid as DP table to save space
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) {
                    continue; // Start point
                } else if (i == 0) {
                    grid[i][j] += grid[i][j - 1];
                } else if (j == 0) {
                    grid[i][j] += grid[i - 1][j];
                } else {
                    grid[i][j] += Math.min(grid[i - 1][j], grid[i][j - 1]);
                }
            }
        }
        
        return grid[m - 1][n - 1];
    }
}
```

### Complexity
- **Time**: O(M * N)
- **Space**: O(1) (In-place)

## Key Takeaways
- Space Optimization by overwriting grid
