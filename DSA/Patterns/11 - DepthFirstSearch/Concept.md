# Depth First Search — Concept

## What Is It?

DFS explores a graph/tree by going as **deep as possible** along each branch before backtracking. Implemented recursively or with an explicit stack.

---

## When to Use

> **Trigger keywords:** "all paths", "connected components", "detect cycle", "topological sort", "island count", "tree depth"

| Trigger | Example |
|---------|---------|
| **Count connected components** | Number of Islands |
| **Find all paths** | All Paths Source to Target |
| **Detect cycle** | Course Schedule |
| **Tree problems** (depth, LCA, validate BST) | Maximum Depth, Validate BST |

---

## Template

### Recursive (Graph)
```java
void dfs(int node, boolean[] visited, List<List<Integer>> graph) {
    visited[node] = true;
    for (int neighbor : graph.get(node)) {
        if (!visited[neighbor]) {
            dfs(neighbor, visited, graph);
        }
    }
}
```

### Iterative (Stack)
```java
Stack<Integer> stack = new Stack<>();
stack.push(start);
visited[start] = true;

while (!stack.isEmpty()) {
    int node = stack.pop();
    for (int neighbor : graph.get(node)) {
        if (!visited[neighbor]) {
            visited[neighbor] = true;
            stack.push(neighbor);
        }
    }
}
```

---

## Visual Walkthrough

### DFS on Tree — Maximum Depth
```
        3
       / \
      9   20
         / \
        15   7

DFS call stack:
  depth(3) = 1 + max(depth(9), depth(20))
  depth(9) = 1 + max(depth(null), depth(null)) = 1
  depth(20) = 1 + max(depth(15), depth(7))
  depth(15) = 1, depth(7) = 1
  depth(20) = 1 + max(1,1) = 2
  depth(3) = 1 + max(1, 2) = 3

Answer: 3
```

---

## Time/Space Complexity

| Metric | Complexity |
|--------|-----------|
| Time | O(V + E) for graph, O(n) for tree |
| Space | O(V) for visited + O(h) stack depth |

---

## Common Mistakes

1. **Stack overflow on deep graphs** → Use iterative DFS for very deep graphs
2. **Forgetting to mark visited** → Infinite loop in cyclic graphs
3. **Using DFS for shortest path** → DFS doesn't find shortest path; use BFS

---

## Related Patterns

- [[10 - BreadthFirstSearch/Concept|BFS]] — Use when shortest path matters
- [[01 - Recursion/Concept|Recursion]] — DFS is inherently recursive
- [[19 - Backtracking/Concept|Backtracking]] — DFS + undo state changes

---

#dfs #graph #dsa #concept
