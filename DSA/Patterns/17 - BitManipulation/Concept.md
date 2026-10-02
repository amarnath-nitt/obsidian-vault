# Bit Manipulation — Concept

## What Is It?

Bit Manipulation operates directly on binary representations of integers using bitwise operators (`&`, `|`, `^`, `~`, `<<`, `>>`). It provides O(1) operations for tasks that otherwise require O(n) with data structures.

---

## When to Use

> **Trigger keywords:** "single number", "power of two", "counting bits", "XOR", "missing number", "subset generation"

---

## Key Operations

| Operation | Code | Purpose |
|-----------|------|---------|
| Check if bit set | `(n >> i) & 1` | Is bit i set? |
| Set bit | `n \| (1 << i)` | Turn on bit i |
| Clear bit | `n & ~(1 << i)` | Turn off bit i |
| Toggle bit | `n ^ (1 << i)` | Flip bit i |
| Check power of 2 | `n & (n-1) == 0` | Only one bit set? |
| Count set bits | `Integer.bitCount(n)` | Population count |
| Get lowest set bit | `n & (-n)` | Isolate rightmost 1 |
| Clear lowest set bit | `n & (n-1)` | Turn off rightmost 1 |

---

## Variants

### XOR tricks
```java
// Find single number (all others appear twice)
int result = 0;
for (int num : nums) result ^= num;
// a ^ a = 0, a ^ 0 = a → only unique remains
```

### Subset generation with bitmask
```java
for (int mask = 0; mask < (1 << n); mask++) {
    List<Integer> subset = new ArrayList<>();
    for (int i = 0; i < n; i++) {
        if ((mask & (1 << i)) != 0) {
            subset.add(nums[i]);
        }
    }
}
```

---

## Visual Walkthrough

### Single Number: `[4, 1, 2, 1, 2]`
```
XOR all elements:
  0000 (result = 0)
^ 0100 (4)    = 0100
^ 0001 (1)    = 0101
^ 0010 (2)    = 0111
^ 0001 (1)    = 0110  ← 1 cancels out
^ 0010 (2)    = 0100  ← 2 cancels out

Result: 0100 = 4 ✓
```

---

## Time/Space Complexity

| Operation | Time | Space |
|-----------|------|-------|
| XOR find single | O(n) | O(1) |
| Count bits | O(1) or O(log n) | O(1) |
| Subset generation | O(2^n × n) | O(n) |

---

## Common Mistakes

1. **Operator precedence** → `(n & (1 << i)) != 0` needs parentheses around `&`
2. **Signed vs unsigned shift** → Use `>>>` for unsigned right shift in Java
3. **Integer overflow** → `1 << 31` overflows int; use `1L << 31` for long

---

## Related Patterns

- [[19 - Backtracking/Concept|Backtracking]] — Bitmask can replace backtracking for subset problems
- [[20 - DynamicProgramming/Concept|Dynamic Programming]] — Bitmask DP for state compression

---

#bit-manipulation #dsa #concept
