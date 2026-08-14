# Day 29 — Dynamic Programming IV (String DP, Partition DP)

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** DP — Strings, Partitioning, Stock Trading, Advanced Optimization
**Difficulty Mix:** Medium / Hard

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Best Time to Buy and Sell Stock (DP Suite)]] | 122/123 | Medium / Hard | ⬜ |
| 2 | [[#Word Break]] | 139 | Medium | ⬜ |
| 3 | [[#Palindrome Partitioning II (Min Cuts)]] | 132 | Hard | ⬜ |
| 4 | [[#Maximum Sum Increasing Subsequence]] | — | Medium | ⬜ |
| 5 | [[#Rod Cutting]] | — | Medium | ⬜ |
| 6 | [[#Maximum Profit in Job Scheduling]] | 1235 | Hard | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Best Time to Buy and Sell Stock (DP Suite) | Try every buy/sell sequence. Exponential. | DP over day, hold state, and remaining transactions. | Space-compressed state variables/tables. O(n*k) or O(n) for fixed k. |
| Word Break | Try all split combinations recursively. Exponential. | Memoized DFS by start index. O(n^2). | Bottom-up DP with HashSet/trie pruning. O(n^2). |
| Palindrome Partitioning II | Generate every palindrome partition. Exponential. | Palindrome table plus cut DP. O(n^2). | Center expansion updates min cuts with O(n) space. |
| Maximum Sum Increasing Subsequence | Enumerate all increasing subsequences. Exponential. | DP best sum ending at each index. O(n^2). | Fenwick/segment tree after coordinate compression. O(n log n). |
| Rod Cutting | Try every way to cut the rod. Exponential. | Unbounded knapsack DP. O(n^2). | 1D DP over rod lengths. O(n^2), O(n) space. |
| Maximum Profit in Job Scheduling | Try every subset of compatible jobs. Exponential. | Sort by end/start and DP with binary search. O(n log n). | Bottom-up or memoized DP over sorted jobs with next-compatible lookup. |

---

## Best Time to Buy and Sell Stock (DP Suite)

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

## Word Break

**LeetCode 139** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/word-break/)

### Problem
Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

### Approach
- **State:** `dp[i]` = true if `s[0..i-1]` can be segmented.
- **Transition:** `dp[i] = true` if there exists `j < i` such that `dp[j] == true` AND `s[j..i-1]` is in the dictionary.

### Java Solution

```java
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> set = new HashSet<>(wordDict);
        int n = s.length();
        boolean[] dp = new boolean[n + 1];
        dp[0] = true; // empty string is always matchable

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && set.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break; // found valid partition
                }
            }
        }
        return dp[n];
    }
}
```

**Complexity:** Time $O(N^2 \times L)$ (where $L$ is max word length in dict) · Space $O(N + D)$ (where $D$ is size of dict)

---

## Palindrome Partitioning II (Min Cuts)

**LeetCode 132** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/palindrome-partitioning-ii/)

### Problem
Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return the minimum cuts needed for a palindrome partitioning of `s`.

### Approach
1. **Precompute Palindromes:** Create a boolean table `isPal[i][j]` representing if `s[i..j]` is a palindrome.
2. **DP for Min Cuts:** Let `cuts[i]` be the minimum cuts needed for `s[0..i]`.
   - If `s[0..i]` is a palindrome, `cuts[i] = 0`.
   - Else, `cuts[i] = min(cuts[j] + 1)` for all `j < i` where `s[j+1..i]` is a palindrome.

### Java Solution

```java
class Solution {
    public int minCut(String s) {
        int n = s.length();
        boolean[][] isPal = new boolean[n][n];
        int[] cuts = new int[n];

        for (int i = 0; i < n; i++) {
            int minCuts = i;
            for (int j = 0; j <= i; j++) {
                if (s.charAt(i) == s.charAt(j) && (i - j < 2 || isPal[j + 1][i - 1])) {
                    isPal[j][i] = true;
                    minCuts = (j == 0) ? 0 : Math.min(minCuts, cuts[j - 1] + 1);
                }
            }
            cuts[i] = minCuts;
        }
        return cuts[n - 1];
    }
}
```

**Complexity:** Time $O(N^2)$ · Space $O(N^2)$

---

## Maximum Sum Increasing Subsequence

**Problem:** Given an array of $N$ positive integers, find the maximum sum increasing subsequence of the given array.

### Approach
- Variation of LIS (Longest Increasing Subsequence).
- **State:** `dp[i]` = maximum sum of an increasing subsequence ending at index `i`.
- **Transition:** `dp[i] = nums[i] + max(dp[j])` for all `j < i` where `nums[j] < nums[i]`. Initialize `dp[i] = nums[i]`.
- **Result:** Max element in `dp`.

### Java Solution

```java
public class MaxSumIS {
    public static int maxSumIS(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        int maxSum = 0;

        for (int i = 0; i < n; i++) {
            dp[i] = nums[i];
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + nums[i]);
                }
            }
            maxSum = Math.max(maxSum, dp[i]);
        }
        return maxSum;
    }
}
```

**Complexity:** Time $O(N^2)$ · Space $O(N)$

---

## Rod Cutting

**Problem:** Given a rod of length $N$ inches and an array of prices that includes prices of all pieces of size smaller than $N$. Determine the maximum value obtainable by cutting up the rod and selling the pieces.

### Approach
- This is equivalent to **Unbounded Knapsack**.
- **State:** `dp[i]` = maximum value obtainable for a rod of length `i`.
- **Transition:** `dp[i] = max(prices[j] + dp[i - (j + 1)])` for all $0 \le j < i$.

### Java Solution

```java
public class RodCutting {
    public static int cutRod(int[] prices, int n) {
        int[] dp = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            int maxVal = Integer.MIN_VALUE;
            for (int j = 0; j < i; j++) {
                maxVal = Math.max(maxVal, prices[j] + dp[i - j - 1]);
            }
            dp[i] = maxVal;
        }
        return dp[n];
    }
}
```

**Complexity:** Time $O(N^2)$ · Space $O(N)$

---

## Maximum Profit in Job Scheduling

**LeetCode 1235** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)

### Problem
Given $N$ jobs where every job has a start time, end time, and a profit. Find the maximum profit you can make such that no two jobs in the subset overlap.

### Approach
1. **Sort:** Sort the jobs by their end times.
2. **DP + Binary Search:**
   - **State:** `dp[i]` = max profit considering the first `i` jobs.
   - For each job `i`:
     - **Option 1: Exclude** job `i` → `dp[i] = dp[i-1]`.
     - **Option 2: Include** job `i` → `dp[i] = profit[i] + dp[latestNonOverlappingJob]`.
     - Use **binary search** (`upper_bound` or equivalent) on end times to find the latest job that ends before job `i` starts.

### Java Solution

```java
class Solution {
    private class Job {
        int start, end, profit;
        Job(int start, int end, int profit) {
            this.start = start;
            this.end = end;
            this.profit = profit;
        }
    }

    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int n = startTime.length;
        Job[] jobs = new Job[n];
        for (int i = 0; i < n; i++) {
            jobs[i] = new Job(startTime[i], endTime[i], profit[i]);
        }

        // Sort jobs by end times
        Arrays.sort(jobs, (a, b) -> Integer.compare(a.end, b.end));

        // dp[i] stores the max profit from first i jobs
        int[] dp = new int[n];
        dp[0] = jobs[0].profit;

        for (int i = 1; i < n; i++) {
            int includeProfit = jobs[i].profit;
            int l = 0, r = i - 1;
            int latestJobIdx = -1;

            // Binary search to find latest non-overlapping job
            while (l <= r) {
                int mid = (l + r) / 2;
                if (jobs[mid].end <= jobs[i].start) {
                    latestJobIdx = mid;
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }

            if (latestJobIdx != -1) {
                includeProfit += dp[latestJobIdx];
            }

            dp[i] = Math.max(dp[i - 1], includeProfit);
        }

        return dp[n - 1];
    }
}
```

**Complexity:** Time $O(N \log N)$ · Space $O(N)$

---

## Summary of Advanced DP Techniques

```
  Technique              Primary Application               Optimization Method
---------------------------------------------------------------------------------
  Interval DP            MCM, Palindrome Partitioning      O(N³) or O(N²) Matrix
  State Machine DP       Stock Trading, Game Theory        State compression, O(1) space
  DP + Binary Search     Weighted Job Scheduling, LIS      Replace O(N²) scan with O(log N)
```

#sde-sheet #dynamic-programming #day29
