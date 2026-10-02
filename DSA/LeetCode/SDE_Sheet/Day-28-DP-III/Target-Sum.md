# Target Sum

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
