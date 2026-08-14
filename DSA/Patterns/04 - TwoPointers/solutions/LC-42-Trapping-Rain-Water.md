# Trapping Rain Water (LC 42)

**Difficulty**: Hard  
**Pattern**: Two Pointers / Dynamic Programming  
**LeetCode**: https://leetcode.com/problems/trapping-rain-water/

## Problem Statement
Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

**Example:**
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

## Approach 1: DP (Prefix Max / Suffix Max)

### Intuition
For any bar `i`, water trapped = `min(max_left[i], max_right[i]) - height[i]`.
Precompute `max_left` and `max_right` arrays.

## Approach 2: Two Pointers (Optimized)

### Intuition
We don't need to store all prefix/suffix maxes. We just need `min(left_max, right_max)`.
Maintain `left` and `right` pointers and `left_max`, `right_max` variables.
- If `height[left] < height[right]`, then `left_max` determines the water level for `left` (because even if right side has huge wall, `left_max` is the bottleneck).
- Update and move the smaller pointer.

### Java Code
```java
class Solution {
    public int trap(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int leftMax = 0;
        int rightMax = 0;
        int water = 0;
        
        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= leftMax) {
                    leftMax = height[left];
                } else {
                    water += leftMax - height[left];
                }
                left++;
            } else {
                if (height[right] >= rightMax) {
                    rightMax = height[right];
                } else {
                    water += rightMax - height[right];
                }
                right--;
            }
        }
        
        return water;
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(1)

## Key Takeaways
- Two pointers can optimize space from O(n) to O(1)
- Bottleneck logic similar to Container With Most Water
