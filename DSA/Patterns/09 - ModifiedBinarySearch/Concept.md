# Modified Binary Search — Concept

## What Is It?

Modified Binary Search adapts the classic binary search algorithm to work on rotated arrays, find boundaries, search on answer spaces, or find elements in non-standard sorted structures. The key insight: if you can define a **monotonic condition**, you can binary search on it.

---

## When to Use

> **Trigger keywords:** "sorted", "rotated sorted", "find minimum", "search in rotated", "find peak", "minimize maximum", "capacity to ship"

| Trigger | Example |
|---------|---------|
| **Rotated sorted array** | Search in Rotated Sorted Array |
| **Find boundary** (first/last occurrence) | First Bad Version |
| **Search on answer** (minimize/maximize) | Koko Eating Bananas, Ship Packages |
| **Find peak/valley** | Find Peak Element |

---

## Variants

### 1. Standard Binary Search
```java
int lo = 0, hi = n - 1;
while (lo <= hi) {
    int mid = lo + (hi - lo) / 2;
    if (arr[mid] == target) return mid;
    else if (arr[mid] < target) lo = mid + 1;
    else hi = mid - 1;
}
```

### 2. Rotated Array Search
```java
while (lo <= hi) {
    int mid = lo + (hi - lo) / 2;
    if (nums[mid] == target) return mid;
    
    if (nums[lo] <= nums[mid]) { // left half sorted
        if (target >= nums[lo] && target < nums[mid]) hi = mid - 1;
        else lo = mid + 1;
    } else { // right half sorted
        if (target > nums[mid] && target <= nums[hi]) lo = mid + 1;
        else hi = mid - 1;
    }
}
```

### 3. Binary Search on Answer
```java
// Find minimum capacity to ship packages in D days
int lo = maxWeight, hi = totalWeight;
while (lo < hi) {
    int mid = lo + (hi - lo) / 2;
    if (canShip(mid, D)) hi = mid;
    else lo = mid + 1;
}
return lo;
```

---

## Visual Walkthrough

### Binary Search on Rotated Array `[4,5,6,7,0,1,2]`, target=0
```
Step 1: lo=0, hi=6, mid=3 → nums[3]=7
        [4,5,6,7,0,1,2]
         L     M     H
        Left half [4,5,6,7] is sorted, target 0 not in [4,7] → go right

Step 2: lo=4, hi=6, mid=5 → nums[5]=1
        [4,5,6,7,0,1,2]
                 L M H
        Left half [0,1] is sorted, target 0 in [0,1] → go left

Step 3: lo=4, hi=4, mid=4 → nums[4]=0 ✓ Found!
```

---

## Time/Space Complexity

| Variant | Time | Space |
|---------|------|-------|
| Standard | O(log n) | O(1) |
| Rotated array | O(log n) | O(1) |
| Binary search on answer | O(n × log(range)) | O(1) |

---

## Common Mistakes

1. **Integer overflow** → Use `lo + (hi - lo) / 2` not `(lo + hi) / 2`
2. **Infinite loop** → Ensure `lo < hi` vs `lo <= hi` is correct for your variant
3. **Wrong half selection** → In rotated arrays, always check which half is sorted first

---

## Related Patterns

- [[04 - TwoPointers/Concept|Two Pointers]] — Binary search is a specialized two-pointer technique
- [[16 - Greedy/Concept|Greedy]] — Binary search on answer often validates with greedy

---

#binary-search #dsa #concept
