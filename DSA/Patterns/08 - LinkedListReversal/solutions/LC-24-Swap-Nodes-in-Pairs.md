# Swap Nodes in Pairs (LC 24)

**Difficulty**: Medium  
**Pattern**: Linked List Reversal  
**LeetCode**: https://leetcode.com/problems/swap-nodes-in-pairs/

## Problem Statement
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed).

**Example:**
```
Input: head = [1,2,3,4]
Output: [2,1,4,3]
```

## Approach 1: Iterative

### Intuition
Equivalent to `Reverse Nodes in k-Group` with `k=2`.
Use a dummy node.
Current sequence: `pre -> a -> b -> rest`
Goal: `pre -> b -> a -> rest`
Update pointers:
1. `pre.next = b`
2. `a.next = b.next`
3. `b.next = a`
4. `pre = a`, `head = a.next` (for next iteration)

### Java Code
```java
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode pre = dummy;
        
        while (pre.next != null && pre.next.next != null) {
            ListNode a = pre.next;
            ListNode b = pre.next.next;
            
            // Swap
            a.next = b.next;
            b.next = a;
            pre.next = b;
            
            // Move forward
            pre = a;
        }
        
        return dummy.next;
    }
}
```

## Approach 2: Recursive

### Intuition
`swap(head)` should return `head.next` (new head).
`head.next` should point to `swap(head.next.next)`.
`newHead.next` should point to `head`.

### Java Code
```java
class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        ListNode second = head.next;
        head.next = swapPairs(second.next);
        second.next = head;
        
        return second;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(1) iterative, O(N) recursive stack

## Key Takeaways
- Special case of k-Group Reversal
- Recursive solution is very elegant for LL problems
