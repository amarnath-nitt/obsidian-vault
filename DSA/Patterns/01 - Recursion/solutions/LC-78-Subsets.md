# Subsets (LC 78)

**Difficulty**: Medium  
**Pattern**: Recursion / Backtracking  
**LeetCode**: https://leetcode.com/problems/subsets/

## Problem Statement
Return all possible subsets of an array of unique integers.

## Intuition: The Power Set via "Include/Exclude"

### The Core Insight
For every element in nums, we have a binary choice:
- **Include it** in the current subset
- **Exclude it** from the current subset

Since each element → 2 choices, we get $2^n$ total subsets (the **power set**).

### Mathematical Perspective
For set {1, 2, 3}:
```
{} - exclude all
{1}, {2}, {3} - include exactly one
{1,2}, {1,3}, {2,3} - include exactly two
{1,2,3} - include all

Total: 2³ = 8 subsets
```

### The Recursion Tree: "Include/Exclude"

```
subsets([1,2,3]):
├─ Include 1:
│  └─ subsets([2,3]) with 1 prepended
│     ├─ Include 2:
│     │  └─ [[1,2], [1,2,3]]
│     └─ Exclude 2:
│        └─ [[1], [1,3]]
└─ Exclude 1:
   └─ subsets([2,3]) without 1
      ├─ Include 2:
      │  └─ [[2], [2,3]]
      └─ Exclude 2:
         └─ [[]]
```

### Why Backtracking?
We want ALL subsets, not just one optimal subset. Backtracking allows us to:
- Build one subset (e.g., [1,2])
- Unchoose the last element (remove 2 from path)
- Try a different path (exclude 2 instead)
- Collect results from all paths

### Comparison: Include/Exclude vs Bitmask
- **Backtracking (include/exclude)**: Natural recursion, easier to understand, builds path incrementally
- **Bitmask**: Compact iterative approach, treats each subset as a binary number
  - Example: Subset `010` (binary) = include element at index 1 only

Both are valid; backtracking is more intuitive for interviews.

## Recursive Idea
At each index, choose whether to include the current number. A cleaner version adds the current path first, then extends it.

## Java Code
```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, 0, new ArrayList<>(), result);
        return result;
    }

	private void backtrack(int[] nums, int index, List<Integer> current, List<List<Integer>> result) {
		if (index == nums.length) {  
		    result.add(new ArrayList<>(current));  
		    return;  
		}  
		current.add(nums[index]);  
		backtrack(nums, index + 1, current, result);  
		current.remove(current.size() - 1);  
		backtrack(nums, index + 1, current, result);
    }
}
```

## Alternative Optimal Solution: Bitmask Enumeration
Each bit in `mask` decides whether to include one number. This is a compact iterative way to generate the power set.

```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        int totalMasks = 1 << nums.length;

        for (int mask = 0; mask < totalMasks; mask++) {
            List<Integer> subset = new ArrayList<>();
            for (int i = 0; i < nums.length; i++) {
                if ((mask & (1 << i)) != 0) {
                    subset.add(nums[i]);
                }
            }
            result.add(subset);
        }

        return result;
    }
}
```

### Alternative Complexity
- **Time**: O(n * 2^n)
- **Space**: O(n) excluding output

## Complexity
- **Time**: O(n * 2^n)
- **Space**: O(n) excluding output

## Key Takeaways
- Subsets generate `2^n` answers.
- `start` prevents reusing earlier elements.
