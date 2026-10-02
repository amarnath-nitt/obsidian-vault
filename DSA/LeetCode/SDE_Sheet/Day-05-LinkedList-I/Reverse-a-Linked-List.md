# Reverse a Linked List

**LeetCode 206** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/reverse-linked-list/)

### Problem
Reverse a singly linked list.

### Approach (Iterative — 3 Pointers)

- Maintain `prev = null`, `curr = head`, `next = null`
- At each step: save next, reverse the pointer, move forward

### Java Solution

```java
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null, curr = head;

        while (curr != null) {
            ListNode next = curr.next; // save next
            curr.next = prev;          // reverse pointer
            prev = curr;               // move prev
            curr = next;               // move curr
        }
        return prev;
    }
}
```

**Recursive:**
```java
public ListNode reverseList(ListNode head) {
    if (head == null || head.next == null) return head;
    ListNode rest = reverseList(head.next);
    head.next.next = head;
    head.next = null;
    return rest;
}
```

**Complexity:** Time O(n) · Space O(1) iterative / O(n) recursive

---
