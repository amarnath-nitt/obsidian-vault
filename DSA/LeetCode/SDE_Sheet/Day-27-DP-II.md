# Day 27 — Dynamic Programming II (2D DP, Grid, LCS)

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** DP — 2D Grid, Subsequences
**Difficulty Mix:** Medium / Hard

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Unique Paths II (with obstacles)]] | 63 | Medium | ⬜ |
| 2 | [[#Minimum Path Sum]] | 64 | Medium | ⬜ |
| 3 | [[#Longest Common Subsequence (LCS)]] | 1143 | Medium | ⬜ |
| 4 | [[#Longest Increasing Subsequence (LIS)]] | 300 | Medium | ⬜ |
| 5 | [[#Edit Distance]] | 72 | Hard | ⬜ |
| 6 | [[#Matrix Chain Multiplication]] | — | Medium | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Unique Paths II | Recursively try right/down paths around obstacles. Exponential. | 2D DP table. O(m*n). | 1D DP over columns. O(m*n) time, O(n) space. |
| Minimum Path Sum | Recursively try every right/down path. Exponential. | 2D DP table. O(m*n). | In-place grid update or 1D DP. O(m*n) time, O(n) or O(1) extra. |
| Longest Common Subsequence | Recursive take/skip both strings. Exponential. | 2D memo/DP. O(n*m). | Two-row DP when only length is needed. O(min(n,m)) space. |
| Longest Increasing Subsequence | Generate all subsequences. O(2^n). | DP ending at each index. O(n^2). | Patience sorting / tails array with binary search. O(n log n). |
| Edit Distance | Recursive insert/delete/replace choices. Exponential. | 2D memo/DP. O(n*m). | Rolling rows. O(n*m) time, O(min(n,m)) space. |
| Matrix Chain Multiplication | Try all parenthesizations recursively. Exponential. | Memoized interval DP. O(n^3). | Bottom-up interval DP. O(n^3), O(n^2) space. |

---

## Unique Paths II (with obstacles)

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

## Minimum Path Sum

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

## Longest Common Subsequence (LCS)

**LeetCode 1143** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/longest-common-subsequence/)

### Problem
Find the length of the longest subsequence common to both strings.

### Approach

- `dp[i][j]` = LCS of `text1[0..i-1]` and `text2[0..j-1]`
- If chars match: `dp[i][j] = dp[i-1][j-1] + 1`
- Else: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

### Java Solution

```java
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length(), n = text2.length();
        int[][] dp = new int[m + 1][n + 1];

        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++) {
                if (text1.charAt(i-1) == text2.charAt(j-1))
                    dp[i][j] = dp[i-1][j-1] + 1;
                else
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
            }
        return dp[m][n];
    }
}
```

**Complexity:** Time O(m×n) · Space O(m×n) → O(n) with rolling array

---

## Longest Increasing Subsequence (LIS)

**LeetCode 300** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/longest-increasing-subsequence/)

### Problem
Find the length of the longest strictly increasing subsequence.

### Approach 1 — DP O(n²)

- `dp[i]` = LIS ending at index i
- `dp[i] = max(dp[j] + 1)` for all j < i where `nums[j] < nums[i]`

### Approach 2 — Binary Search O(n log n) ✅

- Maintain `tails[]` array: `tails[i]` = smallest tail element of all IS of length i+1
- For each element, binary search for its position in tails

### Java Solution (Binary Search)

```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        List<Integer> tails = new ArrayList<>();
        for (int num : nums) {
            int pos = Collections.binarySearch(tails, num);
            if (pos < 0) pos = -(pos + 1); // insertion point
            if (pos == tails.size()) tails.add(num);
            else tails.set(pos, num);
        }
        return tails.size();
    }
}
```

**Complexity:** Time O(n log n) · Space O(n)

---

## Edit Distance

**LeetCode 72** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/edit-distance/)

### Problem
Minimum operations (insert, delete, replace) to convert word1 to word2.

### Approach

- `dp[i][j]` = min operations to convert `word1[0..i-1]` to `word2[0..j-1]`
- If chars match: `dp[i][j] = dp[i-1][j-1]`
- Else: `dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])`
  - `dp[i-1][j]` = delete from word1
  - `dp[i][j-1]` = insert into word1
  - `dp[i-1][j-1]` = replace

### Java Solution

```java
class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        int[][] dp = new int[m + 1][n + 1];

        for (int i = 0; i <= m; i++) dp[i][0] = i;
        for (int j = 0; j <= n; j++) dp[0][j] = j;

        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++) {
                if (word1.charAt(i-1) == word2.charAt(j-1))
                    dp[i][j] = dp[i-1][j-1];
                else
                    dp[i][j] = 1 + Math.min(dp[i-1][j-1],
                                   Math.min(dp[i-1][j], dp[i][j-1]));
            }
        return dp[m][n];
    }
}
```

**Complexity:** Time O(m×n) · Space O(m×n) → O(n) with rolling array

---

## Matrix Chain Multiplication

**Problem:** Find minimum multiplications to compute A₁ × A₂ × ... × Aₙ.

### Approach (Interval DP)

- `dp[i][j]` = min cost to multiply matrices from i to j
- Try every split point k: `dp[i][j] = min(dp[i][k] + dp[k+1][j] + dim[i-1]*dim[k]*dim[j])`

```java
public int matrixChainOrder(int[] dims) {
    int n = dims.length - 1; // number of matrices
    int[][] dp = new int[n][n]; // dp[i][j] = min cost for matrices i..j

    for (int len = 2; len <= n; len++) {
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            dp[i][j] = Integer.MAX_VALUE;
            for (int k = i; k < j; k++) {
                int cost = dp[i][k] + dp[k+1][j] + dims[i] * dims[k+1] * dims[j+1];
                dp[i][j] = Math.min(dp[i][j], cost);
            }
        }
    }
    return dp[0][n-1];
}
```

---

## 2D DP Summary

```
State          Meaning                     Recurrence
dp[i][j]       s1[0..i] and s2[0..j]      LCS, Edit Distance
dp[i][j]       grid[0..i][0..j]           Min/Max path in grid
dp[i][j]       interval [i..j]            Matrix chain, Palindrome partition
```

#sde-sheet #dynamic-programming #day27
