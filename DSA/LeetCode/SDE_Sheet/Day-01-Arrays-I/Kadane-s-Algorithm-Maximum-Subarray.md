# Kadane's Algorithm — Maximum Subarray

**LeetCode 53** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/maximum-subarray/)

### Problem
Find the contiguous subarray with the largest sum.

### Approach

**Key insight:** At each position, decide:
- Extend the existing subarray: `currentSum + nums[i]`
- Start fresh: `nums[i]`
→ Take the maximum of both

Reset `currentSum` to 0 whenever it goes negative.

### Java Solution

```java
class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        int currentSum = 0;

        for (int num : nums) {
            currentSum += num;
            maxSum = Math.max(maxSum, currentSum);
            if (currentSum < 0) currentSum = 0;
        }
        return maxSum;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

> **Follow-up:** Print the actual subarray → track `start`, `end`, `tempStart` indices.

---
