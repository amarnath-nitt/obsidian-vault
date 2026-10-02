---
solved: false
difficulty: Easy
pattern: Fast Slow Pointers
lc_number: 876
date_solved: 
tags:
  - dsa
  - fast-slow-pointers
  - easy
---
# Middle of the Linked List (LC 876)

**Difficulty**: Easy  
**Pattern**: Fast & Slow Pointers  
**LeetCode**: https://leetcode.com/problems/middle-of-the-linked-list/

## Problem Statement
Given the `head` of a singly linked list, return the middle node. If there are two middle nodes, return the second middle node.

**Example 1:**
```
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node is 3.
```

**Example 2:**
```
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since there are two middle nodes (3 and 4), return the second one.
```

## Approach 1: Brute Force (Two Pass)

### Intuition
First pass: count the total number of nodes. Second pass: traverse to the middle position (n/2).

### Java Code
```java
class Solution {
    public ListNode middleNode(ListNode head) {
        // First pass: count nodes
        int count = 0;
        ListNode current = head;
        while (current != null) {
            count++;
            current = current.next;
        }
        
        // Second pass: go to middle
        int middle = count / 2;
        current = head;
        for (int i = 0; i < middle; i++) {
            current = current.next;
        }
        
        return current;
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n) - Two passes through the list
- **Space Complexity**: O(1)

## Approach 2: Optimized (Fast & Slow Pointers - Single Pass)

### Intuition
Use fast and slow pointers. Fast moves 2 steps, slow moves 1 step. When fast reaches the end, slow will be at the middle.

### Java Code
```java
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast != null && fast.next != null) {
            slow = slow.next;        // Move 1 step
            fast = fast.next.next;   // Move 2 steps
        }
        
        return slow; // Slow is at middle
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n) - Single pass, but fast pointer moves faster
- **Space Complexity**: O(1) - Only two pointers

## Why This Works

**For odd length** (e.g., 5 nodes):
```
slow: 1 → 2 → 3
fast: 1 → 3 → 5 → null
When fast reaches null, slow is at node 3 (middle)
```

**For even length** (e.g., 6 nodes):
```
slow: 1 → 2 → 3 → 4
fast: 1 → 3 → 5 → null
When fast.next is null, slow is at node 4 (second middle)
```

## Key Takeaways
- Fast & slow pointer avoids counting nodes first
- When fast reaches end, slow is exactly at middle
-  For even-length lists, returns second middle node automatically
- Single pass vs two-pass optimization
- Common pattern for finding fractional positions in linked lists
