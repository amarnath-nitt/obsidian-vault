# Reverse Pairs

**LeetCode 493** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/reverse-pairs/)

### Problem
Count pairs `(i, j)` where `i < j` and `nums[i] > 2 * nums[j]`.

### Approach (Modified Merge Sort)

- Like Count Inversions, but condition is `arr[i] > 2 * arr[j]`
- **Count phase** (before merge): Use two pointers across left and right halves
- **Merge phase**: Standard merge sort

> ⚠️ Count BEFORE merging, because after merging the halves, relative order changes.

### Java Solution

```java
class Solution {
    public int reversePairs(int[] nums) {
        return mergeSort(nums, 0, nums.length - 1);
    }

    private int mergeSort(int[] nums, int l, int r) {
        if (l >= r) return 0;
        int mid = l + (r - l) / 2;
        int count = mergeSort(nums, l, mid) + mergeSort(nums, mid + 1, r);

        // Count reverse pairs
        int j = mid + 1;
        for (int i = l; i <= mid; i++) {
            while (j <= r && nums[i] > 2L * nums[j]) j++;
            count += (j - mid - 1);
        }

        // Merge
        int[] temp = new int[r - l + 1];
        int i = l, k = 0;
        j = mid + 1;
        while (i <= mid && j <= r)
            temp[k++] = (nums[i] <= nums[j]) ? nums[i++] : nums[j++];
        while (i <= mid) temp[k++] = nums[i++];
        while (j <= r)   temp[k++] = nums[j++];
        for (int x = 0; x < temp.length; x++) nums[l + x] = temp[x];

        return count;
    }
}
```

**Complexity:** Time O(n log n) · Space O(n)

---
