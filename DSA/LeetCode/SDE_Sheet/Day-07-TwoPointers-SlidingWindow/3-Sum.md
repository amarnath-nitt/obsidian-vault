# 3-Sum

**LeetCode 15** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/3sum/)

### Problem
Find all unique triplets that sum to zero.

### Approach

1. **Sort** the array
2. Fix one element `nums[i]`
3. Use **Two Pointers** on the rest
4. Skip duplicates carefully

### Java Solution

```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue; // skip outer dup

            int left = i + 1, right = nums.length - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    while (left < right && nums[left] == nums[left+1]) left++;
                    while (left < right && nums[right] == nums[right-1]) right--;
                    left++; right--;
                } else if (sum < 0) left++;
                else right--;
            }
        }
        return result;
    }
}
```

**Complexity:** Time O(n²) · Space O(1) excluding output

---
