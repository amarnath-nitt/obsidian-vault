# Subsets

**LeetCode 78** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/subsets/)

### Problem
Given an array of unique integers, return all possible subsets (power set).

### Approach

- At each index, we have 2 choices: **include** or **exclude** the element
- Recurse with `start+1` to avoid revisiting elements

### Java Solution

```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, 0, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int[] nums, int start, List<Integer> current, List<List<Integer>> result) {
        result.add(new ArrayList<>(current)); // add at every node

        for (int i = start; i < nums.length; i++) {
            current.add(nums[i]);           // choose
            backtrack(nums, i + 1, current, result);
            current.remove(current.size() - 1); // unchoose
        }
    }
}
```

**Complexity:** Time O(n × 2ⁿ) · Space O(n × 2ⁿ)

---
