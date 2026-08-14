# Linked List Cycle

**Difficulty:** Easy  
**Category:** Linked Lists  
**LeetCode Link:** [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

---

## Problem Statement

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

**Example 1:**
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle where the tail connects to the 1st node (0-indexed).
```

**Example 2:**
```
Input: head = [1], pos = -1
Output: false
```

**Constraints:**
- The number of nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`

---

## Intuition

If there's a cycle, a fast pointer will eventually catch up to a slow pointer. This is Floyd's Cycle Detection Algorithm (Tortoise and Hare).

---

## Approach 1: Hash Set (Naive)

### Algorithm
1. Use a HashSet to track visited nodes
2. Traverse the list
3. If we see a node again, there's a cycle
4. If we reach null, no cycle

### Java Code
```java
class Solution {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> visited = new HashSet<>();
        
        while (head != null) {
            if (visited.contains(head)) {
                return true;  // Cycle detected
            }
            visited.add(head);
            head = head.next;
        }
        
        return false;  // Reached end, no cycle
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(n) - HashSet storage

---

## Approach 2: Floyd's Cycle Detection (Optimized)

### Algorithm
1. Use two pointers: slow (moves 1 step) and fast (moves 2 steps)
2. If there's a cycle, fast will eventually meet slow
3. If fast reaches null, no cycle

### Java Code
```java
class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null) return false;
        
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast != null && fast.next != null) {
            slow = slow.next;        // Move 1 step
            fast = fast.next.next;   // Move 2 steps
            
            if (slow == fast) {
                return true;  // Cycle detected
            }
        }
        
        return false;  // No cycle
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) - Fast pointer visits at most 2n nodes
- **Space Complexity:** O(1) - Only two pointers

### Why This is Better
- ✅ O(1) space vs O(n) space
- ✅ No extra data structures needed
- ✅ Elegant and efficient
- ✅ Classic algorithm

---

## Key Takeaways

1. **Pattern:** Floyd's Cycle Detection (Tortoise and Hare)
2. **Two speeds:** Slow moves 1, fast moves 2
3. **Meeting point:** If cycle exists, they will meet
4. **Space optimization:** O(1) vs O(n) using HashSet

---

## Tags
#linked-lists #two-pointers #cycle-detection #easy #blind75
