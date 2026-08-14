# Search in Rotated Sorted Array (LC 33)

**Difficulty**: Medium  
**Pattern**: Modified Binary Search  
**LeetCode**: https://leetcode.com/problems/search-in-rotated-sorted-array/

## Problem Statement
There is an integer array `nums` sorted in ascending order (with distinct values).
Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`.
Given the array `nums` **after** the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.
You must write an algorithm with `O(log n)` runtime complexity.

**Example:**
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

## Approach: Binary Search (One Pass)

### Intuition
Even though rotated, at least one half (left or right) of the array will always be sorted for any pivot `mid`.
1. Check if `mid` matches target.
2. Determine which side is sorted:
   - If `nums[left] <= nums[mid]`, left side is sorted.
   - Else, right side is sorted.
3. Check if target lies within the sorted range. If so, eliminate the other half. Else, eliminate the sorted half.

### Java Code
```java
class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] == target) {
                return mid;
            }
            
            // Check if left half is sorted
            if (nums[left] <= nums[mid]) {
                if (target >= nums[left] && target < nums[mid]) {
                    right = mid - 1; // Target is in left half
                } else {
                    left = mid + 1; // Target is in right half
                }
            } 
            // Right half must be sorted
            else {
                if (target > nums[mid] && target <= nums[right]) {
                    left = mid + 1; // Target is in right half
                } else {
                    right = mid - 1; // Target is in left half
                }
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
- Modified Binary Search handles breaks in sorting
- Identify proper sorted segment first
- O(log n) achieved without finding pivot explicitly first
