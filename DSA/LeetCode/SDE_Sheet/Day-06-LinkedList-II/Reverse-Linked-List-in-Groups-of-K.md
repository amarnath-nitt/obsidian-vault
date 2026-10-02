# Reverse Linked List in Groups of K

**LeetCode 25** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/reverse-nodes-in-k-group/)

### Problem
Reverse the list k nodes at a time. If remaining < k, leave as is.

### Approach

1. Check if k nodes exist ahead
2. Reverse k nodes (standard reverse with 3 pointers)
3. Connect the reversed segment to the rest
4. Recurse/iterate for next group

### Java Solution

```java
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode curr = head;
        int count = 0;

        // Check if k nodes exist
        while (curr != null && count < k) { curr = curr.next; count++; }
        if (count < k) return head;

        // Reverse k nodes
        ListNode prev = null; curr = head;
        for (int i = 0; i < k; i++) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        // head is now the tail of reversed group
        head.next = reverseKGroup(curr, k);
        return prev; // prev is new head
    }
}
```

**Complexity:** Time O(n) · Space O(n/k) recursive stack

---
