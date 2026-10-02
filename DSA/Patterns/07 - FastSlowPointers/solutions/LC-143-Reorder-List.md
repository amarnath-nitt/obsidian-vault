---
solved: false
difficulty: Medium
pattern: Fast Slow Pointers
lc_number: 143
date_solved: 
tags:
  - dsa
  - fast-slow-pointers
  - medium
---
# Reorder List (LC 143)

**Difficulty**: Medium  
**Pattern**: Fast & Slow Pointers  
**LeetCode**: https://leetcode.com/problems/reorder-list/

## Problem Statement
You are given the head of a singly linked-list. The list can be represented as:
`L0 → L1 → … → Ln - 1 → Ln`
Reorder the list to be on the following form:
`L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …`

**Example:**
```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

## Approach: Find Middle + Reverse + Merge

### Intuition
1. Find the middle of the linked list (Fast & Slow).
2. Reverse the second half of the list.
3. Merge the two halves alternately.

### Java Code
```java
class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) return;
        
        // 1. Find Middle
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // 2. Reverse Second Half
        ListNode prev = null, curr = slow.next, temp;
        slow.next = null; // Break list
        
        while (curr != null) {
            temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }
        
        // 3. Merge
        ListNode first = head, second = prev;
        while (second != null) {
             temp = first.next;
             first.next = second;
             first = temp;
             
             temp = second.next;
             second.next = first;
             second = temp;
        }
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(1)

## Key Takeaways
- Combination of 3 LL patterns: Middle, Reverse, Merge
