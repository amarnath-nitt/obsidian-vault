# Day 8 — Greedy Algorithms

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** Greedy — Making locally optimal choices
**Difficulty Mix:** Medium / Hard

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [N Meetings in One Room](N-Meetings-in-One-Room.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=N+Meetings+in+One+Room)
- [ ] [Minimum Platforms Required](Minimum-Platforms-Required.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Minimum+Platforms+Required)
- [ ] [Job Sequencing Problem](Job-Sequencing-Problem.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Job+Sequencing+Problem)
- [ ] [Fractional Knapsack](Fractional-Knapsack.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Fractional+Knapsack)
- [ ] [Activity Selection / Minimum Arrows to Burst Balloons](Activity-Selection-Minimum-Arrows-to-Burst-Balloons.md) | LeetCode 452 | Medium | [LeetCode](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| N Meetings in One Room | Try every subset/order of meetings. Exponential. | Sort by start and explore compatible choices with DP/backtracking. | Sort by end time and greedily pick earliest finishing meeting. O(n log n). |
| Minimum Platforms Required | For each train, count overlaps with every other train. O(n^2). | Difference array over bounded time values. | Sort arrivals/departures and use two pointers. O(n log n). |
| Job Sequencing Problem | Try all job schedules. Exponential. | Sort by profit and scan backward for a free slot. O(n*d). | DSU tracks latest free slot. O(n log n + n alpha(n)). |
| Fractional Knapsack | Try possible item orders. Exponential. | Sort by value/weight ratio. O(n log n). | Same greedy; take full items then one fraction. O(n log n). |
| Activity Selection / Minimum Arrows | Try all arrow/activity choices. Exponential. | Sort by start and merge overlaps. O(n log n). | Sort by end and greedily shoot/select at earliest finish. O(n log n). |

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
