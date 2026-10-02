---
solved: false
difficulty: Easy
pattern: Fast Slow Pointers
lc_number: 141
date_solved: 
tags:
  - dsa
  - fast-slow-pointers
  - easy
---
# Linked List Cycle (LC 141)

**Difficulty**: Easy  
**Pattern**: Fast & Slow Pointers  
**LeetCode**: https://leetcode.com/problems/linked-list-cycle/

## Problem Statement
Given `head`, the head of a linked list, determine if the linked list has a cycle in it. Return `true` if there is a cycle, `false` otherwise.

**Example 1:**
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

## Existing Solution
This problem is already solved in your Blind75 collection:
→ [Solution](../../../LeetCode/Blind75/Linked-Lists/Linked-List-Cycle.md)

## Approach 1: Brute Force (HashSet)

### Intuition
Store all visited nodes in a HashSet. If we encounter a node we've already seen, there's a cycle.

### Java Code
```java
class Solution {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> visited = new HashSet<>();
        
        ListNode current = head;
        while (current != null) {
            if (visited.contains(current)) {
                return true; // Found cycle
            }
            visited.add(current);
            current = current.next;
        }
        
        return false; // No cycle
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n) - Visit each node once
- **Space Complexity**: O(n) - HashSet stores all nodes

## Approach 2: Optimized (Fast & Slow Pointers - Floyd's Algorithm)

### Intuition
Use two pointers moving at different speeds. If there's a cycle, the fast pointer will eventually catch up to the slow pointer (like runners on a circular track). If there's no cycle, fast pointer will reach the end.

### Java Code
```java
class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) {
            return false;
        }
        
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast != null && fast.next != null) {
            slow = slow.next;           // Move 1 step
            fast = fast.next.next;      // Move 2 steps
            
            if (slow == fast) {
                return true; // Pointers met, cycle exists
            }
        }
        
        return false; // Fast reached end, no cycle
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n) - In worst case, fast pointer visits all nodes
- **Space Complexity**: O(1) - Only two pointers used

## Key Takeaways
- Fast & slow pointer technique eliminates need for extra space
- Fast pointer moves 2x speed of slow pointer
- If cycle exists, they will definitely meet
- Classic application of Floyd's Cycle Detection algorithm
- Always check `fast != null && fast.next != null` to avoid NPE
