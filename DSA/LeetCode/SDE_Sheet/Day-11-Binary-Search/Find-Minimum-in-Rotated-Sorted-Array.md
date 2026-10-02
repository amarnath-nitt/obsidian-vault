# Find Minimum in Rotated Sorted Array

**LeetCode 153** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

### Problem
Find the minimum in a rotated sorted array.

### Approach

- The minimum is at the **pivot point** (where the rotation is)
- If left half is not sorted → minimum is in left half
- Otherwise → minimum is in right half (or mid)

### Java Solution

```java
class Solution {
    public int findMin(int[] nums) {
        int lo = 0, hi = nums.length - 1;

        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] > nums[hi]) lo = mid + 1; // min is in right half
            else hi = mid;                           // min is in left half (including mid)
        }
        return nums[lo];
    }
}
```

**Complexity:** Time O(log n) · Space O(1)

---
