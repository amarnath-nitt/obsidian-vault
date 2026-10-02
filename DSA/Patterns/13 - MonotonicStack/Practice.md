# Monotonic Stack - Practice Notes

## Pattern Overview
A stack that maintains elements in a monotonically increasing or decreasing order, useful for finding next/previous greater or smaller elements.

## Key Concepts
- **Monotonic Increasing**: Stack elements increase from bottom to top
- **Monotonic Decreasing**: Stack elements decrease from bottom to top
- **Time Complexity**: O(n) - each element pushed/popped once

## Template Code

### Next Greater Element
```java
public int[] nextGreaterElement(int[] nums) {
    int n = nums.length;
    int[] result = new int[n];
    Stack<Integer> stack = new Stack<>();
    
    for (int i = n - 1; i >= 0; i--) {
        while (!stack.isEmpty() && stack.peek() <= nums[i]) {
            stack.pop();
        }
        result[i] = stack.isEmpty() ? -1 : stack.peek();
        stack.push(nums[i]);
    }
    return result;
}
```

### Previous Smaller Element
```java
Stack<Integer> stack = new Stack<>();
for (int i = 0; i < nums.length; i++) {
    while (!stack.isEmpty() && nums[stack.peek()] >= nums[i]) {
        stack.pop();
    }
    // stack.peek() has previous smaller element index
    stack.push(i);
}
```

## Practice Problems

### Easy
- [x] [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) (LC 496) → [Solution](solutions/LC-496-Next-Greater-Element-I.md)
- [ ] [Final Prices With a Special Discount in a Shop](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/) (LC 1475) → [Solution](solutions/LC-1475-Final-Prices.md)

### Medium
- [ ] [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) (LC 503) → [Solution](solutions/LC-503-Next-Greater-Element-II.md)
- [ ] [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) (LC 739) → [Solution](solutions/LC-739-Daily-Temperatures.md)
- [ ] [Online Stock Span](https://leetcode.com/problems/online-stock-span/) (LC 901) → [Solution](solutions/LC-901-Online-Stock-Span.md)
- [ ] [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) (LC 735) → [Solution](solutions/LC-735-Asteroid-Collision.md)
- [ ] [Remove K Digits](https://leetcode.com/problems/remove-k-digits/) (LC 402) → [Solution](solutions/LC-402-Remove-K-Digits.md)
- [ ] [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/) (LC 316) → [Solution](solutions/LC-316-Remove-Duplicate-Letters.md)

### Hard
- [ ] [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) (LC 84) → [Solution](solutions/LC-84-Largest-Rectangle-in-Histogram.md)
- [ ] [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) (LC 85) → [Solution](solutions/LC-85-Maximal-Rectangle.md)
- [ ] [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) (LC 42) → [Solution](../TwoPointers/solutions/LC-42-Trapping-Rain-Water.md)

## Reference
[LeetCode Pattern Guide](https://lnkd.in/g2ckwXTW)
