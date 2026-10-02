# Number of Connected Components in Undirected Graph

**Difficulty:** Medium (Premium)
**Category:** Graphs
**LeetCode Link:** [Number of Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

---

## Problem Statement

Given `n` nodes labeled `0` to `n-1` and a list of undirected edges, return the number of connected components in the graph.

**Example:**
```
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
```

---

## Intuition

Each connected component is a group of nodes reachable from each other. Count components by running DFS from each unvisited node — each new DFS start = new component. Alternatively, Union-Find merges connected nodes and counts distinct roots.

---

## Approach 1: DFS

### Algorithm
1. Build adjacency list
2. For each unvisited node, run DFS and increment component count
3. DFS marks all reachable nodes as visited

### Java Code
```java
class Solution {
    public int countComponents(int n, int[][] edges) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());

        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        boolean[] visited = new boolean[n];
        int components = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(graph, visited, i);
                components++;
            }
        }

        return components;
    }

    private void dfs(List<List<Integer>> graph, boolean[] visited, int node) {
        visited[node] = true;
        for (int neighbor : graph.get(node)) {
            if (!visited[neighbor]) dfs(graph, visited, neighbor);
        }
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V + E)

---

## Approach 2: Union-Find (Optimal)

### Algorithm
1. Initialize each node as its own parent
2. For each edge, union the two nodes
3. Count nodes where `parent[i] == i` (distinct roots = components)

### Java Code
```java
class Solution {
    public int countComponents(int n, int[][] edges) {
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        for (int[] edge : edges) union(parent, edge[0], edge[1]);

        int components = 0;
        for (int i = 0; i < n; i++) {
            if (parent[i] == i) components++;
        }
        return components;
    }

    private int find(int[] parent, int node) {
        if (parent[node] != node) parent[node] = find(parent, parent[node]);
        return parent[node];
    }

    private void union(int[] parent, int a, int b) {
        int rootA = find(parent, a), rootB = find(parent, b);
        if (rootA != rootB) parent[rootA] = rootB;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O((V + E) × α(V)) ≈ O(V + E)
- **Space Complexity:** O(V)

---

## Key Takeaways

1. **Pattern:** Each DFS start from unvisited node = new component
2. **Union-Find:** Efficient for dynamic connectivity; path compression makes it nearly O(1)
3. **Both approaches** are valid — Union-Find is preferred for follow-up questions about dynamic edges

---

## Tags
#graphs #union-find #dfs #medium #blind75
