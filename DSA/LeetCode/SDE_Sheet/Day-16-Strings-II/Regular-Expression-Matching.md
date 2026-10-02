# Regular Expression Matching

**LeetCode 10** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/regular-expression-matching/)

### Problem
`.` matches any single char. `*` matches zero or more of the preceding element.

### Approach (DP)

- `dp[i][j]` = does `s[0..i-1]` match `p[0..j-1]`?
- If `p[j-1] == '*'`:
  - Zero of preceding: `dp[i][j] = dp[i][j-2]`
  - One or more of preceding: `dp[i][j] |= dp[i-1][j]` if `s[i-1]` matches `p[j-2]`

### Java Solution

```java
class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();
        boolean[][] dp = new boolean[m + 1][n + 1];
        dp[0][0] = true;

        for (int j = 2; j <= n; j++)
            if (p.charAt(j-1) == '*') dp[0][j] = dp[0][j-2];

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p.charAt(j-1) == '*') {
                    dp[i][j] = dp[i][j-2]; // zero occurrences
                    if (p.charAt(j-2) == '.' || p.charAt(j-2) == s.charAt(i-1))
                        dp[i][j] |= dp[i-1][j]; // one or more occurrences
                } else if (p.charAt(j-1) == '.' || p.charAt(j-1) == s.charAt(i-1)) {
                    dp[i][j] = dp[i-1][j-1];
                }
            }
        }
        return dp[m][n];
    }
}
```

**Complexity:** Time O(m×n) · Space O(m×n)

---
