# Day 7 — Two Pointers & Sliding Window

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** Two Pointers · Sliding Window
**Difficulty Mix:** Easy / Medium / Hard

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [3-Sum](3-Sum.md) | LeetCode 15 | Medium | [LeetCode](https://leetcode.com/problems/3sum/)
- [ ] [Trapping Rain Water](Trapping-Rain-Water.md) | LeetCode 42 | Hard | [LeetCode](https://leetcode.com/problems/trapping-rain-water/)
- [ ] [Remove Duplicates from Sorted Array](Remove-Duplicates-from-Sorted-Array.md) | LeetCode 26 | Easy | [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- [ ] [Max Consecutive Ones III](Max-Consecutive-Ones-III.md) | LeetCode 1004 | Medium | [LeetCode](https://leetcode.com/problems/max-consecutive-ones-iii/)
- [ ] [Minimum Window Substring](Minimum-Window-Substring.md) | LeetCode 76 | Hard | [LeetCode](https://leetcode.com/problems/minimum-window-substring/)
- [ ] [Longest Substring Without Repeating Characters](Longest-Substring-Without-Repeating-Characters.md) | LeetCode 3 | Medium | [LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| 3-Sum | Check every triplet. O(n^3). | Fix one number and use a HashSet for two-sum. O(n^2) space/time. | Sort, fix one number, two pointers, skip duplicates. O(n^2). |
| Trapping Rain Water | For each index, scan left and right max. O(n^2). | Prefix max and suffix max arrays. O(n) space. | Two pointers tracking leftMax/rightMax. O(n), O(1). |
| Remove Duplicates from Sorted Array | Use a set/new array. O(n) space. | Shift elements left after duplicates. O(n^2). | Slow/fast overwrite unique values. O(n), O(1). |
| Max Consecutive Ones III | Check every window and count zeros. O(n^2). | Prefix zero counts with binary search. O(n log n). | Sliding window with at most k zeros. O(n). |
| Minimum Window Substring | Test every substring against target counts. O(n^3). | Use frequency counts to validate faster. O(n^2). | Sliding window with need/have counts. O(n). |
| Longest Substring Without Repeating Characters | Check every substring for uniqueness. O(n^3). | Sliding window with a HashSet. O(n). | Last-seen index map to jump left pointer. O(n). |

---

## Sliding Window Template

```java
// Fixed size window of size k
int sum = 0;
for (int i = 0; i < k; i++) sum += arr[i];
int maxSum = sum;
for (int i = k; i < arr.length; i++) {
    sum += arr[i] - arr[i - k];
    maxSum = Math.max(maxSum, sum);
}

// Variable size window (expand right, shrink left when invalid)
int left = 0;
for (int right = 0; right < arr.length; right++) {
    // add arr[right] to window state
    while (/* window is invalid */) {
        // remove arr[left] from window state
        left++;
    }
    // update answer with window [left, right]
}
```

#sde-sheet #two-pointers #sliding-window #day7
