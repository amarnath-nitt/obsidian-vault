# Check if Linked List is Palindrome

**LeetCode 234** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/palindrome-linked-list/)

### Problem
Determine if the linked list is a palindrome. O(n) time, O(1) space.

### Approach (3 steps)

1. **Find middle** using slow-fast pointers
2. **Reverse** the second half
3. **Compare** first half with reversed second half
4. (Optional) Restore the list

### Java Solution

```java
class Solution {
    public boolean isPalindrome(ListNode head) {
        // Step 1: Find middle
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Step 2: Reverse second half
        ListNode prev = null, curr = slow;
        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        // Step 3: Compare
        ListNode left = head, right = prev;
        while (right != null) {
            if (left.val != right.val) return false;
            left = left.next;
            right = right.next;
        }
        return true;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---
