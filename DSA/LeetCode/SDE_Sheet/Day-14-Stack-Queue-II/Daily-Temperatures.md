# Daily Temperatures

**LeetCode 739** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/daily-temperatures/)

### Problem
For each day, find how many days until a warmer temperature.

### Approach (Monotonic Decreasing Stack of indices)

- While current temp > stack top → that's the warmer day for stack top
- `result[idx] = i - idx`

### Java Solution

```java
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] result = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
                int idx = stack.pop();
                result[idx] = i - idx;
            }
            stack.push(i);
        }
        return result;
    }
}
```

**Complexity:** Time O(n) · Space O(n)

---
