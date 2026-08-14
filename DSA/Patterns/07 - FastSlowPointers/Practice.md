# Fast & Slow Pointers - Practice Notes

## Pattern Overview
Also known as Floyd's Cycle Detection or "Tortoise and Hare" algorithm. Uses two pointers moving at different speeds.

## Key Concepts
- **Fast Pointer**: Moves 2 steps at a time
- **Slow Pointer**: Moves 1 step at a time
- **Cycle Detection**: If there's a cycle, pointers will meet
- **Middle Finding**: When fast reaches end, slow is at middle

## Template Code

### Cycle Detection
```java
public boolean hasCycle(ListNode head) {
    ListNode slow = head, fast = head;
    
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) return true;
    }
    return false;
}
```

### Find Middle
```java
public ListNode findMiddle(ListNode head) {
    ListNode slow = head, fast = head;
    
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
    }
    return slow;
}
```

## Practice Problems

### Easy
- [ ] [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (LC 141) → [Solution](solutions/LC-141-Linked-List-Cycle.md) | [Blind75](../../LeetCode/Blind75/Linked-Lists/Linked-List-Cycle.md)
- [ ] [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) (LC 876) → [Solution](solutions/LC-876-Middle-of-Linked-List.md)
- [ ] [Happy Number](https://leetcode.com/problems/happy-number/) (LC 202) → [Solution](solutions/LC-202-Happy-Number.md)

### Medium
- [ ] [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) (LC 142) → [Solution](solutions/LC-142-Linked-List-Cycle-II.md)
- [ ] [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) (LC 234) → [Solution](solutions/LC-234-Palindrome-Linked-List.md)
- [ ] [Reorder List](https://leetcode.com/problems/reorder-list/) (LC 143) → [Solution](solutions/LC-143-Reorder-List.md)
- [ ] [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) (LC 287) → [Solution](solutions/LC-287-Find-Duplicate-Number.md)

## Reference
[LeetCode Pattern Guide](https://lnkd.in/gcYz5kKj)
