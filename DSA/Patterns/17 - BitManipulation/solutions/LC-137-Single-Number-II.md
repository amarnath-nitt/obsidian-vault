# Single Number II (LC 137)

**Difficulty**: Medium  
**Pattern**: Bit Manipulation  
**LeetCode**: https://leetcode.com/problems/single-number-ii/

## Problem Statement
Given an integer array `nums` where every element appears **three times** except for one, which appears exactly once. Find the single element and return it.
You must implement a solution with a linear runtime complexity and use only constant extra space.

**Example:**
```
Input: nums = [2,2,3,2]
Output: 3
```

## Approach: Bit Counting

### Intuition
For each bit position (0 to 31):
Count how many numbers have this bit set.
If `count % 3 == 0`, the single number has 0 at this bit.
If `count % 3 == 1`, the single number has 1 at this bit.
Reconstruct the number.

### Java Code
```java
class Solution {
    public int singleNumber(int[] nums) {
        int result = 0;
        for (int i = 0; i < 32; i++) {
            int sum = 0;
            for (int num : nums) {
                if (((num >> i) & 1) == 1) {
                    sum++;
                }
            }
            if (sum % 3 != 0) {
                result |= (1 << i);
            }
        }
        return result;
    }
}
```

### Circuit Design Approach (Advanced)
`ones` tracks bits appearing 1st time.
`twos` tracks bits appearing 2nd time.
`threes` (reset logic) clears bits appearing 3rd time.

```java
public int singleNumberOptimized(int[] nums) {
    int ones = 0, twos = 0;
    for (int num : nums) {
        ones = (ones ^ num) & ~twos;
        twos = (twos ^ num) & ~ones;
    }
    return ones;
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(1)

## Key Takeaways
- Counting bits modulo K can solve "occurs K times except one"
