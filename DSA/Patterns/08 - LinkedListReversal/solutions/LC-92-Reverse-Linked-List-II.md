---
solved: false
difficulty: Medium
pattern: Linked List Reversal
lc_number: 92
date_solved: 
tags:
  - dsa
  - linked-list-reversal
  - medium
---
# Reverse Linked List II (LC 92)

**Difficulty**: Medium  
**Pattern**: Linked List Reversal  
**LeetCode**: https://leetcode.com/problems/reverse-linked-list-ii/

## Problem Statement
Given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return the reversed list.

**Example:**
```
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
```

## Approach: Iterative Reversal

### Intuition
1. Skip the first `left - 1` nodes to reach the node just before the reversal part (`pre`).
2. Reverse the sublist from `left` to `right`.
   - Use three pointers (prev, curr, next) logic inside the sublist.
   - Or standard "extract and move to front" logic:
     - `curr` is node at `left`. `next` is `curr.next`.
     - Move `next` to be after `pre`.
     - Repeat `right - left` times.
3. Connect the reversed part back to the rest of the list.

### Java Code
```java
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head == null || left == right) return head;
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode pre = dummy;
        
        // Move pre to the node before 'left'
        for (int i = 0; i < left - 1; i++) {
            pre = pre.next;
        }
        
        // Start Reversing
        ListNode curr = pre.next;
        // Example: 1(pre) -> 2(curr) -> 3(next) -> 4
        // Loop runs right - left times
        for (int i = 0; i < right - left; i++) {
            ListNode next = curr.next;
            curr.next = next.next;
            next.next = pre.next;
            pre.next = next;
        }
        
        return dummy.next;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(1)

## Key Takeaways
- Use a Dummy node to handle edge case where `left=1`.
- "Inject" node to the front of the sublist repeatedly to reverse in-place.
