# Fractional Knapsack

**Problem:** Items with weights and values. Knapsack capacity W. Can take fractions. Maximize value.

### Approach (Greedy — Sort by Value/Weight Ratio)

- Sort items by `value/weight` descending
- Take as much of each item as possible

> Unlike 0/1 knapsack, fractions are allowed → greedy works!

### Java Solution

```java
public double fractionalKnapsack(int W, int[] weight, int[] value) {
    int n = weight.length;
    Integer[] idx = new Integer[n];
    for (int i = 0; i < n; i++) idx[i] = i;
    // Sort by value/weight ratio descending
    Arrays.sort(idx, (a, b) -> Double.compare(
        (double)value[b]/weight[b], (double)value[a]/weight[a]));

    double totalValue = 0;
    for (int i : idx) {
        if (W >= weight[i]) {
            totalValue += value[i];
            W -= weight[i];
        } else {
            totalValue += (double)value[i] / weight[i] * W;
            break;
        }
    }
    return totalValue;
}
```

**Complexity:** Time O(n log n) · Space O(n)

---
