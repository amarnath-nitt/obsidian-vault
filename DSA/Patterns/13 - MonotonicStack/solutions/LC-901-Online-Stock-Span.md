# Online Stock Span (LC 901)

**Difficulty**: Medium  
**Pattern**: Monotonic Stack  
**LeetCode**: https://leetcode.com/problems/online-stock-span/

## Problem Statement
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.
The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward) for which the stock price was less than or equal to today's price.

**Example:**
```
Input: [100, 80, 60, 70, 60, 75, 85]
Output: [1, 1, 1, 2, 1, 4, 6]
```

## Approach: Monotonic Stack (Decreasing)

### Intuition
We want to find the first previous day with price > current price.
Stack pairs: `{price, span}`.
When `currentPrice >= stack.peek().price`, pop and add `stack.peek().span` to current span.
This effectively "merges" ranges of smaller prices.

### Java Code
```java
class StockSpanner {
    Deque<int[]> stack;

    public StockSpanner() {
        stack = new ArrayDeque<>();
    }
    
    public int next(int price) {
        int span = 1;
        while (!stack.isEmpty() && stack.peek()[0] <= price) {
            span += stack.pop()[1];
        }
        stack.push(new int[]{price, span});
        return span;
    }
}
```

### Complexity
- **Time**: O(1) amortized
- **Space**: O(N)

## Key Takeaways
- Merging intervals/counts using stack
- Amortized analysis: each element pushed once, popped once
