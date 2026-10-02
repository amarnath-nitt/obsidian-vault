# House Robber

**LeetCode 198** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/house-robber/)

### Problem
Rob houses in a row, cannot rob two adjacent. Maximize money.

### Approach

- `dp[i]` = max money from first i houses
- `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`

### Java Solution

```java
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];
        int prev2 = nums[0], prev1 = Math.max(nums[0], nums[1]);
        for (int i = 2; i < n; i++) {
            int curr = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---
