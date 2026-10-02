---
solved: false
difficulty: Medium
pattern: Breadth First Search
lc_number: 116
date_solved: 
tags:
  - dsa
  - breadth-first-search
  - medium
---
# Populating Next Right Pointers in Each Node (LC 116)

**Difficulty**: Medium  
**Pattern**: Breadth-First Search  
**LeetCode**: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

## Problem Statement
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.
Initially, all next pointers are set to `NULL`.

**Example:**
```
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
```

## Approach 1: BFS (Level Order)

### Intuition
Standard Level Order.
For each level, iterate nodes `0` to `size-2` and set `node.next = nextNode`.
Last node points to null.
Space: O(N) due to queue.

## Approach 2: Using established 'next' pointers (O(1) Space)

### Intuition
Since we have `next` pointers established for level `N`, we can use them to traverse level `N` while establishing pointers for level `N+1`.
`curr.left.next = curr.right`
`curr.right.next = curr.next.left` (if `curr.next` exists)

### Java Code (O(1) Space)
```java
class Solution {
    public Node connect(Node root) {
        if (root == null) return null;
        
        Node leftMost = root;
        
        while (leftMost.left != null) {
            Node head = leftMost;
            
            while (head != null) {
                // Connection 1: Same parent
                head.left.next = head.right;
                
                // Connection 2: Across parents
                if (head.next != null) {
                    head.right.next = head.next.left;
                }
                
                head = head.next;
            }
            
            leftMost = leftMost.left;
        }
        
        return root;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(1)

## Key Takeaways
- Exploiting structure of Perfect Binary Tree
- Traversing using the pointers created in previous level
