---
solved: true
difficulty: Medium
pattern: Two Pointers
lc_number: 11
date_solved: 
tags:
  - dsa
  - two-pointers
  - medium
---
# Container With Most Water (LC 11)

**Difficulty**: Medium  
**Pattern**: Two Pointers  
**LeetCode**: https://leetcode.com/problems/container-with-most-water/

## Problem Statement
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.
Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store.

**Example:**
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
```

## Approach: Two Pointers

### Intuition
Area = `width * min(height[left], height[right])`.
Start with maximum width (`left = 0`, `right = n-1`).
To maximize area, we want to keep the higher line and hope to find a taller line for the shorter side.
- If `height[left] < height[right]`, moving `right` in won't help (width decreases, height strictly limited by `height[left]`). So we MUST move `left` to potentially find a taller line.
- Vice versa.

### Java Code
```java
class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;
        
        while (left < right) {
            int h = Math.min(height[left], height[right]);
            int w = right - left;
            maxArea = Math.max(maxArea, h * w);
            
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        
        return maxArea;
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(1)

## Key Takeaways
- Greedy Two Pointers logic
- Always move the pointer of the shorter line
- Covers largest width first
