# Day 13 — Stack & Queue I

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** Stack & Queue — Monotonic Stack, NGE
**Difficulty Mix:** Easy / Medium

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Valid Parentheses](Valid-Parentheses.md) | LeetCode 20 | Easy | [LeetCode](https://leetcode.com/problems/valid-parentheses/)
- [ ] [Next Greater Element I](Next-Greater-Element-I.md) | LeetCode 496 | Easy | [LeetCode](https://leetcode.com/problems/next-greater-element-i/)
- [ ] [Next Greater Element II (Circular)](Next-Greater-Element-II-Circular.md) | LeetCode 503 | Medium | [LeetCode](https://leetcode.com/problems/next-greater-element-ii/)
- [ ] [Largest Rectangle in Histogram](Largest-Rectangle-in-Histogram.md) | LeetCode 84 | Hard | [LeetCode](https://leetcode.com/problems/largest-rectangle-in-histogram/)
- [ ] [Min Stack](Min-Stack.md) | LeetCode 155 | Medium | [LeetCode](https://leetcode.com/problems/min-stack/)
- [ ] [Implement Queue using Stacks](Implement-Queue-using-Stacks.md) | LeetCode 232 | Easy | [LeetCode](https://leetcode.com/problems/implement-queue-using-stacks/)

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
