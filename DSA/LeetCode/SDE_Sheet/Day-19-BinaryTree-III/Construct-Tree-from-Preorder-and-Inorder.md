# Construct Tree from Preorder and Inorder

**LeetCode 105** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

### Approach

- `preorder[0]` is always the root
- Find root in `inorder` → elements to its left = left subtree, right = right subtree
- Recurse with correct slices
- Use HashMap for O(1) inorder lookup

### Java Solution

```java
class Solution {
    Map<Integer, Integer> inorderMap = new HashMap<>();
    int[] preorder;
    int preIdx = 0;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        this.preorder = preorder;
        for (int i = 0; i < inorder.length; i++) inorderMap.put(inorder[i], i);
        return build(0, inorder.length - 1);
    }

    private TreeNode build(int left, int right) {
        if (left > right) return null;
        int rootVal = preorder[preIdx++];
        TreeNode root = new TreeNode(rootVal);
        int mid = inorderMap.get(rootVal);
        root.left = build(left, mid - 1);
        root.right = build(mid + 1, right);
        return root;
    }
}
```

**Complexity:** Time O(n) · Space O(n)

> **From Postorder + Inorder:** Last element of postorder = root. Recurse right first.

---
