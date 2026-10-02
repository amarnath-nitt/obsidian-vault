---
solved: false
difficulty: Hard
pattern: Dynamic Programming
lc_number: 72
date_solved: 
tags:
  - dsa
  - dynamic-programming
  - hard
---
# Edit Distance

[Problem Link](https://leetcode.com/problems/edit-distance/)

## Problem Statement
Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.
You have the following three operations permitted on a word:
1.  Insert a character
2.  Delete a character
3.  Replace a character

## Approach
2D DP.
`dp[i][j]` = min operations to convert `word1[0...i-1]` to `word2[0...j-1]`.
- If `word1[i-1] == word2[j-1]`: `dp[i][j] = dp[i-1][j-1]` (No op needed)
- Else: `dp[i][j] = 1 + min(insert, delete, replace)`
    - Insert: `dp[i][j-1]`
    - Delete: `dp[i-1][j]`
    - Replace: `dp[i-1][j-1]`

## Time and Space Complexity
- **Time Complexity:** O(M * N).
- **Space Complexity:** O(M * N).

## Code
```java
class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();
        
        int[][] dp = new int[m + 1][n + 1];
        
        // Base cases
        for (int i = 0; i <= m; i++) dp[i][0] = i; // Deletions
        for (int j = 0; j <= n; j++) dp[0][j] = j; // Insertions
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = 1 + Math.min(dp[i - 1][j - 1], // Replace
                                   Math.min(dp[i - 1][j],    // Delete
                                            dp[i][j - 1]));  // Insert
                }
            }
        }
        return dp[m][n];
    }
}
```
