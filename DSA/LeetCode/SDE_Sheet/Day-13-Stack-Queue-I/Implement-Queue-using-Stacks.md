# Implement Queue using Stacks

**LeetCode 232** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/implement-queue-using-stacks/)

### Problem
Implement a queue using only stacks.

### Approach (Amortized O(1))

- Use two stacks: `inbox` and `outbox`
- Push to `inbox`
- Pop: if `outbox` is empty, pour all of `inbox` into `outbox`, then pop from `outbox`

### Java Solution

```java
class MyQueue {
    Deque<Integer> inbox = new ArrayDeque<>();
    Deque<Integer> outbox = new ArrayDeque<>();

    public void push(int x) { inbox.push(x); }

    public int pop() {
        refill();
        return outbox.pop();
    }

    public int peek() {
        refill();
        return outbox.peek();
    }

    public boolean empty() { return inbox.isEmpty() && outbox.isEmpty(); }

    private void refill() {
        if (outbox.isEmpty())
            while (!inbox.isEmpty()) outbox.push(inbox.pop());
    }
}
```

**Complexity:** Amortized O(1) per operation

---
