# Task Scheduler

**LeetCode 621** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/task-scheduler/)

### Problem
Schedule tasks with cooldown n. Find minimum intervals needed.

### Approach (Greedy + Math)

- Most frequent task determines the structure
- `minTime = (maxFreq - 1) * (n + 1) + countOfMaxFreq`
- Answer = `max(minTime, tasks.length)` (can't be less than total tasks)

### Java Solution

```java
class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] freq = new int[26];
        for (char t : tasks) freq[t - 'A']++;
        Arrays.sort(freq);

        int maxFreq = freq[25];
        int countOfMax = 0;
        for (int f : freq) if (f == maxFreq) countOfMax++;

        int minTime = (maxFreq - 1) * (n + 1) + countOfMax;
        return Math.max(minTime, tasks.length);
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---
