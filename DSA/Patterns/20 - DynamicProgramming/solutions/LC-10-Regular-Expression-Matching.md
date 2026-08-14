# Regular Expression Matching

[Problem Link](https://leetcode.com/problems/regular-expression-matching/)

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for `.` and `*` where:
- `.` Matches any single character.
- `*` Matches zero or more of the preceding element.
The matching should cover the **entire** input string (not partial).

## Approach
2D DP.
`dp[i][j]` = does `s[0...i-1]` match `p[0...j-1]`?
- If `p[j-1]` is normal char or `.`: match `s[i-1]` with `p[j-1]` and take `dp[i-1][j-1]`.
- If `p[j-1]` is `*`:
    - Zero occurrences of `p[j-2]`: take `dp[i][j-2]`.
    - One or more occurrences: matches `s[i-1]` with `p[j-2]` AND take `dp[i-1][j]`.

## Time and Space Complexity
- **Time Complexity:** O(M * N).
- **Space Complexity:** O(M * N).

## Code
```java
class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length();
        int n = p.length();
        boolean[][] dp = new boolean[m + 1][n + 1];
        
        dp[0][0] = true;
        
        // Handle patterns like a*, a*b*, etc. for empty string
        for (int j = 1; j <= n; j++) {
            if (p.charAt(j - 1) == '*') {
                dp[0][j] = dp[0][j - 2];
            }
        }
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p.charAt(j - 1) == '.' || p.charAt(j - 1) == s.charAt(i - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else if (p.charAt(j - 1) == '*') {
                    // Zero occurrences
                    dp[i][j] = dp[i][j - 2];
                    
                    // One or more occurrences
                    if (p.charAt(j - 2) == '.' || p.charAt(j - 2) == s.charAt(i - 1)) {
                        dp[i][j] = dp[i][j] || dp[i - 1][j];
                    }
                }
            }
        }
        
        return dp[m][n];
    }
}
```
