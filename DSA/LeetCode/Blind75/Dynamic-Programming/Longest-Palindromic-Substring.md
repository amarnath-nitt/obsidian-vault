---
solved: false
difficulty: Medium
pattern: Dynamic Programming
lc_number: 5
tags:
  - dsa
  - dp
  - strings
  - medium
  - blind75
---
# Longest Palindromic Substring (LC 5)

**Difficulty:** Medium
**Category:** Dynamic Programming / Strings
**LeetCode:** https://leetcode.com/problems/longest-palindromic-substring/

---

## Problem Statement

Given a string `s`, return the longest palindromic substring in `s`.

**Example 1:**
```
Input: s = "babad"
Output: "bab"
```

**Example 2:**
```
Input: s = "cbbd"
Output: "bb"
```

---

## Approach 1: Brute Force

Check every substring — O(n³).

---

## Approach 2: Expand Around Center ✅

For each index, expand outward while characters match. Try both odd-length (single center) and even-length (two-char center).

### Java Code

```java
class Solution {
    private int start = 0, maxLen = 1;

    public String longestPalindrome(String s) {
        for (int i = 0; i < s.length(); i++) {
            expand(s, i, i);     // odd length
            expand(s, i, i + 1); // even length
        }
        return s.substring(start, start + maxLen);
    }

    private void expand(String s, int l, int r) {
        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
            l--; r++;
        }
        if (r - l - 1 > maxLen) {
            maxLen = r - l - 1;
            start = l + 1;
        }
    }
}
```

**Complexity:** Time O(n²) · Space O(1)

---

## Approach 3: DP

`dp[i][j]` = true if `s[i..j]` is a palindrome.
- Base: `dp[i][i] = true`, `dp[i][i+1] = (s[i] == s[i+1])`
- Transition: `dp[i][j] = (s[i] == s[j]) && dp[i+1][j-1]`

**Complexity:** Time O(n²) · Space O(n²)

---

## Key Takeaways

- Expand around center is the cleanest O(n²) O(1) solution
- There are `2n-1` centers (n single chars + n-1 between chars)
- Manacher's algorithm solves this in O(n) — rarely needed in interviews

---

## Related Problems

- [[Palindrome-Partitioning]] — partition into palindromes
- [[../SDE_Sheet/Day-15-Strings-I|Day 15 Strings I]] — same problem in SDE Sheet

---

#dp #strings #palindrome #medium #blind75
