# Java Coding Practice Plan

Use this as the main practice index. Each solution note includes the concept tested, Java code, complexity, and interview explanation. Solve the problem yourself first, then compare the trade-offs—not only the final code.

## Stream API Exercises

| # | Problem | Solution | Concept Tested |
|---|---------|----------|----------------|
| 1 | Filter and Transform | [Solution](Solved-Exercises/Java-Stream-Filter-and-Transform.md) | `filter`, `map`, `sorted` |
| 2 | Group By and Count | [Solution](Solved-Exercises/Java-Stream-Group-By-and-Count.md) | `groupingBy`, `counting` |
| 3 | Find First and Optional | [Solution](Solved-Exercises/Java-Optional-Find-First.md) | `findFirst`, `Optional` |
| 4 | Flatten Nested Lists | [Solution](Solved-Exercises/Java-Stream-Flatten-Nested-Lists.md) | `flatMap` |
| 5 | Partition Even and Odd | [Solution](Solved-Exercises/Java-Stream-Partition-Even-and-Odd.md) | `partitioningBy` |
| 6 | Employee Processing | [Solution](Solved-Exercises/Java-Stream-Employee-Processing.md) | filtering, sorting, limiting |
| 7 | String Manipulation | [Solution](Solved-Exercises/Java-Stream-String-Manipulation.md) | `flatMap`, `distinct`, `joining` |
| 8 | Average of Top N | [Solution](Solved-Exercises/Java-Stream-Average-of-Top-N.md) | sorting, `mapToInt`, `average` |
| 21 | Stream API Drills | [Solution](Solved-Exercises/Java-Stream-API-Drills.md) | `distinct`, `counting`, `skip` |
| 22 | Second Highest Salary | [Solution](Solved-Exercises/Java-Second-Highest-Salary.md) | `Comparator`, `findFirst`, `distinct` |
| 23 | Sorting Objects | [Solution](Solved-Exercises/Java-Sorting-Objects.md) | `comparingDouble`, `sorted` |
| 25 | First non-repeated character from a `char[]` | [Solution](Solved-Exercises/Java-First-Non-Repeated-Character-from-Char-Array.md) | `String.chars`, `mapToObj`, `LinkedHashMap`, `groupingBy` |

## Lambda Expression Challenges

| # | Problem | Solution | Concept Tested |
|---|---------|----------|----------------|
| 9 | Custom Comparator | [Solution](Solved-Exercises/Java-Custom-Comparator.md) | comparator chaining |
| 10 | Predicate Composition | [Solution](Solved-Exercises/Java-Predicate-Composition.md) | `Predicate.and`, `negate` |
| 11 | Function Chaining | [Solution](Solved-Exercises/Java-Function-Chaining.md) | `Function.andThen` |

## Multithreading Problems

| # | Problem | Solution | Concept Tested |
|---|---------|----------|----------------|
| 12 | Producer-Consumer Pattern | [Solution](Solved-Exercises/Java-Producer-Consumer.md) | `BlockingQueue` |
| 13 | CountDownLatch | [Solution](Solved-Exercises/Java-CountDownLatch.md) | coordination between threads |
| 14 | Thread-Safe Singleton | [Solution](Solved-Exercises/Java-Thread-Safe-Singleton.md) | `volatile`, synchronization, enum singleton |

## Collection Manipulation

| # | Problem | Solution | Concept Tested |
|---|---------|----------|----------------|
| 15 | Remove Duplicates Maintaining Order | [Solution](Solved-Exercises/Java-Remove-Duplicates-Preserve-Order.md) | `LinkedHashSet`, `distinct` |
| 16 | Find Common Elements | [Solution](Solved-Exercises/Java-Find-Common-Elements.md) | `retainAll`, set lookup |
| 17 | Most Frequent Element | [Solution](Solved-Exercises/Java-Most-Frequent-Element.md) | frequency map |

## Advanced Challenges

| # | Problem | Solution | Concept Tested |
|---|---------|----------|----------------|
| 18 | Anagram Grouping | [Solution](Solved-Exercises/Java-Anagram-Grouping.md) | grouping by normalized key |
| 19 | Running Average | [Solution](Solved-Exercises/Java-Running-Average.md) | cumulative aggregation |
| 20 | Custom Object Sorting | [Solution](Solved-Exercises/Java-Custom-Object-Sorting.md) | comparator chaining |

## Persistence Exercise

| # | Problem | Solution | Concept Tested |
|---|---------|----------|----------------|
| 24 | Calling stored procedures with Spring Data JPA | [Solution](Solved-Exercises/Spring-Data-JPA-Stored-Procedures.md) | `@Procedure`, `EntityManager`, output parameters |

---

## Additional Interview Practice

Use these as short drills after the solved examples above.

### Easy

1. Reverse a string without using `StringBuilder.reverse()`.
2. Count vowels and consonants in a sentence.
3. Remove duplicate values from a `List<Integer>` while preserving insertion order.
4. Find the second largest number in an array.
5. Convert a `List<String>` into a comma-separated string.
6. Sort a list of strings by length.
7. Check whether two strings are anagrams.
8. Find duplicate characters in a string.

### Medium

1. Group employees by department using streams.
2. Find the highest-paid employee in each department.
3. Convert a list of objects into a map, handling duplicate keys.
4. Implement a simple LRU cache using `LinkedHashMap`.
5. Write a producer-consumer example using `BlockingQueue`.
6. Parse a list of log lines and count requests by status code.
7. Merge two sorted lists without using library sort.
8. Implement retry logic around a method that can throw an exception.

### Hard

1. Build a thread-safe in-memory cache with TTL expiration.
2. Implement a custom fixed-size thread pool.
3. Detect and explain a deadlock in a small code sample.
4. Design immutable `Employee` and `Address` classes with defensive copying.
5. Implement a rate limiter using token bucket logic.
6. Process a large file line-by-line and aggregate counts safely.
7. Compare `ConcurrentHashMap`, synchronized `HashMap`, and `Hashtable`.
8. Explain how you would profile and fix high GC pauses.

## Notes To Add After Solving

For every new problem, add:

- **Concept tested:** collection, stream, concurrency, JVM, SQL, etc.
- **Common mistake:** null handling, duplicate keys, race condition, wrong collector.
- **Complexity:** time and space.
- **Interview explanation:** two or three sentences you can say aloud.
