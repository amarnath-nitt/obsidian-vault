# Java and SQL Interview Quick Reference

Use this for rapid recall, not as a substitute for explaining runtime behavior and trade-offs. The syntax is durable across modern Java; for version-sensitive guidance, see [Current Java and Spring Backend Standards](Current-Java-and-Spring-Backend-Standards.md).

## Stream API Quick Reference

### Creating Streams

For every common standard-library stream source—including `char[]`, primitive arrays, files, readers, `Optional`, ranges, regular expressions, and custom `Spliterator` sources—see [Java Stream Creation Guide](Java-Stream-Creation-Guide.md).

```java
Stream.of(1, 2, 3)
Arrays.stream(array)
collection.stream()
collection.parallelStream()
Stream.empty()
Stream.generate(() -> Math.random())
Stream.iterate(0, n -> n + 1)
```

### Intermediate Operations (Lazy)
```java
.filter(predicate)           // Filter elements
.map(function)               // Transform elements
.flatMap(function)           // Flatten nested structures
.distinct()                  // Remove duplicates
.sorted()                    // Sort naturally
.sorted(comparator)          // Sort with comparator
.peek(consumer)              // Debug/side effects
.limit(n)                    // Take first n elements
.skip(n)                     // Skip first n elements
```

### Terminal Operations (Eager)
```java
.collect(collector)          // Collect to collection
.forEach(consumer)           // Iterate
.forEachOrdered(consumer)    // Iterate in order
.reduce(accumulator)         // Reduce to single value
.count()                     // Count elements
.anyMatch(predicate)         // Any element matches
.allMatch(predicate)         // All elements match
.noneMatch(predicate)        // No element matches
.findFirst()                 // First element (Optional)
.findAny()                   // Any element (Optional)
.min(comparator)             // Minimum element
.max(comparator)             // Maximum element
.toArray()                   // Convert to array
```

---

## Common Collectors

```java
// To Collection
Collectors.toList()
Collectors.toSet()
Collectors.toCollection(ArrayList::new)

// To Map
Collectors.toMap(keyMapper, valueMapper)
Collectors.toMap(k -> k, v -> v, mergeFunction)

// Joining Strings
Collectors.joining()
Collectors.joining(", ")
Collectors.joining(", ", "[", "]")

// Grouping
Collectors.groupingBy(classifier)
Collectors.groupingBy(classifier, downstream)
Collectors.partitioningBy(predicate)

// Aggregations
Collectors.counting()
Collectors.summingInt(mapper)
Collectors.averagingInt(mapper)
Collectors.summarizingInt(mapper)

// Min/Max
Collectors.maxBy(comparator)
Collectors.minBy(comparator)

// Mapping
Collectors.mapping(mapper, downstream)

// Teeing (Java 12+)
Collectors.teeing(collector1, collector2, merger)
```

---

## Lambda Syntax Patterns

```java
// No parameters
() -> expression
() -> { statements; }

// One parameter
x -> expression
x -> { statements; }
(x) -> expression

// Multiple parameters
(x, y) -> expression
(x, y) -> { statements; return value; }

// With types
(Integer x, Integer y) -> x + y
```

---

## Method Reference Types

```java
// Static method
ClassName::staticMethod
Integer::parseInt

// Instance method on object
object::instanceMethod
str::toUpperCase

// Instance method on arbitrary object
ClassName::instanceMethod
String::length

// Constructor
ClassName::new
ArrayList::new
```

---

## Functional Interfaces

```java
// Predicate<T> - T -> boolean
Predicate<String> isEmpty = String::isEmpty;

// Function<T, R> - T -> R
Function<String, Integer> length = String::length;

// Consumer<T> - T -> void
Consumer<String> print = System.out::println;

// Supplier<T> - () -> T
Supplier<Double> random = Math::random;

// BiFunction<T, U, R> - (T, U) -> R
BiFunction<Integer, Integer, Integer> add = Integer::sum;

// BiPredicate<T, U> - (T, U) -> boolean
BiPredicate<String, String> equals = String::equals;

// BiConsumer<T, U> - (T, U) -> void
BiConsumer<String, Integer> map = map::put;

// UnaryOperator<T> - T -> T
UnaryOperator<Integer> square = x -> x * x;

// BinaryOperator<T> - (T, T) -> T
BinaryOperator<Integer> sum = Integer::sum;
```

