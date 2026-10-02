---
solved: true
difficulty: Medium
pattern: Prefix Sum
lc_number: 525
date_solved: 
tags:
  - dsa
  - prefix-sum
  - medium
---
# Contiguous Array (LC 525)

**Difficulty**: Medium  
**Pattern**: Prefix Sum / HashMap  
**LeetCode**: https://leetcode.com/problems/contiguous-array/

## Problem Statement
Given a binary array `nums`, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

**Example:**
```
Input: nums = [0,1]
Output: 2
```

## Approach: Prefix Sum (Treat 0 as -1)

### Intuition
Transform `0` to `-1`.
Then problem becomes "Find longest subarray with sum 0".
Using Prefix Sum: `Sum[i...j] = PrefixSum[j] - PrefixSum[i-1]`.
We want `Sum = 0`, so `PrefixSum[j] = PrefixSum[i-1]`.
Store first occurrence of each `PrefixSum` in a map.
If `PrefixSum` repeats at index `j`, length is `j - map.get(PrefixSum)`.

### Java Code
```java
class Solution {
    public int findMaxLength(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, -1); // Base case: sum 0 at index -1
        
        int maxLen = 0;
        int count = 0;
        
        for (int i = 0; i < nums.length; i++) {
            count += (nums[i] == 1) ? 1 : -1;
            
            if (map.containsKey(count)) {
                maxLen = Math.max(maxLen, i - map.get(count));
            } else {
                map.put(count, i); // Only store first occurrence to maximize length
            }
        }
        
        return maxLen;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(N)

## Key Takeaways
- Transform values to apply "Zero Sum Subarray" pattern
