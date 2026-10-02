# Kth Missing Positive Number

**LeetCode 1539** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/kth-missing-positive-number/)

### Problem
Find the kth missing positive integer.

### Approach (Binary Search on the array)

- At index `i`, the number of missing positives before `arr[i]` = `arr[i] - (i+1)`
- Binary search for the first index where `arr[mid] - (mid+1) >= k`
- Answer = `lo + k`

### Java Solution

```java
class Solution {
    public int findKthPositive(int[] arr, int k) {
        int lo = 0, hi = arr.length;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] - (mid + 1) >= k) hi = mid;
            else lo = mid + 1;
        }
        return lo + k;
    }
}
```

**Complexity:** Time O(log n) · Space O(1)

---
