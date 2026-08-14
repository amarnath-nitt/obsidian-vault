# Day 11 — Binary Search

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** Binary Search — on arrays & on answers
**Difficulty Mix:** Medium / Hard

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Binary Search]] | 704 | Easy | ⬜ |
| 2 | [[#Search in Rotated Sorted Array]] | 33 | Medium | ⬜ |
| 3 | [[#Find Minimum in Rotated Sorted Array]] | 153 | Medium | ⬜ |
| 4 | [[#Kth Missing Positive Number]] | 1539 | Easy | ⬜ |
| 5 | [[#Aggressive Cows]] | — | Medium | ⬜ |
| 6 | [[#Allocate Minimum Pages]] | — | Medium | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Binary Search | Linear scan. O(n). | Recursive binary search. O(log n) time, O(log n) stack. | Iterative binary search. O(log n), O(1). |
| Search in Rotated Sorted Array | Linear scan. O(n). | Find pivot, then binary search the correct half. O(log n). | One-pass modified binary search by identifying sorted half. O(log n). |
| Find Minimum in Rotated Sorted Array | Scan all elements. O(n). | Find pivot with binary search. O(log n). | Binary search by comparing mid with right boundary. O(log n). |
| Kth Missing Positive Number | Simulate positive integers until kth missing. O(n+k). | Walk array and count gaps. O(n). | Binary search on missing count before index. O(log n). |
| Aggressive Cows | Try all cow placements. Exponential. | Binary search distance and greedily check feasibility. O(n log range). | Same after sorting stalls; this is the standard optimal pattern. |
| Allocate Minimum Pages | Try every partition among students. Exponential. | DP over books/students. O(n^2*k). | Binary search max pages with greedy feasibility. O(n log sum). |

---

## Binary Search Templates

```java
// Standard - find exact target
int lo = 0, hi = n - 1;
while (lo <= hi) {
    int mid = lo + (hi - lo) / 2;
    if (arr[mid] == target) return mid;
    else if (arr[mid] < target) lo = mid + 1;
    else hi = mid - 1;
}

// Find first true in monotonic predicate
int lo = 0, hi = n;
while (lo < hi) {
    int mid = lo + (hi - lo) / 2;
    if (predicate(mid)) hi = mid;  // could be answer
    else lo = mid + 1;
}
// answer is lo

// Binary search on answer (feasibility)
int lo = minPossible, hi = maxPossible;
while (lo < hi) {
    int mid = lo + (hi - lo) / 2;
    if (canAchieve(mid)) hi = mid;
    else lo = mid + 1;
}
```

---

## Binary Search

**LeetCode 704** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/binary-search/)

### Java Solution

```java
class Solution {
    public int search(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == target) return mid;
            else if (nums[mid] < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return -1;
    }
}
```

---

## Search in Rotated Sorted Array

**LeetCode 33** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/search-in-rotated-sorted-array/)

### Problem
Array was sorted, then rotated at an unknown pivot. Find target.

### Approach

- One half is always **sorted**
- Determine which half is sorted, check if target lies in it
- Eliminate the other half

### Java Solution

```java
class Solution {
    public int search(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == target) return mid;

            // Left half is sorted
            if (nums[lo] <= nums[mid]) {
                if (target >= nums[lo] && target < nums[mid]) hi = mid - 1;
                else lo = mid + 1;
            }
            // Right half is sorted
            else {
                if (target > nums[mid] && target <= nums[hi]) lo = mid + 1;
                else hi = mid - 1;
            }
        }
        return -1;
    }
}
```

**Complexity:** Time O(log n) · Space O(1)

---

## Find Minimum in Rotated Sorted Array

**LeetCode 153** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

### Problem
Find the minimum in a rotated sorted array.

### Approach

- The minimum is at the **pivot point** (where the rotation is)
- If left half is not sorted → minimum is in left half
- Otherwise → minimum is in right half (or mid)

### Java Solution

```java
class Solution {
    public int findMin(int[] nums) {
        int lo = 0, hi = nums.length - 1;

        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] > nums[hi]) lo = mid + 1; // min is in right half
            else hi = mid;                           // min is in left half (including mid)
        }
        return nums[lo];
    }
}
```

**Complexity:** Time O(log n) · Space O(1)

---

## Kth Missing Positive Number

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

## Aggressive Cows

**Problem:** Place C cows in N stalls (at positions). Maximize the minimum distance between any two cows.

### Approach (Binary Search on Answer)

- Binary search on the **minimum distance** (answer space: 1 to max_pos)
- For a given distance `d`, check if C cows can be placed with at least `d` apart
- Maximize valid `d`

### Java Solution

```java
public int aggressiveCows(int[] stalls, int c) {
    Arrays.sort(stalls);
    int lo = 1, hi = stalls[stalls.length-1] - stalls[0];

    while (lo < hi) {
        int mid = lo + (hi - lo + 1) / 2; // upper mid (maximize)
        if (canPlace(stalls, c, mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}

boolean canPlace(int[] stalls, int c, int minDist) {
    int count = 1, last = stalls[0];
    for (int i = 1; i < stalls.length; i++) {
        if (stalls[i] - last >= minDist) {
            count++;
            last = stalls[i];
            if (count == c) return true;
        }
    }
    return count >= c;
}
```

**Complexity:** Time O(n log(max_distance)) · Space O(1)

---

## Allocate Minimum Pages

**Problem:** N books, M students. Allocate books to minimize the maximum pages a student reads. Each student gets contiguous books.

### Approach (Binary Search on Answer)

- Binary search on max pages (answer space: max_single_book to sum_all_books)
- For a given max `mid`, check if M students can read all books
- Minimize valid `mid`

### Java Solution

```java
public int allocatePages(int[] books, int m) {
    if (m > books.length) return -1;
    int lo = Arrays.stream(books).max().getAsInt();
    int hi = Arrays.stream(books).sum();

    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (canAllocate(books, m, mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}

boolean canAllocate(int[] books, int m, int maxPages) {
    int students = 1, pagesRead = 0;
    for (int pages : books) {
        if (pages > maxPages) return false;
        if (pagesRead + pages > maxPages) {
            students++;
            pagesRead = 0;
        }
        pagesRead += pages;
    }
    return students <= m;
}
```

**Complexity:** Time O(n log(sum)) · Space O(1)

---

## Binary Search on Answer — Identify the Pattern

```
Key signals:
✅ "Minimize the maximum" → BS on answer, check feasibility
✅ "Maximize the minimum" → BS on answer, check feasibility
✅ "Can you achieve X with constraint Y?" → feasibility check function

Template:
  lo = minimum possible answer
  hi = maximum possible answer
  Binary search → find the boundary
```

#sde-sheet #binary-search #day11
