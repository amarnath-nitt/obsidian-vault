# Word Break

**LeetCode 139** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/word-break/)

### Problem
Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

### Approach
- **State:** `dp[i]` = true if `s[0..i-1]` can be segmented.
- **Transition:** `dp[i] = true` if there exists `j < i` such that `dp[j] == true` AND `s[j..i-1]` is in the dictionary.

### Java Solution

```java
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> set = new HashSet<>(wordDict);
        int n = s.length();
        boolean[] dp = new boolean[n + 1];
        dp[0] = true; // empty string is always matchable

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && set.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break; // found valid partition
                }
            }
        }
        return dp[n];
    }
}
```

**Complexity:** Time $O(N^2 \times L)$ (where $L$ is max word length in dict) · Space $O(N + D)$ (where $D$ is size of dict)

---
