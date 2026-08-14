# Greedy Algorithm - Practice Notes

## Pattern Overview
Making locally optimal choices at each step with the hope of finding a global optimum.

## Key Concepts
- **Local optimum**: Best choice at current step
- **Greedy choice property**: Local optimum leads to global optimum
- **No backtracking**: Decisions are final
- **Time Complexity**: Usually O(n log n) due to sorting

## Template Code

### Interval Scheduling
```java
public int maxMeetings(int[][] intervals) {
    Arrays.sort(intervals, (a, b) -> a[1] - b[1]); // Sort by end time
    int count = 1;
    int end = intervals[0][1];
    
    for (int i = 1; i < intervals.length; i++) {
        if (intervals[i][0] >= end) {
            count++;
            end = intervals[i][1];
        }
    }
    return count;
}
```

### Greedy with Priority Queue
```java
public int minimumCost(int[][] costs) {
    PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
    for (int[] cost : costs) {
        pq.offer(cost);
    }
    
    int total = 0;
    while (!pq.isEmpty()) {
        int[] curr = pq.poll();
        total += curr[0];
        // Process based on greedy strategy
    }
    return total;
}
```

## Practice Problems

### Easy
- [ ] [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) (LC 121) → [Solution](solutions/LC-121-Best-Time-Stock.md)
- [ ] [Assign Cookies](https://leetcode.com/problems/assign-cookies/) (LC 455) → [Solution](solutions/LC-455-Assign-Cookies.md)
- [ ] [Lemonade Change](https://leetcode.com/problems/lemonade-change/) (LC 860) → [Solution](solutions/LC-860-Lemonade-Change.md)
- [ ] [Longest Palindrome](https://leetcode.com/problems/longest-palindrome/) (LC 409) → [Solution](solutions/LC-409-Longest-Palindrome.md)

### Medium
- [ ] [Jump Game](https://leetcode.com/problems/jump-game/) (LC 55) → [Solution](solutions/LC-55-Jump-Game.md)
- [ ] [Jump Game II](https://leetcode.com/problems/jump-game-ii/) (LC 45) → [Solution](solutions/LC-45-Jump-Game-II.md)
- [ ] [Gas Station](https://leetcode.com/problems/gas-station/) (LC 134) → [Solution](solutions/LC-134-Gas-Station.md)
- [ ] [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (LC 53) → [Solution](solutions/LC-53-Maximum-Subarray.md)
- [ ] [Task Scheduler](https://leetcode.com/problems/task-scheduler/) (LC 621) → [Solution](solutions/LC-621-Task-Scheduler.md)
- [ ] [Partition Labels](https://leetcode.com/problems/partition-labels/) (LC 763) → [Solution](solutions/LC-763-Partition-Labels.md)
- [ ] [Largest Number](https://leetcode.com/problems/largest-number/) (LC 179) → [Solution](solutions/LC-179-Largest-Number.md)
- [ ] [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) (LC 435)
- [ ] [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) (LC 435)

### Hard
- [ ] [Candy](https://leetcode.com/problems/candy/) (LC 135) → [Solution](solutions/LC-135-Candy.md)
- [ ] [Minimum Number of Taps to Open to Water a Garden](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/) (LC 1326) → [Solution](solutions/LC-1326-Minimum-Taps.md)

## Reference
[LeetCode Pattern Guide](https://lnkd.in/guCMb8k4)
