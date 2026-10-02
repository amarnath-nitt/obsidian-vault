# Merge Two BSTs

**Problem:** Merge two BSTs into one balanced BST.

### Approach

1. Inorder traversal of both BSTs → two sorted arrays
2. Merge two sorted arrays → one sorted array
3. Convert sorted array to balanced BST

```java
List<Integer> inorder(TreeNode root) { /* standard inorder */ }

List<Integer> merge(List<Integer> a, List<Integer> b) {
    /* standard merge of two sorted lists */
}

TreeNode sortedToBST(List<Integer> list, int l, int r) {
    if (l > r) return null;
    int mid = (l + r) / 2;
    TreeNode root = new TreeNode(list.get(mid));
    root.left = sortedToBST(list, l, mid - 1);
    root.right = sortedToBST(list, mid + 1, r);
    return root;
}
```

**Complexity:** Time O(m+n) · Space O(m+n)

---
