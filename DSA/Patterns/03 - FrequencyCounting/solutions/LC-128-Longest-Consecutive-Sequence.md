# Longest Consecutive Sequence (LC 128)

**Difficulty**: Medium  
**Pattern**: Frequency Counting / HashSet  
**LeetCode**: https://leetcode.com/problems/longest-consecutive-sequence/

## Problem Statement
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in `O(n)` time.

**Example:**
```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

## Approach: HashSet

### Intuition
Put all numbers in a HashSet for O(1) loopkup.
For each number `x`, if `x-1` does NOT exist in set, then `x` is the start of a sequence.
If `x` is a start, count how many consecutive numbers `x+1, x+2...` exist in set.
This ensures each number is part of a sequence build process exactly once.

### Java Code
```java
class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }
        
        int longestStreak = 0;
        
        for (int num : numSet) {
            // Only search forward if this number is the start of a sequence
            if (!numSet.contains(num - 1)) {
                int currentNum = num;
                int currentStreak = 1;
                
                while (numSet.contains(currentNum + 1)) {
                    currentNum += 1;
                    currentStreak += 1;
                }
                
                longestStreak = Math.max(longestStreak, currentStreak);
            }
        }
        
        return longestStreak;
    }
}
```

### Complexity
- **Time**: O(n). Although nested loop, the `while` loop runs only for sequence starts, and total iterations across all execution is roughly N.
- **Space**: O(n) for set.

## Key Takeaways
- O(N) constraint forces Hash Set/Map
- Idea of "Start of sequence" prevents O(N^2) work
- Sorting would be O(N log N)
