# Critical Connections (Bridges)

**LeetCode 1192** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/critical-connections-in-a-network/)

### Problem
Find all bridges — edges whose removal disconnects the graph.

### Approach (Tarjan's Bridge Finding Algorithm)

- Maintain `disc[]` (discovery time) and `low[]` (lowest disc reachable)
- An edge `(u, v)` is a bridge if `low[v] > disc[u]`

```java
class Solution {
    List<List<Integer>> result = new ArrayList<>();
    int[] disc, low;
    int timer = 0;

    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        disc = new int[n]; low = new int[n];
        Arrays.fill(disc, -1);
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (List<Integer> c : connections) {
            adj.get(c.get(0)).add(c.get(1));
            adj.get(c.get(1)).add(c.get(0));
        }
        dfs(0, -1, adj);
        return result;
    }

    void dfs(int u, int parent, List<List<Integer>> adj) {
        disc[u] = low[u] = timer++;
        for (int v : adj.get(u)) {
            if (disc[v] == -1) {
                dfs(v, u, adj);
                low[u] = Math.min(low[u], low[v]);
                if (low[v] > disc[u]) result.add(Arrays.asList(u, v)); // bridge
            } else if (v != parent) {
                low[u] = Math.min(low[u], disc[v]);
            }
        }
    }
}
```

**Complexity:** Time O(V+E) · Space O(V+E)

---
