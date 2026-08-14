# Day 28 — Dynamic Programming III (Knapsack Variants)

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** DP — Knapsack, Subsets, Coin Change
**Difficulty Mix:** Medium

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#0/1 Knapsack]] | — | Medium | ⬜ |
| 2 | [[#Subset Sum]] | — | Medium | ⬜ |
| 3 | [[#Partition Equal Subset Sum]] | 416 | Medium | ⬜ |
| 4 | [[#Coin Change (Min Coins)]] | 322 | Medium | ⬜ |
| 5 | [[#Coin Change II (Total Ways)]] | 518 | Medium | ⬜ |
| 6 | [[#Target Sum]] | 494 | Medium | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| 0/1 Knapsack | Include/exclude every item. O(2^n). | 2D DP by item and capacity. O(n*W). | 1D DP over capacity in reverse. O(W) space. |
| Subset Sum | Enumerate all subsets. O(2^n). | 2D boolean DP. O(n*sum). | 1D boolean DP in reverse. O(sum) space. |
| Partition Equal Subset Sum | Enumerate subsets and check half sum. O(2^n). | Reduce to subset sum target total/2. | 1D DP or bitset subset-sum. O(sum) space. |
| Coin Change (Min Coins) | Try all coin combinations recursively. Exponential. | Memoized recursion by amount. | Bottom-up 1D DP for min coins. O(amount*coins). |
| Coin Change II (Total Ways) | Recursively count all combinations. Exponential. | 2D DP by coin index and amount. | 1D combinations DP with coins as outer loop. |
| Target Sum | Assign plus/minus to every number. O(2^n). | Memoize index and current sum. | Transform to subset-count DP. O(n*target). |

---

## 0/1 Knapsack

**Problem:** Given weights and values of $N$ items, put these items in a knapsack of capacity $W$ to get the maximum total value.

### Approach

1. **State:** `dp[i][w]` = max value choosing from first `i` items with capacity `w`.
2. **Transitions:**
   - **Exclude:** `dp[i][w] = dp[i-1][w]`
   - **Include:** If `weight[i-1] <= w`, `dp[i][w] = max(dp[i-1][w], val[i-1] + dp[i-1][w-weight[i-1]])`
3. **Space Optimization:** Since `dp[i]` only depends on `dp[i-1]`, we can use a single array of size `W + 1` and update it **backwards** (from $W$ down to 0) to avoid using updated values from the current row.

### Java Solution (Space Optimized)

```java
public class Knapsack {
    public static int knapsack(int[] weights, int[] values, int n, int W) {
        int[] dp = new int[W + 1];

        for (int i = 0; i < n; i++) {
            for (int w = W; w >= weights[i]; w--) {
                dp[w] = Math.max(dp[w], values[i] + dp[w - weights[i]]);
            }
        }
        return dp[W];
    }
}
```

**Complexity:** Time $O(N \times W)$ · Space $O(W)$

---

## Subset Sum

**Problem:** Given an array of non-negative integers and a target sum, determine if there is a subset whose sum equals the target.

### Approach

1. **State:** `dp[w]` = boolean, whether sum `w` is possible.
2. **Transition:**
   - Initialize `dp[0] = true`, all others `false`.
   - For each number `num` in the array, iterate `w` from `target` down to `num`:
     `dp[w] = dp[w] || dp[w - num]`

### Java Solution (Space Optimized)

```java
public class SubsetSum {
    public static boolean isSubsetSum(int[] arr, int target) {
        int n = arr.length;
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;

        for (int num : arr) {
            for (int w = target; w >= num; w--) {
                if (dp[w - num]) {
                    dp[w] = true;
                }
            }
        }
        return dp[target];
    }
}
```

**Complexity:** Time $O(N \times \text{target})$ · Space $O(\text{target})$

---

## Partition Equal Subset Sum

**LeetCode 416** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/partition-equal-subset-sum/)

### Problem
Determine if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

### Approach
- A partition is only possible if the total sum of the array is **even**.
- If even, the problem reduces to finding if there exists a subset with sum equal to `totalSum / 2` (exactly the Subset Sum problem).

### Java Solution

```java
class Solution {
    public boolean canPartition(int[] nums) {
        int sum = 0;
        for (int num : nums) sum += num;
        if (sum % 2 != 0) return false;
        
        int target = sum / 2;
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;

        for (int num : nums) {
            for (int w = target; w >= num; w--) {
                if (dp[w - num]) {
                    dp[w] = true;
                }
            }
        }
        return dp[target];
    }
}
```

**Complexity:** Time $O(N \times \text{target})$ · Space $O(\text{target})$ where $\text{target} = \text{Sum}/2$

---

## Coin Change (Min Coins)

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

## Coin Change II (Total Ways)

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

## Target Sum

**LeetCode 494** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/target-sum/)

### Problem
Assign `+` or `-` sign to each element in `nums` to build an expression that evaluates to `target`. Return the number of different expressions.

### Approach
- Let the sum of positive elements be $S_1$ and negative elements be $S_2$.
- $S_1 - S_2 = \text{target}$
- $S_1 + S_2 = \text{totalSum}$
- Adding both equations: $2 \times S_1 = \text{totalSum} + \text{target} \implies S_1 = (\text{totalSum} + \text{target}) / 2$
- The problem is reduced to finding the number of subsets with sum $S_1$.
- **Edge cases:** If `totalSum + target` is negative or odd, return 0. Handle zeros in the input correctly by initializing the DP base case carefully or scaling.

### Java Solution

```java
class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int totalSum = 0;
        for (int num : nums) totalSum += num;
        
        if (totalSum < Math.abs(target) || (totalSum + target) % 2 != 0) {
            return 0;
        }
        
        int subsetSum = (totalSum + target) / 2;
        int[] dp = new int[subsetSum + 1];
        dp[0] = 1;

        for (int num : nums) {
            for (int w = subsetSum; w >= num; w--) {
                dp[w] += dp[w - num];
            }
        }
        return dp[subsetSum];
    }
}
```

**Complexity:** Time $O(N \times \text{subsetSum})$ · Space $O(\text{subsetSum})$

---

## Knapsack Decision Tree

```
                      Knapsack Problems
                             |
         -----------------------------------------
        |                                         |
   Bounded (0/1)                              Unbounded
(Use each item max 1 time)               (Use each item inf times)
  - Backwards iteration                    - Forwards iteration
  - `w` from `W` down to `cost`            - `w` from `cost` up to `W`
  - Examples: 0/1 Knapsack,                 - Examples: Coin Change I/II,
    Subset Sum, Target Sum                   Rod Cutting
```

#sde-sheet #dynamic-programming #day28
