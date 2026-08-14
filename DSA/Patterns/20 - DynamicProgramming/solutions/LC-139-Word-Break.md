# Word Break (LC 139)

**Difficulty**: Medium  
**Pattern**: Dynamic Programming  
**LeetCode**: https://leetcode.com/problems/word-break/

## Problem Statement
Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words. Note that the same word in the dictionary may be reused multiple times in the segmentation.

**Example:**
```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
```

## Approach: Bottom-Up DP

### Intuition
`dp[i]` = true if `s[0...i-1]` is valid segmentation.
`dp[i] = true` if exists `j < i` such that `dp[j]` is true AND `s[j...i-1]` is in dictionary.
Base case: `dp[0] = true` (empty string).

### Java Code
```java
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        
        for (int i = 1; i <= s.length(); i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && wordSet.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        
        return dp[s.length()];
    }
}
```

### Complexity
- **Time**: O(N^2 * M) if substring and hashing takes time. O(N^2) effectively.
- **Space**: O(N)

## Key Takeaways
- Splitting string problem usually recursive or DP
- Using Set for O(1) word lookup
