# Odd Even Linked List

[Problem Link](https://leetcode.com/problems/odd-even-linked-list/)

## Problem Statement
Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity.

## Approach
Use two pointers `odd` and `even`, and keep a reference to `evenHead`.
1.  `odd` points to head, `even` points to `head.next`.
2.  While `even` and `even.next` are not null:
    - `odd.next = even.next` (Link odd to next odd)
    - `odd = odd.next` (Move odd)
    - `even.next = odd.next` (Link even to next even)
    - `even = even.next` (Move even)
3.  Connect the end of odd list to `evenHead`.

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) {
        if (head == null) return null;
        
        ListNode odd = head;
        ListNode even = head.next;
        ListNode evenHead = even;
        
        while (even != null && even.next != null) {
            odd.next = even.next;
            odd = odd.next;
            
            even.next = odd.next;
            even = even.next;
        }
        
        odd.next = evenHead;
        
        return head;
    }
}
```
