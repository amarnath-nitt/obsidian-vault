# Missing Number (LC 268)

**Difficulty**: Easy  
**Pattern**: Bit Manipulation  
**LeetCode**: https://leetcode.com/problems/missing-number/

## Problem Statement
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

**Example:**
```
Input: nums = [3,0,1]
Output: 2
```

## Approach 1: Bit Manipulation (XOR)

### Intuition
XOR of a number with itself is 0.
XOR `[0...n]` and XOR all elements in `nums`.
The result will be the missing number, as all others appear twice (once in range, once in array).

### Java Code
```java
class Solution {
    public int missingNumber(int[] nums) {
        int xor = 0;
        for (int i = 0; i <= nums.length; i++) {
            xor ^= i;
        }
        for (int num : nums) {
            xor ^= num;
        }
        return xor;
    }
}
```

## Approach 2: Math (Sum)

### Intuition
Sum of `[0...n]` is `n * (n + 1) / 2`.
Subtract sum of array elements.
Result is missing number.

### Java Code
```java
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int expectedSum = n * (n + 1) / 2;
        int actualSum = 0;
        for (int num : nums) {
            actualSum += num;
        }
        return expectedSum - actualSum;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(1)

## Key Takeaways
- XOR cancels out duplicates
- Gauss Sum formula