---

## Optional Methods

```java
Optional.of(value)              // Non-null value
Optional.ofNullable(value)      // Nullable value
Optional.empty()                // Empty Optional

.isPresent()                    // Has value?
.isEmpty()                      // Empty? (Java 11+)
.get()                          // Get value (throws if empty)
.orElse(defaultValue)           // Default if empty
.orElseGet(supplier)            // Lazy default
.orElseThrow()                  // Throw if empty
.orElseThrow(exceptionSupplier) // Custom exception
.ifPresent(consumer)            // Execute if present
.ifPresentOrElse(consumer, runnable) // Java 9+
.filter(predicate)              // Filter value
.map(function)                  // Transform value
.flatMap(function)              // Transform to Optional
```

---

## Comparator Utilities

```java
// Natural order
Comparator.naturalOrder()
Comparator.reverseOrder()

// Comparing
Comparator.comparing(keyExtractor)
Comparator.comparing(keyExtractor, comparator)
Comparator.comparingInt(keyExtractor)
Comparator.comparingLong(keyExtractor)
Comparator.comparingDouble(keyExtractor)

// Chaining
comparator.thenComparing(keyExtractor)
comparator.thenComparingInt(keyExtractor)
comparator.reversed()

// Nulls handling
Comparator.nullsFirst(comparator)
Comparator.nullsLast(comparator)

// Example
Comparator.comparing(Person::getLastName)
          .thenComparing(Person::getFirstName)
```

---

## Collection Hierarchy

```
Collection
├── List (ordered, allows duplicates)
│   ├── ArrayList (resizable array)
│   ├── LinkedList (doubly-linked list)
│   └── Vector (synchronized ArrayList)
├── Set (no duplicates)
│   ├── HashSet (hash table, no order)
│   ├── LinkedHashSet (insertion order)
│   └── TreeSet (sorted, red-black tree)
└── Queue (FIFO/priority)
    ├── PriorityQueue (heap)
    └── ArrayDeque (double-ended queue)

Map (key-value pairs)
├── HashMap (hash table, no order)
├── LinkedHashMap (insertion order)
├── TreeMap (sorted keys)
└── Hashtable (legacy, synchronized)
```

---

## Exception Hierarchy

```
Throwable
├── Error (system errors, don't catch)
│   ├── OutOfMemoryError
│   ├── StackOverflowError
│   └── VirtualMachineError
└── Exception
    ├── RuntimeException (unchecked)
    │   ├── NullPointerException
    │   ├── ArrayIndexOutOfBoundsException
    │   ├── IllegalArgumentException
    │   ├── ArithmeticException
    │   └── ClassCastException
    └── Checked Exceptions
        ├── IOException
        ├── SQLException
        └── ClassNotFoundException
```

---

## Key Differences

### ArrayList vs LinkedList
- **ArrayList**: Fast random access (O(1)), slow insertion/deletion in middle (O(n))
- **LinkedList**: Slow random access (O(n)), fast insertion/deletion (O(1))

### HashMap vs TreeMap vs LinkedHashMap
- **HashMap**: No order, O(1) operations
- **TreeMap**: Sorted by keys, O(log n) operations
- **LinkedHashMap**: Insertion order, O(1) operations

### HashSet vs TreeSet
- **HashSet**: No order, O(1) add/remove/contains
- **TreeSet**: Sorted, O(log n) operations

### == vs .equals()
- **==**: Reference equality (memory address)
- **.equals()**: Value equality (content)

### String vs StringBuilder vs StringBuffer
- **String**: Immutable, thread-safe
- **StringBuilder**: Mutable, not thread-safe, fast
- **StringBuffer**: Mutable, thread-safe, slower

