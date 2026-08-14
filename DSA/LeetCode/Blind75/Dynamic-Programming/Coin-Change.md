# Coin Change

**Difficulty:** Medium  
**Category:** Dynamic Programming  
**LeetCode Link:** [Coin Change](https://leetcode.com/problems/coin-change/)

---

## Problem Statement

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount cannot be made up by any combination of the coins, return `-1`.

---

## Approach: Bottom-Up DP

### Java Code
```java
class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;
        
        for (int amt = 1; amt <= amount; amt++) {
            for (int coin : coins) {
                if (amt >= coin) {
                    dp[amt] = Math.min(dp[amt], dp[amt - coin] + 1);
                }
            }
        }
        
        return dp[amount] > amount ? -1 : dp[amount];
    }
}
```

### Complexity
- **Time:** O(amount × coins)
- **Space:** O(amount)

---

## Tags
#dynamic-programming #medium #blind75
