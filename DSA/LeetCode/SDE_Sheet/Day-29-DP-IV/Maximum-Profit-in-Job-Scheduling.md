# Maximum Profit in Job Scheduling

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
