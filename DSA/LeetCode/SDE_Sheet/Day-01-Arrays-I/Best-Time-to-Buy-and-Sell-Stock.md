# Best Time to Buy and Sell Stock

**LeetCode 121** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

### Problem
Given prices array, find the maximum profit from one transaction (buy then sell).

### Approach

- Track `minPrice` seen so far (best day to buy)
- At each day, compute profit = `price - minPrice`
- Track `maxProfit` across all days

### Java Solution

```java
class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;

        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price;
            } else {
                maxProfit = Math.max(maxProfit, price - minPrice);
            }
        }
        return maxProfit;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---
