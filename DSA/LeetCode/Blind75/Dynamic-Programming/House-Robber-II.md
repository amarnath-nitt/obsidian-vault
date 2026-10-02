# House Robber II

**Difficulty:** Medium
**Category:** Dynamic Programming
**LeetCode Link:** [House Robber II](https://leetcode.com/problems/house-robber-ii/)

---

## Problem Statement

Same as House Robber, but houses are arranged in a circle — the first and last house are adjacent. Return the maximum amount you can rob.

**Example:**
```
Input: nums = [2,3,2]
Output: 3  (can't rob both house 0 and house 2)
```

---

## Intuition

Since houses are circular, house 0 and house n-1 are adjacent — we can't rob both. Break the circle by running House Robber twice:
- Once on `nums[0..n-2]` (exclude last house)
- Once on `nums[1..n-1]` (exclude first house)

Take the maximum of both results.

---

## Approach: Two Passes of House Robber I

### Algorithm
1. If only one house, return `nums[0]`
2. Run `robRange(nums, 0, n-2)` — skip last house
3. Run `robRange(nums, 1, n-1)` — skip first house
4. Return `max` of both

### Java Code
```java
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0];

        return Math.max(
            robRange(nums, 0, nums.length - 2),
            robRange(nums, 1, nums.length - 1)
        );
    }

    private int robRange(int[] nums, int start, int end) {
        int prev2 = 0, prev1 = 0;

        for (int i = start; i <= end; i++) {
            int current = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) — two linear passes
- **Space Complexity:** O(1)

---

## Key Takeaways

1. **Circular constraint:** First and last house can't both be robbed
2. **Break the circle:** Two separate linear passes, each excluding one endpoint
3. **Reuse:** robRange is exactly House Robber I logic

---

## Tags
#dynamic-programming #medium #blind75
