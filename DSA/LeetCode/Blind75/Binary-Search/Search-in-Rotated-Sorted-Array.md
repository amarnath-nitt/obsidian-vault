# Search in Rotated Sorted Array

**Difficulty:** Medium  
**Category:** Binary Search  
**LeetCode Link:** [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

---

## Problem Statement

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with **O(log n)** runtime complexity.

**Example 1:**
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

**Example 2:**
```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

**Constraints:**
- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are **unique**.
- `nums` is an ascending array that is possibly rotated.

---

## Intuition

Even though the array is rotated, one half is always sorted. We can use this property to decide which half to search.

---

## Approach 1: Find Pivot Then Binary Search (Naive)

### Algorithm
1. Find the rotation pivot point
2. Determine which half contains the target
3. Binary search in that half

### Java Code
```java
class Solution {
    public int search(int[] nums, int target) {
        int n = nums.length;
        
        // Find pivot
        int pivot = findPivot(nums);
        
        // Decide which half to search
        if (pivot == 0 || target < nums[0]) {
            return binarySearch(nums, pivot, n - 1, target);
        } else {
            return binarySearch(nums, 0, pivot - 1, target);
        }
    }
    
    private int findPivot(int[] nums) {
        int left = 0, right = nums.length - 1;
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
    
    private int binarySearch(int[] nums, int left, int right, int target) {
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return -1;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(log n) - Two binary searches
- **Space Complexity:** O(1)

---

## Approach 2: One-Pass Binary Search (Optimized)

### Algorithm
1. Use modified binary search
2. At each step, determine which half is sorted
3. Check if target is in the sorted half
4. Adjust search range accordingly

### Java Code
```java
class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] == target) {
                return mid;
            }
            
            // Determine which half is sorted
            if (nums[left] <= nums[mid]) {
                // Left half is sorted
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;  // Target in left half
                } else {
                    left = mid + 1;   // Target in right half
                }
            } else {
                // Right half is sorted
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;   // Target in right half
                } else {
                    right = mid - 1;  // Target in left half
                }
            }
        }
        
        return -1;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(log n) - Single binary search
- **Space Complexity:** O(1)

### Why This is Better
- ✅ Single pass instead of two
- ✅ More elegant solution
- ✅ Same time complexity but fewer operations
- ✅ Handles all cases in one loop

---

## Key Takeaways

1. **Pattern:** Modified binary search for rotated arrays
2. **Key insight:** One half is always sorted
3. **Decision making:** Check if target is in sorted half
4. **Edge case:** Handle when left == mid (single element)

---

## Step-by-Step Example

For `nums = [4,5,6,7,0,1,2]`, `target = 0`:

```
left=0, right=6, mid=3, nums[mid]=7
  Left half [4,5,6,7] is sorted
  0 not in [4,7], search right half
  
left=4, right=6, mid=5, nums[mid]=1
  Right half [1,2] is sorted
  0 not in [1,2], search left half
  
left=4, right=4, mid=4, nums[mid]=0
  Found! Return 4
```

---

## Edge Cases

- No rotation: `[1,2,3,4,5]`, target=3 → `2`
- Rotated at start: `[2,3,4,5,1]`, target=1 → `4`
- Single element: `[1]`, target=1 → `0`
- Target not found: `[4,5,6,7,0,1,2]`, target=3 → `-1`

---

## Related Problems
- [[Find-Minimum-in-Rotated-Sorted-Array]] - Find pivot
- [[Search-in-Rotated-Sorted-Array-II]] - With duplicates
- [[Binary-Search]] - Standard binary search

---

## Tags
#binary-search #arrays #medium #blind75
