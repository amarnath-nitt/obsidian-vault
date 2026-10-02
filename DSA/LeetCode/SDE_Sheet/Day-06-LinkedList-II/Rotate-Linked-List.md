# Rotate Linked List

**LeetCode 61** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/rotate-list/)

### Problem
Rotate the list to the right by k places.

### Approach

1. Find **length** and connect tail to head (make circular)
2. Effective rotation = `k % length`
3. Move to `(length - k%length - 1)` position → that's the new tail
4. Break the circle there

### Java Solution

```java
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0) return head;

        // Find length and tail
        ListNode tail = head;
        int len = 1;
        while (tail.next != null) { tail = tail.next; len++; }

        // Make circular
        tail.next = head;

        // Find new tail (position len - k%len - 1)
        int stepsToNewTail = len - k % len - 1;
        ListNode newTail = head;
        for (int i = 0; i < stepsToNewTail; i++) newTail = newTail.next;

        ListNode newHead = newTail.next;
        newTail.next = null;
        return newHead;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---
