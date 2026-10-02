# Wildcard Matching

**LeetCode 44** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/wildcard-matching/)

### Problem
`?` matches any single character. `*` matches any sequence (including empty).

### Approach (DP)

- `dp[i][j]` = does `s[0..i-1]` match `p[0..j-1]`?
- If `p[j-1] == '*'`: `dp[i][j] = dp[i][j-1]` (empty) OR `dp[i-1][j]` (match one more char)
- If `p[j-1] == '?' || p[j-1] == s[i-1]`: `dp[i][j] = dp[i-1][j-1]`

### Java Solution

```java
class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();
        boolean[][] dp = new boolean[m + 1][n + 1];
        dp[0][0] = true;

        // '*' can match empty string
        for (int j = 1; j <= n; j++)
            if (p.charAt(j-1) == '*') dp[0][j] = dp[0][j-1];

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p.charAt(j-1) == '*') {
                    dp[i][j] = dp[i][j-1] || dp[i-1][j]; // empty or match one
                } else if (p.charAt(j-1) == '?' || p.charAt(j-1) == s.charAt(i-1)) {
                    dp[i][j] = dp[i-1][j-1];
                }
            }
        }
        return dp[m][n];
    }
}
```

**Complexity:** Time O(m×n) · Space O(m×n) → optimizable to O(n)

---
