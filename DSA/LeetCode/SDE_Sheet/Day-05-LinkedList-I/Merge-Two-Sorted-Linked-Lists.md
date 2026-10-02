# Merge Two Sorted Linked Lists

**LeetCode 21** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/merge-two-sorted-lists/)

### Problem
Merge two sorted linked lists into one sorted list.

### Approach

- Use a **dummy head** to simplify edge cases
- Compare list1 and list2 node by node, attach smaller one
- Attach remaining list at end

### Java Solution

```java
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;

        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) { curr.next = l1; l1 = l1.next; }
            else                  { curr.next = l2; l2 = l2.next; }
            curr = curr.next;
        }
        curr.next = (l1 != null) ? l1 : l2;
        return dummy.next;
    }
}
```

**Complexity:** Time O(m+n) · Space O(1)

---
