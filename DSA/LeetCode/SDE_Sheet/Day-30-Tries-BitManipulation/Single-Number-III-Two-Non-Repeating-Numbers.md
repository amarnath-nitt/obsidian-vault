# Single Number III (Two Non-Repeating Numbers)

**LeetCode 260** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/single-number-iii/)

### Problem
Given an integer array `nums`, in which exactly two elements appear only once and all other elements appear exactly twice. Find the two elements that appear only once.

### Approach
1. XOR all numbers. The result `XOR_total` will be $A \oplus B$ (since all duplicates cancel out).
2. Since $A \neq B$, `XOR_total` must have at least one set bit. Find the lowest set bit: `rightmost_set_bit = XOR_total & -XOR_total`.
3. Use this set bit to divide all numbers in the array into two groups:
   - Group 1: Numbers that have this bit set.
   - Group 2: Numbers that do not have this bit set.
4. XORing all numbers in Group 1 will yield $A$, and XORing Group 2 will yield $B$.

### Java Solution

```java
class Solution {
    public int[] singleNumber(int[] nums) {
        int xor = 0;
        for (int num : nums) {
            xor ^= num;
        }

        // Get the rightmost set bit
        int rightmostSetBit = xor & -xor;

        int a = 0, b = 0;
        for (int num : nums) {
            if ((num & rightmostSetBit) != 0) {
                a ^= num;
            } else {
                b ^= num;
            }
        }
        return new int[]{a, b};
    }
}
```

**Complexity:** Time $O(N)$ · Space $O(1)$

---
