# Topological Sort (Kahn's BFS)

**Problem:** Linear ordering of vertices in a DAG such that for every edge u→v, u comes before v.

### Approach (Kahn's — BFS with in-degree)

1. Compute **in-degree** of all nodes
2. Add all nodes with `in-degree == 0` to queue
3. Process queue: decrement neighbor's in-degree; if 0, add to queue
4. If total processed == n → valid topo sort; else cycle exists

### Java Solution

```java
List<Integer> topoSort(int n, List<List<Integer>> adj) {
    int[] inDegree = new int[n];
    for (int u = 0; u < n; u++)
        for (int v : adj.get(u)) inDegree[v]++;

    Queue<Integer> queue = new LinkedList<>();
    for (int i = 0; i < n; i++)
        if (inDegree[i] == 0) queue.offer(i);

    List<Integer> order = new ArrayList<>();
    while (!queue.isEmpty()) {
        int node = queue.poll();
        order.add(node);
        for (int neighbor : adj.get(node)) {
            if (--inDegree[neighbor] == 0) queue.offer(neighbor);
        }
    }
    return order.size() == n ? order : new ArrayList<>(); // empty if cycle
}
```

### DFS Topo Sort

```java
void dfsTopoSort(int node, boolean[] visited, Deque<Integer> stack, List<List<Integer>> adj) {
    visited[node] = true;
    for (int neighbor : adj.get(node))
        if (!visited[neighbor]) dfsTopoSort(neighbor, visited, stack, adj);
    stack.push(node); // push AFTER processing all neighbors
}
```

---
