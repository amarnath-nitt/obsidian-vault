---
solved: false
difficulty: Medium
pattern: Monotonic Stack
lc_number: 503
date_solved: 
tags:
  - dsa
  - monotonic-stack
  - medium
---
# Next Greater Element II (LC 503)

**Difficulty**: Medium  
**Pattern**: Monotonic Stack  
**LeetCode**: https://leetcode.com/problems/next-greater-element-ii/

## Problem Statement
Given a circular integer array `nums`, return the next greater number for every element in `nums`.
If it doesn't exist, return -1.

**Example:**
```
Input: nums = [1,2,1]
Output: [2,-1,2]
```

## Approach: Monotonic Stack + Circular Logic

### Intuition
Standard Next Greater Element uses stack to store indices.
Loop `2 * n` times (mod `n`) to simulate circular array.
Index `i % n`.

### Java Code
```java
class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        Arrays.fill(result, -1);
        Deque<Integer> stack = new ArrayDeque<>(); // Stores indices
        
        for (int i = 0; i < 2 * n; i++) {
            int num = nums[i % n];
            while (!stack.isEmpty() && nums[stack.peek()] < num) {
                result[stack.pop()] = num;
            }
            if (i < n) {
                stack.push(i);
            }
        }
        
        return result;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(N)

## Key Takeaways
- Circular array handled by iterating `2 * N` with modulo
- Store indices in stack to update result array
