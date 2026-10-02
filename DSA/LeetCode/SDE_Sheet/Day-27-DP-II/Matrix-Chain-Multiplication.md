# Matrix Chain Multiplication

**Problem:** Find minimum multiplications to compute A₁ × A₂ × ... × Aₙ.

### Approach (Interval DP)

- `dp[i][j]` = min cost to multiply matrices from i to j
- Try every split point k: `dp[i][j] = min(dp[i][k] + dp[k+1][j] + dim[i-1]*dim[k]*dim[j])`

```java
public int matrixChainOrder(int[] dims) {
    int n = dims.length - 1; // number of matrices
    int[][] dp = new int[n][n]; // dp[i][j] = min cost for matrices i..j

    for (int len = 2; len <= n; len++) {
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            dp[i][j] = Integer.MAX_VALUE;
            for (int k = i; k < j; k++) {
                int cost = dp[i][k] + dp[k+1][j] + dims[i] * dims[k+1] * dims[j+1];
                dp[i][j] = Math.min(dp[i][j], cost);
            }
        }
    }
    return dp[0][n-1];
}
```

---
