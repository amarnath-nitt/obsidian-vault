# Construct Binary Tree from Preorder and Inorder Traversal (LC 105)

**Difficulty**: Medium  
**Pattern**: Depth First Search / Tree  
**LeetCode**: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

## Problem Statement
Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

**Example:**
```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

## Approach: Recursive with HashMap

### Intuition
Preorder: `[Root, Left, Right]`
Inorder: `[Left, Root, Right]`
1. The first element of preorder is the root.
2. Find this root in inorder array. Elements to the left are the left subtree, elements to the right are the right subtree.
3. Recursively build left and right subtrees.
Use a HashMap to store inorder indices for O(1) lookup.

### Java Code
```java
class Solution {
    private Map<Integer, Integer> inorderMap;
    private int preorderIndex;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        inorderMap = new HashMap<>();
        preorderIndex = 0;
        
        for (int i = 0; i < inorder.length; i++) {
            inorderMap.put(inorder[i], i);
        }
        
        return arrayToTree(preorder, 0, preorder.length - 1);
    }
    
    private TreeNode arrayToTree(int[] preorder, int left, int right) {
        if (left > right) return null;
        
        int rootValue = preorder[preorderIndex++];
        TreeNode root = new TreeNode(rootValue);
        
        int inorderIndex = inorderMap.get(rootValue);
        
        root.left = arrayToTree(preorder, left, inorderIndex - 1);
        root.right = arrayToTree(preorder, inorderIndex + 1, right);
        
        return root;
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(n)

## Key Takeaways
- Root is always first in Preorder
- Inorder helps define boundaries of subtrees
- HashMap optimization avoids O(n) search at each step
