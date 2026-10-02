---
solved: false
difficulty: Easy
pattern: Modified Binary Search
lc_number: 704
date_solved: 
tags:
  - dsa
  - modified-binary-search
  - easy
---
# Binary Search (LC 704)

**Difficulty**: Easy  
**Pattern**: Modified Binary Search  
**LeetCode**: https://leetcode.com/problems/binary-search/

## Problem Statement
Given a sorted array of integers `nums` and target value `target`, return the index of `target` if found, otherwise return -1.

**Example:**
```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
```

## Approach 1: Linear Search

### Java Code
```java
class Solution {
    public int search(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                return i;
            }
        }
        return -1;
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(1)

## Approach 2: Binary Search (Optimized)

### Java Code
```java
class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return -1;
    }
}
```

### Complexity
- **Time**: O(log n)
- **Space**: O(1)

## Key Takeaways
- Classic binary search template
- Use `left + (right - left) / 2` to avoid overflow
- Works only on sorted arrays
- Foundation for many binary search variations
