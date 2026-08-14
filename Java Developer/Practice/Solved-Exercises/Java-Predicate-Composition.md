# Predicate Composition

**Concept tested**: `Predicate.and`, `Predicate.or`, `Predicate.negate`

## Solution
```java
Predicate<Employee> isIT = e -> "IT".equals(e.getDepartment());
Predicate<Employee> highSalary = e -> e.getSalary() > 80000;

List<Employee> filtered = employees.stream()
    .filter(isIT.and(highSalary))
    .collect(Collectors.toList());

Predicate<Employee> lowSalary = highSalary.negate();
```

## Complexity
- **Time**: O(n)
- **Space**: O(n) for the result

## Interview Explanation
Predicates make conditions reusable and composable. `and` requires both conditions, while `negate` creates the opposite condition.
