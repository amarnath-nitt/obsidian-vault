# Reverse Linked List (LC 206)

**Difficulty**: Easy  
**Pattern**: LinkedList In-place Reversal  
**LeetCode**: https://leetcode.com/problems/reverse-linked-list/

## Existing Solution Reference
Similar approach in Blind75: → [Reorder List](../../../LeetCode/Blind75/Linked-Lists/Reorder-List.md)

## Problem Statement
Given the `head` of a singly linked list, reverse the list and return the reversed list.

**Example:**
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

## Approach 1: Using Stack

### Java Code
```java
class Solution {
    public ListNode reverseList(ListNode head) {
        Stack<ListNode> stack = new Stack<>();
        ListNode current = head;
        
        while (current != null) {
            stack.push(current);
            current = current.next;
        }
        
        ListNode dummy = new ListNode(0);
        current = dummy;
        
        while (!stack.isEmpty()) {
            current.next = stack.pop();
            current = current.next;
        }
        current.next = null;
        
        return dummy.next;
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(n)

## Approach 2: Iterative (Optimized)

### Java Code
```java
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        
        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        
        return prev;
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(1)

## Approach 3: Recursive

### Java Code
```java
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        ListNode newHead = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        
        return newHead;
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(n) - Recursion stack

## Visual Example
```
Original: 1 → 2 → 3 → null

Step by step:
prev=null, curr=1
  next=2, 1→null, prev=1, curr=2

prev=1, curr=2
  next=3, 2→1, prev=2, curr=3

prev=2, curr=3
  next=null, 3→2, prev=3, curr=null

Result: 3 → 2 → 1 → null
```

## Key Takeaways
- Iterative approach uses three pointers: prev, curr, next
- Save next before breaking the link
- Recursive approach elegant but uses O(n) space
- Foundation for many linked list reversal problems
