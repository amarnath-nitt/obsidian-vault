# Max Consecutive Ones III

**LeetCode 1004** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/max-consecutive-ones-iii/)

### Problem
Given binary array, you can flip at most k zeros. Find max length of consecutive 1s.

### Approach (Sliding Window)

- Maintain a window with at most k zeros
- Expand right; when zeros > k, shrink from left

### Java Solution

```java
class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0, zeros = 0, maxLen = 0;

        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) zeros++;
            while (zeros > k) {
                if (nums[left] == 0) zeros--;
                left++;
            }
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---
