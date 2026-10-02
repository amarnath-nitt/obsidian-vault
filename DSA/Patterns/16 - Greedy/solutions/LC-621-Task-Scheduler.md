---
solved: false
difficulty: Medium
pattern: Greedy
lc_number: 621
date_solved: 
tags:
  - dsa
  - greedy
  - medium
---
# Task Scheduler (LC 621)

**Difficulty**: Medium  
**Pattern**: Greedy / Heap  
**LeetCode**: https://leetcode.com/problems/task-scheduler/

## Problem Statement
Given a characters array `tasks`, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
However, there is a non-negative integer `n` that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least `n` units of time between any two same tasks.
Return the least number of units of times that the CPU will take to finish all the given tasks.

**Example:**
```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B
```

## Approach: Math / Greedy

### Intuition
The bottleneck is the most frequent task.
Say task A appears `max_freq` times.
We need `(max_freq - 1)` groups of size `(n + 1)`.
Last group size depends on how many tasks share `max_freq`.
Formula: `(max_freq - 1) * (n + 1) + count_of_max_freq_tasks`.
Result is `max(tasks.length, formula)`.

### Java Code
```java
class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] freq = new int[26];
        int maxFreq = 0;
        
        for (char task : tasks) {
            freq[task - 'A']++;
            maxFreq = Math.max(maxFreq, freq[task - 'A']);
        }
        
        int countMax = 0;
        for (int f : freq) {
            if (f == maxFreq) countMax++;
        }
        
        int partCount = maxFreq - 1;
        int emptySlots = partCount * (n - (countMax - 1)); // Actually simpler formula available
        int formula = (maxFreq - 1) * (n + 1) + countMax;
        
        return Math.max(tasks.length, formula);
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(1)

## Key Takeaways
- Identify bottleneck
- Scheduling slots visualization
