# Kth Smallest Element in a BST

**Difficulty:** Medium  
**Category:** Trees  
**LeetCode Link:** [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

---

## Problem Statement

Given the `root` of a binary search tree, and an integer `k`, return the `kth` smallest value (1-indexed) of all the values of the nodes in the tree.

---

## Approach: Inorder Traversal

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
- **Time:** O(n)
- **Space:** O(h)

---

## Tags
#trees #bst #inorder #medium #blind75
