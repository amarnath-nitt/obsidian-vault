# Climbing Stairs

**LeetCode 70** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/climbing-stairs/)

### Problem
n stairs, can climb 1 or 2 steps. How many ways to reach top?

### Approach

- `dp[i]` = ways to reach stair i = `dp[i-1] + dp[i-2]` (Fibonacci!)

### Java Solution

```java
class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;
        int a = 1, b = 2;
        for (int i = 3; i <= n; i++) {
            int c = a + b;
            a = b; b = c;
        }
        return b;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---
