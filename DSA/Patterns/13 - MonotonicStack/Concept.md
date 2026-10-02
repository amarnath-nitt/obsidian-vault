# Monotonic Stack — Concept

## What Is It?

A Monotonic Stack maintains elements in strictly increasing or decreasing order. When a new element violates the monotonic property, we pop elements from the stack. This pattern efficiently solves **"next greater/smaller element"** problems in O(n).

---

## When to Use

> **Trigger keywords:** "next greater element", "next smaller", "previous greater", "daily temperatures", "stock span", "largest rectangle"

---

## Variants

### 1. Next Greater Element (Decreasing Stack)
```java
int[] result = new int[n];
Arrays.fill(result, -1);
Stack<Integer> stack = new Stack<>(); // stores indices

for (int i = 0; i < n; i++) {
    while (!stack.isEmpty() && nums[stack.peek()] < nums[i]) {
        result[stack.pop()] = nums[i];
    }
    stack.push(i);
}
```

### 2. Previous Smaller Element (Increasing Stack)
```java
int[] prevSmaller = new int[n];
Stack<Integer> stack = new Stack<>();

for (int i = 0; i < n; i++) {
    while (!stack.isEmpty() && nums[stack.peek()] >= nums[i]) {
        stack.pop();
    }
    prevSmaller[i] = stack.isEmpty() ? -1 : stack.peek();
    stack.push(i);
}
```

---

## Visual Walkthrough

### Daily Temperatures: `[73, 74, 75, 71, 69, 72, 76, 73]`
```
i=0: stack=[73]           result=[_,_,_,_,_,_,_,_]
i=1: 74>73 → pop 73      result=[1,_,_,_,_,_,_,_]
     stack=[74]
i=2: 75>74 → pop 74      result=[1,1,_,_,_,_,_,_]
     stack=[75]
i=3: 71<75                result=[1,1,_,_,_,_,_,_]
     stack=[75,71]
i=4: 69<71                stack=[75,71,69]
i=5: 72>69 → pop 69      result=[1,1,_,_,1,_,_,_]
     72>71 → pop 71      result=[1,1,_,2,1,_,_,_]
     stack=[75,72]
i=6: 76>72 → pop 72      result=[1,1,_,2,1,1,_,_]
     76>75 → pop 75      result=[1,1,4,2,1,1,_,_]
     stack=[76]
i=7: 73<76                stack=[76,73]

Final: [1,1,4,2,1,1,0,0]
```

---

## Time/Space Complexity

| Metric | Complexity |
|--------|-----------|
| Time | O(n) — each element pushed/popped at most once |
| Space | O(n) for stack |

---

## Common Mistakes

1. **Storing values instead of indices** → Store indices to calculate distances
2. **Wrong monotonic direction** → Decreasing stack for "next greater", increasing for "next smaller"
3. **Not handling remaining stack elements** → Elements left in stack have no next greater/smaller

---

## Related Patterns

- [[15 - TopKElements/Concept|Top K Elements]] — Sometimes monotonic stack + heap combined
- [[06 - SlidingWindow/Concept|Sliding Window]] — Sliding Window Maximum uses monotonic deque

---

#monotonic-stack #stack #dsa #concept
