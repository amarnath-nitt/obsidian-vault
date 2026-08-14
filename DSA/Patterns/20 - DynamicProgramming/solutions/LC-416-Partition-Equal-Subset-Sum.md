# Partition Equal Subset Sum (LC 416)

**Difficulty**: Medium  
**Pattern**: Dynamic Programming / Knapsack  
**LeetCode**: https://leetcode.com/problems/partition-equal-subset-sum/

## Problem Statement
Given an integer array `nums`, return `true` if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or `false` otherwise.

**Example:**
```
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

## Approach: 0/1 Knapsack DP

### Intuition
Total sum `S`. We need to find if there is a subset with sum `S / 2`.
If `S` is odd, return false.
Target `K = S / 2`.
`dp[i]` = boolean, true if sum `i` can be formed.
Iterate through numbers, update `dp` array backwards (to avoid using same number twice).

### Java Code
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
            for (int i = target; i >= num; i--) {
                dp[i] = dp[i] || dp[i - num];
            }
        }
        
        return dp[target];
    }
}
```

### Complexity
- **Time**: O(N * Sum)
- **Space**: O(Sum)

## Key Takeaways
- Reduced to Subset Sum problem
- 1D DP optimization for Knapsack
- Iterating backwards is crucial for 1D array
