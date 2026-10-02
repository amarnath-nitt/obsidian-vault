# Unique Paths

**Difficulty:** Medium
**Category:** Dynamic Programming
**LeetCode Link:** [Unique Paths](https://leetcode.com/problems/unique-paths/)

---

## Problem Statement

A robot is on an `m x n` grid at the top-left corner. It can only move right or down. How many unique paths are there to reach the bottom-right corner?

**Example:**
```
Input: m = 3, n = 7
Output: 28
```

---

## Intuition

To reach any cell `(i, j)`, the robot must come from either `(i-1, j)` (above) or `(i, j-1)` (left). So `dp[i][j] = dp[i-1][j] + dp[i][j-1]`. The entire first row and first column are all 1 (only one way to reach them — go straight right or straight down).

---

## Approach 1: 2D DP

### Java Code
```java
class Solution {
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];

        for (int i = 0; i < m; i++) dp[i][0] = 1;
        for (int j = 0; j < n; j++) dp[0][j] = 1;

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }

        return dp[m - 1][n - 1];
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(m × n)
- **Space Complexity:** O(m × n)

---

## Approach 2: 1D DP (Space Optimized)

### Algorithm
Since each row only depends on the row above, compress to a single 1D array. `dp[j] += dp[j-1]` updates in-place.

### Java Code
```java
class Solution {
    public int uniquePaths(int m, int n) {
        int[] dp = new int[n];
        Arrays.fill(dp, 1);

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[j] += dp[j - 1];
            }
        }

        return dp[n - 1];
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(m × n)
- **Space Complexity:** O(n)

---

## Key Takeaways

1. **Recurrence:** `dp[i][j] = dp[i-1][j] + dp[i][j-1]`
2. **Base case:** All cells in first row and column = 1
3. **Space optimization:** Only need previous row → compress to 1D

---

## Tags
#dynamic-programming #medium #blind75
