# Next Permutation

**LeetCode 31** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/next-permutation/)

### Problem
Rearrange numbers into the lexicographically next greater permutation. If no next permutation exists, sort ascending.

### Approach (3-step in-place)

1. **Find the "dip"**: Scan right-to-left, find index `i` where `nums[i] < nums[i+1]`
2. **Find the swap partner**: Scan right-to-left, find smallest element > `nums[i]`, swap
3. **Reverse the suffix**: Reverse everything after index `i`

> If no dip found → the array is fully descending → reverse the whole array

### Java Solution

```java
class Solution {
    public void nextPermutation(int[] nums) {
        int n = nums.length;
        int i = n - 2;

        // Step 1: Find dip
        while (i >= 0 && nums[i] >= nums[i + 1]) i--;

        if (i >= 0) {
            // Step 2: Find swap partner
            int j = n - 1;
            while (nums[j] <= nums[i]) j--;
            int tmp = nums[i]; nums[i] = nums[j]; nums[j] = tmp;
        }

        // Step 3: Reverse suffix
        int left = i + 1, right = n - 1;
        while (left < right) {
            int tmp = nums[left]; nums[left] = nums[right]; nums[right] = tmp;
            left++; right--;
        }
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---
