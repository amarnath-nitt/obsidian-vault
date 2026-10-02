---
solved: false
difficulty: Medium
pattern: Dynamic Programming
lc_number: 62
date_solved: 
tags:
  - dsa
  - dynamic-programming
  - medium
---
# Unique Paths (LC 62)

**Difficulty**: Medium  
**Pattern**: Dynamic Programming  
**LeetCode**: https://leetcode.com/problems/unique-paths/

## Problem Statement
There is a robot on an `m x n` grid. The robot is initially located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.
Given the two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

**Example:**
```
Input: m = 3, n = 7
Output: 28
```

## Approach: 2D DP

### Intuition
`dp[i][j]` = number of paths to reach `(i, j)`.
`dp[i][j] = dp[i-1][j] + dp[i][j-1]` (Sum of paths from top and left).
Base cases: First row and first column have 1 path.

### Java Code
```java
class Solution {
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || j == 0) {
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
                }
            }
        }
        
        return dp[m - 1][n - 1];
    }
}
```

### Complexity
- **Time**: O(M * N)
- **Space**: O(M * N) (Optimizable to O(N))

## Key Takeaways
- Basic Grid DP
- Combinatorics Solution: (M+N-2) Choose (M-1)
