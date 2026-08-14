# Path with Maximum Probability (LC 1514)

**Difficulty**: Medium  
**Pattern**: Shortest Path (Dijkstra Variant)  
**LeetCode**: https://leetcode.com/problems/path-with-maximum-probability/

## Problem Statement
You are given an undirected weighted graph of `n` nodes (0-indexed), represented by an edge list where `edges[i] = [a, b]` is an undirected edge connecting the nodes `a` and `b` with a probability of success of traversing that edge `succProb[i]`.
Given two nodes `start` and `end`, find the path with the maximum probability of success to go from `start` to `end`.
If there is no path from `start` to `end`, return 0.

**Example:**
```
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25 (0->1->2: 0.5 * 0.5 = 0.25)
```

## Approach: Dijkstra (Max Heap)

### Intuition
Standard Dijkstra finds min distance (sum of weights).
Here, we want max probability (product of probabilities).
Since probabilities are `<= 1`, multiplying makes them smaller.
Use Max-Heap. Relax edge if `curr_prob * edge_prob > neighbor_prob`.

### Java Code
```java
class Solution {
    public double maxProbability(int n, int[][] edges, double[] succProb, int start, int end) {
        List<List<Pair>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        
        for (int i = 0; i < edges.length; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            double p = succProb[i];
            graph.get(u).add(new Pair(v, p));
            graph.get(v).add(new Pair(u, p));
        }
        
        double[] probs = new double[n]; // Init to 0.0
        probs[start] = 1.0;
        
        PriorityQueue<Pair> pq = new PriorityQueue<>((a, b) -> Double.compare(b.prob, a.prob));
        pq.offer(new Pair(start, 1.0));
        
        while (!pq.isEmpty()) {
            Pair curr = pq.poll();
            int u = curr.node;
            double p = curr.prob;
            
            if (u == end) return p;
            
            if (p < probs[u]) continue;
            
            for (Pair neighbor : graph.get(u)) {
                int v = neighbor.node;
                double edgeProb = neighbor.prob;
                
                if (probs[u] * edgeProb > probs[v]) {
                    probs[v] = probs[u] * edgeProb;
                    pq.offer(new Pair(v, probs[v]));
                }
            }
        }
        
        return 0.0;
    }
    
    class Pair {
        int node;
        double prob;
        Pair(int node, double prob) {
            this.node = node;
            this.prob = prob;
        }
    }
}
```

### Complexity
- **Time**: O(E log V)
- **Space**: O(V + E)

## Key Takeaways
- Dijkstra works for "Max Product" if factors are <= 1
- Use Max-Heap
