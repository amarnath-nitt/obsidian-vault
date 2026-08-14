# Cheapest Flights Within K Stops (LC 787)

**Difficulty**: Medium  
**Pattern**: Shortest Path / Bellman-Ford / Dijkstra  
**LeetCode**: https://leetcode.com/problems/cheapest-flights-within-k-stops/

## Problem Statement
There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = [from, to, price]`.
You are also given three integers `src`, `dst`, and `k`, return the cheapest price from `src` to `dst` with at most `k` stops. If there is no such route, return `-1`.

**Example:**
```
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
```

## Approach: Bellman-Ford (Relaxation)

### Intuition
Standard Dijkstra finds shortest path but doesn't handle "at most K stops" constraint strictly (exploring min path might exceed K stops).
Bellman-Ford relaxes all edges `K+1` times. `dp[i][v]` = min cost to reach `v` using at most `i` edges.
Optimization: Use two arrays `prices` and `tempPrices` to store state of previous iteration.

### Java Code
```java
class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        int[] prices = new int[n];
        Arrays.fill(prices, Integer.MAX_VALUE);
        prices[src] = 0;
        
        for (int i = 0; i <= k; i++) {
            int[] tempPrices = prices.clone();
            
            for (int[] flight : flights) {
                int u = flight[0]; // From
                int v = flight[1]; // To
                int price = flight[2]; 
                
                if (prices[u] != Integer.MAX_VALUE && prices[u] + price < tempPrices[v]) {
                    tempPrices[v] = prices[u] + price;
                }
            }
            
            prices = tempPrices;
        }
        
        return prices[dst] == Integer.MAX_VALUE ? -1 : prices[dst];
    }
}
```

### Complexity
- **Time**: O((K+1) * E)
- **Space**: O(N)

## Key Takeaways
- "At most K stops" = "At most K+1 edges"
- Bellman-Ford level-by-level relaxation fits perfectly
- `tempPrices` array prevents using a node updated in *current* iteration
