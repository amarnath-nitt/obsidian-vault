# Reorder List

**Difficulty:** Medium  
**Category:** Linked Lists  
**LeetCode Link:** [Reorder List](https://leetcode.com/problems/reorder-list/)

---

## Problem Statement

You are given the head of a singly linked-list. Reorder the list to be: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

**Example 1:**
```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

**Example 2:**
```
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

**Constraints:**
- The number of nodes in the list is in the range `[1, 5 * 10^4]`.
- `1 <= Node.val <= 1000`

---

## Intuition

Split the list in half, reverse the second half, then merge the two halves alternately.

---

## Approach: Find Middle + Reverse + Merge

### Algorithm
1. Find the middle of the list (slow/fast pointers)
2. Reverse the second half
3. Merge the two halves alternately

### Java Code
```java
class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) return;
        
        // Step 1: Find middle
        ListNode slow = head, fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // Step 2: Reverse second half
        ListNode second = reverse(slow.next);
        slow.next = null;  // Split the list
        
        // Step 3: Merge two halves
        ListNode first = head;
        while (second != null) {
            ListNode temp1 = first.next;
            ListNode temp2 = second.next;
            
            first.next = second;
            second.next = temp1;
            
            first = temp1;
            second = temp2;
        }
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

### Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## Key Takeaways

1. **Pattern:** Find middle + Reverse + Merge
2. **Three steps:** Break down complex problem
3. **In-place:** No extra space needed

---

## Tags
#linked-lists #two-pointers #medium #blind75
