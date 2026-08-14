# Kth Smallest Element in a BST (LC 230)

**Difficulty**: Medium  
**Pattern**: Tree / DFS / Inorder  
**LeetCode**: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

## Problem Statement
Given the `root` of a binary search tree, and an integer `k`, return the `k`th smallest value (1-indexed) of all the values of the nodes in the tree.

**Example:**
```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

## Approach: Inorder Traversal

### Intuition
Inorder traversal of a BST yields sorted values. We just need to stop at the k-th element.

### Java Code
```java
class Solution {
    private int count = 0;
    private int result = 0;
    
    public int kthSmallest(TreeNode root, int k) {
        inorder(root, k);
        return result;
    }
    
    private void inorder(TreeNode node, int k) {
        if (node == null) return;
        
        inorder(node.left, k);
        
        count++;
        if (count == k) {
            result = node.val;
            return;
        }
        
        inorder(node.right, k);
    }
}
```

### Complexity
- **Time**: O(n) (or O(k) optimized)
- **Space**: O(h)

## Key Takeaways
- BST Inorder = Sorted List
- Iterative stack approach allows early return comfortably too
