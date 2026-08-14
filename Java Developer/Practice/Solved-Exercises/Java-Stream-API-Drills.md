# Stream API Drills

This note covers common small-scale stream manipulations frequently asked in coding rounds.

## 1. Find Duplicate Elements
```java
List<Integer> list = Arrays.asList(10, 20, 30, 10, 40, 20);

Set<Integer> duplicates = list.stream()
    .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()))
    .entrySet().stream()
    .filter(entry -> entry.getValue() > 1)
    .map(Map.Entry::getKey)
    .collect(Collectors.toSet());
```

## 2. Find Second Non-Repeated Character
```java
String input = "java articles are useful";

Character result = input.chars()
    .mapToObj(c -> (char) c)
    .filter(c -> !Character.isWhitespace(c))
    .collect(Collectors.groupingBy(Function.identity(), LinkedHashMap::new, Collectors.counting()))
    .entrySet().stream()
    .filter(entry -> entry.getValue() == 1L)
    .map(Map.Entry::getKey)
    .skip(1) // Skip the first one to find the second
    .findFirst()
    .orElse(null);
```

## 3. Count Occurrence of Elements
```java
List<String> items = Arrays.asList("apple", "apple", "banana", "apple", "orange", "banana");

Map<String, Long> counts = items.stream()
    .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
```

## 4. Find Second Highest Number
```java
List<Integer> numbers = Arrays.asList(15, 33, 15, 88, 45, 88, 12);

Optional<Integer> secondHighest = numbers.stream()
    .distinct()
    .sorted(Comparator.reverseOrder())
    .skip(1)
    .findFirst();
```

## Complexity Analysis
- **Time Complexity**: Most operations are $O(N)$ for collection and $O(K \log K)$ for sorting where $K$ is the number of distinct elements.
- **Space Complexity**: $O(N)$ to store the intermediate map or set.

## Interview Explanation
For finding duplicates and counts, the `groupingBy` collector is the most robust approach. To maintain character order for "non-repeated" logic, using `LinkedHashMap` as the map supplier in `groupingBy` is essential.