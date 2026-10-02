# Rabin-Karp String Hashing

**Approach:** Rolling hash to find pattern in text in O(n+m) average.

```java
public int search(String text, String pattern) {
    int n = text.length(), m = pattern.length();
    long base = 31, mod = 1_000_000_007;
    long patHash = 0, winHash = 0, power = 1;

    for (int i = 0; i < m - 1; i++) power = power * base % mod;

    for (int i = 0; i < m; i++) {
        patHash = (patHash * base + pattern.charAt(i)) % mod;
        winHash = (winHash * base + text.charAt(i)) % mod;
    }

    for (int i = 0; i <= n - m; i++) {
        if (winHash == patHash) {
            // Verify (collision check)
            if (text.substring(i, i + m).equals(pattern)) return i;
        }
        if (i < n - m) {
            winHash = (winHash - text.charAt(i) * power % mod + mod) % mod;
            winHash = (winHash * base + text.charAt(i + m)) % mod;
        }
    }
    return -1;
}
```

**Complexity:** Time O(n+m) average, O(nm) worst · Space O(1)

---
