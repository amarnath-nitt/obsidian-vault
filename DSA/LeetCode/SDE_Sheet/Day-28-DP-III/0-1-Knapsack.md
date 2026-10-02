# 0/1 Knapsack

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
