# Daily Temperatures (LC 739)

**Difficulty**: Medium  
**Pattern**: Monotonic Stack  
**LeetCode**: https://leetcode.com/problems/daily-temperatures/

## Problem Statement
Given an array of integers `temperatures` representing daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `ith` day to get a warmer temperature.

**Example:**
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

## Approach 1: Brute Force

### Java Code
```java
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] answer = new int[n];
        
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (temperatures[j] > temperatures[i]) {
                    answer[i] = j - i;
                    break;
                }
            }
        }
        
        return answer;
    }
}
```

### Complexity
- **Time**: O(n²)
- **Space**: O(1)

## Approach 2: Monotonic Stack (Optimized)

### Intuition
Use a decreasing monotonic stack. Store indices. When we find a warmer day, pop from stack and calculate distance.

### Java Code
```java
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] answer = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();
        
        for (int i = 0; i < n; i++) {
            // While current temp is warmer than stack top
            while (!stack.isEmpty() && 
                   temperatures[i] > temperatures[stack.peek()]) {
                int prevIndex = stack.pop();
                answer[prevIndex] = i - prevIndex;
            }
            stack.push(i);
        }
        
        return answer;
    }
}
```

### Complexity
- **Time**: O(n) - Each element pushed/popped once
- **Space**: O(n) - Stack

## Key Takeaways
- Monotonic stack perfect for "next greater element" problems
- Stack stores indices, not values
- Pop when condition satisfied (warmer temperature)
- Remaining elements in stack have no answer (stays 0)
