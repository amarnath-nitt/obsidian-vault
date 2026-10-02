---
solved: false
difficulty: Medium
pattern: Dynamic Programming
lc_number: 322
date_solved: 
tags:
  - dsa
  - dynamic-programming
  - medium
---
# Coin Change (LC 322)

**Difficulty**: Medium  
**Pattern**: Dynamic Programming (Unbounded Knapsack)  
**LeetCode**: https://leetcode.com/problems/coin-change/

## Problem Statement
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.
You may assume that you have an infinite number of each kind of coin.

**Example:**
```
Input: coins = [1,2,5], amount = 11
Output: 3 (11 = 5 + 5 + 1)
```

## Approach: Bottom-Up DP

### Intuition
`dp[i]` = min coins to make amount `i`.
Transition: `dp[i] = min(dp[i], dp[i - coin] + 1)` for each coin.
Base case: `dp[0] = 0`. Initialize others to `amount + 1` (infinity).

### Java Code
```java
class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;
        
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (i >= coin) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }
        
        return dp[amount] > amount ? -1 : dp[amount];
    }
}
```

### Complexity
- **Time**: O(Amount * Coins)
- **Space**: O(Amount)

## Key Takeaways
- Classic Unbounded Knapsack variation (Minimization)
- Initialize DP array with value > max possible answer
