# Remove Duplicates from Sorted Array

**LeetCode 26** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

### Problem
Remove duplicates in-place from sorted array, return new length.

### Approach (Slow-Fast Write Pointer)

- `slow` = where to write the next unique element
- `fast` scans the array

### Java Solution

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        int slow = 1;
        for (int fast = 1; fast < nums.length; fast++) {
            if (nums[fast] != nums[fast - 1]) {
                nums[slow++] = nums[fast];
            }
        }
        return slow;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---
