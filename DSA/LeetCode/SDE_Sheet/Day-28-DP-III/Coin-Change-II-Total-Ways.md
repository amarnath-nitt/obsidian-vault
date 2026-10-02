# Coin Change II (Total Ways)

**LeetCode 518** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/coin-change-ii/)

### Problem
Return the number of combinations that make up that amount. You may assume that you have an infinite number of each kind of coin.

### Approach
- Again, **unbounded knapsack** (infinite supply).
- **State:** `dp[w]` = number of ways to make sum `w`.
- **Transition:** `dp[w] += dp[w - coin]`
- **Traversal direction:** Forward from `coin` to `amount` to allow unbounded selection.

### Java Solution

```java
class Solution {
    public int change(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        dp[0] = 1;

        for (int coin : coins) {
            for (int w = coin; w <= amount; w++) {
                dp[w] += dp[w - coin];
            }
        }
        return dp[amount];
    }
}
```

**Complexity:** Time $O(N \times \text{amount})$ · Space $O(\text{amount})$

---
