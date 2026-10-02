# Delete a Given Node (no head access)

**LeetCode 237** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/delete-node-in-a-linked-list/)

### Problem
Delete a node given only access to that node (not the head). Not the tail.

### Approach

- **Copy** the next node's value into current node
- Then **skip** the next node

> We can't actually delete the current node, so we make it "become" the next node.

### Java Solution

```java
class Solution {
    public void deleteNode(ListNode node) {
        node.val = node.next.val;
        node.next = node.next.next;
    }
}
```

**Complexity:** Time O(1) · Space O(1)

---
