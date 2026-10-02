# Longest Palindromic Substring

**LeetCode 5** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/longest-palindromic-substring/)

### Approach (Expand Around Center)

- For each center position (2n-1 centers including between chars)
- Expand outward while characters match
- Track max length palindrome

### Java Solution

```java
class Solution {
    String result = "";

    public String longestPalindrome(String s) {
        for (int i = 0; i < s.length(); i++) {
            expand(s, i, i);     // odd length
            expand(s, i, i + 1); // even length
        }
        return result;
    }

    private void expand(String s, int l, int r) {
        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
            l--; r++;
        }
        // [l+1, r-1] is the palindrome
        if (r - l - 1 > result.length())
            result = s.substring(l + 1, r);
    }
}
```

**Complexity:** Time O(n²) · Space O(1)

> **Manacher's Algorithm** solves this in O(n) — complex but worth knowing.

---
