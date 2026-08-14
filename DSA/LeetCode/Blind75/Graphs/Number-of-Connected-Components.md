# Number of Connected Components in Undirected Graph

**Difficulty:** Medium (Premium)  
**Category:** Graphs  
**LeetCode Link:** [Number of Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

---

## Problem Statement

Given `n` nodes labeled from `0` to `n-1` and a list of undirected edges, return the number of connected components in the graph.

**Example:**
```
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
```

**Constraints:**
- `1 <= n <= 2000`
- `0 <= edges.length <= 5000`

---

## Intuition

Count how many separate groups of connected nodes exist. Can use DFS, BFS, or Union-Find.

---

## Approach: Union-Find

### Algorithm
1. Initialize each node as its own component
2. For each edge, union the two nodes
3. Count number of unique roots

### Java Code
```java
class Solution {
    public int countComponents(int n, int[][] edges) {
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        
        // Union all edges
        for (int[] edge : edges) {
            union(parent, edge[0], edge[1]);
        }
        
        // Count unique roots
        int components = 0;
        for (int i = 0; i < n; i++) {
            if (parent[i] == i) {
                components++;
            }
        }
        
        return components;
    }
    
    private int find(int[] parent, int node) {
        if (parent[node] != node) {
            parent[node] = find(parent, parent[node]);
        }
        return parent[node];
    }
    
    private void union(int[] parent, int a, int b) {
        int rootA = find(parent, a);
        int rootB = find(parent, b);
        if (rootA != rootB) {
            parent[rootA] = rootB;
        }
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n + m * α(n)) ≈ O(n + m) where m = edges
- **Space Complexity:** O(n) - Parent array

---

## Tags
#graphs #union-find #dfs #bfs #medium #blind75

---

## Visualization

- Embed: `![](../assets/connected-components/step-1.svg)`
- Obsidian embed: `![[../assets/connected-components/step-1.svg]]`

<svg xmlns="http://www.w3.org/2000/svg" width="760" height="140">
    <style>text{font-family: Arial, sans-serif; font-size:13px}</style>
    <text x="20" y="28" fill="#222">Union-Find groups visualization</text>
    <g transform="translate(20,50)">
        <circle cx="40" cy="20" r="12" fill="#cfe8ff" stroke="#9cc3ff"/>
        <text x="40" y="24" text-anchor="middle">0</text>
        <circle cx="100" cy="20" r="12" fill="#cfe8ff" stroke="#9cc3ff"/>
        <text x="100" y="24" text-anchor="middle">1</text>
        <circle cx="160" cy="20" r="12" fill="#cfe8ff" stroke="#9cc3ff"/>
        <text x="160" y="24" text-anchor="middle">2</text>
        <path d="M52 20 L88 20" stroke="#999"/>
        <path d="M112 20 L148 20" stroke="#999"/>
    </g>
</svg>
