# Day 8 — Greedy Algorithms

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** Greedy — Making locally optimal choices
**Difficulty Mix:** Medium / Hard

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#N Meetings in One Room]] | — | Medium | ⬜ |
| 2 | [[#Minimum Platforms Required]] | — | Medium | ⬜ |
| 3 | [[#Job Sequencing Problem]] | — | Medium | ⬜ |
| 4 | [[#Fractional Knapsack]] | — | Medium | ⬜ |
| 5 | [[#Activity Selection / Minimum Arrows to Burst Balloons]] | 452 | Medium | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| N Meetings in One Room | Try every subset/order of meetings. Exponential. | Sort by start and explore compatible choices with DP/backtracking. | Sort by end time and greedily pick earliest finishing meeting. O(n log n). |
| Minimum Platforms Required | For each train, count overlaps with every other train. O(n^2). | Difference array over bounded time values. | Sort arrivals/departures and use two pointers. O(n log n). |
| Job Sequencing Problem | Try all job schedules. Exponential. | Sort by profit and scan backward for a free slot. O(n*d). | DSU tracks latest free slot. O(n log n + n alpha(n)). |
| Fractional Knapsack | Try possible item orders. Exponential. | Sort by value/weight ratio. O(n log n). | Same greedy; take full items then one fraction. O(n log n). |
| Activity Selection / Minimum Arrows | Try all arrow/activity choices. Exponential. | Sort by start and merge overlaps. O(n log n). | Sort by end and greedily shoot/select at earliest finish. O(n log n). |

---

## N Meetings in One Room

**Problem:** Given start and end times of N meetings, find the maximum number of meetings that can be held in one room.

### Approach (Activity Selection — Earliest Finish Time)

1. Sort meetings by **end time**
2. Greedily pick a meeting if its **start time > last meeting's end time**

> **Why earliest finish?** By finishing early, we leave maximum room for future meetings.

### Java Solution

```java
import java.util.Arrays;

public class NMeetings {
    static int maxMeetings(int[] start, int[] end) {
        int n = start.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Arrays.sort(idx, (a, b) -> end[a] - end[b]); // sort by end time

        int count = 1, lastEnd = end[idx[0]];
        for (int i = 1; i < n; i++) {
            if (start[idx[i]] > lastEnd) {
                count++;
                lastEnd = end[idx[i]];
            }
        }
        return count;
    }
}
```

**Complexity:** Time O(n log n) · Space O(n)

---

## Minimum Platforms Required

**Problem:** Given arrival and departure times of trains, find the minimum number of platforms needed.

### Approach (Sort + Two Pointers)

- Sort arrival and departure arrays separately
- Use two pointers: advance arrival or departure based on which is smaller
- Track platforms in use and max platforms used

### Java Solution

```java
public int minPlatforms(int[] arr, int[] dep) {
    Arrays.sort(arr);
    Arrays.sort(dep);

    int platforms = 1, maxPlatforms = 1;
    int i = 1, j = 0;

    while (i < arr.length && j < dep.length) {
        if (arr[i] <= dep[j]) { // new train arrives before current leaves
            platforms++;
            i++;
        } else {
            platforms--;
            j++;
        }
        maxPlatforms = Math.max(maxPlatforms, platforms);
    }
    return maxPlatforms;
}
```

**Complexity:** Time O(n log n) · Space O(1)

---

## Job Sequencing Problem

**Problem:** Jobs with deadlines and profits. Each job takes 1 unit. Find max profit sequence.

### Approach (Greedy — Sort by Profit Descending)

1. Sort jobs by **profit descending**
2. For each job, assign to the latest available slot ≤ deadline
3. Use a boolean array to track occupied slots

### Java Solution

```java
public int[] jobSequencing(int[] id, int[] deadline, int[] profit) {
    int n = id.length;
    Integer[] idx = new Integer[n];
    for (int i = 0; i < n; i++) idx[i] = i;
    Arrays.sort(idx, (a, b) -> profit[b] - profit[a]); // sort by profit desc

    int maxDeadline = Arrays.stream(deadline).max().getAsInt();
    boolean[] slots = new boolean[maxDeadline + 1];
    int jobsDone = 0, totalProfit = 0;

    for (int i : idx) {
        for (int j = deadline[i]; j > 0; j--) {
            if (!slots[j]) {
                slots[j] = true;
                jobsDone++;
                totalProfit += profit[i];
                break;
            }
        }
    }
    return new int[]{jobsDone, totalProfit};
}
```

**Complexity:** Time O(n² worst) / O(n log n) with Union-Find · Space O(maxDeadline)

---

## Fractional Knapsack

**Problem:** Items with weights and values. Knapsack capacity W. Can take fractions. Maximize value.

### Approach (Greedy — Sort by Value/Weight Ratio)

- Sort items by `value/weight` descending
- Take as much of each item as possible

> Unlike 0/1 knapsack, fractions are allowed → greedy works!

### Java Solution

```java
public double fractionalKnapsack(int W, int[] weight, int[] value) {
    int n = weight.length;
    Integer[] idx = new Integer[n];
    for (int i = 0; i < n; i++) idx[i] = i;
    // Sort by value/weight ratio descending
    Arrays.sort(idx, (a, b) -> Double.compare(
        (double)value[b]/weight[b], (double)value[a]/weight[a]));

    double totalValue = 0;
    for (int i : idx) {
        if (W >= weight[i]) {
            totalValue += value[i];
            W -= weight[i];
        } else {
            totalValue += (double)value[i] / weight[i] * W;
            break;
        }
    }
    return totalValue;
}
```

**Complexity:** Time O(n log n) · Space O(n)

---

## Activity Selection / Minimum Arrows to Burst Balloons

**LeetCode 452** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

### Problem
Balloons represented as intervals. Minimum arrows to burst all (arrow at x bursts all balloons spanning x).

### Approach (Activity Selection / Greedy)

- Sort by **end coordinate**
- Shoot an arrow at the end of the first balloon
- Skip all balloons the arrow hits
- Next arrow at the next unpopped balloon's end

### Java Solution

```java
class Solution {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, (a, b) -> Integer.compare(a[1], b[1]));

        int arrows = 1;
        int arrowPos = points[0][1];

        for (int i = 1; i < points.length; i++) {
            if (points[i][0] > arrowPos) { // balloon starts after current arrow
                arrows++;
                arrowPos = points[i][1];
            }
        }
        return arrows;
    }
}
```

**Complexity:** Time O(n log n) · Space O(1)

---

## Greedy Cheatsheet

| Problem Type | Greedy Strategy |
|---|---|
| Meeting rooms / Activity selection | Sort by end time |
| Job sequencing with deadlines | Sort by profit desc, fill from deadline |
| Fractional knapsack | Sort by value/weight ratio |
| Minimum platforms | Sort arrivals & departures separately |
| Interval scheduling | Sort by end, take non-overlapping |
| Minimum arrows / intervals | Sort by end, merge overlapping |

---

## When Greedy Works vs Doesn't

✅ **Works when:**
- Local optimal = global optimal (e.g., fractional knapsack)
- Exchange argument proves correctness

❌ **Fails when:**
- Future choices affect current (use DP instead, e.g., 0/1 knapsack)

#sde-sheet #greedy #day8
