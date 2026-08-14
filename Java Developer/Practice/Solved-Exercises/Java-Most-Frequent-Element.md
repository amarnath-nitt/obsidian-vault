# Most Frequent Element

**Concept tested**: Frequency counting with streams

## Solution
```java
List<String> items = Arrays.asList("apple", "banana", "apple", "orange", "banana", "apple");

String mostFrequent = items.stream()
    .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()))
    .entrySet()
    .stream()
    .max(Map.Entry.comparingByValue())
    .map(Map.Entry::getKey)
    .orElse(null);
```

## Complexity
- **Time**: O(n)
- **Space**: O(k), where `k` is number of distinct items

## Interview Explanation
First build a frequency map. Then stream over the map entries and choose the entry with the largest count.
