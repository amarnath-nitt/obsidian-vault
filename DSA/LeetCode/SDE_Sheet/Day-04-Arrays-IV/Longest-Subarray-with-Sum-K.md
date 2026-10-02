# Longest Subarray with Sum K

**Problem:** Find the longest subarray with sum equal to k. Array can have negatives.

### Approach (Prefix Sum + HashMap)

- `prefixSum[i] - k = prefixSum[j]` → subarray `(j+1, i)` has sum k
- Store first occurrence of each prefix sum

### Java Solution

```java
public int longestSubarrayWithSumK(int[] arr, int k) {
    Map<Integer, Integer> map = new HashMap<>();
    map.put(0, -1);
    int sum = 0, maxLen = 0;

    for (int i = 0; i < arr.length; i++) {
        sum += arr[i];
        if (map.containsKey(sum - k))
            maxLen = Math.max(maxLen, i - map.get(sum - k));
        if (!map.containsKey(sum))  // store only first occurrence
            map.put(sum, i);
    }
    return maxLen;
}
```

> **If array has only non-negative numbers:** Use two-pointer sliding window instead (O(n) no extra space).

**Complexity:** Time O(n) · Space O(n)

---
