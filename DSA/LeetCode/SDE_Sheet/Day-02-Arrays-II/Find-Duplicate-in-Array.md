# Find Duplicate in Array

**LeetCode 287** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/find-the-duplicate-number/)

### Problem
Array of `n+1` integers in range `[1,n]`. Find the one duplicate without modifying the array. O(1) extra space.

### Approach (Floyd's Cycle Detection)

- Treat array as a **linked list** where `index → nums[index]`
- Since there's a duplicate, there must be a cycle
- Use **slow/fast pointers** to detect cycle entry point

```
Phase 1: Find intersection inside cycle
  slow = nums[slow], fast = nums[nums[fast]]
Phase 2: Find cycle entry (= duplicate)
  Move slow from head, keep fast at intersection, both move 1 step
```

### Java Solution

```java
class Solution {
    public int findDuplicate(int[] nums) {
        // Phase 1: Detect cycle
        int slow = nums[0], fast = nums[0];
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);

        // Phase 2: Find entry point
        slow = nums[0];
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---
