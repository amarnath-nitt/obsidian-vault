# Linked List Reversal — Concept

## What Is It?

In-place reversal of a linked list (or portion of it) by manipulating pointers. The key operation: for each node, point its `next` to the previous node instead of the next node.

---

## When to Use

> **Trigger keywords:** "reverse linked list", "reverse between", "swap pairs", "rotate list", "reorder list"

---

## Variants

### 1. Full Reversal (Iterative)
```java
ListNode prev = null, curr = head;
while (curr != null) {
    ListNode next = curr.next;
    curr.next = prev;
    prev = curr;
    curr = next;
}
return prev; // new head
```

### 2. Reverse Between Positions [m, n]
```java
// Skip to position m, then reverse n-m+1 nodes
ListNode dummy = new ListNode(0);
dummy.next = head;
ListNode pre = dummy;
for (int i = 1; i < m; i++) pre = pre.next;

ListNode curr = pre.next;
for (int i = 0; i < n - m; i++) {
    ListNode next = curr.next;
    curr.next = next.next;
    next.next = pre.next;
    pre.next = next;
}
```

### 3. Reverse in K-Groups
```java
// Reverse every k nodes
ListNode dummy = new ListNode(0);
dummy.next = head;
ListNode groupPrev = dummy;

while (true) {
    ListNode kth = getKth(groupPrev, k);
    if (kth == null) break;
    ListNode groupNext = kth.next;
    // reverse between groupPrev and groupNext
    reverse(groupPrev, groupNext);
    groupPrev = curr; // curr is now the tail
}
```

---

## Visual Walkthrough

```
Original:  1 → 2 → 3 → 4 → null

Step 1: prev=null, curr=1
        null ← 1   2 → 3 → 4
        
Step 2: prev=1, curr=2
        null ← 1 ← 2   3 → 4
        
Step 3: prev=2, curr=3
        null ← 1 ← 2 ← 3   4
        
Step 4: prev=3, curr=4
        null ← 1 ← 2 ← 3 ← 4

Result: 4 → 3 → 2 → 1 → null
```

---

## Time/Space Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Full reversal | O(n) | O(1) |
| Reverse between [m,n] | O(n) | O(1) |
| Reverse in K-groups | O(n) | O(1) |
| Recursive reversal | O(n) | O(n) stack |

---

## Common Mistakes

1. **Losing the reference to `next`** → Always save `curr.next` before overwriting
2. **Forgetting the dummy node** → Use a dummy for edge cases where head changes
3. **Not handling k < list length** → In K-group reversal, don't reverse the last group if < k nodes

---

## Related Patterns

- [[07 - FastSlowPointers/Concept|Fast & Slow Pointers]] — Find middle, then reverse second half (palindrome check)
- [[04 - TwoPointers/Concept|Two Pointers]] — Sometimes combined with reversal for reorder problems

---

#linked-list #reversal #dsa #concept
