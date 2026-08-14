# Day 19 — Binary Tree III

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** Binary Tree — Paths, LCA, Max Path Sum
**Difficulty Mix:** Medium / Hard

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Binary Tree Maximum Path Sum]] | 124 | Hard | ⬜ |
| 2 | [[#Lowest Common Ancestor of Binary Tree]] | 236 | Medium | ⬜ |
| 3 | [[#Construct Tree from Preorder and Inorder]] | 105 | Medium | ⬜ |
| 4 | [[#Serialize and Deserialize Binary Tree]] | 297 | Hard | ⬜ |
| 5 | [[#Flatten Binary Tree to Linked List]] | 114 | Medium | ⬜ |
| 6 | [[#Root to Node Path]] | — | Medium | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Binary Tree Maximum Path Sum | Consider paths between many node pairs. O(n^2) or worse. | DFS returns max gain from each node. O(n). | Same DFS updates global best with left+node+right. |
| Lowest Common Ancestor of Binary Tree | Build root-to-node paths and compare. O(n) space. | Recursive search returns matching child/root. O(n). | Same one-pass recursion with O(h) stack. |
| Construct Tree from Preorder and Inorder | Recursively scan inorder to find root. O(n^2). | HashMap value to inorder index. O(n). | Pass index ranges, avoid array copies. O(n). |
| Serialize and Deserialize Binary Tree | Level-order with many null markers. O(n). | Preorder with null markers. O(n). | StringBuilder/queue parser to avoid costly string operations. |
| Flatten Binary Tree to Linked List | Store preorder nodes in a list, then relink. O(n) space. | Reverse preorder recursion with prev pointer. O(h) stack. | Morris-like rewiring using rightmost node of left subtree. O(1) extra. |
| Root to Node Path | Generate all root-to-leaf paths, then search. | DFS backtracking with early return. O(n). | Same, stopping as soon as target is found. |

---

## Binary Tree Maximum Path Sum

**LeetCode 124** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

### Problem
Find the max sum path between any two nodes.

### Approach

- For each node: max contribution going up = `node.val + max(leftGain, rightGain, 0)`
- Path through node = `node.val + leftGain + rightGain` (can go both sides)
- Update global max with path through current node

### Java Solution

```java
class Solution {
    int maxSum = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        gainFrom(root);
        return maxSum;
    }

    private int gainFrom(TreeNode node) {
        if (node == null) return 0;
        int leftGain = Math.max(gainFrom(node.left), 0);
        int rightGain = Math.max(gainFrom(node.right), 0);
        maxSum = Math.max(maxSum, node.val + leftGain + rightGain);
        return node.val + Math.max(leftGain, rightGain); // can only go one way up
    }
}
```

**Complexity:** Time O(n) · Space O(h)

---

## Lowest Common Ancestor of Binary Tree

**LeetCode 236** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

### Problem
Find LCA of two nodes p and q.

### Approach

- If root is null → return null
- If root == p or root == q → return root
- Recurse left and right
- If both sides return non-null → current node is LCA
- Else return the non-null side

### Java Solution

```java
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if (left != null && right != null) return root; // found in both subtrees
        return (left != null) ? left : right;
    }
}
```

**Complexity:** Time O(n) · Space O(h)

---

## Construct Tree from Preorder and Inorder

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

## Serialize and Deserialize Binary Tree

**LeetCode 297** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

### Approach (Preorder with null markers)

- Serialize: preorder DFS, write "null" for null nodes
- Deserialize: parse the sequence, rebuild using same preorder logic

### Java Solution

```java
public class Codec {
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        serDfs(root, sb);
        return sb.toString();
    }

    private void serDfs(TreeNode node, StringBuilder sb) {
        if (node == null) { sb.append("null,"); return; }
        sb.append(node.val).append(",");
        serDfs(node.left, sb);
        serDfs(node.right, sb);
    }

    public TreeNode deserialize(String data) {
        Queue<String> queue = new LinkedList<>(Arrays.asList(data.split(",")));
        return desDfs(queue);
    }

    private TreeNode desDfs(Queue<String> queue) {
        String val = queue.poll();
        if (val.equals("null")) return null;
        TreeNode node = new TreeNode(Integer.parseInt(val));
        node.left = desDfs(queue);
        node.right = desDfs(queue);
        return node;
    }
}
```

**Complexity:** Time O(n) · Space O(n)

---

## Flatten Binary Tree to Linked List

**LeetCode 114** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

### Problem
Flatten in-place to a linked list in preorder order.

### Approach (Morris-like — Reverse Preorder)

- Process nodes in **reverse preorder** (right → left → root)
- Maintain a `prev` pointer
- Set `node.right = prev`, `node.left = null`

```java
class Solution {
    TreeNode prev = null;

    public void flatten(TreeNode root) {
        if (root == null) return;
        flatten(root.right);
        flatten(root.left);
        root.right = prev;
        root.left = null;
        prev = root;
    }
}
```

**Alternative (Iterative):** At each node, insert left subtree between node and node.right.

**Complexity:** Time O(n) · Space O(h)

---

## Root to Node Path

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

## Tree Path Problems Summary

| Problem | Approach |
|---------|----------|
| Max path sum | DFS, return max gain, update global at each node |
| LCA | DFS, return non-null; if both sides non-null → LCA |
| Path to node | DFS with backtracking |
| All root-to-leaf paths | DFS, collect path, add when leaf |

#sde-sheet #binary-tree #day19
