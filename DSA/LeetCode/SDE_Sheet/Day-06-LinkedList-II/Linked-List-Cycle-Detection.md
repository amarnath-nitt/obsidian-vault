# Linked List Cycle Detection

**LeetCode 141** (Detect) · **142** (Find start) · Medium
🔗 [LC 141](https://leetcode.com/problems/linked-list-cycle/) · [LC 142](https://leetcode.com/problems/linked-list-cycle-ii/)

### Problem
- 141: Does the list have a cycle?
- 142: If yes, return the node where the cycle begins.

### Approach (Floyd's Cycle Detection)

**Step 1:** Use slow/fast pointers. If they meet → cycle exists.

**Step 2 (find start):** After meeting:
- Move `slow` back to `head`
- Move both `slow` and `fast` one step at a time
- They will meet at the **cycle start**

**Why does this work?**
If fast traveled `2d` and slow traveled `d`, and cycle length is `c`:
`d = n*c` for some integer n → distance from head to cycle start = distance from meeting point to cycle start.

### Java Solution

```java
// LC 141 — Detect
public boolean hasCycle(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) return true;
    }
    return false;
}

// LC 142 — Find cycle start
public ListNode detectCycle(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) {
            slow = head;
            while (slow != fast) {
                slow = slow.next;
                fast = fast.next;
            }
            return slow;
        }
    }
    return null;
}
```

**Complexity:** Time O(n) · Space O(1)

---
