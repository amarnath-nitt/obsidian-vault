# Dynamic Programming - Practice Notes

## Pattern Overview
Breaking down problems into overlapping subproblems and storing solutions to avoid redundant computation.

## Key Concepts
- **Overlapping Subproblems**: Same subproblems solved multiple times
- **Optimal Substructure**: Optimal solution contains optimal solutions to subproblems
- **Memoization**: Top-down with caching
- **Tabulation**: Bottom-up with table

## Common DP Patterns

### 1. Linear DP (1D)
```java
// Climbing stairs, house robber
int[] dp = new int[n];
dp[0] = base_case;
for (int i = 1; i < n; i++) {
    dp[i] = Math.max(dp[i-1], dp[i-2] + nums[i]);
}
```

### 2. Grid DP (2D)
```java
// Unique paths, minimum path sum
int[][] dp = new int[m][n];
for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
        dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
    }
}
```

### 3. Knapsack (0/1)
```java
// 0/1 knapsack
int[][] dp = new int[n+1][capacity+1];
for (int i = 1; i <= n; i++) {
    for (int w = 0; w <= capacity; w++) {
        if (weight[i-1] <= w) {
            dp[i][w] = Math.max(dp[i-1][w], 
                               value[i-1] + dp[i-1][w - weight[i-1]]);
        } else {
            dp[i][w] = dp[i-1][w];
        }
    }
}
```

### 4. Longest Common Subsequence (LCS)
```java
int[][] dp = new int[m+1][n+1];
for (int i = 1; i <= m; i++) {
    for (int j = 1; j <= n; j++) {
        if (s1.charAt(i-1) == s2.charAt(j-1)) {
            dp[i][j] = dp[i-1][j-1] + 1;
        } else {
            dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
        }
    }
}
```

### 5. Longest Increasing Subsequence (LIS)
```java
int[] dp = new int[n];
Arrays.fill(dp, 1);
for (int i = 1; i < n; i++) {
    for (int j = 0; j < i; j++) {
        if (nums[i] > nums[j]) {
            dp[i] = Math.max(dp[i], dp[j] + 1);
        }
    }
}
```

## Practice Problems

### Easy
- [ ] [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) (LC 70) → [Solution](solutions/LC-70-Climbing-Stairs.md)
- [ ] [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) (LC 746) → [Solution](solutions/LC-746-Min-Cost-Climbing-Stairs.md)
- [ ] [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) (LC 509) → [Solution](solutions/LC-509-Fibonacci-Number.md)

### Medium
- [ ] [House Robber](https://leetcode.com/problems/house-robber/) (LC 198) → [Solution](solutions/LC-198-House-Robber.md)
- [ ] [Coin Change](https://leetcode.com/problems/coin-change/) (LC 322) → [Solution](solutions/LC-322-Coin-Change.md)
- [ ] [Coin Change II](https://leetcode.com/problems/coin-change-ii/) (LC 518) → [Solution](solutions/LC-518-Coin-Change-II.md)
- [ ] [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) (LC 300) → [Solution](solutions/LC-300-Longest-Increasing-Subsequence.md)
- [ ] [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) (LC 1143) → [Solution](solutions/LC-1143-Longest-Common-Subsequence.md)
- [ ] [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) (LC 5) → [Solution](solutions/LC-5-Longest-Palindromic-Substring.md)
- [ ] [Word Break](https://leetcode.com/problems/word-break/) (LC 139) → [Solution](solutions/LC-139-Word-Break.md)
- [ ] [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) (LC 152) → [Solution](solutions/LC-152-Maximum-Product-Subarray.md)
- [ ] [Decode Ways](https://leetcode.com/problems/decode-ways/) (LC 91) → [Solution](solutions/LC-91-Decode-Ways.md)
- [ ] [Unique Paths](https://leetcode.com/problems/unique-paths/) (LC 62) → [Solution](solutions/LC-62-Unique-Paths.md)
- [ ] [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) (LC 64) → [Solution](solutions/LC-64-Minimum-Path-Sum.md)
- [ ] [House Robber II](https://leetcode.com/problems/house-robber-ii/) (LC 213) → [Solution](solutions/LC-213-House-Robber-II.md)
- [ ] [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) (LC 416) → [Solution](solutions/LC-416-Partition-Equal-Subset-Sum.md)

### Hard
- [ ] [Edit Distance](https://leetcode.com/problems/edit-distance/) (LC 72) → [Solution](solutions/LC-72-Edit-Distance.md)
- [ ] [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) (LC 10) → [Solution](solutions/LC-10-Regular-Expression-Matching.md)
- [ ] [Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) (LC 123) → [Solution](solutions/LC-123-Best-Time-Stock-III.md)

## Reference
[LeetCode Pattern Guide](https://lnkd.in/gmi-Ji8K)
