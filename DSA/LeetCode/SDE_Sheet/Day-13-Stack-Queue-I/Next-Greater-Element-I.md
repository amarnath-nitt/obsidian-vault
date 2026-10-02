# Next Greater Element I

**LeetCode 496** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/next-greater-element-i/)

### Problem
For each element in `nums1`, find the next greater element in `nums2`.

### Approach (Monotonic Stack)

- Process `nums2` left to right with a **monotonic decreasing stack**
- When we find an element greater than stack top → that's the NGE
- Store results in a map

### Java Solution

```java
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer, Integer> nge = new HashMap<>();
        Deque<Integer> stack = new ArrayDeque<>();

        for (int num : nums2) {
            while (!stack.isEmpty() && stack.peek() < num) {
                nge.put(stack.pop(), num); // num is NGE of popped element
            }
            stack.push(num);
        }

        int[] result = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++)
            result[i] = nge.getOrDefault(nums1[i], -1);
        return result;
    }
}
```

**Complexity:** Time O(n+m) · Space O(n)

---
