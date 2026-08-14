# Linked List Cycle II (LC 142)

**Difficulty**: Medium  
**Pattern**: Fast & Slow Pointers  
**LeetCode**: https://leetcode.com/problems/linked-list-cycle-ii/

## Problem Statement
Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

**Example 1:**
```
Input: head = [3,2,0,-4], pos = 1
Output: Node with value 2
Explanation: Cycle starts at node with value 2.
```

## Approach 1: Brute Force (HashSet)

### Intuition
Store visited nodes in a HashSet. The first node we visit twice is the cycle start.

### Java Code
```java
class Solution {
    public ListNode detectCycle(ListNode head) {
        Set<ListNode> visited = new HashSet<>();
        
        ListNode current = head;
        while (current != null) {
            if (visited.contains(current)) {
                return current; // First repeated node is cycle start
            }
            visited.add(current);
            current = current.next;
        }
        
        return null; // No cycle
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n)
- **Space Complexity**: O(n) - HashSet stores nodes

## Approach 2: Optimized (Fast & Slow Pointers with Math)

### Intuition
**Phase 1**: Detect if cycle exists using fast & slow pointers.
**Phase 2**: Find cycle start using mathematical property:
- Distance from head to cycle start = Distance from meeting point to cycle start
- Reset one pointer to head, move both at same speed until they meet

### Mathematical Proof
```
Let:
- L = distance from head to cycle start
- C = cycle length
- k = distance from cycle start to meeting point

When they meet:
- Slow traveled: L + k
- Fast traveled: L + k + nC (n cycles)
- Fast = 2 × Slow
- L + k + nC = 2(L + k)
- L = nC - k

This means: distance from head to start = distance from meeting point to start
```

### Java Code
```java
class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null) return null;
        
        // Phase 1: Detect cycle
        ListNode slow = head;
        ListNode fast = head;
        boolean hasCycle = false;
        
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            
            if (slow == fast) {
                hasCycle = true;
                break;
            }
        }
        
        if (!hasCycle) return null;
        
        // Phase 2: Find cycle start
        slow = head; // Reset slow to head
        
        while (slow != fast) {
            slow = slow.next;
            fast = fast.next; // Both move at same speed
        }
        
        return slow; // Meeting point is cycle start
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

## Visual Example
```
3 → 2 → 0 → -4
    ↑         ↓
    ← ← ← ← ← 

Phase 1: Fast and slow meet at node 0
Phase 2: Reset slow to head (3)
        Move both at same speed:
        slow: 3 → 2
        fast: 0 → -4 → 2
        They meet at node 2 (cycle start)
```

## Key Takeaways
- Mathematical property enables O(1) space solution
- Two-phase approach: detect cycle, then find start
- After meeting, distance to start is equal from both head and meeting point
- Demonstrates advanced application of Floyd's algorithm
- Understanding the math makes the solution intuitive
