# Second Highest Salary

**Concept tested**: Stream API (`map`, `distinct`, `sorted`, `skip`)

## Problem
Find the second highest salary among a list of employees.

## Solution
```java
public Optional<Double> getSecondHighestSalary(List<Employee> employees) {
    return employees.stream()
        .map(Employee::getSalary)          // Extract salaries
        .distinct()                         // Remove duplicates (e.g., if two people earn the max)
        .sorted(Comparator.reverseOrder())  // Sort descending
        .skip(1)                            // Skip the highest
        .findFirst();                       // Take the next one (which is the 2nd highest)
}
```

## Alternative: Finding the Employee Object
If you need the actual `Employee` object instead of just the salary value:
```java
Optional<Employee> secondHighestEmployee = employees.stream()
    .sorted(Comparator.comparingDouble(Employee::getSalary).reversed())
    .skip(1)
    .findFirst();
```
*Note: This version does not handle duplicate top salaries unless you add custom logic to filter unique salaries first.*

## Complexity
- **Time Complexity**: $O(N \log N)$ due to the sorting operation.
- **Space Complexity**: $O(N)$ for the stream pipeline (or $O(1)$ extra space depending on the internal sort implementation).

## Interview Explanation
To find the second highest value using Java Streams, we first extract the numeric values and apply `distinct()` to ensure that if multiple employees share the top salary, we still find the actual second unique value. We then sort the stream in reverse order, use `skip(1)` to bypass the maximum, and use `findFirst()` to retrieve the result. Returning an `Optional` is the best practice here to handle cases where the list has fewer than two distinct salaries.