# Largest Rectangle in Histogram

**LeetCode 84** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/largest-rectangle-in-histogram/)

### Problem
Given bar heights, find the largest rectangle area.

### Approach (Monotonic Increasing Stack)

- For each bar, find the **previous smaller** and **next smaller** bar
- Width = `nextSmaller[i] - prevSmaller[i] - 1`
- Area = `height[i] * width`

### Java Solution (One-pass)

```java
class Solution {
    public int largestRectangleArea(int[] heights) {
        Deque<Integer> stack = new ArrayDeque<>();
        int maxArea = 0;
        int n = heights.length;

        for (int i = 0; i <= n; i++) {
            int h = (i == n) ? 0 : heights[i];
            while (!stack.isEmpty() && heights[stack.peek()] > h) {
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

**Complexity:** Time O(n) · Space O(n)

> **Variant:** [Maximal Rectangle (LC 85)](https://leetcode.com/problems/maximal-rectangle/) — apply this histogram approach on each row.

---
