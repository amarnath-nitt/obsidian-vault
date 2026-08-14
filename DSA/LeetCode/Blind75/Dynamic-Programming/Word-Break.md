# Word Break

**Difficulty:** Medium  
**Category:** Dynamic Programming  
**LeetCode Link:** [Word Break](https://leetcode.com/problems/word-break/)

---

## Approach: DP

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
- **Time:** O(n² × m) where m = avg word length
- **Space:** O(n)

---

## Tags
#dynamic-programming #medium #blind75
