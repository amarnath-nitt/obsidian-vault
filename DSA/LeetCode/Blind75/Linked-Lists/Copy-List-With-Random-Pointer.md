# Copy List with Random Pointer

**Difficulty:** Medium  
**Category:** Linked Lists  
**LeetCode Link:** [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)

---

## Problem Statement

A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

Construct a **deep copy** of the list.

**Example:**
```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

**Constraints:**
- `0 <= n <= 1000`
- `-10^4 <= Node.val <= 10^4`
- `Node.random` is `null` or is pointing to some node in the linked list.

---

## Intuition

Use a HashMap to map original nodes to their copies, then set next and random pointers.

---

## Approach: HashMap

### Algorithm
1. First pass: create all nodes and store in HashMap
2. Second pass: set next and random pointers using HashMap

### Java Code
```java
class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) return null;
        
        Map<Node, Node> map = new HashMap<>();
        
        // First pass: create all nodes
        Node current = head;
        while (current != null) {
            map.put(current, new Node(current.val));
            current = current.next;
        }
        
        // Second pass: set pointers
        current = head;
        while (current != null) {
            map.get(current).next = map.get(current.next);
            map.get(current).random = map.get(current.random);
            current = current.next;
        }
        
        return map.get(head);
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(n) - HashMap

---

## Tags
#linked-lists #hash-table #medium #blind75
