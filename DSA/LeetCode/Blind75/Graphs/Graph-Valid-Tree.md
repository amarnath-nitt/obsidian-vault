# Graph Valid Tree

**Difficulty:** Medium (Premium)  
**Category:** Graphs  
**LeetCode Link:** [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)

---

## Problem Statement

Given `n` nodes labeled from `0` to `n-1` and a list of undirected edges, check if these edges form a valid tree.

**Example 1:**
```
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
```

**Example 2:**
```
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
```

**Constraints:**
- `1 <= n <= 2000`
- `0 <= edges.length <= 5000`

---

## Intuition

A valid tree must satisfy two conditions:
1. **Exactly n-1 edges** (tree property)
2. **All nodes connected** (no disconnected components)
3. **No cycles** (tree property)

---

## Approach: Union-Find

### Algorithm
1. Check if edges.length == n - 1 (necessary condition)
2. Use Union-Find to detect cycles
3. Check if all nodes are in one component

### Java Code
```java
class Solution {
    public boolean validTree(int n, int[][] edges) {
        // Tree must have exactly n-1 edges
        if (edges.length != n - 1) {
            return false;
        }
        
        // Union-Find
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        
        // Try to union all edges
        for (int[] edge : edges) {
            int root1 = find(parent, edge[0]);
            int root2 = find(parent, edge[1]);
            
            // If already in same set, there's a cycle
            if (root1 == root2) {
                return false;
            }
            
            // Union the sets
            parent[root1] = root2;
        }
        
        // If we have n-1 edges and no cycles, it's a valid tree
        return true;
    }
    
    private int find(int[] parent, int node) {
        if (parent[node] != node) {
            parent[node] = find(parent, parent[node]);  // Path compression
        }
        return parent[node];
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n * α(n)) ≈ O(n) - Union-Find with path compression
- **Space Complexity:** O(n) - Parent array

---

## Key Takeaways

1. **Tree properties:** n nodes, n-1 edges, connected, acyclic
2. **Union-Find:** Perfect for cycle detection
3. **Early check:** n-1 edges is necessary but not sufficient

---

## Tags
#graphs #union-find #tree #medium #blind75
