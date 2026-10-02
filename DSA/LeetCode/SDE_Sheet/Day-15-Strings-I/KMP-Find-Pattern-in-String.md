# KMP — Find Pattern in String

**LeetCode 28** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

### Problem
Find first occurrence of `needle` in `haystack`.

### Approach (KMP Algorithm)

**Phase 1: Build LPS (Longest Proper Prefix which is also Suffix) array**
- `lps[i]` = length of longest proper prefix of `pattern[0..i]` that is also a suffix

**Phase 2: Search using LPS**
- On mismatch: jump using `lps[j-1]` instead of restarting from beginning

### Java Solution

```java
class Solution {
    public int strStr(String haystack, String needle) {
        int n = haystack.length(), m = needle.length();
        if (m == 0) return 0;

        // Build LPS
        int[] lps = new int[m];
        for (int i = 1, len = 0; i < m; ) {
            if (needle.charAt(i) == needle.charAt(len)) lps[i++] = ++len;
            else if (len > 0) len = lps[len - 1];
            else lps[i++] = 0;
        }

        // Search
        for (int i = 0, j = 0; i < n; ) {
            if (haystack.charAt(i) == needle.charAt(j)) { i++; j++; }
            if (j == m) return i - j;
            else if (i < n && haystack.charAt(i) != needle.charAt(j)) {
                if (j > 0) j = lps[j - 1];
                else i++;
            }
        }
        return -1;
    }
}
```

**Complexity:** Time O(n+m) · Space O(m)

---
