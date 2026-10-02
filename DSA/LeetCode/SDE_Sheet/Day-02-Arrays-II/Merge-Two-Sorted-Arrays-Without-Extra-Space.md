# Merge Two Sorted Arrays Without Extra Space

**LeetCode 88** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/merge-sorted-array/)

### Problem
Merge `nums2` into `nums1` in-place. `nums1` has enough space at the end.

### Approach

- Start filling from the **end** of `nums1` (avoid overwriting)
- Use three pointers: `i = m-1`, `j = n-1`, `k = m+n-1`
- Compare `nums1[i]` and `nums2[j]`, place the larger at `k`

### Java Solution

```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1, j = n - 1, k = m + n - 1;

        while (i >= 0 && j >= 0) {
            if (nums1[i] > nums2[j]) {
                nums1[k--] = nums1[i--];
            } else {
                nums1[k--] = nums2[j--];
            }
        }

        // Remaining nums2 elements
        while (j >= 0) nums1[k--] = nums2[j--];
    }
}
```

**Complexity:** Time O(m+n) · Space O(1)

---
