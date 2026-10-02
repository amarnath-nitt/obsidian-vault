# Rod Cutting

**Problem:** Given a rod of length $N$ inches and an array of prices that includes prices of all pieces of size smaller than $N$. Determine the maximum value obtainable by cutting up the rod and selling the pieces.

### Approach
- This is equivalent to **Unbounded Knapsack**.
- **State:** `dp[i]` = maximum value obtainable for a rod of length `i`.
- **Transition:** `dp[i] = max(prices[j] + dp[i - (j + 1)])` for all $0 \le j < i$.

### Java Solution

```java
public class RodCutting {
    public static int cutRod(int[] prices, int n) {
        int[] dp = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            int maxVal = Integer.MIN_VALUE;
            for (int j = 0; j < i; j++) {
                maxVal = Math.max(maxVal, prices[j] + dp[i - j - 1]);
            }
            dp[i] = maxVal;
        }
        return dp[n];
    }
}
```

**Complexity:** Time $O(N^2)$ · Space $O(N)$

---
