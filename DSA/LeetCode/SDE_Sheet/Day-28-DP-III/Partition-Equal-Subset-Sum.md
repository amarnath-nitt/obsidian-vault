# Partition Equal Subset Sum

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
