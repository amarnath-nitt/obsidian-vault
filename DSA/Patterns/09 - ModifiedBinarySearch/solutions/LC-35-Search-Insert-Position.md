---
solved: false
difficulty: Easy
pattern: Modified Binary Search
lc_number: 35
date_solved: 
tags:
  - dsa
  - modified-binary-search
  - easy
---
# Search Insert Position (LC 35)

**Difficulty**: Easy  
**Pattern**: Modified Binary Search  
**LeetCode**: https://leetcode.com/problems/search-insert-position/

## Problem Statement
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with `O(log n)` runtime complexity.

**Example:**
```
Input: nums = [1,3,5,6], target = 5
Output: 2
```

## Approach: Lower Bound

### Intuition
We want to find the first index where `nums[i] >= target`.
If `nums[mid] >= target`, answer is `mid` or left (`right = mid`).
Wait, standard Binary Search finds match. If not found, `left` usually points to insertion position.
Standard algorithm `left <= right`:
If `nums[mid] < target`: `left = mid + 1`.
If `nums[mid] > target`: `right = mid - 1`.
Loop terminates when `left > right`. `left` is the insertion point.

### Java Code
```java
class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] == target) return mid;
            
            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return left;
    }
}
```

### Complexity
- **Time**: O(log N)
- **Space**: O(1)

## Key Takeaways
- Standard Binary Search `left` variable naturally lands on the insertion index (or first element greater than target)
