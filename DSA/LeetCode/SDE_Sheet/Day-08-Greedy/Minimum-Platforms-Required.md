# Minimum Platforms Required

**Problem:** Given arrival and departure times of trains, find the minimum number of platforms needed.

### Approach (Sort + Two Pointers)

- Sort arrival and departure arrays separately
- Use two pointers: advance arrival or departure based on which is smaller
- Track platforms in use and max platforms used

### Java Solution

```java
public int minPlatforms(int[] arr, int[] dep) {
    Arrays.sort(arr);
    Arrays.sort(dep);

    int platforms = 1, maxPlatforms = 1;
    int i = 1, j = 0;

    while (i < arr.length && j < dep.length) {
        if (arr[i] <= dep[j]) { // new train arrives before current leaves
            platforms++;
            i++;
        } else {
            platforms--;
            j++;
        }
        maxPlatforms = Math.max(maxPlatforms, platforms);
    }
    return maxPlatforms;
}
```

**Complexity:** Time O(n log n) · Space O(1)

---
