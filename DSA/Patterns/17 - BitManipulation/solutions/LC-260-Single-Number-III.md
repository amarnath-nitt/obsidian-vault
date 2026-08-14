# Single Number III (LC 260)

**Difficulty**: Medium  
**Pattern**: Bit Manipulation  
**LeetCode**: https://leetcode.com/problems/single-number-iii/

## Problem Statement
Given an integer array `nums`, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

**Example:**
```
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
```

## Approach: XOR Partition

### Intuition
XOR all numbers. Result `xor` = `a ^ b` (where a and b are the unique numbers).
Since `a != b`, `xor` must have at least one bit set.
Find rightmost set bit: `diff = xor & -xor`.
This bit distinguishes `a` and `b`. One has it set, the other doesn't.
Partition array into two groups based on this bit. XORing each group reveals `a` and `b`.

### Java Code
```java
class Solution {
    public int[] singleNumber(int[] nums) {
        int xor = 0;
        for (int num : nums) {
            xor ^= num;
        }
        
        // Get rightmost set bit
        int diff = xor & -xor;
        
        int[] result = new int[2];
        for (int num : nums) {
            if ((num & diff) == 0) {
                result[0] ^= num;
            } else {
                result[1] ^= num;
            }
        }
        
        return result;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(1)

## Key Takeaways
- Two-pass bit manipulation
- Logic extends Single Number I (XOR cancelation)
- `x & -x` isolates rightmost 1-bit
