# Best Time to Buy and Sell Stock III

[Problem Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

## Problem Statement
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.
Find the maximum profit you can achieve. You may complete **at most two** transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

## Approach
DP State Machine.
States:
- `buy1`: Max profit after first buy.
- `sell1`: Max profit after first sell.
- `buy2`: Max profit after second buy.
- `sell2`: Max profit after second sell.

Transitions:
- `buy1 = max(buy1, -price)`
- `sell1 = max(sell1, buy1 + price)`
- `buy2 = max(buy2, sell1 - price)`
- `sell2 = max(sell2, buy2 + price)`

Initialize `buy` states to `-infinity`, `sell` states to `0`.

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```java
class Solution {
    public int maxProfit(int[] prices) {
        int buy1 = Integer.MIN_VALUE, sell1 = 0;
        int buy2 = Integer.MIN_VALUE, sell2 = 0;
        
        for (int p : prices) {
            buy1 = Math.max(buy1, -p);
            sell1 = Math.max(sell1, buy1 + p);
            buy2 = Math.max(buy2, sell1 - p);
            sell2 = Math.max(sell2, buy2 + p);
        }
        
        return sell2;
    }
}
```
