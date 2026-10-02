# Find Middle of Linked List

**LeetCode 876** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/middle-of-the-linked-list/)

### Problem
Find the middle node of a linked list. If two middles, return the second.

### Approach (Slow-Fast Pointers / Floyd's)

- `slow` moves 1 step, `fast` moves 2 steps
- When `fast` reaches end, `slow` is at the middle

### Java Solution

```java
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---
