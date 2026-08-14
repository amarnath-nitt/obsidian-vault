# Longest Consecutive Sequence

**Difficulty:** Medium  
**Category:** Arrays & Hashing  
**LeetCode Link:** [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

---

## Problem Statement

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in **O(n)** time.

**Example 1:**
```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4]. Length is 4.
```

**Example 2:**
```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

**Constraints:**
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Intuition

We need to find the longest sequence of consecutive integers. The challenge is doing this in O(n) time without sorting.

---

## Approach 1: Sorting (Naive Solution)

### Algorithm
1. Sort the array
2. Iterate through and count consecutive sequences
3. Track the maximum length found

### Java Code
```java
class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;
        
        Arrays.sort(nums);
        
        int maxLength = 1;
        int currentLength = 1;
        
        for (int i = 1; i < nums.length; i++) {
            // Skip duplicates
            if (nums[i] == nums[i - 1]) {
                continue;
            }
            // Check if consecutive
            else if (nums[i] == nums[i - 1] + 1) {
                currentLength++;
                maxLength = Math.max(maxLength, currentLength);
            }
            // Reset sequence
            else {
                currentLength = 1;
            }
        }
        
        return maxLength;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n log n) - Dominated by sorting
- **Space Complexity:** O(1) or O(n) - Depends on sorting algorithm

### Drawbacks
- Doesn't meet O(n) requirement
- Sorting is unnecessary overhead

---

## Approach 2: HashSet (Optimized Solution)

### Algorithm
1. Add all numbers to a HashSet for O(1) lookup
2. For each number, check if it's the start of a sequence (num-1 not in set)
3. If it's a start, count how long the sequence goes
4. Track the maximum length

### Java Code
```java
class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;
        
        // Add all numbers to set
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }
        
        int maxLength = 0;
        
        // Check each number
        for (int num : numSet) {
            // Only start counting if this is the beginning of a sequence
            if (!numSet.contains(num - 1)) {
                int currentNum = num;
                int currentLength = 1;
                
                // Count consecutive numbers
                while (numSet.contains(currentNum + 1)) {
                    currentNum++;
                    currentLength++;
                }
                
                maxLength = Math.max(maxLength, currentLength);
            }
        }
        
        return maxLength;
    }
}
```

### Step-by-Step Example
For `nums = [100, 4, 200, 1, 3, 2]`:

```
Set: {100, 4, 200, 1, 3, 2}

num = 100: 99 not in set → start of sequence
  Check: 101 not in set → length = 1

num = 4: 3 in set → skip (not start)

num = 200: 199 not in set → start of sequence
  Check: 201 not in set → length = 1

num = 1: 0 not in set → start of sequence
  Check: 2 in set → currentNum = 2, length = 2
  Check: 3 in set → currentNum = 3, length = 3
  Check: 4 in set → currentNum = 4, length = 4
  Check: 5 not in set → stop, length = 4

num = 3: 2 in set → skip (not start)

num = 2: 1 in set → skip (not start)

Max length = 4
```

### Complexity Analysis
- **Time Complexity:** O(n) - Each number visited at most twice
- **Space Complexity:** O(n) - HashSet storage

### Why This is Better
- ✅ O(n) time complexity - meets requirement
- ✅ Smart optimization: only count from sequence starts
- ✅ Each number processed at most twice (once in outer loop, once in while loop)
- ✅ No sorting needed

---

## Key Insight

The crucial optimization is: **only start counting from the beginning of a sequence**.

- If `num - 1` exists, then `num` is NOT the start of a sequence
- We'll count this number when we process the actual start
- This prevents redundant counting and ensures O(n) time

---

## Key Takeaways

1. **Pattern:** HashSet for O(1) membership testing
2. **Optimization:** Only process sequence starts to avoid redundancy
3. **Time complexity:** Even with nested loop, each element visited at most twice
4. **Trade-off:** O(n) space for O(n) time vs O(1) space for O(n log n) time

---

## Edge Cases

- Empty array: `[]` → `0`
- Single element: `[1]` → `1`
- All consecutive: `[1,2,3,4,5]` → `5`
- No consecutive: `[1,3,5,7]` → `1`
- Duplicates: `[1,2,2,3]` → `3`
- Negative numbers: `[-1,0,1]` → `3`

---

## Related Problems
- [[Longest-Increasing-Subsequence]] - Similar sequence problem
- [[Number-of-Islands]] - Similar connected component concept
- [[Longest-Substring-Without-Repeating-Characters]] - Similar optimization pattern

---

## Tags
#arrays #hashing #union-find #medium #blind75
