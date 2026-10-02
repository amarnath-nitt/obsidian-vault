# Breadth First Search — Concept

## What Is It?

BFS explores a graph/tree **level by level** using a queue. It guarantees finding the **shortest path** in unweighted graphs and processes all nodes at distance d before distance d+1.

---

## When to Use

> **Trigger keywords:** "shortest path (unweighted)", "level order", "minimum steps", "nearest", "layer by layer"

| Trigger | Example |
|---------|---------|
| **Shortest path** in unweighted graph | Word Ladder, Open the Lock |
| **Level-order** traversal | Binary Tree Level Order |
| **Minimum steps** to reach a state | 01 Matrix, Rotting Oranges |
| **Multi-source BFS** | Start from multiple sources simultaneously |

---

## Template

```java
Queue<int[]> queue = new LinkedList<>();
boolean[][] visited = new boolean[m][n];

queue.offer(new int[]{startR, startC});
visited[startR][startC] = true;
int level = 0;

while (!queue.isEmpty()) {
    int size = queue.size();
    for (int i = 0; i < size; i++) {
        int[] curr = queue.poll();
        // Process current node
        
        for (int[] dir : directions) {
            int nr = curr[0] + dir[0], nc = curr[1] + dir[1];
            if (isValid(nr, nc) && !visited[nr][nc]) {
                visited[nr][nc] = true;
                queue.offer(new int[]{nr, nc});
            }
        }
    }
    level++;
}
```

---

## Visual Walkthrough

### Rotting Oranges (Multi-Source BFS)
```
Time 0:     Time 1:     Time 2:     Time 3:
2 1 1       2 2 1       2 2 2       2 2 2
1 1 0       2 1 0       2 2 0       2 2 0
0 1 1       0 1 1       0 2 1       0 2 2

Queue starts with all rotten (2) positions.
Each minute: all rotten oranges spread to adjacent fresh oranges.
Answer: 3 minutes (or -1 if unreachable fresh oranges remain)
```

---

## Time/Space Complexity

| Metric | Complexity |
|--------|-----------|
| Time | O(V + E) for graph, O(m×n) for grid |
| Space | O(V) for queue + visited |

---

## Common Mistakes

1. **Not marking visited before adding to queue** → Leads to duplicate processing
2. **Forgetting to capture queue size per level** → Breaks level tracking
3. **Using DFS when shortest path is needed** → DFS doesn't guarantee shortest path

---

## Related Patterns

- [[11 - DepthFirstSearch/Concept|DFS]] — Alternative traversal; use BFS for shortest path
- [[12 - MatrixTraversal/Concept|Matrix Traversal]] — Grid-based BFS/DFS
- [[21 - ShortestPath/Concept|Shortest Path]] — Weighted version (Dijkstra)

---

#bfs #graph #dsa #concept
