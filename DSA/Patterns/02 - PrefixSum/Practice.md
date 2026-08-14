# Prefix Sum Pattern - Practice Notes

## Pattern Overview
Prefix Sum is a technique used to efficiently answer range sum queries by preprocessing the array to store cumulative sums.

## Key Concepts
- **Prefix Array**: `prefix[i]` = sum of elements from index 0 to i
- **Range Sum Formula**: `sum(i, j)` = `prefix[j]` - `prefix[i-1]`
- **Time Complexity**: O(n) preprocessing, O(1) query

## Template Code

```java
// Building prefix sum array
int[] prefixSum = new int[n+1];
prefixSum[0] = 0;
for (int i = 1; i <= n; i++) {
    prefixSum[i] = prefixSum[i-1] + arr[i-1];
}

// Range sum query [l, r]
int rangeSum = prefixSum[r+1] - prefixSum[l];
```

## Practice Problems

### Easy
- [x] [Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) (LC 1480) → [Solution](solutions/LC-1480-Running-Sum.md)
- [x] [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) (LC 724) → [Solution](solutions/LC-724-Find-Pivot-Index.md)
- [x] [Find the Middle Index in Array](https://leetcode.com/problems/find-the-middle-index-in-array/) (LC 1991) → [Solution](solutions/LC-1991-Find-Middle-Index.md)

### Medium
- [x] [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) (LC 560) → [Solution](solutions/LC-560-Subarray-Sum-Equals-K.md)
- [x] [Contiguous Array](https://leetcode.com/problems/contiguous-array/) (LC 525) → [Solution](solutions/LC-525-Contiguous-Array.md)
- [x] [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) (LC 238) → [Solution](solutions/LC-238-Product-Except-Self.md)
- [x] [Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) (LC 974) → [Solution](solutions/LC-974-Subarray-Sums-Divisible-by-K.md)
- [x] [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) (LC 303) → [Solution](solutions/LC-303-Range-Sum-Query-Immutable.md)
- [x] [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) (LC 304) → [Solution](solutions/LC-304-Range-Sum-Query-2D.md)

### Hard
- [ ] [Maximum Sum of 3 Non-Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/) (LC 689) → [Solution](solutions/LC-689-Max-Sum-3-Subarrays.md)

## Reference
[LeetCode Pattern Guide](https://lnkd.in/g2EXKs32)
