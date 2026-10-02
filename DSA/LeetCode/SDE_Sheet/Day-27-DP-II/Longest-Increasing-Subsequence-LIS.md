# Longest Increasing Subsequence (LIS)

**LeetCode 300** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/longest-increasing-subsequence/)

### Problem
Find the length of the longest strictly increasing subsequence.

### Approach 1 — DP O(n²)

- `dp[i]` = LIS ending at index i
- `dp[i] = max(dp[j] + 1)` for all j < i where `nums[j] < nums[i]`

### Approach 2 — Binary Search O(n log n) ?

- Maintain `tails[]` array: `tails[i]` = smallest tail element of all IS of length i+1
- For each element, binary search for its position in tails

### Java Solution (Binary Search)

```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        List<Integer> tails = new ArrayList<>();
        for (int num : nums) {
            int pos = Collections.binarySearch(tails, num);
            if (pos < 0) pos = -(pos + 1); // insertion point
            if (pos == tails.size()) tails.add(num);
            else tails.set(pos, num);
        }
        return tails.size();
    }
}
```

**Complexity:** Time O(n log n) · Space O(n)

---
