# Delete Node in BST

**Difficulty:** Medium  
**Category:** Trees  
**LeetCode Link:** [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)

---

## Problem Statement

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

**Example:**
```
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
```

**Constraints:**
- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- Each node has a unique value.
- `root` is a valid binary search tree.
- `-10^5 <= key <= 10^5`

---

## Intuition

Deleting from BST requires handling three cases: node with no children, one child, or two children. The tricky case is two children - replace with successor or predecessor.

---

## Approach: Recursive BST Deletion

### Algorithm
1. Search for the node to delete
2. **Case 1:** No children → return null
3. **Case 2:** One child → return that child
4. **Case 3:** Two children → replace with inorder successor (leftmost of right subtree)

### Java Code
```java
class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null;
        
        // Search for the node
        if (key < root.val) {
            root.left = deleteNode(root.left, key);
        } else if (key > root.val) {
            root.right = deleteNode(root.right, key);
        } else {
            // Found the node to delete
            
            // Case 1: No children or one child
            if (root.left == null) return root.right;
            if (root.right == null) return root.left;
            
            // Case 2: Two children
            // Find inorder successor (smallest in right subtree)
            TreeNode successor = findMin(root.right);
            root.val = successor.val;
            root.right = deleteNode(root.right, successor.val);
        }
        
        return root;
    }
    
    private TreeNode findMin(TreeNode node) {
        while (node.left != null) {
            node = node.left;
        }
        return node;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(h) - Height of tree
- **Space Complexity:** O(h) - Recursion stack

---

## Key Takeaways

1. **Pattern:** BST deletion has three distinct cases
2. **Successor:** Leftmost node in right subtree
3. **Predecessor:** Rightmost node in left subtree (alternative)
4. **BST property:** Must maintain after deletion

---

## Tags
#trees #bst #recursion #medium #blind75
