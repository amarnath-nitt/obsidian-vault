# Largest Subarray with Zero Sum

**Problem:** Find the length of the largest subarray with sum = 0.

### Approach (Prefix Sum + HashMap)

- `prefixSum[i]` = sum of elements from index 0 to i
- If `prefixSum[i] == prefixSum[j]` for i < j, then subarray `(i+1, j)` has sum 0
- Store **first occurrence** of each prefix sum in a map
- If prefix sum repeats → update max length

### Java Solution

```java
public int maxLen(int[] arr) {
    Map<Integer, Integer> map = new HashMap<>();
    map.put(0, -1);
    int maxLen = 0, sum = 0;

    for (int i = 0; i < arr.length; i++) {
        sum += arr[i];
        if (map.containsKey(sum)) {
            maxLen = Math.max(maxLen, i - map.get(sum));
        } else {
            map.put(sum, i);
        }
    }
    return maxLen;
}
```

**Complexity:** Time O(n) · Space O(n)

---
