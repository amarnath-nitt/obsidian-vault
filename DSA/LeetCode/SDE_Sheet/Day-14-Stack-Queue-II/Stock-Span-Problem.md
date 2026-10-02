# Stock Span Problem

**LeetCode 901** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/online-stock-span/)

### Problem
For each day's price, find the number of consecutive days (including today) where price ≤ today's price.

### Approach (Monotonic Stack)

- Stack stores `(price, span)` pairs
- When today's price ≥ stack top → absorb its span

### Java Solution

```java
class StockSpanner {
    Deque<int[]> stack = new ArrayDeque<>(); // [price, span]

    public int next(int price) {
        int span = 1;
        while (!stack.isEmpty() && stack.peek()[0] <= price) {
            span += stack.pop()[1]; // absorb previous spans
        }
        stack.push(new int[]{price, span});
        return span;
    }
}
```

**Complexity:** Amortized O(1) per call

---
