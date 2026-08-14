# First Bad Version (LC 278)

**Difficulty**: Easy  
**Pattern**: Modified Binary Search  
**LeetCode**: https://leetcode.com/problems/first-bad-version/

## Problem Statement
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version.

**Example:**
```
Input: n = 5, bad = 4
Output: 4
```

## Approach: Lower Bound Binary Search

### Intuition
The versions are sorted: `[Good, Good, ..., Good, Bad, Bad, ... Bad]`.
We want to find the first `True` (Bad).
Standard Lower Bound pattern.
If `mid` is bad, it could be the first, or first is to left (`right = mid`).
If `mid` is good, first bad is to right (`left = mid + 1`).

### Java Code
```java
public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int left = 1, right = n;
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid)) {
                right = mid; // Possible answer, check left
            } else {
                left = mid + 1; // Must be after mid
            }
        }
        
        return left;
    }
}
```

### Complexity
- **Time**: O(log N)
- **Space**: O(1)

## Key Takeaways
- Classic "Find First True" binary search template
