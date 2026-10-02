# Word Break

**LeetCode 139** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/word-break/)

### Problem
Can `s` be segmented into words from `wordDict`?

### Approach (DP)

- `dp[i]` = can `s[0..i-1]` be segmented?
- For each position `i`, check all substrings `s[j..i]` where `dp[j]` is true

### Java Solution

```java
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> dict = new HashSet<>(wordDict);
        int n = s.length();
        boolean[] dp = new boolean[n + 1];
        dp[0] = true;

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && dict.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }
}
```

**Complexity:** Time O(n³) (or O(n²) with trie) · Space O(n)

---
