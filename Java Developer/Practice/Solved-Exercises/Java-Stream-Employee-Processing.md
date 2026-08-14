# Employee Processing

**Concept tested**: Stream filtering, sorting, limiting

## Problem
Find the top 3 highest-paid employees in the IT department.

## Solution
```java
class Employee {
    private final String name;
    private final String department;
    private final double salary;

    Employee(String name, String department, double salary) {
        this.name = name;
        this.department = department;
        this.salary = salary;
    }

    String getName() { return name; }
    String getDepartment() { return department; }
    double getSalary() { return salary; }
}

List<Employee> topIT = employees.stream()
    .filter(e -> "IT".equals(e.getDepartment()))
    .sorted(Comparator.comparingDouble(Employee::getSalary).reversed())
    .limit(3)
    .collect(Collectors.toList());
```

## Complexity
- **Time**: O(n log n)
- **Space**: O(n)

## Interview Explanation
Filter by department first to reduce the dataset, sort remaining employees by salary descending, then take the first three.
