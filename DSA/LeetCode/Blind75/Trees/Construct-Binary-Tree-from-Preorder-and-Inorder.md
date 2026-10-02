# Construct Binary Tree from Preorder and Inorder Traversal

**Difficulty:** Medium
**Category:** Trees
**LeetCode Link:** [Construct Binary Tree from Preorder and Inorder](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

---

## Problem Statement

Given two integer arrays `preorder` and `inorder`, construct and return the binary tree.

**Example:**
```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

---

## Intuition

- **Preorder** = [root, left subtree, right subtree] → first element is always the root
- **Inorder** = [left subtree, root, right subtree] → root's position splits left and right subtrees

So: take root from preorder, find it in inorder, everything left of it is the left subtree, everything right is the right subtree. Recurse.

---

## Approach: Recursive with HashMap

### Algorithm
1. Build a HashMap of `value → index` for inorder array (O(1) lookup)
2. Use a global `preIndex` pointer into preorder array
3. At each call: pick `preorder[preIndex]` as root, find its position in inorder
4. Recursively build left subtree (inorder left portion), then right subtree

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

### Complexity Analysis
- **Time Complexity:** O(n) — each node processed once, O(1) lookup via HashMap
- **Space Complexity:** O(n) — HashMap + recursion stack

---

## Step-by-Step Example

`preorder = [3,9,20,15,7]`, `inorder = [9,3,15,20,7]`
```
preIndex=0: root=3, mid=1 in inorder
  Left: inorder[0..0] → preIndex=1: root=9, leaf
  Right: inorder[2..4] → preIndex=2: root=20, mid=3
    Left: inorder[2..2] → preIndex=3: root=15, leaf
    Right: inorder[4..4] → preIndex=4: root=7, leaf
```

---

## Key Takeaways

1. **Preorder first element = root** always
2. **Inorder root position** divides left and right subtrees
3. **HashMap** avoids O(n) linear search per node
4. **preIndex** advances globally across all recursive calls

---

## Tags
#trees #divide-and-conquer #medium #blind75
