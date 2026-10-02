---
solved: false
difficulty: Medium
pattern: Greedy
lc_number: 179
date_solved: 
tags:
  - dsa
  - greedy
  - medium
---
# Largest Number (LC 179)

**Difficulty**: Medium  
**Pattern**: Greedy / Sorting  
**LeetCode**: https://leetcode.com/problems/largest-number/

## Problem Statement
Given a list of non-negative integers `nums`, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

**Example:**
```
Input: nums = [3,30,34,5,9]
Output: "9534330"
```

## Approach: Custom Sort

### Intuition
To decide if `a` comes before `b`, compare `a + b` vs `b + a`.
If `a + b` > `b + a`, then `a` should come first.
Sort all numbers using this comparator.
Edge case: "00" should be "0".

### Java Code
```java
class Solution {
    public String largestNumber(int[] nums) {
        String[] strs = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            strs[i] = String.valueOf(nums[i]);
        }
        
        Arrays.sort(strs, (a, b) -> (b + a).compareTo(a + b));
        
        if (strs[0].equals("0")) return "0";
        
        StringBuilder sb = new StringBuilder();
        for (String s : strs) sb.append(s);
        
        return sb.toString();
    }
}
```

### Complexity
- **Time**: O(N log N * L) where L is max digits
- **Space**: O(N * L)

## Key Takeaways
- Custom comparator logic determines Greedy choice
