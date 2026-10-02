# Grid Unique Paths

**LeetCode 62** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/unique-paths/)

### Problem
Count unique paths in an `m×n` grid from top-left to bottom-right (only right/down moves).

### Approach 1 — DP

- `dp[i][j]` = number of ways to reach cell (i, j)
- `dp[i][j] = dp[i-1][j] + dp[i][j-1]`

### Approach 2 — Combinatorics ? Best

- Total moves: `(m-1) + (n-1)` = `m+n-2`
- Choose `m-1` down moves out of total: `C(m+n-2, m-1)`

### Java Solution (DP)

```java
class Solution {
    public int uniquePaths(int m, int n) {
        int[] dp = new int[n];
        Arrays.fill(dp, 1);

        for (int i = 1; i < m; i++)
            for (int j = 1; j < n; j++)
                dp[j] += dp[j - 1];

        return dp[n - 1];
    }
}
```

**Complexity:** Time O(m×n) · Space O(n)

---
