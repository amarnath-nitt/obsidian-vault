# Unique Paths II (with obstacles)

**LeetCode 63** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/unique-paths-ii/)

### Approach

- Same as Unique Paths but `dp[i][j] = 0` if obstacle
- `dp[i][j] = dp[i-1][j] + dp[i][j-1]` if no obstacle

### Java Solution

```java
class Solution {
    public int uniquePathsWithObstacles(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        if (grid[0][0] == 1 || grid[m-1][n-1] == 1) return 0;

        int[] dp = new int[n];
        dp[0] = 1;

        for (int i = 0; i < m; i++) {
            if (grid[i][0] == 1) dp[0] = 0;
            for (int j = 1; j < n; j++) {
                if (grid[i][j] == 1) dp[j] = 0;
                else dp[j] += dp[j-1];
            }
        }
        return dp[n-1];
    }
}
```

**Complexity:** Time O(m×n) · Space O(n)

---
