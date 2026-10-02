# Root to Node Path

**Problem:** Find the path from root to a given node. Return as list.

```java
boolean findPath(TreeNode root, TreeNode target, List<TreeNode> path) {
    if (root == null) return false;
    path.add(root);
    if (root == target) return true;
    if (findPath(root.left, target, path) || findPath(root.right, target, path))
        return true;
    path.remove(path.size() - 1); // backtrack
    return false;
}
```

> **Application:** Finding path between two nodes = path(root→p) + path(root→q) trimmed at LCA.

---
