# Jump Game

**LeetCode 55** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/jump-game/)

### Problem
Given jump lengths, can you reach the last index?

### Approach (Greedy)

- Track `maxReach` = farthest index reachable so far
- If current index > maxReach → stuck, return false

### Java Solution

```java
class Solution {
    public boolean canJump(int[] nums) {
        int maxReach = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > maxReach) return false;
            maxReach = Math.max(maxReach, i + nums[i]);
        }
        return true;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---
