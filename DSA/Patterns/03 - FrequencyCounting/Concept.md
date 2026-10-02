# Frequency Counting — Concept

## What Is It?

Frequency Counting uses a HashMap or array to count the occurrences of elements, enabling efficient lookups, duplicate detection, and frequency-based decisions in **O(n)** time.

---

## When to Use

> **Trigger keywords:** "count", "frequency", "duplicate", "anagram", "most common", "majority", "unique"

| Trigger | Example |
|---------|---------|
| Check for **duplicates** | Contains Duplicate |
| Compare **character frequencies** | Valid Anagram, Ransom Note |
| Find the **most/least frequent** | Top K Frequent Elements |
| Group elements by **some key** | Group Anagrams |

---

## Variants

### 1. HashMap (General)
```java
Map<Integer, Integer> freq = new HashMap<>();
for (int num : nums) {
    freq.put(num, freq.getOrDefault(num, 0) + 1);
}
```

### 2. Fixed Array (for chars 'a'-'z')
```java
int[] freq = new int[26];
for (char c : s.toCharArray()) {
    freq[c - 'a']++;
}
```

### 3. Counter Comparison (Two Strings)
```java
int[] count = new int[26];
for (int i = 0; i < s.length(); i++) {
    count[s.charAt(i) - 'a']++;
    count[t.charAt(i) - 'a']--;
}
// All zeros → anagram
```

### 4. Boyer-Moore Voting (Majority Element)
```java
int candidate = 0, count = 0;
for (int num : nums) {
    if (count == 0) candidate = num;
    count += (num == candidate) ? 1 : -1;
}
```

---

## Visual Walkthrough

```
Input: "anagram" vs "nagaram"

Count array after processing "anagram":
  a: +3, n: +1, g: +1, r: +1, m: +1

After subtracting "nagaram":
  a: 3-3=0, n: 1-1=0, g: 1-1=0, r: 1-1=0, m: 1-1=0

All zeros → Valid anagram ✓
```

---

## Time/Space Complexity

| Approach | Time | Space |
|----------|------|-------|
| HashMap counting | O(n) | O(k) where k = unique elements |
| Array counting | O(n) | O(1) for fixed charset |
| Boyer-Moore | O(n) | O(1) |

---

## Common Mistakes

1. **Using `freq.get(key)` without null check** — Always use `getOrDefault(key, 0)`
2. **Forgetting to handle different string lengths** — Check `s.length() != t.length()` early for anagram problems
3. **Not considering case sensitivity** — Clarify if 'A' and 'a' are the same

---

## Related Patterns

- [[06 - SlidingWindow/Concept|Sliding Window]] — Often uses frequency maps to track window contents
- [[02 - PrefixSum/Concept|Prefix Sum]] — Combined with frequency for subarray sum problems
- [[15 - TopKElements/Concept|Top K Elements]] — Uses frequency counting + heap

---

#frequency-counting #dsa #concept
