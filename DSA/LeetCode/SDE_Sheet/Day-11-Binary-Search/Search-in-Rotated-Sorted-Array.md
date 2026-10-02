# Search in Rotated Sorted Array

**LeetCode 33** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/search-in-rotated-sorted-array/)

### Problem
Array was sorted, then rotated at an unknown pivot. Find target.

### Approach

- One half is always **sorted**
- Determine which half is sorted, check if target lies in it
- Eliminate the other half

### Java Solution

```java
class Solution {
    public int search(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == target) return mid;

            // Left half is sorted
            if (nums[lo] <= nums[mid]) {
                if (target >= nums[lo] && target < nums[mid]) hi = mid - 1;
                else lo = mid + 1;
            }
            // Right half is sorted
            else {
                if (target > nums[mid] && target <= nums[hi]) lo = mid + 1;
                else hi = mid - 1;
            }
        }
        return -1;
    }
}
```

**Complexity:** Time O(log n) · Space O(1)

---
