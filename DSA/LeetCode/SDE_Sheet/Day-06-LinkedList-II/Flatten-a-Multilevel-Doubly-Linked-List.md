# Flatten a Multilevel Doubly Linked List

**LeetCode 430** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)

### Problem
Flatten a doubly linked list where each node can have a `child` pointer.

### Approach

- When we encounter a node with a `child`:
  1. Save the current `next`
  2. Connect current node to child
  3. Traverse to the **end of the child list**
  4. Connect end of child list to saved `next`

### Java Solution

```java
class Solution {
    public Node flatten(Node head) {
        Node curr = head;
        while (curr != null) {
            if (curr.child != null) {
                Node child = curr.child;
                Node next = curr.next;

                curr.next = child;
                child.prev = curr;
                curr.child = null;

                // Find tail of child list
                Node tail = child;
                while (tail.next != null) tail = tail.next;

                tail.next = next;
                if (next != null) next.prev = tail;
            }
            curr = curr.next;
        }
        return head;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---
