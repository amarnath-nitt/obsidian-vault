# Shortest Path Visiting All Nodes

[Problem Link](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)

## Problem Statement
You have an undirected, connected graph of `n` nodes labeled from `0` to `n - 1`. You are given an array `graph` where `graph[i]` is a list of all the nodes connected with node `i` by an edge.
Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

## Approach
BFS with State (Node, Mask).
State: `(currentNode, visitedMask)`.
We want shortest path to reach state where `visitedMask == (1 << n) - 1`.
Since edge weights are 1 (steps), BFS works.
Start BFS from ALL nodes simultaneously with initial mask `1 << i`.
Visited set uses `(node, mask)` to avoid cycles/redundant work.

## Time and Space Complexity
- **Time Complexity:** O(N * 2^N).
- **Space Complexity:** O(N * 2^N).

## Code
```java
class Solution {
    public int shortestPathLength(int[][] graph) {
        int n = graph.length;
        if (n == 1) return 0;
        
        // Queue stores [node, mask, dist]
        Queue<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[n][1 << n];
        
        for (int i = 0; i < n; i++) {
            queue.offer(new int[]{i, 1 << i, 0});
            visited[i][1 << i] = true;
        }
        
        int finalMask = (1 << n) - 1;
        
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int u = curr[0];
            int mask = curr[1];
            int dist = curr[2];
            
            if (mask == finalMask) return dist;
            
            for (int v : graph[u]) {
                int newMask = mask | (1 << v);
                if (!visited[v][newMask]) {
                    visited[v][newMask] = true;
                    queue.offer(new int[]{v, newMask, dist + 1});
                }
            }
        }
        return -1;
    }
}
```
