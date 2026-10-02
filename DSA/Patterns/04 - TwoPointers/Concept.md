# Two Pointers — Concept

## What Is It?

Two Pointers uses two index variables to traverse a data structure (typically a sorted array or linked list), converging or diverging based on conditions. It reduces brute-force O(n²) solutions to O(n).

---

## When to Use

> **Trigger keywords:** "sorted array", "pair with sum", "remove duplicates", "palindrome", "converge from ends", "in-place"

| Trigger | Example |
|---------|---------|
| Array is **sorted** and you need pairs | Two Sum II, 3Sum |
| Check something from **both ends** | Valid Palindrome, Container With Most Water |
| **Remove duplicates in-place** | Remove Duplicates from Sorted Array |
| **Partitioning** elements | Sort Colors (Dutch National Flag) |

---

## Variants

### 1. Opposite Direction (Converging)
Start from both ends, move inward.
```java
int left = 0, right = arr.length - 1;
while (left < right) {
    if (arr[left] + arr[right] == target) { /* found */ }
    else if (arr[left] + arr[right] < target) left++;
    else right--;
}
```

### 2. Same Direction (Fast & Slow)
Both start from beginning, move at different rates.
```java
int slow = 0;
for (int fast = 0; fast < arr.length; fast++) {
    if (condition) {
        arr[slow] = arr[fast];
        slow++;
    }
}
```

### 3. Three Pointers (Dutch National Flag)
Partition into three groups.
```java
int low = 0, mid = 0, high = arr.length - 1;
while (mid <= high) {
    if (arr[mid] == 0) swap(arr, low++, mid++);
    else if (arr[mid] == 1) mid++;
    else swap(arr, mid, high--);
}
```

---

## Visual Walkthrough

### Container With Most Water
```
Height: [1, 8, 6, 2, 5, 4, 8, 3, 7]

Step 1: left=0(h=1), right=8(h=7)
        Area = min(1,7) × 8 = 8
        Move left (shorter side)
        
     8           8
     |     6     |     7
     |  |  |     |  |  |
     |  |  |  5  |  |  |
     |  |  |  |  4  |  |
     |  |  |  |  |  |  3
     |  |  |  |  |  |  |  |
  1  |  |  2  |  |  |  |  |
  L-→                    ←-R

Step 2: left=1(h=8), right=8(h=7)
        Area = min(8,7) × 7 = 49 ← MAX
        Move right (shorter side)
```

---

## Time/Space Complexity

| Variant | Time | Space |
|---------|------|-------|
| Opposite direction | O(n) | O(1) |
| Same direction | O(n) | O(1) |
| With sorting first | O(n log n) | O(1) |

---

## Common Mistakes

1. **Using Two Pointers on unsorted array** — Sort first, or verify the problem doesn't need sorting
2. **Infinite loop from not moving pointers** — Ensure at least one pointer moves in every iteration
3. **Skipping duplicates incorrectly in 3Sum** — Must skip after finding a valid triplet, not before

---

## Related Patterns

- [[06 - SlidingWindow/Concept|Sliding Window]] — Same-direction two pointers with a window
- [[07 - FastSlowPointers/Concept|Fast & Slow Pointers]] — Variant for linked lists and cycle detection
- [[14 - OverlappingIntervals/Concept|Overlapping Intervals]] — Two pointers after sorting by start time

---

#two-pointers #dsa #concept
