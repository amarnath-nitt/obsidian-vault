# Prefix Sum — Concept

## What Is It?

Prefix Sum is a preprocessing technique that builds a cumulative sum array, allowing you to answer **range sum queries in O(1)** after an O(n) build step.

---

## When to Use

> **Trigger keywords:** "sum of subarray", "range sum", "cumulative", "running total", "sum between indices"

| Trigger | Example |
|---------|---------|
| Need **sum of elements in a range [i, j]** | Range Sum Query |
| Multiple range queries on **static array** | Immutable prefix sum |
| Finding subarrays with a **target sum** | Subarray Sum Equals K |
| Need a **running total** | Running Sum of 1D Array |

---

## Variants

### 1. 1D Prefix Sum
```java
int[] prefix = new int[n + 1];
for (int i = 0; i < n; i++) {
    prefix[i + 1] = prefix[i] + nums[i];
}
// Sum of range [i, j] = prefix[j+1] - prefix[i]
```

### 2. 2D Prefix Sum (Matrix)
```java
int[][] prefix = new int[m + 1][n + 1];
for (int i = 1; i <= m; i++) {
    for (int j = 1; j <= n; j++) {
        prefix[i][j] = matrix[i-1][j-1]
                      + prefix[i-1][j]
                      + prefix[i][j-1]
                      - prefix[i-1][j-1];
    }
}
```

### 3. Prefix Sum + HashMap
Find subarrays with sum = k using `prefix[j] - prefix[i] = k`.
```java
Map<Integer, Integer> map = new HashMap<>();
map.put(0, 1);
int sum = 0, count = 0;
for (int num : nums) {
    sum += num;
    count += map.getOrDefault(sum - k, 0);
    map.put(sum, map.getOrDefault(sum, 0) + 1);
}
```

---

## Visual Walkthrough

```
Array:   [2, 4, 1, 3, 5]
Prefix:  [0, 2, 6, 7, 10, 15]

Query: Sum of [1, 3] (elements 4, 1, 3)
Answer: prefix[4] - prefix[1] = 10 - 2 = 8 ✓

         0    2    6    7    10   15
prefix:  |----|----|----|----|----| 
              ^              ^
           prefix[1]      prefix[4]
           
         prefix[4] - prefix[1] = 10 - 2 = 8
```

---

## Time/Space Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Build prefix array | O(n) | O(n) |
| Range sum query | O(1) | — |
| 2D build | O(m×n) | O(m×n) |
| Prefix + HashMap | O(n) | O(n) |

---

## Common Mistakes

1. **Off-by-one errors** — Use `prefix[j+1] - prefix[i]` not `prefix[j] - prefix[i]`
2. **Forgetting `map.put(0, 1)`** — For HashMap variant, the empty prefix (sum = 0) must be initialized
3. **Using prefix sum on a mutable array** — Prefix sum is for static arrays; use Fenwick/Segment Tree for updates

---

## Related Patterns

- [[03 - FrequencyCounting/Concept|Frequency Counting]] — Often combined: count occurrences + prefix sum
- [[06 - SlidingWindow/Concept|Sliding Window]] — Alternative for contiguous subarray problems
- [[20 - DynamicProgramming/Concept|Dynamic Programming]] — Prefix sum is a form of DP

---

#prefix-sum #dsa #concept
