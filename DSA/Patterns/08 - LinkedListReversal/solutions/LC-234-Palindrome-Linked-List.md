# Palindrome Linked List

[Problem Link](https://leetcode.com/problems/palindrome-linked-list/)

## Problem Statement
Given the `head` of a singly linked list, return `true` if it is a palindrome.

## Approach
1.  Find the middle of the linked list using Fast & Slow pointers.
2.  Reverse the second half of the linked list.
3.  Compare the first half and the reversed second half.
4.  (Optional) Restore the list.

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```java
class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) return true;
        
        // Find middle
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // Reverse second half
        ListNode secondHalf = reverse(slow);
        ListNode copySecondHalf = secondHalf; // To restore later if needed
        
        // Compare
        ListNode p1 = head;
        ListNode p2 = secondHalf;
        boolean isPal = true;
        
        while (p2 != null) {
            if (p1.val != p2.val) {
                isPal = false;
                break;
            }
            p1 = p1.next;
            p2 = p2.next;
        }
        
        // Restore (optional)
        // reverse(copySecondHalf);
        
        return isPal;
    }
    
    private ListNode reverse(ListNode head) {
        ListNode prev = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = prev;
            prev = head;
            head = next;
        }
        return prev;
    }
}
```
