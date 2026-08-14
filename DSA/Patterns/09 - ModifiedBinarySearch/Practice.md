# Modified Binary Search - Practice Notes

## Pattern Overview
Adapting binary search algorithm to solve problems beyond simple searching in sorted arrays.

## Key Concepts
- **Sorted property**: Need some ordering or monotonic property
- **Search space**: Can be values, indices, or answer range
- **Time Complexity**: O(log n)

## Template Code

### Classic Binary Search
```java
public int binarySearch(int[] arr, int target) {
    int left = 0, right = arr.length - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}
```

### Find First/Last Position
```java
// Find first position
int left = 0, right = arr.length - 1;
while (left < right) {
    int mid = left + (right - left) / 2;
    if (arr[mid] < target) {
        left = mid + 1;
    } else {
        right = mid;
    }
}
```

### Binary Search on Answer
```java
// Finding minimum value that satisfies condition
int left = minPossible, right = maxPossible;
while (left < right) {
    int mid = left + (right - left) / 2;
    if (isValid(mid)) {
        right = mid;
    } else {
        left = mid + 1;
    }
}
return left;
```

## Practice Problems

### Easy
- [ ] [Binary Search](https://leetcode.com/problems/binary-search/) (LC 704) → [Solution](solutions/LC-704-Binary-Search.md)
- [ ] [First Bad Version](https://leetcode.com/problems/first-bad-version/) (LC 278) → [Solution](solutions/LC-278-First-Bad-Version.md)
- [ ] [Search Insert Position](https://leetcode.com/problems/search-insert-position/) (LC 35) → [Solution](solutions/LC-35-Search-Insert-Position.md)
- [ ] [Sqrt(x)](https://leetcode.com/problems/sqrtx/) (LC 69) → [Solution](solutions/LC-69-Sqrt-x.md)

### Medium
- [ ] [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) (LC 33) → [Solution](solutions/LC-33-Search-in-Rotated-Sorted-Array.md)
- [ ] [Find Peak Element](https://leetcode.com/problems/find-peak-element/) (LC 162) → [Solution](solutions/LC-162-Find-Peak-Element.md)
- [ ] [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) (LC 153) → [Solution](solutions/LC-153-Find-Minimum-in-Rotated-Sorted-Array.md)
- [ ] [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) (LC 34) → [Solution](solutions/LC-34-Find-First-and-Last-Position.md)
- [ ] [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) (LC 875) → [Solution](solutions/LC-875-Koko-Eating-Bananas.md)
- [ ] [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) (LC 1011) → [Solution](solutions/LC-1011-Capacity-Ship-Packages.md)

### Hard
- [ ] [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) (LC 4) → [Solution](solutions/LC-4-Median-Two-Sorted-Arrays.md)
- [ ] [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) (LC 410) → [Solution](solutions/LC-410-Split-Array-Largest-Sum.md)

## Reference
[LeetCode Pattern Guide](https://lnkd.in/gc3HzSgh)
