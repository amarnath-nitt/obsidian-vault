# Cheapest Flights Within K Stops

**LeetCode 787** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

### Approach (Modified Bellman-Ford — K+1 iterations)

- Relax edges exactly **K+1 times** (K stops = K+1 edges)
- Use a **copy** of dist array to avoid using edges from same iteration

```java
class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[src] = 0;

        for (int i = 0; i <= k; i++) { // K stops = K+1 edges
            int[] temp = Arrays.copyOf(dist, n);
            for (int[] flight : flights) {
                int u = flight[0], v = flight[1], w = flight[2];
                if (dist[u] != Integer.MAX_VALUE && dist[u] + w < temp[v])
                    temp[v] = dist[u] + w;
            }
            dist = temp;
        }
        return dist[dst] == Integer.MAX_VALUE ? -1 : dist[dst];
    }
}
```

**Complexity:** Time O(K×E) · Space O(V)

---