### Checked vs Unchecked Exceptions
- **Checked**: Must handle, compile-time check
- **Unchecked**: Optional handling, runtime exception

### Comparable vs Comparator
- **Comparable**: Natural ordering, implement in class
- **Comparator**: Custom ordering, separate class

---

## SQL Query Patterns

### Basic Query Structure
```sql
SELECT [columns]
FROM [table]
WHERE [conditions]
GROUP BY [columns]
HAVING [group conditions]
ORDER BY [columns] [ASC|DESC]
LIMIT [number];
```

### Common Patterns

**Find Duplicates:**
```sql
SELECT column, COUNT(*)
FROM table
GROUP BY column
HAVING COUNT(*) > 1;
```

**Nth Highest Value:**
```sql
SELECT DISTINCT column
FROM table
ORDER BY column DESC
LIMIT 1 OFFSET n-1;
```

**Delete Duplicates:**
```sql
DELETE FROM table
WHERE id NOT IN (
    SELECT MIN(id)
    FROM table
    GROUP BY unique_column
);
```

**Running Total:**
```sql
SELECT 
    date,
    amount,
    SUM(amount) OVER (ORDER BY date) as running_total
FROM table;
```

**Rank:**
```sql
SELECT 
    name,
    value,
    RANK() OVER (ORDER BY value DESC) as rank
FROM table;
```

---

## SQL JOINs Visual

```
INNER JOIN:     ∩       Only matching rows
LEFT JOIN:      ⊂       All left + matching right
RIGHT JOIN:     ⊃       All right + matching left
FULL JOIN:      ∪       All from both
```

---

## Window Functions

```sql
-- Ranking
ROW_NUMBER() OVER (ORDER BY col)
RANK() OVER (ORDER BY col)
DENSE_RANK() OVER (ORDER BY col)
NTILE(n) OVER (ORDER BY col)

-- Aggregate
SUM(col) OVER (PARTITION BY col ORDER BY col)
AVG(col) OVER (PARTITION BY col)
COUNT(*) OVER (PARTITION BY col)
MIN(col) OVER (PARTITION BY col)
MAX(col) OVER (PARTITION BY col)

-- Navigation
LAG(col, offset) OVER (ORDER BY col)
LEAD(col, offset) OVER (ORDER BY col)
FIRST_VALUE(col) OVER (ORDER BY col)
LAST_VALUE(col) OVER (ORDER BY col)
```

---

## Date/Time (Java 8+)

```java
LocalDate.now()
LocalDate.of(2024, 1, 15)
LocalDate.parse("2024-01-15")

LocalTime.now()
LocalTime.of(14, 30)

LocalDateTime.now()
LocalDateTime.of(2024, 1, 15, 14, 30)

ZonedDateTime.now(ZoneId.of("America/New_York"))

// Formatting
DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss")
dateTime.format(formatter)
LocalDateTime.parse(string, formatter)

// Operations
date.plusDays(1)
date.minusMonths(2)
date.withYear(2025)

// Period & Duration
Period.between(date1, date2)
Duration.between(time1, time2)
```

---

## Performance Tips

**Java:**
- Use `StringBuilder` for string concatenation in loops
- Use primitive streams (`IntStream`, `LongStream`) for better performance
- Prefer `ArrayList` over `LinkedList` for most cases
- Use parallel streams only for large datasets and CPU-intensive tasks
- Cache `hashCode()` in immutable objects
- Use `EnumSet` instead of `HashSet` for enums

**SQL:**
- Create indexes on frequently queried columns
- Avoid `SELECT *`, specify needed columns
- Use `EXISTS` instead of `IN` for subqueries
- Use joins instead of subqueries when possible
- Avoid functions on indexed columns in WHERE
- Use LIMIT to restrict large result sets

---

## Interview Pro Tips

✅ **Explain your thought process** out loud  
✅ **Ask clarifying questions** before coding  
✅ **Consider edge cases** (null, empty, duplicates)  
✅ **Discuss time/space complexity**  
✅ **Test your code** mentally or on paper  
✅ **Know when to stop** optimizing  
✅ **Be honest** about what you don't know
