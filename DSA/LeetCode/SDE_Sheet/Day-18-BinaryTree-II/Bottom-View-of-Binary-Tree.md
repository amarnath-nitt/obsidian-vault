# Bottom View of Binary Tree

**Problem:** For each vertical column (horizontal distance), show the bottom-most node.

### Approach (BFS + HashMap by HD)

- Assign **horizontal distance (HD)**: root = 0, left child = HD-1, right child = HD+1
- BFS — at each HD, overwrite with current node (last overwrite = bottom)

### Java Solution

```java
public List<Integer> bottomView(TreeNode root) {
    if (root == null) return new ArrayList<>();
    Map<Integer, Integer> map = new TreeMap<>(); // sorted by HD
    Queue<int[]> queue = new LinkedList<>(); // [node, HD] — use wrapper or pair
    // Since Java has no Pair, use a helper approach:
    Queue<TreeNode> nodes = new LinkedList<>();
    Queue<Integer> hds = new LinkedList<>();
    nodes.offer(root); hds.offer(0);

    while (!nodes.isEmpty()) {
        TreeNode node = nodes.poll();
        int hd = hds.poll();
        map.put(hd, node.val); // overwrite → bottom view
        if (node.left != null) { nodes.offer(node.left); hds.offer(hd - 1); }
        if (node.right != null) { nodes.offer(node.right); hds.offer(hd + 1); }
    }
    return new ArrayList<>(map.values());
}
```

**Complexity:** Time O(n log n) · Space O(n)

---
