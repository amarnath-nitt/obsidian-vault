# Contains Duplicate

**Difficulty:** Easy  
**Category:** Arrays & Hashing  
**LeetCode Link:** [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

---

## Problem Statement

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

**Example 1:**
```
Input: nums = [1,2,3,1]
Output: true
```

**Example 2:**
```
Input: nums = [1,2,3,4]
Output: false
```

**Example 3:**
```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

**Constraints:**
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Intuition

We need to detect if any number appears more than once. The challenge is doing this efficiently without comparing every element to every other element.

---

## Approach 1: Brute Force (Naive Solution)

### Algorithm
1. For each element, compare it with all other elements
2. If we find a match, return true
3. If no matches found after checking all pairs, return false

### Java Code
```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        // Compare each element with every other element
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] == nums[j]) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n²) - Nested loops checking all pairs
- **Space Complexity:** O(1) - No extra space used

### Drawbacks
- Extremely slow for large arrays
- Many redundant comparisons

---

## Approach 2: Sorting (Better Solution)

### Algorithm
1. Sort the array
2. Check adjacent elements
3. If any two adjacent elements are equal, return true

### Java Code
```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        // Sort the array
        Arrays.sort(nums);
        
        // Check adjacent elements
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                return true;
            }
        }
        return false;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n log n) - Dominated by sorting
- **Space Complexity:** O(1) or O(n) - Depends on sorting algorithm

---

## Approach 3: Hash Set (Optimized Solution)

### Algorithm
1. Create a HashSet to track seen numbers
2. For each number:
   - If it's already in the set, we found a duplicate → return true
   - Otherwise, add it to the set
3. If we finish the loop, no duplicates exist → return false

### Java Code
```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        // HashSet to track seen numbers
        Set<Integer> seen = new HashSet<>();
        
        for (int num : nums) {
            // If number already exists in set, we found a duplicate
            if (seen.contains(num)) {
                return true;
            }
            // Add number to set
            seen.add(num);
        }
        
        // No duplicates found
        return false;
    }
}
```

### Alternative One-liner Approach
```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        // If set size < array length, there were duplicates
        return set.size() < nums.length;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) - Single pass through array
- **Space Complexity:** O(n) - HashSet stores up to n unique elements

### Why This is Better
- ✅ Linear time complexity
- ✅ Early termination when duplicate found
- ✅ O(1) lookup time for HashSet
- ✅ Simple and clean code

---

## Key Takeaways

1. **Pattern:** HashSet is perfect for detecting duplicates
2. **Trade-off:** O(n) space for O(n) time vs O(1) space for O(n²) time
3. **Early exit:** We can return immediately when duplicate is found
4. **Set properties:** Sets automatically handle uniqueness

---

## Related Problems
- [[Contains-Duplicate-II]] - Duplicates within k distance
- [[Contains-Duplicate-III]] - Duplicates within value range
- [[Valid-Anagram]] - Similar hashing concept

---

## Tags
#arrays #hashing #set #easy #blind75
