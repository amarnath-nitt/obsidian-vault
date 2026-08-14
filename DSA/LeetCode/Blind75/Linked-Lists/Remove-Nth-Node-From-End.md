# Remove Nth Node From End of List

**Difficulty:** Medium  
**Category:** Linked Lists  
**LeetCode Link:** [Remove Nth Node From End](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

---

## Problem Statement

Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

**Example 1:**
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

**Example 2:**
```
Input: head = [1], n = 1
Output: []
```

**Constraints:**
- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

---

## Intuition

Use two pointers with a gap of `n` between them. When the fast pointer reaches the end, the slow pointer is at the node before the one to remove.

---

## Approach 1: Two Pass (Naive)

### Algorithm
1. First pass: count total nodes
2. Calculate position from start: `length - n`
3. Second pass: traverse to that position and remove

### Java Code
```java
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // Count length
        int length = 0;
        ListNode current = head;
        while (current != null) {
            length++;
            current = current.next;
        }
        
        // Edge case: remove head
        if (length == n) {
            return head.next;
        }
        
        // Find node before the one to remove
        current = head;
        for (int i = 0; i < length - n - 1; i++) {
            current = current.next;
        }
        
        // Remove node
        current.next = current.next.next;
        return head;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) - Two passes
- **Space Complexity:** O(1)

---

## Approach 2: One Pass with Two Pointers (Optimized)

### Algorithm
1. Use dummy node to handle edge cases
2. Fast pointer moves `n+1` steps ahead
3. Move both pointers until fast reaches end
4. Slow pointer is now before the node to remove

### Java Code
```java
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        ListNode fast = dummy;
        ListNode slow = dummy;
        
        // Move fast n+1 steps ahead
        for (int i = 0; i <= n; i++) {
            fast = fast.next;
        }
        
        // Move both until fast reaches end
        while (fast != null) {
            fast = fast.next;
            slow = slow.next;
        }
        
        // Remove node
        slow.next = slow.next.next;
        
        return dummy.next;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) - Single pass
- **Space Complexity:** O(1)

### Why This is Better
- ✅ Single pass vs two passes
- ✅ Dummy node simplifies edge cases
- ✅ More elegant solution

---

## Key Takeaways

1. **Pattern:** Two pointers with fixed gap
2. **Dummy node:** Handles removing head elegantly
3. **Gap of n+1:** Positions slow before node to remove
4. **One pass:** More efficient than counting first

---

## Tags
#linked-lists #two-pointers #medium #blind75
