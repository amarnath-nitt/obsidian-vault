---
solved: false
difficulty: Medium
pattern: Shortest Path
lc_number: 743
date_solved: 
tags:
  - dsa
  - shortest-path
  - medium
---
# Network Delay Time (LC 743)

**Difficulty**: Medium  
**Pattern**: Shortest Path  
**LeetCode**: https://leetcode.com/problems/network-delay-time/

## Problem Statement
You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (ui, vi, wi)`, where `ui` is the source node, `vi` is the target node, and `wi` is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return the minimum time it takes for all the `n` nodes to receive the signal. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

**Example:**
```
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
```

## Approach 1: Dijkstra's Algorithm

### Intuition
This is a classic single-source shortest path problem with non-negative weights. Dijkstra's algorithm is efficient for this. We want the maximum of shortest paths to all nodes.

### Java Code
```java
class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        // Build graph
        Map<Integer, List<int[]>> graph = new HashMap<>();
        for (int[] time : times) {
            graph.computeIfAbsent(time[0], x -> new ArrayList<>()).add(new int[]{time[1], time[2]});
        }
        
        // Priority Queue for Dijkstra: [node, time] sorted by time
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        pq.offer(new int[]{k, 0});
        
        Map<Integer, Integer> dist = new HashMap<>();
        
        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int node = current[0];
            int time = current[1];
            
            if (dist.containsKey(node)) continue;
            dist.put(node, time);
            
            if (graph.containsKey(node)) {
                for (int[] edge : graph.get(node)) {
                    int neighbor = edge[0];
                    int weight = edge[1];
                    if (!dist.containsKey(neighbor)) {
                        pq.offer(new int[]{neighbor, time + weight});
                    }
                }
            }
        }
        
        if (dist.size() != n) return -1;
        
        int maxTime = 0;
        for (int time : dist.values()) {
            maxTime = Math.max(maxTime, time);
        }
        
        return maxTime;
    }
}
```

### Complexity
- **Time**: O(E log V) or O(E + V log V) depending on implementation
- **Space**: O(V + E)

## Approach 2: Bellman-Ford

### Intuition
Since N is small (up to 100), Bellman-Ford can also work. It runs in O(V*E).

### Java Code
```java
class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        int[] dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[k] = 0;
        
        // Relax all edges V-1 times
        for (int i = 0; i < n - 1; i++) {
            for (int[] time : times) {
                int u = time[0];
                int v = time[1];
                int w = time[2];
                if (dist[u] != Integer.MAX_VALUE && dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                }
            }
        }
        
        int maxTime = 0;
        for (int i = 1; i <= n; i++) {
            maxTime = Math.max(maxTime, dist[i]);
        }
        
        return maxTime == Integer.MAX_VALUE ? -1 : maxTime;
    }
}
```

## Key Takeaways
- Dijkstra is preferred for non-negative weights
- Priority Queue manages the "frontier" of exploration
- `dist` map/array tracks shortest path found so far
