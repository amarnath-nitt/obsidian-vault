# Rotate List (LC 61)

**Difficulty**: Medium  
**Pattern**: Linked List Reversal / Manipulation  
**LeetCode**: https://leetcode.com/problems/rotate-list/

## Problem Statement
Given the `head` of a linked list, rotate the list to the right by `k` places.

**Example:**
```
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
```

## Approach: Circular List

### Intuition
Rotating by `k` is equivalent to cutting the list at `length - k` (modulo length) and appending the first part to the end.
1. Find length `len` and tail.
2. Connect tail to head (make it circular).
3. Move `len - (k % len)` steps from head to find new tail.
4. Break the circle: `newHead = newTail.next`, `newTail.next = null`.

### Java Code
```java
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0) return head;
        
        // 1. Find length and tail
        ListNode tail = head;
        int len = 1;
        while (tail.next != null) {
            tail = tail.next;
            len++;
        }
        
        // 2. Normalize k
        k = k % len;
        if (k == 0) return head;
        
        // 3. Connect tail to head
        tail.next = head;
        
        // 4. Find new tail (len - k steps from start)
        // Since we are at old tail, we can move len - k steps from THERE? 
        // No, from head it is len - k - 1?
        // Let's just iterate from head for clarity or continue from tail.
        // Actually simpler: iterate len - k steps from old head.
        
        ListNode newTail = head;
        for (int i = 0; i < len - k - 1; i++) {
            newTail = newTail.next;
        }
        
        ListNode newHead = newTail.next;
        newTail.next = null;
        
        return newHead;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(1)

## Key Takeaways
- `k` can be larger than length, use modulo
- Circular connection simplifies logic (no need to maintain separate pointers for new tail/new head initially)
