# Decode Ways

**LeetCode 91** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/decode-ways/)

### Problem
String of digits, decode like 'A'=1...'Z'=26. Count ways to decode.

### Approach

- `dp[i]` = ways to decode `s[0..i-1]`
- Single digit: if `s[i-1] != '0'` → `dp[i] += dp[i-1]`
- Two digits: if `s[i-2..i-1]` is `10-26` → `dp[i] += dp[i-2]`

### Java Solution

```java
class Solution {
    public int numDecodings(String s) {
        int n = s.length();
        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = s.charAt(0) == '0' ? 0 : 1;

        for (int i = 2; i <= n; i++) {
            int oneDigit = s.charAt(i-1) - '0';
            int twoDigit = Integer.parseInt(s.substring(i-2, i));

            if (oneDigit >= 1) dp[i] += dp[i-1]; // valid single digit
            if (twoDigit >= 10 && twoDigit <= 26) dp[i] += dp[i-2]; // valid two digits
        }
        return dp[n];
    }
}
```

**Complexity:** Time O(n) · Space O(n) → O(1) with variables

---
