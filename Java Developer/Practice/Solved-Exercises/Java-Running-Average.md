# Running Average

**Concept tested**: Cumulative aggregation

## Solution
```java
List<Integer> numbers = Arrays.asList(10, 20, 30, 40, 50);

List<Double> runningAvg = new ArrayList<>();
int sum = 0;

for (int i = 0; i < numbers.size(); i++) {
    sum += numbers.get(i);
    runningAvg.add(sum / (double) (i + 1));
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)

## Interview Explanation
Keep a cumulative sum while scanning the list once. At every index, divide the current sum by the number of elements seen so far.
