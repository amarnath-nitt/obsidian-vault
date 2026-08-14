# Custom Object Sorting

**Concept tested**: Comparator chaining on objects

## Problem
Sort employees by salary descending, then by name ascending when salaries are equal.

## Solution
```java
employees.sort(
    Comparator.comparingDouble(Employee::getSalary).reversed()
              .thenComparing(Employee::getName)
);
```

## Complexity
- **Time**: O(n log n)
- **Space**: O(1) to O(n), depending on sort implementation

## Interview Explanation
Sort by the primary business rule first: highest salary. Then use `thenComparing` for deterministic ordering when two salaries match.
