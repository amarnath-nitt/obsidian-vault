# Sort an Array of 0s 1s 2s (Dutch National Flag)

**LeetCode 75** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/sort-colors/)

### Problem
Sort an array containing only 0, 1, 2 in-place without using library sort.

### Approach (Dutch National Flag — Dijkstra's 3-way partition)

- Maintain 3 pointers: `low`, `mid`, `high`
- Invariant: `[0..low-1]` = 0s, `[low..mid-1]` = 1s, `[high+1..n-1]` = 2s
- Process `mid` to `high`:
  - `nums[mid] == 0` → swap with `low`, advance both `low` and `mid`
  - `nums[mid] == 1` → advance `mid`
  - `nums[mid] == 2` → swap with `high`, decrease `high` (don't advance `mid`)

### Java Solution

```java
class Solution {
    public void sortColors(int[] nums) {
        int low = 0, mid = 0, high = nums.length - 1;

        while (mid <= high) {
            if (nums[mid] == 0) {
                int tmp = nums[low]; nums[low] = nums[mid]; nums[mid] = tmp;
                low++; mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                int tmp = nums[mid]; nums[mid] = nums[high]; nums[high] = tmp;
                high--;
            }
        }
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---
