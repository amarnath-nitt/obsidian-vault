# Average of Top N

**Concept tested**: Sorting, limiting, primitive streams

## Solution
```java
List<Integer> numbers = Arrays.asList(10, 20, 30, 40, 50);

double avgTop3 = numbers.stream()
    .sorted(Comparator.reverseOrder())
    .limit(3)
    .mapToInt(Integer::intValue)
    .average()
    .orElse(0.0);
```

## Complexity
- **Time**: O(n log n)
- **Space**: O(n)

## Interview Explanation
Sort descending, keep the top three numbers, convert to an `IntStream`, then calculate the average. `orElse` handles an empty input.
