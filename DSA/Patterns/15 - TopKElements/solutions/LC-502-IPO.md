---
solved: false
difficulty: Hard
pattern: Top KElements
lc_number: 502
date_solved: 
tags:
  - dsa
  - top-kelements
  - hard
---
# IPO

[Problem Link](https://leetcode.com/problems/ipo/)

## Problem Statement
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most `k` distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most `k` distinct projects.
You are given `n` projects where the `i-th` project has a pure profit `profits[i]` and a minimum capital of `capital[i]` is needed to start it.
Initially, you have `w` capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.
Return the maximum total capital you can obtain after at most `k` distinct projects.

## Approach
Greedy approach with Two Heaps.
1.  **Min-Heap**: Store all projects ordered by required capital.
2.  **Max-Heap**: Store projects that can be afforded (capital <= current W), ordered by profit.
3.  In each step (up to k times):
    - Move all affordable projects from Min-Heap to Max-Heap.
    - If Max-Heap is empty, we can't do any more projects, break.
    - Pick top of Max-Heap (most profitable), add profit to W, decrement k.

## Time and Space Complexity
- **Time Complexity:** O(N log N + K log N).
- **Space Complexity:** O(N).

## Code
```java
class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        int n = profits.length;
        // Min-heap for projects based on capital needed
        PriorityQueue<int[]> minCapitalHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        // Max-heap for projects based on profit
        PriorityQueue<int[]> maxProfitHeap = new PriorityQueue<>((a, b) -> b[1] - a[1]);
        
        for (int i = 0; i < n; i++) {
            minCapitalHeap.offer(new int[]{capital[i], profits[i]});
        }
        
        while (k > 0) {
            // Add all affordable projects to maxProfitHeap
            while (!minCapitalHeap.isEmpty() && minCapitalHeap.peek()[0] <= w) {
                maxProfitHeap.offer(minCapitalHeap.poll());
            }
            
            if (maxProfitHeap.isEmpty()) {
                break;
            }
            
            w += maxProfitHeap.poll()[1];
            k--;
        }
        
        return w;
    }
}
```
