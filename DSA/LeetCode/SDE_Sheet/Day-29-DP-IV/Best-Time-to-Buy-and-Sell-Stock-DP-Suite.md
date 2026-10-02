# Best Time to Buy and Sell Stock (DP Suite)

**LeetCode 122 / 123** · Medium / Hard
🔗 [LeetCode Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | [LeetCode Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

### Approach

We can model the stock trading problems with a state machine.
- **State:** `dp[i][buy][k]` = max profit on day `i`, with `buy` indicating whether we can buy (1) or sell (0), and `k` remaining transactions.

#### Stock II (Infinite Transactions)
- **Transition:**
  - If we buy: `dp[i][1] = max(-prices[i] + dp[i+1][0], dp[i+1][1])`
  - If we sell: `dp[i][0] = max(prices[i] + dp[i+1][1], dp[i+1][0])`

#### Stock III (At most 2 Transactions)
- Keep track of transaction limit `k` (from 2 down to 1).
- `dp[i][buy][k]`:
  - Buy: `max(-prices[i] + dp[i+1][0][k], dp[i+1][1][k])`
  - Sell: `max(prices[i] + dp[i+1][1][k-1], dp[i+1][0][k])`

### Java Solution (Stock III - Space Optimized)

```java
class Solution {
    public int maxProfit(int[] prices) {
        int buy1 = Integer.MAX_VALUE, buy2 = Integer.MAX_VALUE;
        int sell1 = 0, sell2 = 0;

        for (int price : prices) {
            buy1 = Math.min(buy1, price);
            sell1 = Math.max(sell1, price - buy1);
            buy2 = Math.min(buy2, price - sell1);
            sell2 = Math.max(sell2, price - buy2);
        }
        return sell2;
    }
}
```

**Complexity:** Time $O(N)$ · Space $O(1)$

---
