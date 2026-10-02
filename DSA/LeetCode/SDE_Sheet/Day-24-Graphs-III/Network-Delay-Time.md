# Network Delay Time

**LeetCode 743** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/network-delay-time/)

### Problem
Find time for signal to reach all nodes from source k (weighted directed graph).

### Java Solution (Dijkstra)

```java
class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());
        for (int[] t : times) adj.get(t[0]).add(new int[]{t[1], t[2]});

        int[] dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[k] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        pq.offer(new int[]{0, k});

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            if (curr[0] > dist[curr[1]]) continue;
            for (int[] edge : adj.get(curr[1])) {
                int newDist = dist[curr[1]] + edge[1];
                if (newDist < dist[edge[0]]) {
                    dist[edge[0]] = newDist;
                    pq.offer(new int[]{newDist, edge[0]});
                }
            }
        }

        int maxDist = 0;
        for (int i = 1; i <= n; i++) {
            if (dist[i] == Integer.MAX_VALUE) return -1;
            maxDist = Math.max(maxDist, dist[i]);
        }
        return maxDist;
    }
}
```

---
