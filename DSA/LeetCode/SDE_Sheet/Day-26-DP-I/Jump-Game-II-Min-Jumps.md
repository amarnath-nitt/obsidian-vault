# Jump Game II (Min Jumps)

**LeetCode 45** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/jump-game-ii/)

### Problem
Find minimum number of jumps to reach the last index.

### Approach (Greedy — BFS levels)

- Track `currEnd` (farthest reachable in current jump) and `farthest`
- When we reach `currEnd` → must make another jump → `currEnd = farthest`

### Java Solution

```java
class Solution {
    public int jump(int[] nums) {
        int jumps = 0, currEnd = 0, farthest = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            farthest = Math.max(farthest, i + nums[i]);
            if (i == currEnd) { // exhausted current jump range
                jumps++;
                currEnd = farthest;
            }
        }
        return jumps;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---
