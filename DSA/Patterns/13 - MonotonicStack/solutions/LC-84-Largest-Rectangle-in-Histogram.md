---
solved: false
difficulty: Hard
pattern: Monotonic Stack
lc_number: 84
date_solved: 
tags:
  - dsa
  - monotonic-stack
  - hard
---
# Largest Rectangle in Histogram (LC 84)

**Difficulty**: Hard  
**Pattern**: Monotonic Stack  
**LeetCode**: https://leetcode.com/problems/largest-rectangle-in-histogram/

## Problem Statement
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

**Example:**
```
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The largest rectangle is shown in the red area, which has an area = 10 units. (bars 5 and 6)
```

## Approach 1: Monotonic Stack

### Intuition
For each bar `h`, if we know the first bar to the left that is shorter (`left_limit`) and the first bar to the right that is shorter (`right_limit`), then the width of the rectangle with height `h` is `right_limit - left_limit - 1`.
We can find next smaller element (NSE) and previous smaller element (PSE) using a monotonic increasing stack.

### Java Code
```java
class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length;
        Stack<Integer> stack = new Stack<>();
        int maxArea = 0;
        
        // We can process "NSE" logic. When we pop an element, the current element 'i' is the Right Boundary (exclusive).
        // The element remaining on stack after popping is the Left Boundary (exclusive).
        
        for (int i = 0; i <= n; i++) {
            // Use 0 height for virtual bar at end to flush stack
            int h = (i == n) ? 0 : heights[i];
            
            while (!stack.isEmpty() && h < heights[stack.peek()]) {
                int height = heights[stack.pop()];
                int width = stack.isEmpty() ? i : i - stack.peek() - 1;
                maxArea = Math.max(maxArea, height * width);
            }
            
            stack.push(i);
        }
        
        return maxArea;
    }
}
```

### Complexity
- **Time**: O(n) - Each element pushed/popped once
- **Space**: O(n) - Stack

## Key Takeaways
- Monotonic stack helps find boundaries (Next/Previous Smaller Elements)
- Virtual bar at end force-pops remaining elements
- Area = `height * (right_index - left_index - 1)`
