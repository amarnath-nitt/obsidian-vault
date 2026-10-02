# House Robber II (Circular)

**LeetCode 213** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/house-robber-ii/)

### Problem
Houses arranged in a circle — first and last are adjacent.

### Approach

- Can't rob both first and last
- **Case 1:** Rob from `nums[0..n-2]` (exclude last)
- **Case 2:** Rob from `nums[1..n-1]` (exclude first)
- Take max of both cases

### Java Solution

```java
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];
        return Math.max(
            robRange(nums, 0, n - 2),
            robRange(nums, 1, n - 1)
        );
    }

    private int robRange(int[] nums, int l, int r) {
        int prev2 = 0, prev1 = 0;
        for (int i = l; i <= r; i++) {
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
