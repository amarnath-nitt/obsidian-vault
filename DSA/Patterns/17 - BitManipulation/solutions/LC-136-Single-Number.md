---
solved: false
difficulty: Easy
pattern: Bit Manipulation
lc_number: 136
date_solved: 
tags:
  - dsa
  - bit-manipulation
  - easy
---
# Single Number (LC 136)

**Difficulty**: Easy  
**Pattern**: Bit Manipulation  
**LeetCode**: https://leetcode.com/problems/single-number/

## Existing Solution Reference
Similar in Blind75: → [Bit Manipulation problems](../../../LeetCode/Blind75/)

## Problem Statement
Given a non-empty array where every element appears twice except one, find that single element. Must use linear time and constant space.

**Example:**
```
Input: nums = [4,1,2,1,2]
Output: 4
```

## Approach 1: HashMap

### Java Code
```java
class Solution {
    public int singleNumber(int[] nums) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }
        
        for (int num : count.keySet()) {
            if (count.get(num) == 1) {
                return num;
            }
        }
        
        return -1;
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(n)

## Approach 2: XOR (Optimized)

### Intuition
XOR has properties:
- `a ^ a = 0`
- `a ^ 0 = a`
- XOR is commutative and associative

So XORing all numbers cancels out duplicates, leaving only the single number.

### Java Code
```java
class Solution {
    public int singleNumber(int[] nums) {
        int result = 0;
        for (int num : nums) {
            result ^= num;
        }
        return result;
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(1)

## Visual Example
```
nums = [4,1,2,1,2]

4 ^ 1 = 5 (0100 ^ 0001 = 0101)
5 ^ 2 = 7 (0101 ^ 0010 = 0111)
7 ^ 1 = 6 (0111 ^ 0001 = 0110)
6 ^ 2 = 4 (0110 ^ 0010 = 0100)

Result: 4
```

## Key Takeaways
- XOR perfect for finding unique element when others appear in pairs
- Exploits mathematical properties of XOR
- Classic bit manipulation trick
- O(1) space solution
