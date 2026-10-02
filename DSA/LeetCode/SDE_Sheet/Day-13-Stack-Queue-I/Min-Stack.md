# Min Stack

**LeetCode 155** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/min-stack/)

### Problem
Design a stack that supports push, pop, top, and getMin in O(1).

### Approach

- Use **two stacks**: one for data, one for minimums
- Push to min stack only when new element ≤ current min

### Java Solution

```java
class MinStack {
    Deque<Integer> stack = new ArrayDeque<>();
    Deque<Integer> minStack = new ArrayDeque<>();

    public void push(int val) {
        stack.push(val);
        if (minStack.isEmpty() || val <= minStack.peek())
            minStack.push(val);
    }

    public void pop() {
        int val = stack.pop();
        if (val == minStack.peek()) minStack.pop();
    }

    public int top() { return stack.peek(); }

    public int getMin() { return minStack.peek(); }
}
```

**Complexity:** All operations O(1)

---
