# Sliding Window Maximum

**LeetCode 239** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/sliding-window-maximum/)

### Problem
Given array and window size k, find max in each window.

### Approach (Monotonic Deque)

- Maintain a **deque of indices** in decreasing order of values
- Remove indices outside the window from the front
- Remove smaller elements from the back (they can never be maximum)

### Java Solution

```java
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        int[] result = new int[n - k + 1];
        Deque<Integer> dq = new ArrayDeque<>(); // stores indices

        for (int i = 0; i < n; i++) {
            // Remove out-of-window indices
            while (!dq.isEmpty() && dq.peekFirst() < i - k + 1) dq.pollFirst();

            // Remove smaller elements from back
            while (!dq.isEmpty() && nums[dq.peekLast()] < nums[i]) dq.pollLast();

            dq.offerLast(i);

            if (i >= k - 1) result[i - k + 1] = nums[dq.peekFirst()];
        }
        return result;
    }
}
```

**Complexity:** Time O(n) · Space O(k)

---
