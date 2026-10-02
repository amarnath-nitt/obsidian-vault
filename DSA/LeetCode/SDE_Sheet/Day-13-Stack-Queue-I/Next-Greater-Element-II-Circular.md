# Next Greater Element II (Circular)

**LeetCode 503** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/next-greater-element-ii/)

### Problem
Find the next greater element for each element in a circular array.

### Approach

- Traverse the array **twice** (simulate circular using `i % n`)
- Only update result in the first pass

### Java Solution

```java
class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        Arrays.fill(result, -1);
        Deque<Integer> stack = new ArrayDeque<>(); // stores indices

        for (int i = 0; i < 2 * n; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] < nums[i % n]) {
                result[stack.pop()] = nums[i % n];
            }
            if (i < n) stack.push(i);
        }
        return result;
    }
}
```

**Complexity:** Time O(n) · Space O(n)

---
