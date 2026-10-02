# Trapping Rain Water

**LeetCode 42** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/trapping-rain-water/)

### Problem
Given an elevation map, compute how much water can be trapped.

### Approach 1 — Prefix Max Arrays O(n) time, O(n) space

- `leftMax[i]` = max height from left up to i
- `rightMax[i]` = max height from right up to i
- Water at i = `min(leftMax[i], rightMax[i]) - height[i]`

### Approach 2 — Two Pointers O(n) time, O(1) space ?

- If `leftMax < rightMax` → process left pointer (it's the bottleneck)
- Else → process right pointer

### Java Solution (Two Pointers)

```java
class Solution {
    public int trap(int[] height) {
        int left = 0, right = height.length - 1;
        int leftMax = 0, rightMax = 0, water = 0;

        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= leftMax) leftMax = height[left];
                else water += leftMax - height[left];
                left++;
            } else {
                if (height[right] >= rightMax) rightMax = height[right];
                else water += rightMax - height[right];
                right--;
            }
        }
        return water;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---
