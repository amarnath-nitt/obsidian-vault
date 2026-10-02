---
solved: true
difficulty: Easy
pattern: Frequency Counting
lc_number: 169
date_solved: 
tags:
  - dsa
  - frequency-counting
  - easy
---
# Majority Element (LC 169)

**Difficulty**: Easy  
**Pattern**: Frequency Counting / Boyer-Moore  
**LeetCode**: https://leetcode.com/problems/majority-element/

## Problem Statement
Given an array `nums` of size `n`, return the majority element.
The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**Example:**
```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

## Approach 1: Frequency Map

### Intuition
Count occurrences. Return if count > n/2.

### Java Code
```java
class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<>();
        int n = nums.length;
        for (int num : nums) {
            int count = counts.getOrDefault(num, 0) + 1;
            if (count > n / 2) return num;
            counts.put(num, count);
        }
        return -1;
    }
}
```

## Approach 2: Boyer-Moore Voting Algorithm

### Intuition
Maintain a `candidate` and a `count`.
If `count == 0`, new candidate.
If `num == candidate`, `count++`.
Else `count--`.
The logic is that the majority element will eventually cancel out all other non-majority elements and stay positive because it is > 50%.

### Java Code
```java
class Solution {
    public int majorityElement(int[] nums) {
        int count = 0;
        Integer candidate = null;

        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            count += (num == candidate) ? 1 : -1;
        }

        return candidate;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(1)

## Key Takeaways
- O(N) time and O(1) space optimal solution exists (Boyer-Moore)
- > n/2 guarantee simplifies things
