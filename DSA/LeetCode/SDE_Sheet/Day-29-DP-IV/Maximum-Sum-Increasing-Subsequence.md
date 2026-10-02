# Maximum Sum Increasing Subsequence

**Problem:** Given an array of $N$ positive integers, find the maximum sum increasing subsequence of the given array.

### Approach
- Variation of LIS (Longest Increasing Subsequence).
- **State:** `dp[i]` = maximum sum of an increasing subsequence ending at index `i`.
- **Transition:** `dp[i] = nums[i] + max(dp[j])` for all `j < i` where `nums[j] < nums[i]`. Initialize `dp[i] = nums[i]`.
- **Result:** Max element in `dp`.

### Java Solution

```java
public class MaxSumIS {
    public static int maxSumIS(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        int maxSum = 0;

        for (int i = 0; i < n; i++) {
            dp[i] = nums[i];
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + nums[i]);
                }
            }
            maxSum = Math.max(maxSum, dp[i]);
        }
        return maxSum;
    }
}
```

**Complexity:** Time $O(N^2)$ · Space $O(N)$

---
