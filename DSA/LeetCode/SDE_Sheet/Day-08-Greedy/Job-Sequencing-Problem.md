# Job Sequencing Problem

**Problem:** Jobs with deadlines and profits. Each job takes 1 unit. Find max profit sequence.

### Approach (Greedy — Sort by Profit Descending)

1. Sort jobs by **profit descending**
2. For each job, assign to the latest available slot ≤ deadline
3. Use a boolean array to track occupied slots

### Java Solution

```java
public int[] jobSequencing(int[] id, int[] deadline, int[] profit) {
    int n = id.length;
    Integer[] idx = new Integer[n];
    for (int i = 0; i < n; i++) idx[i] = i;
    Arrays.sort(idx, (a, b) -> profit[b] - profit[a]); // sort by profit desc

    int maxDeadline = Arrays.stream(deadline).max().getAsInt();
    boolean[] slots = new boolean[maxDeadline + 1];
    int jobsDone = 0, totalProfit = 0;

    for (int i : idx) {
        for (int j = deadline[i]; j > 0; j--) {
            if (!slots[j]) {
                slots[j] = true;
                jobsDone++;
                totalProfit += profit[i];
                break;
            }
        }
    }
    return new int[]{jobsDone, totalProfit};
}
```

**Complexity:** Time O(n² worst) / O(n log n) with Union-Find · Space O(maxDeadline)

---
