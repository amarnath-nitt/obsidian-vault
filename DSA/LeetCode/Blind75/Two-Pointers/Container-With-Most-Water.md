# Container With Most Water

**Difficulty:** Medium  
**Category:** Two Pointers  
**LeetCode Link:** [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

---

## Problem Statement

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i-th` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

**Note:** You may not slant the container.

**Example 1:**
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: Lines at index 1 (height=8) and index 8 (height=7)
form a container with area = min(8,7) * (8-1) = 7 * 7 = 49
```

**Example 2:**
```
Input: height = [1,1]
Output: 1
```

**Constraints:**
- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

---

## Intuition

The area of water is determined by: `width × min(left_height, right_height)`. We need to find the pair of lines that maximizes this area.

---

## Approach 1: Brute Force (Naive Solution)

### Algorithm
1. Try all possible pairs of lines
2. Calculate area for each pair
3. Track maximum area

### Java Code
```java
class Solution {
    public int maxArea(int[] height) {
        int maxArea = 0;
        
        // Try all pairs
        for (int i = 0; i < height.length; i++) {
            for (int j = i + 1; j < height.length; j++) {
                int width = j - i;
                int minHeight = Math.min(height[i], height[j]);
                int area = width * minHeight;
                maxArea = Math.max(maxArea, area);
            }
        }
        
        return maxArea;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n²) - Check all pairs
- **Space Complexity:** O(1) - Only tracking max

### Drawbacks
- Too slow for large inputs
- Many unnecessary comparisons

---

## Approach 2: Two Pointers (Optimized Solution)

### Algorithm
1. Start with widest container: left = 0, right = n-1
2. Calculate current area
3. Move the pointer with smaller height inward
   - Why? The width will decrease, so we need a taller line to potentially increase area
4. Repeat until pointers meet

### Java Code
```java
class Solution {
    public int maxArea(int[] height) {
        int maxArea = 0;
        int left = 0;
        int right = height.length - 1;
        
        while (left < right) {
            // Calculate current area
            int width = right - left;
            int minHeight = Math.min(height[left], height[right]);
            int area = width * minHeight;
            maxArea = Math.max(maxArea, area);
            
            // Move pointer with smaller height
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

### Step-by-Step Example
For `height = [1,8,6,2,5,4,8,3,7]`:

```
left=0(1), right=8(7): area = 8 * min(1,7) = 8 * 1 = 8
  height[left] < height[right] → left++

left=1(8), right=8(7): area = 7 * min(8,7) = 7 * 7 = 49 ✓
  height[left] > height[right] → right--

left=1(8), right=7(3): area = 6 * min(8,3) = 6 * 3 = 18
  height[left] > height[right] → right--

left=1(8), right=6(8): area = 5 * min(8,8) = 5 * 8 = 40
  height[left] = height[right] → right--

left=1(8), right=5(4): area = 4 * min(8,4) = 4 * 4 = 16
  height[left] > height[right] → right--

...continues until left >= right

Max area = 49
```

### Complexity Analysis
- **Time Complexity:** O(n) - Single pass with two pointers
- **Space Complexity:** O(1) - Only using pointers and variables

### Why This is Better
- ✅ O(n) vs O(n²) - linear time
- ✅ Greedy approach: always move the limiting factor
- ✅ No need to check all pairs
- ✅ Optimal solution

---

## Why the Greedy Approach Works

**Key Insight:** Moving the pointer with the smaller height is always the right choice.

**Proof by contradiction:**
- Suppose we're at position (left, right) with `height[left] < height[right]`
- If we move `right` inward:
  - Width decreases
  - Height is limited by `min(height[left], height[right-1])`
  - Since `height[left]` is already the limiting factor, area can only decrease or stay same
- Therefore, we should move `left` to potentially find a taller line

---

## Key Takeaways

1. **Pattern:** Two pointers from both ends with greedy movement
2. **Greedy choice:** Always move the pointer with smaller height
3. **Area formula:** `width × min(left_height, right_height)`
4. **Optimization:** Don't need to check all pairs
5. **Proof:** Understanding why greedy works is important

---

## Common Mistakes

- Moving the wrong pointer (taller instead of shorter)
- Not understanding why the greedy approach is optimal
- Forgetting that width decreases as pointers move inward
- Using `max` instead of `min` for height

---

## Edge Cases

- Two lines: `[1,2]` → `1`
- All same height: `[5,5,5,5]` → `15` (width=3, height=5)
- Increasing heights: `[1,2,3,4,5]` → `6` (indices 0 and 4)
- One very tall: `[1,100,1]` → `2` (indices 0 and 2)

---

## Related Problems
- [[Trapping-Rain-Water]] - Similar two-pointer concept
- [[Largest-Rectangle-in-Histogram]] - Related area problem
- [[Maximal-Rectangle]] - 2D version

---

## Tags
#arrays #two-pointers #greedy #medium #blind75

---

## Visualization

- Embed: `![](../assets/container-with-most-water/step-1.svg)`
- Obsidian embed: `![[../assets/container-with-most-water/step-1.svg]]`

<svg xmlns="http://www.w3.org/2000/svg" width="760" height="140">
  <style>text{font-family: Arial, sans-serif; font-size:13px}</style>
  <text x="20" y="28" fill="#222">Two pointers: area calculation sketch</text>
  <g transform="translate(20,50)">
    <rect x="0" y="0" width="40" height="60" fill="#fff" stroke="#4b6cc1"/>
    <text x="20" y="36" text-anchor="middle">1</text>
    <rect x="300" y="0" width="40" height="80" fill="#fff" stroke="#4b6cc1"/>
    <text x="320" y="46" text-anchor="middle">7</text>
    <text x="160" y="90" fill="#666">width × min(left,right)</text>
  </g>
</svg>
