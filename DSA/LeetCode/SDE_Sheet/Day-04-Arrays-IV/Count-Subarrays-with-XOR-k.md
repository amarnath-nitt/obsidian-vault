# Count Subarrays with XOR = k

**Problem:** Count subarrays whose XOR equals k.

### Approach (Prefix XOR + HashMap)

- Like prefix sum but with XOR
- `XOR(i, j) = prefXOR[j] ^ prefXOR[i-1]`
- If `prefXOR[j] ^ k = prefXOR[i-1]` → subarray XOR = k
- Store frequency of each prefix XOR in map

### Java Solution

```java
public int countSubarraysWithXOR(int[] arr, int k) {
    Map<Integer, Integer> map = new HashMap<>();
    map.put(0, 1);
    int prefXOR = 0, count = 0;

    for (int num : arr) {
        prefXOR ^= num;
        count += map.getOrDefault(prefXOR ^ k, 0);
        map.put(prefXOR, map.getOrDefault(prefXOR, 0) + 1);
    }
    return count;
}
```

**Complexity:** Time O(n) · Space O(n)

---
