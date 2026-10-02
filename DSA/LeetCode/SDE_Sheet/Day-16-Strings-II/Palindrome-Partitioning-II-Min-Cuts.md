# Palindrome Partitioning II (Min Cuts)

**LeetCode 132** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/palindrome-partitioning-ii/)

### Problem
Find the minimum number of cuts to partition string into palindromes.

### Approach (DP)

- `dp[i]` = min cuts for `s[0..i]`
- For each `i`, expand from every center to find palindromes
- If `s[j..i]` is palindrome: `dp[i] = min(dp[i], dp[j-1] + 1)`

### Java Solution

```java
class Solution {
    public int minCut(String s) {
        int n = s.length();
        boolean[][] isPalin = new boolean[n][n];
        int[] dp = new int[n];

        // Precompute palindromes
        for (int i = 0; i < n; i++) {
            Arrays.fill(isPalin[i], false);
            dp[i] = i; // max cuts = i (cut every character)
        }

        for (int center = 0; center < 2 * n - 1; center++) {
            int l = center / 2, r = l + center % 2;
            while (l >= 0 && r < n && s.charAt(l) == s.charAt(r)) {
                isPalin[l][r] = true;
                if (l == 0) dp[r] = 0;
                else dp[r] = Math.min(dp[r], dp[l-1] + 1);
                l--; r++;
            }
        }
        return dp[n - 1];
    }
}
```

**Complexity:** Time O(n²) · Space O(n²)

---
