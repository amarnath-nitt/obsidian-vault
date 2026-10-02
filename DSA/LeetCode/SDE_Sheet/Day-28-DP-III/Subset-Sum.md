# Subset Sum

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
