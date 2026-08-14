# Day 13 — Stack & Queue I

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** Stack & Queue — Monotonic Stack, NGE
**Difficulty Mix:** Easy / Medium

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Valid Parentheses]] | 20 | Easy | ⬜ |
| 2 | [[#Next Greater Element I]] | 496 | Easy | ⬜ |
| 3 | [[#Next Greater Element II (Circular)]] | 503 | Medium | ⬜ |
| 4 | [[#Largest Rectangle in Histogram]] | 84 | Hard | ⬜ |
| 5 | [[#Min Stack]] | 155 | Medium | ⬜ |
| 6 | [[#Implement Queue using Stacks]] | 232 | Easy | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Valid Parentheses | Repeatedly remove matching pairs. O(n^2). | Use a stack for opening brackets. O(n). | Stack with early mismatch/odd-length exits. O(n), O(n) space. |
| Next Greater Element I | For each query, find it in nums2 and scan right. O(n*m). | Build index map, then scan right. O(n*m). | Monotonic stack precomputes next greater for nums2. O(n+m). |
| Next Greater Element II | For each index, scan circularly. O(n^2). | Duplicate the array and use a stack. O(n) extra. | Monotonic stack over 2*n indices. O(n). |
| Largest Rectangle in Histogram | Try every subarray and find minimum height. O(n^3). | Expand left/right for each bar. O(n^2). | Monotonic increasing stack. O(n). |
| Min Stack | Normal stack; scan for min on getMin. O(n). | Two stacks: values and current minimums. O(1). | Pair/encoded stack stores min with each push. O(1). |
| Implement Queue using Stacks | Move elements on every push or pop. O(n) each. | Use input/output stacks and transfer only when needed. | Amortized O(1) queue operations with two stacks. |

---

## Valid Parentheses

**LeetCode 20** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/valid-parentheses/)

### Approach

- Push opening brackets onto stack
- For closing bracket, check if top of stack matches

### Java Solution

```java
class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) return false;
                char top = stack.pop();
                if (c == ')' && top != '(') return false;
                if (c == '}' && top != '{') return false;
                if (c == ']' && top != '[') return false;
            }
        }
        return stack.isEmpty();
    }
}
```

**Complexity:** Time O(n) · Space O(n)

---

## Next Greater Element I

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

## Next Greater Element II (Circular)

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

## Largest Rectangle in Histogram

**LeetCode 84** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/largest-rectangle-in-histogram/)

### Problem
Given bar heights, find the largest rectangle area.

### Approach (Monotonic Increasing Stack)

- For each bar, find the **previous smaller** and **next smaller** bar
- Width = `nextSmaller[i] - prevSmaller[i] - 1`
- Area = `height[i] * width`

### Java Solution (One-pass)

```java
class Solution {
    public int largestRectangleArea(int[] heights) {
        Deque<Integer> stack = new ArrayDeque<>();
        int maxArea = 0;
        int n = heights.length;

        for (int i = 0; i <= n; i++) {
            int h = (i == n) ? 0 : heights[i];
            while (!stack.isEmpty() && heights[stack.peek()] > h) {
                int height = heights[stack.pop()];
                int width = stack.isEmpty() ? i : i - stack.peek() - 1;
                maxArea = Math.max(maxArea, height * width);
            }
            stack.push(i);
        }
        return maxArea;
    }
}
```

**Complexity:** Time O(n) · Space O(n)

> **Variant:** [Maximal Rectangle (LC 85)](https://leetcode.com/problems/maximal-rectangle/) — apply this histogram approach on each row.

---

## Min Stack

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

## Implement Queue using Stacks

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

## Monotonic Stack — The Pattern

```
Monotonic Decreasing Stack → find Next Greater Element
Monotonic Increasing Stack → find Next Smaller Element

Template for NGE:
  for each element:
    while stack not empty AND stack.top < current:
      result[stack.pop()] = current  // current is NGE
    stack.push(current)

Template for NSE:
  for each element:
    while stack not empty AND stack.top > current:
      result[stack.pop()] = current  // current is NSE
    stack.push(current)
```

#sde-sheet #stack #queue #monotonic-stack #day13
