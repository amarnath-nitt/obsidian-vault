# Sliding Window — Concept

## What Is It?

Sliding Window maintains a **contiguous window** over an array/string, expanding and shrinking it to find optimal subarrays/substrings. It converts O(n²) brute-force into O(n) by reusing computation from the previous window position.

---

## When to Use

> **Trigger keywords:** "subarray", "substring", "contiguous", "window of size k", "longest/shortest with condition"

| Trigger | Example |
|---------|---------|
| Find **longest/shortest subarray** with condition | Longest Substring Without Repeating |
| **Fixed-size window** computation | Maximum Average Subarray |
| **At most K** distinct elements | Fruit Into Baskets |
| String **pattern matching** | Find All Anagrams, Permutation in String |

---

## Variants

### 1. Fixed Window
```java
// Compute over window of size k
int windowSum = 0;
for (int i = 0; i < k; i++) windowSum += arr[i];

for (int i = k; i < n; i++) {
    windowSum += arr[i] - arr[i - k]; // slide: add right, remove left
    result = Math.max(result, windowSum);
}
```

### 2. Dynamic Window (Expand + Shrink)
```java
int left = 0;
for (int right = 0; right < n; right++) {
    // Expand: add arr[right] to window
    
    while (windowIsInvalid) {
        // Shrink: remove arr[left] from window
        left++;
    }
    
    result = Math.max(result, right - left + 1);
}
```

### 3. Sliding Window + HashMap (Character Frequency)
```java
Map<Character, Integer> window = new HashMap<>();
int left = 0;
for (int right = 0; right < s.length(); right++) {
    window.merge(s.charAt(right), 1, Integer::sum);
    
    while (window.size() > k) {
        char c = s.charAt(left);
        window.merge(c, -1, Integer::sum);
        if (window.get(c) == 0) window.remove(c);
        left++;
    }
}
```

---

## Visual Walkthrough

### Longest Substring Without Repeating: `"abcabcbb"`
```
Step 1: [a] b c a b c b b     window="a"      len=1
Step 2: [a b] c a b c b b     window="ab"     len=2
Step 3: [a b c] a b c b b     window="abc"    len=3 ★
Step 4:  a [b c a] b c b b    window="bca"    len=3
         ↑ 'a' repeated → shrink left past first 'a'
Step 5:  a b [c a b] c b b    window="cab"    len=3
Step 6:  a b c [a b c] b b    window="abc"    len=3
Step 7:  a b c a [b c b] b    → 'b' repeats → shrink
Step 8:  a b c a b [c b] b    window="cb"     len=2

Answer: 3
```

---

## Time/Space Complexity

| Variant | Time | Space |
|---------|------|-------|
| Fixed window | O(n) | O(1) |
| Dynamic window | O(n) | O(k) for HashMap |
| With frequency counting | O(n) | O(charset) |

> Each element is added and removed from the window **at most once** → amortized O(n).

---

## Common Mistakes

1. **Forgetting to shrink the window** → Results in growing window that never contracts
2. **Off-by-one in window size** → `right - left + 1` for inclusive window
3. **Not cleaning up the HashMap** → Remove keys when count reaches 0

---

## Related Patterns

- [[04 - TwoPointers/Concept|Two Pointers]] — Sliding window is a two-pointer variant
- [[03 - FrequencyCounting/Concept|Frequency Counting]] — Often used inside the window
- [[02 - PrefixSum/Concept|Prefix Sum]] — Alternative for sum-based subarray problems

---

#sliding-window #dsa #concept
