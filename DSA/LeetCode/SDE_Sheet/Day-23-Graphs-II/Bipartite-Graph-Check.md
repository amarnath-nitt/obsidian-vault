# Bipartite Graph Check

**LeetCode 785** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/is-graph-bipartite/)

### Problem
A graph is bipartite if we can color nodes with 2 colors such that no two adjacent nodes share the same color.

### Approach (BFS Coloring)

- Color nodes alternately
- If a neighbor has the same color → not bipartite

### Java Solution

```java
class Solution {
    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        int[] color = new int[n]; // 0=uncolored, 1=red, -1=blue

        for (int i = 0; i < n; i++) {
            if (color[i] != 0) continue;
            Queue<Integer> queue = new LinkedList<>();
            queue.offer(i);
            color[i] = 1;
            while (!queue.isEmpty()) {
                int node = queue.poll();
                for (int neighbor : graph[node]) {
                    if (color[neighbor] == 0) {
                        color[neighbor] = -color[node];
                        queue.offer(neighbor);
                    } else if (color[neighbor] == color[node]) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}
```

**Complexity:** Time O(V+E) · Space O(V)

---
