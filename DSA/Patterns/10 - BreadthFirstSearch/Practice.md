# Breadth-First Search (BFS) - Practice Notes

## Pattern Overview
Explores nodes level by level, useful for finding shortest paths and level-order traversals.

## Key Concepts
- **Queue-based**: FIFO processing
- **Time Complexity**: O(V + E) for graphs, O(n) for trees
- **Shortest Path**: In unweighted graphs

## Template Code

### Tree BFS
```java
public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> result = new ArrayList<>();
    if (root == null) return result;
    
    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);
    
    while (!queue.isEmpty()) {
        int size = queue.size();
        List<Integer> level = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            TreeNode node = queue.poll();
            level.add(node.val);
            if (node.left != null) queue.offer(node.left);
            if (node.right != null) queue.offer(node.right);
        }
        result.add(level);
    }
    return result;
}
```

### Graph BFS
```java
public List<Integer> bfs(int start, List<List<Integer>> graph) {
	List<Integer> result = new ArrayList<>();
    boolean[] visited = new boolean[graph.size()];
    Queue<Integer> queue = new LinkedList<>();
    queue.offer(start);
    visited[start] = true;
    
    while (!queue.isEmpty()) {
        int node = queue.poll();
        // Process node
        result.add(node);
        for (int neighbor : graph.get(node)) {
            if (!visited[neighbor]) {
                queue.offer(neighbor);
                visited[neighbor] = true;
            }
        }
    }
    return result;
}
```

### Shortest Path
```java
public int shortestPath(int start, int end, List<List<Integer>> graph) {
    Queue<Integer> queue = new LinkedList<>();
    boolean[] visited = new boolean[graph.size()];
    queue.offer(start);
    visited[start] = true;
    int distance = 0;
    
    while (!queue.isEmpty()) {
        int size = queue.size();
        for (int i = 0; i < size; i++) {
            int node = queue.poll();
            if (node == end) return distance;
            
            for (int neighbor : graph.get(node)) {
                if (!visited[neighbor]) {
                    queue.offer(neighbor);
                    visited[neighbor] = true;
                }
            }
        }
        distance++;
    }
    return -1;
}
```

## Practice Problems

### Easy
- [x] [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) (LC 102) → [Solution](solutions/LC-102-Binary-Tree-Level-Order.md)
- [x] [Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) (LC 107) → [Solution](solutions/LC-107-Binary-Tree-Level-Order-II.md)
- [x] [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) (LC 111) → [Solution](solutions/LC-111-Minimum-Depth-Binary-Tree.md)
- [x] [Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/) (LC 637) → [Solution](solutions/LC-637-Average-of-Levels.md)

### Medium
- [ ] [Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/) (LC 116) → [Solution](solutions/LC-116-Populating-Next-Right-Pointers.md)
- [ ] [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) (LC 994) → [Solution](solutions/LC-994-Rotting-Oranges.md)
- [ ] [01 Matrix](https://leetcode.com/problems/01-matrix/) (LC 542) → [Solution](solutions/LC-542-01-Matrix.md)
- [ ] [Word Ladder](https://leetcode.com/problems/word-ladder/) (LC 127) → [Solution](solutions/LC-127-Word-Ladder.md)
- [ ] [Open the Lock](https://leetcode.com/problems/open-the-lock/) (LC 752) → [Solution](solutions/LC-752-Open-the-Lock.md)
- [ ] [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) (LC 1091) → [Solution](../ShortestPath/solutions/LC-1091-Shortest-Path-in-Binary-Matrix.md)
- [ ] [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) (LC 103) → [Solution](solutions/LC-103-Binary-Tree-Zigzag.md)
- [ ] [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) (LC 199) → [Solution](solutions/LC-199-Binary-Tree-Right-Side.md)

### Hard
- [ ] [Word Ladder II](https://leetcode.com/problems/word-ladder-ii/) (LC 126) → [Solution](solutions/LC-126-Word-Ladder-II.md)
- [ ] [Shortest Path to Get All Keys](https://leetcode.com/problems/shortest-path-to-get-all-keys/) (LC 864) → [Solution](solutions/LC-864-Shortest-Path-All-Keys.md)

## Reference
[LeetCode Pattern Guide](https://lnkd.in/gJueWjk2)
