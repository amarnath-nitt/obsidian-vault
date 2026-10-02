# Subsets II (with duplicates)

**LeetCode 90** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/subsets-ii/)

### Problem
Same as Subsets, but array may contain duplicates. Return unique subsets.

### Approach

- **Sort** first to group duplicates
- At the same recursion level, skip duplicate values (not the first occurrence)

### Java Solution

```java
class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, 0, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int[] nums, int start, List<Integer> current, List<List<Integer>> result) {
        result.add(new ArrayList<>(current));

        for (int i = start; i < nums.length; i++) {
            if (i > start && nums[i] == nums[i-1]) continue; // skip dup at same level
            current.add(nums[i]);
            backtrack(nums, i + 1, current, result);
            current.remove(current.size() - 1);
        }
    }
}
```

**Complexity:** Time O(n × 2ⁿ) · Space O(n × 2ⁿ)

---
