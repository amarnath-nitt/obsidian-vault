# Decode Ways (LC 91)

**Difficulty**: Medium  
**Pattern**: Dynamic Programming  
**LeetCode**: https://leetcode.com/problems/decode-ways/

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the mapping 'A'->1, 'B'->2 ... 'Z'->26.
Given a string `s` containing only digits, return the number of ways to decode it.

**Example:**
```
Input: s = "226"
Output: 3 (BZ, VF, BBF)
```

## Approach: DP (Fibonacci Variant)

### Intuition
`dp[i]` = ways to decode `s[0...i-1]`.
Last digit can be 1 char: if `s[i-1] != '0'`, `dp[i] += dp[i-1]`.
Last two digits can be 1 char: if `s[i-2...i-1]` is between "10" and "26", `dp[i] += dp[i-2]`.
Base cases: `dp[0]=1`. `dp[1]=1` if valid.

### Java Code
```java
class Solution {
    public int numDecodings(String s) {
        if (s == null || s.length() == 0 || s.charAt(0) == '0') return 0;
        
        int n = s.length();
        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = 1;
        
        for (int i = 2; i <= n; i++) {
            int oneDigit = Integer.valueOf(s.substring(i - 1, i));
            int twoDigits = Integer.valueOf(s.substring(i - 2, i));
            
            if (oneDigit >= 1) {
                dp[i] += dp[i - 1];
            }
            
            if (twoDigits >= 10 && twoDigits <= 26) {
                dp[i] += dp[i - 2];
            }
        }
        
        return dp[n];
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(N)

## Key Takeaways
- Similar to Climbing Stairs but with validity conditions
