# Coin Change

**Difficulty:** Medium
**Category:** Dynamic Programming
**LeetCode Link:** [Coin Change](https://leetcode.com/problems/coin-change/)

---

## Problem Statement

Given coins of different denominations and an `amount`, return the fewest number of coins needed to make up that amount. Return `-1` if it's not possible.

**Example:**
```
Input: coins = [1,5,11], amount = 15
Output: 3  (5+5+5)
```

---

## Intuition

For each amount from 1 to target, the minimum coins needed = 1 + minimum coins needed for `(amount - coin)` for each valid coin. This is a classic unbounded knapsack / bottom-up DP problem.

---

## Approach 1: Brute Force Recursion

### Algorithm
Try every coin at each step recursively. Exponential — many repeated subproblems.

### Complexity Analysis
- **Time Complexity:** O(amount^coins) — exponential
- **Space Complexity:** O(amount) — recursion stack

---

## Approach 2: Bottom-Up DP (Optimized)

### Algorithm
1. Create `dp[0..amount]`, initialize all to `amount + 1` (infinity)
2. Base case: `dp[0] = 0`
3. For each amount from 1 to target, try every coin: `dp[amt] = min(dp[amt], dp[amt - coin] + 1)`
4. Return `dp[amount]` if reachable, else `-1`

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

### Step-by-Step Example
`coins = [1,5,11], amount = 15`:
```
dp[0]=0
dp[1]=1  (1)
dp[5]=1  (5)
dp[10]=2 (5+5)
dp[11]=1 (11)
dp[15]=3 (5+5+5)
```

### Complexity Analysis
- **Time Complexity:** O(amount × coins)
- **Space Complexity:** O(amount)

---

## Key Takeaways

1. **Pattern:** Unbounded knapsack — each coin can be used multiple times
2. **Init with infinity:** `amount + 1` acts as infinity (max coins needed ≤ amount)
3. **Build bottom-up:** Each subproblem depends only on smaller amounts

---

## Tags
#dynamic-programming #medium #blind75
