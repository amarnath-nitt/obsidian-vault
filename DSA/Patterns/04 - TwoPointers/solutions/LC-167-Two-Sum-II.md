---
solved: true
difficulty: Medium
pattern: Two Pointers
lc_number: 167
date_solved: 
tags:
  - dsa
  - two-pointers
  - medium
---
# Two Sum II - Input Array Is Sorted (LC 167)

**Difficulty**: Medium  
**Pattern**: Two Pointers  
**LeetCode**: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

## Problem Statement
Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Return the indices of the two numbers.

**Example:**
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
```

## Approach: Two Pointers

### Intuition
Since array is sorted:
- Start `left` at 0, `right` at end.
- `sum = nums[left] + nums[right]`
- If `sum == target`, done.
- If `sum < target`, need bigger sum -> `left++`
- If `sum > target`, need smaller sum -> `right--`

### Java Code
```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;
        
        while (left < right) {
            int sum = numbers[left] + numbers[right];
            
            if (sum == target) {
                return new int[]{left + 1, right + 1}; // 1-indexed
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        
        return new int[]{-1, -1};
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(1)

## Key Takeaways
- Sorted array + Find Pair = Two Pointers
- O(n) time, O(1) space dominating O(n) space of HashMap approach
