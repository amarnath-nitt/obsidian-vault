# Longest Consecutive Sequence

**LeetCode 128** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/longest-consecutive-sequence/)

### Problem
Find the length of the longest consecutive elements sequence. Must be O(n).

### Approach

- Add all elements to a **HashSet**
- For each number, check if it's the **start of a sequence** (`num-1` not in set)
- Count consecutive elements from there

### Java Solution

```java
class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int n : nums) set.add(n);

        int maxLen = 0;
        for (int n : set) {
            if (!set.contains(n - 1)) { // n is sequence start
                int len = 1;
                while (set.contains(n + len)) len++;
                maxLen = Math.max(maxLen, len);
            }
        }
        return maxLen;
    }
}
```

**Complexity:** Time O(n) · Space O(n)

---
