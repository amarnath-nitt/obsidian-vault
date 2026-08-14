# Min Stack

**LeetCode Problem:** [155. Min Stack](https://leetcode.com/problems/min-stack/)  
**Difficulty:** Medium  
**Topic:** Design, Stack, Data Structure

---

## Problem Statement

Design a stack that supports push, pop, top, and retrieving the minimum element in **constant time**.

Implement the `MinStack` class:

- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element val onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with **O(1)** time complexity for each function.

---

## Examples

### Example 1:
```
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output:
[null,null,null,null,-3,null,0,-2]

Explanation:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

---

## Approach 1: Two Stacks

### Key Insights:
1. Use **two stacks**: one for all elements, one for tracking minimums
2. **Main Stack**: Normal stack operations
3. **Min Stack**: Only pushes when new minimum is found or equals current minimum
4. When popping, check if the value matches current minimum; if so, pop from min stack too

### Algorithm:
1. **push(val)**:
   - Push to main stack
   - If min stack is empty OR val <= current minimum, push to min stack
   
2. **pop()**:
   - Pop from main stack
   - If popped value equals current minimum, pop from min stack
   
3. **top()**:
   - Return top of main stack
   
4. **getMin()**:
   - Return top of min stack

---

## Java Implementation - Approach 1 (Two Stacks)

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
        
        // Push to minStack if it's empty or val is new minimum
        if (minStack.isEmpty() || val <= minStack.peek()) {
            minStack.push(val);
        }
    }
    
    public void pop() {
        int popped = stack.pop();
        
        // If popped element was the minimum, remove from minStack
        if (popped == minStack.peek()) {
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

### Complexity Analysis:
- **Time Complexity**: O(1) for all operations
- **Space Complexity**: O(n) - in worst case (strictly increasing sequence), both stacks store all elements

---

## Approach 2: Single Stack with Pairs

### Key Insights:
1. Store **pairs (value, current_min)** in a single stack
2. Each element knows what the minimum was at the time it was pushed

### Algorithm:
Each node stores:
- The actual value
- The minimum value at that point in the stack

---

## Java Implementation - Approach 2 (Stack of Pairs)

```java
class MinStack {
    private Stack<int[]> stack; // Each element: [value, min_at_this_point]
    
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

### Complexity Analysis:
- **Time Complexity**: O(1) for all operations
- **Space Complexity**: O(n) - stores pairs for each element

---

## Approach 3: Single Stack with Difference Technique (Space Optimized)

### Key Insights:
1. Store **difference** between value and current minimum
2. Only track one minimum variable
3. When difference is negative, we found a new minimum

### Algorithm:
- If `val < min`, push `val - min` (negative difference) and update min
- If `val >= min`, push `val - min` (non-negative difference)
- On pop, if top is negative, restore previous minimum

---

## Java Implementation - Approach 3 (Difference Technique)

```java
class MinStack {
    private Stack<Long> stack;
    private long min;
    
    public MinStack() {
        stack = new Stack<>();
    }
    
    public void push(int val) {
        if (stack.isEmpty()) {
            stack.push(0L);
            min = val;
        } else {
            // Push difference from current min
            stack.push((long) val - min);
            if (val < min) {
                min = val; // Update min
            }
        }
    }
    
    public void pop() {
        if (stack.isEmpty()) return;
        
        long top = stack.pop();
        
        // If top is negative, we need to restore previous min
        if (top < 0) {
            min = min - top; // Restore previous min
        }
    }
    
    public int top() {
        long top = stack.peek();
        
        if (top < 0) {
            return (int) min; // Current min is the actual top element
        } else {
            return (int) (min + top); // Actual value = min + difference
        }
    }
    
    public int getMin() {
        return (int) min;
    }
}
```

### Complexity Analysis:
- **Time Complexity**: O(1) for all operations
- **Space Complexity**: O(n) - single stack, but uses Long to handle overflow

---

## Comparison of Approaches

| Approach | Space | Pros | Cons |
|----------|-------|------|------|
| Two Stacks | O(n) worst, O(1) best | Simple, intuitive | Extra space for min stack |
| Stack of Pairs | O(2n) = O(n) | Always works, easy to understand | Stores 2 values per element |
| Difference Technique | O(n) | Space efficient, clever | Harder to understand, needs Long for overflow |

**Recommendation**: Use **Approach 1 (Two Stacks)** in interviews - it's clear, simple, and efficient.

---

## Key Points for Interviews

1. **Why O(1) is Required?**
   - If we scan the entire stack to find minimum, it would be O(n)
   - The challenge is maintaining minimum without scanning

2. **Why Use Two Stacks?**
   - One stack for normal operations
   - One stack to track minimum at each state
   - Min stack only stores values when a new minimum is encountered

3. **Edge Cases:**
   - Empty stack
   - Duplicate minimums
   - All elements are the same
   - Integer overflow (use Long in difference approach)

4. **Common Mistakes:**
   - Using `val < minStack.peek()` instead of `val <= minStack.peek()` (fails with duplicates)
   - Not checking if stack is empty before peek/pop
   - Not restoring previous minimum correctly in difference approach

5. **Follow-up Questions:**
   - How would you implement MaxStack?
   - Can you support getMax() as well?
   - How would you implement this with a linked list?

---

## Test Cases

```java
public class MinStackTest {
    public static void main(String[] args) {
        MinStack minStack = new MinStack();
        
        // Test 1: Basic operations
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        System.out.println(minStack.getMin()); // -3
        minStack.pop();
        System.out.println(minStack.top());    // 0
        System.out.println(minStack.getMin()); // -2
        
        // Test 2: Duplicate minimums
        MinStack stack2 = new MinStack();
        stack2.push(0);
        stack2.push(1);
        stack2.push(0);
        System.out.println(stack2.getMin()); // 0
        stack2.pop();
        System.out.println(stack2.getMin()); // 0
    }
}
```

---

## Related Problems

- [[LRU-Cache|146. LRU Cache]]
- [716. Max Stack](https://leetcode.com/problems/max-stack/)
- [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

---

## Tags

`#design` `#stack` `#data-structure` `#medium` `#two-stacks` `#constant-time`
