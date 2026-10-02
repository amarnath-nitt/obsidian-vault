# Repeat and Missing Number

**Problem:** Given array of size N with values 1 to N, one number is repeated and one is missing. Find both.

### Approach (Math)

Let:
- `S` = sum of array, `S_n` = n*(n+1)/2
- `S2` = sum of squares of array, `S2_n` = n*(n+1)*(2n+1)/6

Then:
- `S - S_n = repeat - missing` → equation 1
- `S2 - S2_n = repeat² - missing²` → divide by eq1 → `repeat + missing` → equation 2

Solve two equations for repeat and missing.

### Java Solution

```java
public int[] findMissingRepeating(int[] arr) {
    long n = arr.length;
    long S = 0, S2 = 0;
    for (int x : arr) { S += x; S2 += (long)x*x; }

    long Sn = n*(n+1)/2;
    long S2n = n*(n+1)*(2*n+1)/6;

    long diff = S - Sn;          // repeat - missing
    long diff2 = (S2 - S2n) / diff; // repeat + missing

    long repeat = (diff + diff2) / 2;
    long missing = repeat - diff;

    return new int[]{(int)repeat, (int)missing};
}
```

**Complexity:** Time O(n) · Space O(1)

---
