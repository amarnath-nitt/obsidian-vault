---
solved: false
difficulty: Hard
pattern: Linked List Reversal
lc_number: 25
date_solved: 
tags:
  - dsa
  - linked-list-reversal
  - hard
---
# Reverse Nodes in k-Group (LC 25)

**Difficulty**: Hard  
**Pattern**: Linked List Reversal  
**LeetCode**: https://leetcode.com/problems/reverse-nodes-in-k-group/

## Problem Statement
Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.
`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

**Example:**
```
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
```

## Approach: Iterative Reversal in Chunks

### Intuition
1. Count nodes. If count < k, done.
2. Reverse next `k` nodes.
   - Use standard reversal logic strictly for `k` steps.
   - Keep track of `pre` (node before group), `curr` (first node of group), `next` (node after group).
3. Connect `pre.next` to new head of reversed group.
4. `curr` becomes the tail of reversed group. Connect `curr.next` to the renaming list.
5. Update `pre` to `curr` and repeat.

### Java Code
```java
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || k == 1) return head;
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        ListNode curr = head;
        int count = 0;
        while (curr != null) {
            curr = curr.next;
            count++;
        }
        
        ListNode pre = dummy;
        curr = head;
        
        while (count >= k) {
            curr = pre.next; // First node of group
            ListNode next = curr.next;
            
            // Reverse k-1 links
            for (int i = 1; i < k; i++) {
                curr.next = next.next;
                next.next = pre.next;
                pre.next = next;
                next = curr.next;
            }
            
            pre = curr;
            count -= k;
        }
        
        return dummy.next;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(1)

## Key Takeaways
- Extension of "Reverse Linked List II" logic
- Count total nodes first to know when to stop
- Maintain `pre` pointer carefully between groups
