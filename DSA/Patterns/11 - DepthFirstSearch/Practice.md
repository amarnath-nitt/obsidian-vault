# Depth-First Search (DFS) - Practice Notes

## Pattern Overview
Explores as far as possible along each branch before backtracking, used for trees and graphs.

## Key Concepts
- **Stack-based**: Uses recursion or explicit stack
- **Time Complexity**: O(V + E) for graphs, O(n) for trees
- **Space Complexity**: O(h) where h is height

## Template Code

### Tree DFS (Recursive)
```java
public void dfs(TreeNode root) {
    if (root == null) return;
    
    // Process current node
    System.out.println(root.val);
    
    // Recurse on children
    dfs(root.left);
    dfs(root.right);
}
```

### Graph DFS (Iterative)
```java
public List<Integer> dfs(int start, List<List<Integer>> graph) {
	List<Integer> result = new ArrayList<>();
    boolean[] visited = new boolean[graph.size()];
    Stack<Integer> stack = new Stack<>();
    stack.push(start);
    visited[start] = true;
    while (!stack.isEmpty()) {
        int node = stack.pop();
        // Process node
        result.add(node);
        for (int neighbor : graph.get(node)) {
            if (!visited[neighbor]) {
	            visited[neighbor] = true;
                stack.push(neighbor);
            }
        }
    }
    return result;
}
```

### Path Finding
```java
public boolean hasPath(TreeNode root, int targetSum) {
    if (root == null) return false;
    if (root.left == null && root.right == null) {
        return targetSum == root.val;
    }
    return hasPath(root.left, targetSum - root.val) ||
           hasPath(root.right, targetSum - root.val);
}
```

## Practice Problems

### Easy
- [x] [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) (LC 104) → [Solution](solutions/LC-104-Maximum-Depth-Binary-Tree.md)
- [x] [Path Sum](https://leetcode.com/problems/path-sum/) (LC 112) → [Solution](solutions/LC-112-Path-Sum.md)
- [x] [Same Tree](https://leetcode.com/problems/same-tree/) (LC 100) → [Solution](solutions/LC-100-Same-Tree.md)
- [x] [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) (LC 101) → [Solution](solutions/LC-101-Symmetric-Tree.md)

### Medium
- [ ] [Path Sum II](https://leetcode.com/problems/path-sum-ii/) (LC 113) → [Solution](solutions/LC-113-Path-Sum-II.md)
- [ ] [Number of Islands](https://leetcode.com/problems/number-of-islands/) (LC 200) → [Solution](solutions/LC-200-Number-of-Islands.md)
- [ ] [Clone Graph](https://leetcode.com/problems/clone-graph/) (LC 133) → [Solution](solutions/LC-133-Clone-Graph.md)
- [ ] [All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/) (LC 797) → [Solution](solutions/LC-797-All-Paths-Source-Target.md)
- [ ] [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) (LC 98) → [Solution](solutions/LC-98-Validate-Binary-Search-Tree.md)
- [ ] [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) (LC 230) → [Solution](solutions/LC-230-Kth-Smallest-Element-BST.md)
- [ ] [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) (LC 236) → [Solution](solutions/LC-236-LCA-Binary-Tree.md)
- [ ] [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) (LC 105) → [Solution](solutions/LC-105-Construct-Binary-Tree-Preorder-Inorder.md)

### Hard
- [ ] [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) (LC 124) → [Solution](solutions/LC-124-Binary-Tree-Maximum-Path-Sum.md)
- [ ] [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) (LC 297) → [Solution](solutions/LC-297-Serialize-Deserialize-Binary-Tree.md)

## Reference
[LeetCode Pattern Guide](https://lnkd.in/gqvJNYE6)
