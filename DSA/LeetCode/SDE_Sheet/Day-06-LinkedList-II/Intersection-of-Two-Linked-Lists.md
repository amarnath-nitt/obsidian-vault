# Intersection of Two Linked Lists

**LeetCode 160** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/intersection-of-two-linked-lists/)

### Problem
Find the node where two linked lists intersect. Return null if they don't intersect.

### Approach (Two Pointer — Equalize Distance)

- `pA` starts at `headA`, `pB` starts at `headB`
- When `pA` reaches end → redirect to `headB`
- When `pB` reaches end → redirect to `headA`
- They will meet at intersection (or both reach null)

**Why?** Both traverse `lenA + lenB` steps total — they equalize the "head distance" gap.

### Java Solution

```java
class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode a = headA, b = headB;
        while (a != b) {
            a = (a == null) ? headB : a.next;
            b = (b == null) ? headA : b.next;
        }
        return a;
    }
}
```

**Complexity:** Time O(m+n) · Space O(1)

---
