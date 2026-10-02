# Two Sum

**LeetCode 1** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/two-sum/)

### Problem
Find indices of two numbers that add up to target.

### Approach

- Use a **HashMap** to store `value → index`
- For each element, check if `target - nums[i]` exists in map

### Java Solution

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement))
                return new int[]{map.get(complement), i};
            map.put(nums[i], i);
        }
        return new int[]{};
    }
}
```

**Complexity:** Time O(n) · Space O(n)

---
