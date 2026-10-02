# Permutations

**LeetCode 46** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/permutations/)

### Problem
Return all possible permutations of unique integers.

### Approach (Swap-based)

- Swap `nums[start]` with each element from `start` to `end`
- Recurse with `start+1`
- Swap back (backtrack)

### Java Solution

```java
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, 0, result);
        return result;
    }

    private void backtrack(int[] nums, int start, List<List<Integer>> result) {
        if (start == nums.length) {
            List<Integer> perm = new ArrayList<>();
            for (int n : nums) perm.add(n);
            result.add(perm);
            return;
        }
        for (int i = start; i < nums.length; i++) {
            swap(nums, start, i);
            backtrack(nums, start + 1, result);
            swap(nums, start, i); // backtrack
        }
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i]; nums[i] = nums[j]; nums[j] = tmp;
    }
}
```

**Complexity:** Time O(n × n!) · Space O(n!)

---
