---
solved: true
difficulty: Easy
pattern: Monotonic Stack
lc_number: 496
date_solved: 
tags:
  - dsa
  - monotonic-stack
  - easy
---
# Next Greater Element I (LC 496)

**Difficulty**: Easy  
**Pattern**: Monotonic Stack  
**LeetCode**: https://leetcode.com/problems/next-greater-element-i/

## Problem Statement
The **next greater element** of some element `x` in an array is the first greater element that is to the right of `x` in the same array.
You are given two distinct 0-indexed integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.
For each `0 <= i < nums1.length`, find the index `j` such that `nums1[i] == nums2[j]` and determine the next greater element of `nums2[j]` in `nums2`. If there is no next greater element, then the answer for this query is `-1`.

**Example:**
```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so -1.
- 1 is underlined in nums2 = [1,3,4,2]. Next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so -1.
```

## Approach: Monotonic Stack + HashMap

### Intuition
We want to find the next greater element for *every* element in `nums2` first.
Traverse `nums2`. Use a stack to keep track of elements whose "next greater" we haven't found yet.
If current element `num` > `stack.peek()`, then `num` is the Next Greater Element for `stack.pop()`.
Store these relationships in a HashMap.

### Java Code
```java
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        // Map to store (element -> next greater element)
        Map<Integer, Integer> map = new HashMap<>(); 
        Stack<Integer> stack = new Stack<>();
        
        for (int num : nums2) {
            // While stack is not empty and current num is greater than stack top
            while (!stack.isEmpty() && num > stack.peek()) {
                map.put(stack.pop(), num);
            }
            stack.push(num);
        }
        
        // Populate result for nums1
        int[] result = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            result[i] = map.getOrDefault(nums1[i], -1);
        }
        
        return result;
    }
    
    // Alternative for simple "Next Greater Element for all in array"
    // Using array right-to-left
    /*
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        Stack<Integer> stack = new Stack<>();
        
        for (int i = n - 1; i >= 0; i--) {
            while(!stack.isEmpty() && stack.peek() <= nums[i]) {
                stack.pop();
            }
            result[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(nums[i]);
        }
        return result;
    }
    */
}
```

### Complexity
- **Time**: O(N + M) where N is nums2 length, M is nums1 length.
- **Space**: O(N) for stack and map

## Key Takeaways
- Classic Monotonic Decreasing Stack application
- Map results for fast lookup
- Process elements and resolve "pending" queries on stack
