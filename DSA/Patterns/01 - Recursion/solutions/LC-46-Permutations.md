---
solved: true
difficulty: Medium
pattern: Recursion
lc_number: 46
date_solved: 
tags:
  - dsa
  - recursion
  - medium
---
# Permutations (LC 46)

**Difficulty**: Medium  
**Pattern**: Recursion / Backtracking  
**LeetCode**: https://leetcode.com/problems/permutations/

## Problem Statement
Return all possible permutations of an array of distinct integers.

## Recursive Idea
Build the permutation one position at a time. At each position, try every unused number.

## Interview Intuition: Backtracking Pattern

### The Key Insight
A permutation is an arrangement using each element exactly once.

**The strategy**: **Build position by position**
- Position 1: pick any of n elements
- Position 2: pick any of remaining n-1 elements
- ...
- Position n: pick the last remaining element

This generates n! total permutations.

### The "Choose, Explore, Unchoose" Pattern
This is **THE fundamental backtracking pattern**:

```
for each candidate:
    1. CHOOSE: add candidate to current solution
    2. EXPLORE: recursively solve the rest
    3. UNCHOOSE: remove candidate (backtrack)
       ↓ This step allows exploring other candidates
```

**Why unchoose?** Because we need to explore ALL possible permutations, not just find one.

### Visual Example: nums=[1,2,3]

```
Start: []
├─ Choose 1: [1]
│  ├─ Choose 2: [1,2]
│  │  └─ Choose 3: [1,2,3] ✓ SAVE
│  └─ Choose 3: [1,3]
│     └─ Choose 2: [1,3,2] ✓ SAVE
├─ Choose 2: [2]
│  ├─ Choose 1: [2,1]
│  │  └─ Choose 3: [2,1,3] ✓ SAVE
│  └─ Choose 3: [2,3]
│     └─ Choose 1: [2,3,1] ✓ SAVE
└─ Choose 3: [3]
   ├─ Choose 1: [3,1]
   │  └─ Choose 2: [3,1,2] ✓ SAVE
   └─ Choose 2: [3,2]
      └─ Choose 1: [3,2,1] ✓ SAVE

Total: 3! = 6 permutations
```

### Two Implementation Approaches

1. **HashSet Tracking**: Track which elements are used (clear intent)
   - Pro: Easy to understand which elements are available
   - Con: O(n) lookup on each check

2. **In-Place Swapping**: Swap to mark as used, swap back to unmark (more efficient)
   - Pro: O(1) access, fewer memory allocations
   - Con: Modifies input array (but works in this problem)

Both achieve the same result; choose based on clarity vs efficiency.

## Java Code
```java
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int[] nums, List<Integer> path, List<List<Integer>> result) {
        if (path.size() == nums.length) {
            result.add(new ArrayList<>(path));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if(!path.contains(nums[i])) {
	            path.add(nums[i]);
	            backtrack(nums, used, path, result);
	            path.remove(path.size() - 1);
            }
        }
    }
}
```

## Alternative Optimal Solution: In-Place Swapping
Instead of a `used` array, place one value at the current index by swapping. Swap back after the recursive call.

```java
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(0, nums, result);
        return result;
    }

    private void backtrack(int start, int[] nums, List<List<Integer>> result) {
        if (start == nums.length) {
            List<Integer> permutation = new ArrayList<>();
            for (int num : nums) {
                permutation.add(num);
            }
            result.add(permutation);
            return;
        }

        for (int i = start; i < nums.length; i++) {
            swap(nums, start, i);
            backtrack(start + 1, nums, result);
            swap(nums, start, i);
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
```

### Alternative Complexity
- **Time**: O(n * n!)
- **Space**: O(n) recursion stack, excluding output

## Complexity
- **Time**: O(n * n!)
- **Space**: O(n) excluding output

## Key Takeaways
- Use a `used` array when each element can appear once.
- Copy `path` only when a complete answer is found.
