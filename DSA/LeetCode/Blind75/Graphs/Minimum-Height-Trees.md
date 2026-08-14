# Minimum Height Trees

**Difficulty:** Medium  
**Category:** Graphs / Topological Sort  
**LeetCode Link:** [Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/)

---

## Problem Statement

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of `n` nodes labeled from `0` to `n - 1`, and an array of `n - 1` edges where `edges[i] = [ai, bi]` indicates that there is an undirected edge between the two nodes `ai` and `bi` in the tree, you can choose any node of the tree as the root.

Return a list of all **minimum height trees** (MHT) root labels. The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

**Example:**
```
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]

Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
```

---

## Intuition

The key insight: **minimum height tree roots are at the "center" of the tree**.

Think of it as **reverse topological sort** - repeatedly remove leaf nodes (nodes with degree 1) until we reach the center(s). The remaining 1-2 nodes are our answer.

Why 1-2 nodes?
- Tree with odd diameter → 1 center
- Tree with even diameter → 2 centers

---

## Approach: Trim Leaves (Similar to Kahn's Algorithm)

### Algorithm
1. Build adjacency list and calculate degrees
2. Add all leaves (degree = 1) to queue
3. Remove leaves layer by layer
4. Each removal reduces neighbors' degrees
5. Stop when ≤ 2 nodes remain (these are centers)

### Java Code
```java
class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n == 1) return Collections.singletonList(0);
        
        // Build adjacency list
        List<Set<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new HashSet<>());
        }
        
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }
        
        // Find all leaves (degree = 1)
        Queue<Integer> leaves = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (graph.get(i).size() == 1) {
                leaves.offer(i);
            }
        }
        
        // Trim leaves layer by layer
        int remaining = n;
        while (remaining > 2) {
            int size = leaves.size();
            remaining -= size;
            
            for (int i = 0; i < size; i++) {
                int leaf = leaves.poll();
                // Get the only neighbor
                int neighbor = graph.get(leaf).iterator().next();
                graph.get(neighbor).remove(leaf);
                
                // If neighbor becomes a leaf, add to queue
                if (graph.get(neighbor).size() == 1) {
                    leaves.offer(neighbor);
                }
            }
        }
        
        return new ArrayList<>(leaves);
    }
}
```

### Complexity
- **Time:** O(N) - Visit each node once
- **Space:** O(N) - Adjacency list

---

## Alternative: HashSet for Neighbors

```java
class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n == 1) return Arrays.asList(0);
        
        List<List<Integer>> graph = new ArrayList<>();
        int[] degree = new int[n];
        
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
            degree[edge[0]]++;
            degree[edge[1]]++;
        }
        
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (degree[i] == 1) queue.offer(i);
        }
        
        int remaining = n;
        while (remaining > 2) {
            int size = queue.size();
            remaining -= size;
            
            for (int i = 0; i < size; i++) {
                int node = queue.poll();
                for (int neighbor : graph.get(node)) {
                    degree[neighbor]--;
                    if (degree[neighbor] == 1) {
                        queue.offer(neighbor);
                    }
                }
            }
        }
        
        List<Integer> result = new ArrayList<>();
        while (!queue.isEmpty()) {
            result.add(queue.poll());
        }
        return result;
    }
}
```

---

## Key Insights

1. **MHT roots = tree centers** - Minimize maximum distance to leaves
2. **Reverse topological sort** - Instead of starting from nodes with in-degree 0, start from leaves (degree 1)
3. **At most 2 centers** - Mathematical property of trees
4. **Layer-by-layer removal** - Similar to BFS/Kahn's algorithm

---

## Edge Cases
- Single node: `n = 1` → return `[0]`
- Two nodes: `n = 2` → both are centers
- Linear tree: Middle node(s) are centers

---

## Visual Example

```
Tree: 0-1-2-3-4
        |
        5

Step 1: Remove leaves [0,3,4,5]
Remaining: [1,2]

Result: [1,2] (both centers)
```

---

## Tags
#topological-sort #graphs #bfs #tree #trim-leaves #medium #center-finding
