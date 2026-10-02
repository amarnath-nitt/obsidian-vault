# Number of Operations to Make Network Connected

**LeetCode 1319** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)

### Problem
Minimum cable moves to connect all computers. Return -1 if not enough cables.

### Approach (DSU)

- Count connected components
- Need at least `n-1` cables to connect `n` computers
- Answer = number of components - 1

```java
class Solution {
    public int makeConnected(int n, int[][] connections) {
        if (connections.length < n - 1) return -1; // not enough cables

        DSU dsu = new DSU(n);
        int components = n;
        for (int[] c : connections)
            if (dsu.union(c[0], c[1])) components--;

        return components - 1;
    }
}
```

---
