# Palindrome Partitioning II (Min Cuts)

**LeetCode 132** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/palindrome-partitioning-ii/)

### Problem
Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return the minimum cuts needed for a palindrome partitioning of `s`.

### Approach
1. **Precompute Palindromes:** Create a boolean table `isPal[i][j]` representing if `s[i..j]` is a palindrome.
2. **DP for Min Cuts:** Let `cuts[i]` be the minimum cuts needed for `s[0..i]`.
   - If `s[0..i]` is a palindrome, `cuts[i] = 0`.
   - Else, `cuts[i] = min(cuts[j] + 1)` for all `j < i` where `s[j+1..i]` is a palindrome.

### Java Solution

```java
class Solution {
    public int minCut(String s) {
        int n = s.length();
        boolean[][] isPal = new boolean[n][n];
        int[] cuts = new int[n];

        for (int i = 0; i < n; i++) {
            int minCuts = i;
            for (int j = 0; j <= i; j++) {
                if (s.charAt(i) == s.charAt(j) && (i - j < 2 || isPal[j + 1][i - 1])) {
                    isPal[j][i] = true;
                    minCuts = (j == 0) ? 0 : Math.min(minCuts, cuts[j - 1] + 1);
                }
            }
            cuts[i] = minCuts;
        }
        return cuts[n - 1];
    }
}
```

**Complexity:** Time $O(N^2)$ · Space $O(N^2)$

---
