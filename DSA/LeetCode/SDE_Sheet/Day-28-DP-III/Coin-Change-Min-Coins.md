# Coin Change (Min Coins)

**LeetCode 322** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/coin-change/)

### Problem
Given an integer array `coins` representing coins of different denominations and an integer `amount`, return the fewest number of coins that you need to make up that amount. If that amount cannot be made up, return `-1`.

### Approach
- This is an **unbounded knapsack** variant because you can reuse coins infinitely.
- **State:** `dp[w]` = minimum coins to make sum `w`.
- **Transition:** `dp[w] = min(dp[w], 1 + dp[w - coin])` for each coin.
- **Traversal direction:** Iterate `w` from `coin` up to `amount` (forward iteration allows multiple selections of the same coin).

### Java Solution

```java
class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;

        for (int coin : coins) {
            for (int w = coin; w <= amount; w++) {
                dp[w] = Math.min(dp[w], 1 + dp[w - coin]);
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
}
```

**Complexity:** Time $O(N \times \text{amount})$ · Space $O(\text{amount})$

---
