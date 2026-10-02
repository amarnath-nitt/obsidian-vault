# Celebrity Problem

**Problem:** N people, a celebrity is known by all but knows nobody. Find the celebrity.

### Approach (Stack Elimination)

1. Push all people on stack
2. Pop two people `a, b`: if `a knows b` → a can't be celebrity (pop a, keep b); else b can't be
3. Last person on stack is the **candidate**
4. Verify: all others know candidate, candidate knows no one

### Java Solution

```java
// knows(a, b) returns true if a knows b (given as API)
public int findCelebrity(int n) {
    // Find candidate
    int candidate = 0;
    for (int i = 1; i < n; i++)
        if (knows(candidate, i)) candidate = i;

    // Verify candidate
    for (int i = 0; i < n; i++) {
        if (i == candidate) continue;
        if (knows(candidate, i) || !knows(i, candidate)) return -1;
    }
    return candidate;
}
```

**Complexity:** Time O(n) · Space O(1)

---
