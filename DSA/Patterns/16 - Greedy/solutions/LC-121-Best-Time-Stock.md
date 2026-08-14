# Best Time to Buy and Sell Stock

[Problem Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## Problem Statement
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

## Approach
Greedy.
Track `minPrice` so far.
For each price, `profit = price - minPrice`.
Update `maxProfit`.

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```java
class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;
        
        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price;
            } else if (price - minPrice > maxProfit) {
                maxProfit = price - minPrice;
            }
        }
        
        return maxProfit;
    }
}
```
