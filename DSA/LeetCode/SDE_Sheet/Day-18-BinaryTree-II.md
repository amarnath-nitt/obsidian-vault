# Day 18 — Binary Tree II

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** Binary Tree — Views, Boundary, Vertical Order
**Difficulty Mix:** Medium

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Binary Tree Right Side View]] | 199 | Medium | ⬜ |
| 2 | [[#Bottom View of Binary Tree]] | — | Medium | ⬜ |
| 3 | [[#Top View of Binary Tree]] | — | Medium | ⬜ |
| 4 | [[#Vertical Order Traversal]] | 987 | Hard | ⬜ |
| 5 | [[#Boundary Traversal]] | — | Medium | ⬜ |
| 6 | [[#Zigzag Level Order Traversal]] | 103 | Medium | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Binary Tree Right Side View | Store full level order and take last node per level. O(n). | BFS and record last node of each level. | DFS right-first, add first node seen at each depth. O(n). |
| Bottom View of Binary Tree | Build every vertical list, then take deepest node. | BFS with horizontal distance and overwrite map entry. | TreeMap/min-max horizontal distance for ordered output. O(n log n) or O(n). |
| Top View of Binary Tree | Build every vertical list, then take first node. | BFS with horizontal distance and keep first entry only. | Track min/max horizontal distance to output without sorting where possible. |
| Vertical Order Traversal | Collect nodes, rows, columns, then sort. O(n log n). | BFS with nested maps/priority queues. | DFS/BFS collect triples and sort by column,row,value. O(n log n). |
| Boundary Traversal | Traverse all nodes and filter boundary afterward. | Separate left boundary, leaves, and reversed right boundary. | One clean pass per boundary part, avoiding duplicates. O(n). |
| Zigzag Level Order Traversal | BFS levels, then reverse alternate levels. O(n). | Deque insert front/back depending on level. | Fill an array by index direction per level. O(n). |

---

## Binary Tree Right Side View

**LeetCode 199** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/binary-tree-right-side-view/)

### Approach
BFS level order — collect the **last** node at each level.

### Java Solution

```java
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                if (i == size - 1) result.add(node.val); // last of level
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
        }
        return result;
    }
}
```

**Complexity:** Time O(n) · Space O(n)

---

## Bottom View of Binary Tree

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

## Top View of Binary Tree

**Problem:** For each HD, show the top-most (first seen) node.

### Approach

Same as Bottom View but only insert if HD not already in map.

```java
if (!map.containsKey(hd)) map.put(hd, node.val); // first seen = top view
```

---

## Vertical Order Traversal

**LeetCode 987** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/)

### Problem
Return vertical order traversal. Nodes at same position sorted by value.

### Approach

- Assign `(col, row)` to each node
- Sort by: col → row → value
- Group by column

### Java Solution

```java
class Solution {
    List<int[]> nodes = new ArrayList<>(); // [col, row, val]

    public List<List<Integer>> verticalTraversal(TreeNode root) {
        dfs(root, 0, 0);
        nodes.sort((a, b) -> a[0] != b[0] ? a[0] - b[0] :
                             a[1] != b[1] ? a[1] - b[1] : a[2] - b[2]);

        List<List<Integer>> result = new ArrayList<>();
        int prevCol = Integer.MIN_VALUE;

        for (int[] node : nodes) {
            if (node[0] != prevCol) {
                result.add(new ArrayList<>());
                prevCol = node[0];
            }
            result.get(result.size() - 1).add(node[2]);
        }
        return result;
    }

    private void dfs(TreeNode node, int col, int row) {
        if (node == null) return;
        nodes.add(new int[]{col, row, node.val});
        dfs(node.left, col - 1, row + 1);
        dfs(node.right, col + 1, row + 1);
    }
}
```

**Complexity:** Time O(n log n) · Space O(n)

---

## Boundary Traversal

**Problem:** Print the boundary of a binary tree (anti-clockwise): left boundary + leaves + right boundary (reversed).

### Approach

1. **Left boundary**: root → left subtree top → before last leaf (going down left)
2. **All leaves**: in-order DFS to collect all leaf nodes
3. **Right boundary**: (right subtree → root) reversed, excluding last leaf

```java
public List<Integer> boundaryOfBinaryTree(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    if (root == null) return result;
    if (!isLeaf(root)) result.add(root.val);

    // Left boundary (top-down, not including leaf)
    TreeNode node = root.left;
    while (node != null) {
        if (!isLeaf(node)) result.add(node.val);
        node = (node.left != null) ? node.left : node.right;
    }

    // All leaves
    addLeaves(root, result);

    // Right boundary (bottom-up, not including leaf)
    Deque<Integer> stack = new ArrayDeque<>();
    node = root.right;
    while (node != null) {
        if (!isLeaf(node)) stack.push(node.val);
        node = (node.right != null) ? node.right : node.left;
    }
    while (!stack.isEmpty()) result.add(stack.pop());
    return result;
}

boolean isLeaf(TreeNode node) { return node.left == null && node.right == null; }
void addLeaves(TreeNode node, List<Integer> result) {
    if (node == null) return;
    if (isLeaf(node)) { result.add(node.val); return; }
    addLeaves(node.left, result);
    addLeaves(node.right, result);
}
```

---

## Zigzag Level Order Traversal

**LeetCode 103** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

### Approach

- Standard BFS level order
- Alternate direction with a boolean flag
- Use `LinkedList` to add to front or back based on direction

### Java Solution

```java
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        boolean leftToRight = true;

        while (!queue.isEmpty()) {
            Deque<Integer> level = new ArrayDeque<>();
            for (int size = queue.size(); size > 0; size--) {
                TreeNode node = queue.poll();
                if (leftToRight) level.addLast(node.val);
                else level.addFirst(node.val);
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            result.add(new ArrayList<>(level));
            leftToRight = !leftToRight;
        }
        return result;
    }
}
```

---

## Key Insight for View Problems

```
View Type        → What to extract from BFS/DFS
──────────────────────────────────────────────────
Right Side View  → Last node at each level
Left Side View   → First node at each level
Top View         → First node at each HD (BFS order)
Bottom View      → Last node at each HD (BFS order)
Vertical Order   → Sort by (col, row, val)
```

#sde-sheet #binary-tree #day18
