---
solved: false
difficulty: Hard
pattern: Greedy
lc_number: 135
date_solved: 
tags:
  - dsa
  - greedy
  - hard
---
# Candy

[Problem Link](https://leetcode.com/problems/candy/)

## Problem Statement
There are `n` children standing in a line. Each child is assigned a rating value given in the integer array `ratings`.
You are giving candies to these children subjected to the following requirements:
1.  Each child must have at least one candy.
2.  Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

## Approach
Two Pass Greedy.
1.  Left to Right: If `ratings[i] > ratings[i-1]`, then `candies[i] = candies[i-1] + 1`. Else `1`.
2.  Right to Left: If `ratings[i] > ratings[i+1]`, then `candies[i] = max(candies[i], candies[i+1] + 1)`.

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N).

## Code
```java
class Solution {
    public int candy(int[] ratings) {
        int n = ratings.length;
        int[] candies = new int[n];
        Arrays.fill(candies, 1);
        
        // Left to Right
        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) {
                candies[i] = candies[i - 1] + 1;
            }
        }
        
        // Right to Left
        int sum = candies[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1]) {
                candies[i] = Math.max(candies[i], candies[i + 1] + 1);
            }
            sum += candies[i];
        }
        
        return sum;
    }
}
```
