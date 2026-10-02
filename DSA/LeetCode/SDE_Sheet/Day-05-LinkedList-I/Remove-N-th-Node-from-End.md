# Remove N-th Node from End

**LeetCode 19** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

### Problem
Remove the n-th node from the end of the list in one pass.

### Approach (Two Pointers — Gap of N)

- Move `fast` pointer n+1 steps ahead
- Move both `slow` and `fast` until `fast` is null
- `slow` now points to the node **before** the one to delete

### Java Solution

```java
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode slow = dummy, fast = dummy;

        // Move fast n+1 steps
        for (int i = 0; i <= n; i++) fast = fast.next;

        // Move both until fast is null
        while (fast != null) {
            slow = slow.next;
            fast = fast.next;
        }

        slow.next = slow.next.next;
        return dummy.next;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---
