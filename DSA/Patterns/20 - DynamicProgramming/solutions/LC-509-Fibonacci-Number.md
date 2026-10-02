---
solved: false
difficulty: Easy
pattern: Dynamic Programming
lc_number: 509
date_solved: 
tags:
  - dsa
  - dynamic-programming
  - easy
---
# Fibonacci Number

[Problem Link](https://leetcode.com/problems/fibonacci-number/)

## Problem Statement
The Fibonacci numbers, commonly denoted `F(n)` form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from `0` and `1`. That is:
`F(0) = 0, F(1) = 1`
`F(n) = F(n - 1) + F(n - 2), for n > 1.`
Given `n`, calculate `F(n)`.

## Approach
DP / Iterative.
`a = 0, b = 1`.
Loop `n` times to compute next.

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```java
class Solution {
    public int fib(int n) {
        if (n <= 1) return n;
        
        int a = 0, b = 1;
        for (int i = 2; i <= n; i++) {
            int temp = a + b;
            a = b;
            b = temp;
        }
        return b;
    }
}
```
