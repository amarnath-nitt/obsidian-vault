# Prim's MST Algorithm

### Approach (Greedy + Min-Heap)

1. Start from any vertex, add it to MST
2. Use min-heap to always pick the minimum weight edge connecting MST to non-MST vertex
3. Add picked vertex to MST, add its edges to heap

### Java Solution

```java
public int primMST(int n, List<List<int[]>> adj) {
    boolean[] inMST = new boolean[n];
    PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
    pq.offer(new int[]{0, 0}); // [weight, node]
    int totalWeight = 0;

    while (!pq.isEmpty()) {
        int[] curr = pq.poll();
        int w = curr[0], node = curr[1];
        if (inMST[node]) continue;
        inMST[node] = true;
        totalWeight += w;
        for (int[] edge : adj.get(node)) {
            if (!inMST[edge[0]]) pq.offer(new int[]{edge[1], edge[0]});
        }
    }
    return totalWeight;
}
```

**Complexity:** Time O(E log V) · Space O(V+E)

---
