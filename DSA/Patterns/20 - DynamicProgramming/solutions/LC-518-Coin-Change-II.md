---
solved: false
difficulty: Medium
pattern: Dynamic Programming
lc_number: 518
date_solved: 
tags:
  - dsa
  - dynamic-programming
  - medium
---
# Coin Change II (LC 518)

**Difficulty**: Medium  
**Pattern**: Dynamic Programming (Unbounded Knapsack)  
**LeetCode**: https://leetcode.com/problems/coin-change-ii/

## Problem Statement
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.
Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
You may assume that you have an infinite number of each kind of coin.

**Example:**
```
Input: amount = 5, coins = [1,2,5]
Output: 4
```

## Approach: Bottom-Up DP (Combinations)

### Intuition
`dp[i]` = number of ways to make amount `i`.
Outer loop: For each `coin`
  Inner loop: For each `amount` from `coin` to `target`.
    `dp[amount] += dp[amount - coin]`.
Important: Loop order matters. Coins outer loop ensures we count combinations (order doesn't matter), not permutations.

### Java Code
```java
class Solution {
    public int change(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        dp[0] = 1;
        
        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                dp[i] += dp[i - coin];
            }
        }
        
        return dp[amount];
    }
}
```

### Complexity
- **Time**: O(Amount * Coins)
- **Space**: O(Amount)

## Key Takeaways
- Coin Change 2 is Counting ways vs Coin Change 1 Minimizing count
- Loop order ensures Combination vs Permutation
