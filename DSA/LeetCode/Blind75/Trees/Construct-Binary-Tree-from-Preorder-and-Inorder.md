# Construct Binary Tree from Preorder and Inorder Traversal

**Difficulty:** Medium  
**Category:** Trees  
**LeetCode Link:** [Construct Binary Tree from Preorder and Inorder](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

---

## Problem Statement

Given two integer arrays `preorder` and `inorder`, construct and return the binary tree.

---

## Approach: Recursive Construction

### Java Code
```java
class Solution {
    private int preIndex = 0;
    private Map<Integer, Integer> inorderMap = new HashMap<>();
    
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for (int i = 0; i < inorder.length; i++) {
            inorderMap.put(inorder[i], i);
        }
        return build(preorder, 0, inorder.length - 1);
    }
    
    private TreeNode build(int[] preorder, int left, int right) {
        if (left > right) return null;
        
        int rootVal = preorder[preIndex++];
        TreeNode root = new TreeNode(rootVal);
        
        int mid = inorderMap.get(rootVal);
        root.left = build(preorder, left, mid - 1);
        root.right = build(preorder, mid + 1, right);
        
        return root;
    }
}
```

### Complexity
- **Time:** O(n)
- **Space:** O(n)

---

## Tags
#trees #divide-and-conquer #medium #blind75
