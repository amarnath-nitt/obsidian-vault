---
solved: false
difficulty: Easy
pattern: Monotonic Stack
lc_number: 1475
date_solved: 
tags:
  - dsa
  - monotonic-stack
  - easy
---
# Final Prices With a Special Discount in a Shop (LC 1475)

**Difficulty**: Easy  
**Pattern**: Monotonic Stack  
**LeetCode**: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

## Problem Statement
Given an integer array `prices` where `prices[i]` is the price of the `i`th item in a shop.
There is a special discount for items. If you buy the `i`th item, then you will receive a discount equivalent to `prices[j]` where `j` is the minimum index such that `j > i` and `prices[j] <= prices[i]`. Otherwise, you will not receive any discount at all.
Return an array where the `i`th element is the final price you will pay for the `i`th item.

**Example:**
```
Input: prices = [8,4,6,2,3]
Output: [4,2,4,2,3]
```

## Approach: Monotonic Stack (Increasing)

### Intuition
Equivalent to finding the "Next Smaller Element".
Use stack to keep track of indices.
When we see `prices[i] <= prices[stack.peek()]`, it means `prices[i]` is the discount for `stack.peek()`.
Apply discount and pop.

### Java Code
```java
class Solution {
    public int[] finalPrices(int[] prices) {
        int n = prices.length;
        Deque<Integer> stack = new ArrayDeque<>(); // Indices
        
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && prices[stack.peek()] >= prices[i]) {
                int index = stack.pop();
                prices[index] -= prices[i];
            }
            stack.push(i);
        }
        
        return prices;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(N)

## Key Takeaways
- Direct application of "Next Smaller Element"
- In-place modification of prices array possible
