# Longest Common Subsequence (LC 1143)

**Difficulty**: Medium  
**Pattern**: Dynamic Programming  
**LeetCode**: https://leetcode.com/problems/longest-common-subsequence/

## Problem Statement
Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return 0.

**Example:**
```
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
```

## Approach: 2D Dynamic Programming

### Intuition
`dp[i][j]` = length of LCS of `text1[0...i-1]` and `text2[0...j-1]`.
If `text1[i-1] == text2[j-1]`, we can extend the LCS found so far: `dp[i][j] = 1 + dp[i-1][j-1]`.
Else, we take the max of excluding current char from either string: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

### Java Code
```java
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length();
        int n = text2.length();
        int[][] dp = new int[m + 1][n + 1];
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        
        return dp[m][n];
    }
}
```

### Complexity
- **Time**: O(m * n)
- **Space**: O(m * n)

## Key Takeaways
- Classic 2D DP pattern for string comparison
- Relies on optimal substructure
- Can optimize space to O(min(m, n)) using only previous row
