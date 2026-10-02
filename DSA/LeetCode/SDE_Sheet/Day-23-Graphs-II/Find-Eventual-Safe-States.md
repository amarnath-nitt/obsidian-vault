# Find Eventual Safe States

**LeetCode 802** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/find-eventual-safe-states/)

### Problem
A node is "safe" if every path from it leads to a terminal node (no cycle).

### Approach

- A node is safe if it's NOT in a cycle
- Reverse the graph and find nodes reachable from terminal nodes using Kahn's

```java
class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int n = graph.length;
        List<List<Integer>> reverseGraph = new ArrayList<>();
        int[] inDegree = new int[n];
        for (int i = 0; i < n; i++) reverseGraph.add(new ArrayList<>());

        for (int u = 0; u < n; u++)
            for (int v : graph[u]) {
                reverseGraph.get(v).add(u);
                inDegree[u]++;
            }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++)
            if (inDegree[i] == 0) queue.offer(i);

        boolean[] safe = new boolean[n];
        while (!queue.isEmpty()) {
            int node = queue.poll();
            safe[node] = true;
            for (int prev : reverseGraph.get(node))
                if (--inDegree[prev] == 0) queue.offer(prev);
        }

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) if (safe[i]) result.add(i);
        return result;
    }
}
```

---
