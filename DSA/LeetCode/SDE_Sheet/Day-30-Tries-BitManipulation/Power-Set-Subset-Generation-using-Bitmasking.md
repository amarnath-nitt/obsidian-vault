# Power Set (Subset Generation using Bitmasking)

**LeetCode 78** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/subsets/)

### Problem
Given an integer array `nums` of unique elements, return all possible subsets (the power set).

### Approach
- An array of size $N$ has $2^N$ subsets.
- We can map each subset to a binary number from $0$ to $2^N - 1$.
- For any number $i$ in this range, if the $j$-th bit of $i$ is set (i.e., `(i >> j) & 1 == 1`), then `nums[j]` is included in that subset.

### Java Solution

```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        int n = nums.length;
        int totalSubsets = 1 << n; // 2^n

        for (int i = 0; i < totalSubsets; i++) {
            List<Integer> subset = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                if (((i >> j) & 1) == 1) {
                    subset.add(nums[j]);
                }
            }
            result.add(subset);
        }
        return result;
    }
}
```

**Complexity:** Time $O(N \times 2^N)$ · Space $O(N \times 2^N)$

---
