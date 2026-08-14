# Min Stack

**Difficulty:** Medium  
**Category:** Stack  
**LeetCode Link:** [Min Stack](https://leetcode.com/problems/min-stack/)

---

## Problem Statement

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element val onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with **O(1)** time complexity for each function.

**Example:**
```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

**Constraints:**
- `-2^31 <= val <= 2^31 - 1`
- Methods `pop`, `top` and `getMin` will always be called on non-empty stacks.
- At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`.

---

## Intuition

The challenge is maintaining the minimum element in O(1) time. We need to track the minimum at each level of the stack.

---

## Approach 1: Track Min with Each Element (Naive)

### Algorithm
1. Store pairs of (value, current_min) for each element
2. When pushing, calculate new min
3. When popping, previous min is automatically maintained

### Java Code
```java
class MinStack {
    private Stack<int[]> stack;  // [value, min_at_this_level]
    
    public MinStack() {
        stack = new Stack<>();
    }
    
    public void push(int val) {
        if (stack.isEmpty()) {
            stack.push(new int[]{val, val});
        } else {
            int currentMin = Math.min(val, stack.peek()[1]);
            stack.push(new int[]{val, currentMin});
        }
    }
    
    public void pop() {
        stack.pop();
    }
    
    public int top() {
        return stack.peek()[0];
    }
    
    public int getMin() {
        return stack.peek()[1];
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(1) for all operations
- **Space Complexity:** O(n) - Stores 2 integers per element

### Drawbacks
- Uses 2x space (stores min with each element)
- Can be optimized

---

## Approach 2: Separate Min Stack (Optimized)

### Algorithm
1. Use two stacks: main stack and min stack
2. Min stack only stores values when they're new minimums
3. Both stacks stay synchronized

### Java Code
```java
class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> minStack;
    
    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }
    
    public void push(int val) {
        stack.push(val);
        
        // Only push to minStack if it's a new minimum
        if (minStack.isEmpty() || val <= minStack.peek()) {
            minStack.push(val);
        }
    }
    
    public void pop() {
        int val = stack.pop();
        
        // Remove from minStack if it was the minimum
        if (val == minStack.peek()) {
            minStack.pop();
        }
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(1) for all operations
- **Space Complexity:** O(n) - But typically uses less space than approach 1

### Why This is Better
- ✅ O(1) time for all operations
- ✅ More space-efficient in practice
- ✅ Clean separation of concerns
- ✅ Min stack only grows when necessary

---

## Key Takeaways

1. **Pattern:** Auxiliary data structure to track metadata
2. **Two stacks:** Main stack + min stack work together
3. **Synchronization:** Keep stacks aligned during push/pop
4. **Optimization:** Only store mins when they change

---

## Edge Cases

- Single element: Min is that element
- All same values: Min stack mirrors main stack
- Decreasing sequence: Min stack mirrors main stack
- Increasing sequence: Min stack has only first element

---

## Related Problems
- [[Max-Stack]] - Similar but for maximum
- [[Stack-With-Increment]] - Another stack design problem

---

## Tags
#stack #design #medium #blind75
