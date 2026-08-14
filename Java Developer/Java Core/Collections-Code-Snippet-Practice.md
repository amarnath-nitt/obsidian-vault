# Collections — Code Snippet Practice

Practice these "What does this code print?" questions for Java Collections. Attempt each snippet before revealing the answer.

Related theory: [Core Java Interview Questions](Java Core/Core-Java-Interview-Questions.mdCore-Java-Interview-Questions.md)

---

## Snippet 1 — ConcurrentModificationException 🟢

**What happens when this code runs?**

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>(Arrays.asList("A", "B", "C", "D"));

        for (String item : list) {
            if (item.equals("B")) {
                list.remove(item);
            }
        }
        System.out.println(list);
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Exception in thread "main" java.util.ConcurrentModificationException
```

**Explanation:**
- The enhanced for-loop uses an `Iterator` internally.
- Calling `list.remove()` directly (not through the iterator) modifies the list structurally during iteration.
- The iterator detects this via `modCount` mismatch and throws `ConcurrentModificationException`.
- **Fix — use Iterator.remove():**
```java
Iterator<String> it = list.iterator();
while (it.hasNext()) {
    if (it.next().equals("B")) {
        it.remove();  // safe removal via iterator
    }
}
```
- **Fix — Java 8+:**
```java
list.removeIf(item -> item.equals("B"));
```

**Interview Tip:** "Never modify a collection directly during enhanced for-loop iteration. Use `Iterator.remove()` or `removeIf()`. This is a fail-fast behavior."

</details>

---

## Snippet 2 — HashMap With Mutable Key 🔴

**What does this code print?**

```java
import java.util.*;

class Key {
    int id;

    Key(int id) { this.id = id; }

    @Override
    public int hashCode() { return id; }

    @Override
    public boolean equals(Object o) {
        return o instanceof Key && ((Key) o).id == this.id;
    }
}

public class Main {
    public static void main(String[] args) {
        Map<Key, String> map = new HashMap<>();
        Key key = new Key(1);
        map.put(key, "Hello");

        System.out.println(map.get(key));

        key.id = 2;  // mutate the key

        System.out.println(map.get(key));
        System.out.println(map.containsKey(key));
        System.out.println(map.size());
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Hello
null
false
1
```

**Explanation:**
- Initially `key.id = 1`, hashCode is `1`, entry is stored in bucket for hash `1`.
- After `key.id = 2`, hashCode becomes `2`. `map.get(key)` looks in bucket for hash `2` — the entry is in bucket `1`, so it's not found → `null`.
- `containsKey(key)` also fails for the same reason → `false`.
- The entry still exists (`size()` is `1`), but it's **orphaned** — unreachable by normal lookup.
- **Lesson:** Never use mutable objects as `HashMap` keys. Use immutable types like `String`, `Integer`, or properly immutable custom classes.

**Interview Tip:** "Mutating a HashMap key after insertion breaks the hash-based lookup. The entry becomes unreachable. Always use immutable keys."

</details>

---

## Snippet 3 — equals Without hashCode in HashSet 🟡

**What does this code print?**

```java
import java.util.*;

class Product {
    String name;

    Product(String name) { this.name = name; }

    @Override
    public boolean equals(Object o) {
        return o instanceof Product && ((Product) o).name.equals(this.name);
    }

    // hashCode() NOT overridden
}

public class Main {
    public static void main(String[] args) {
        Set<Product> set = new HashSet<>();
        set.add(new Product("Laptop"));
        set.add(new Product("Laptop"));

        System.out.println(set.size());
        System.out.println(set.contains(new Product("Laptop")));
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
2
false
```

**Explanation:**
- `equals()` is overridden to compare by name, but `hashCode()` is NOT overridden.
- Default `hashCode()` from `Object` returns different values for different object instances.
- `HashSet` (backed by `HashMap`) checks `hashCode()` first to find the bucket.
- Two `new Product("Laptop")` instances get different hash codes → different buckets → both are added → `size() = 2`.
- `contains(new Product("Laptop"))` creates yet another instance with a different hash code → bucket miss → `false`.
- **Rule:** If `a.equals(b)` is `true`, then `a.hashCode()` MUST equal `b.hashCode()`.

**Interview Tip:** "Always override `hashCode()` when you override `equals()`. Hash-based collections use `hashCode()` first; if hashes differ, `equals()` is never checked."

</details>

---

## Snippet 4 — List.of() vs Arrays.asList() Mutability 🟡

**What happens when this code runs?**

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Scenario 1
        List<String> list1 = Arrays.asList("A", "B", "C");
        list1.set(0, "X");
        System.out.println("list1: " + list1);

        try {
            list1.add("D");
        } catch (UnsupportedOperationException e) {
            System.out.println("list1 add failed");
        }

        // Scenario 2
        List<String> list2 = List.of("A", "B", "C");
        try {
            list2.set(0, "X");
        } catch (UnsupportedOperationException e) {
            System.out.println("list2 set failed");
        }
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
list1: [X, B, C]
list1 add failed
list2 set failed
```

**Explanation:**
- `Arrays.asList()` returns a **fixed-size** list backed by the array:
  - `set()` works (modifies existing elements) ✓
  - `add()`/`remove()` fail with `UnsupportedOperationException` (can't change size) ✗
- `List.of()` (Java 9+) returns a **fully immutable** list:
  - `set()`, `add()`, `remove()` all fail with `UnsupportedOperationException` ✗
  - Also rejects `null` elements.

| Method | Set Elements | Add/Remove | Null Values |
|---|---|---|---|
| `Arrays.asList()` | ✓ | ✗ | ✓ |
| `List.of()` | ✗ | ✗ | ✗ |
| `new ArrayList<>(List.of(...))` | ✓ | ✓ | ✓ |

**Interview Tip:** "`Arrays.asList()` is fixed-size but element-mutable. `List.of()` is fully immutable. Wrap in `new ArrayList<>()` if you need a mutable list."

</details>

---

## Snippet 5 — TreeSet With Non-Comparable Objects 🟡

**What happens when this code runs?**

```java
import java.util.*;

class Student {
    String name;
    Student(String name) { this.name = name; }
}

public class Main {
    public static void main(String[] args) {
        Set<Student> set = new TreeSet<>();
        set.add(new Student("Alice"));
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Exception in thread "main" java.lang.ClassCastException:
Student cannot be cast to java.lang.Comparable
```

**Explanation:**
- `TreeSet` maintains sorted order. It needs to compare elements.
- `Student` does not implement `Comparable` and no `Comparator` was provided to the `TreeSet` constructor.
- When `add()` is called, `TreeSet` tries to cast `Student` to `Comparable` → `ClassCastException`.
- Note: The first `add()` itself fails (even though comparison is normally needed only from the second element, `TreeSet` still casts on the first insert).
- **Fix 1:** Implement `Comparable<Student>`:
```java
class Student implements Comparable<Student> {
    public int compareTo(Student other) {
        return this.name.compareTo(other.name);
    }
}
```
- **Fix 2:** Pass a `Comparator` to the constructor:
```java
Set<Student> set = new TreeSet<>(Comparator.comparing(s -> s.name));
```

**Interview Tip:** "`TreeSet` requires either `Comparable` elements or a `Comparator` in the constructor. Without either, you get `ClassCastException`."

</details>

---

## Snippet 6 — Collections.unmodifiableList Trap 🟡

**What does this code print?**

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<String> original = new ArrayList<>(Arrays.asList("A", "B", "C"));
        List<String> unmodifiable = Collections.unmodifiableList(original);

        System.out.println(unmodifiable);

        original.add("D");
        System.out.println(unmodifiable);
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
[A, B, C]
[A, B, C, D]
```

**Explanation:**
- `Collections.unmodifiableList()` returns a **read-only view** of the original list — NOT a copy.
- You cannot call `add()`, `remove()`, `set()` on the unmodifiable view.
- BUT if the **original** list is modified, the view reflects those changes.
- This is a common source of bugs when trying to create defensive copies.
- **True immutable copy:** `List.copyOf(original)` (Java 10+) or `new ArrayList<>(original)` wrapped in `Collections.unmodifiableList()`.

**Common wrong answer:** "[A, B, C]" for the second print — assuming unmodifiable means independent.

**Interview Tip:** "`Collections.unmodifiableList()` is a read-only view, not a copy. The original can still be mutated. Use `List.copyOf()` for a truly independent immutable copy."

</details>

---

## Snippet 7 — LinkedHashMap Access-Order Mode 🔴

**What does this code print?**

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Map<String, Integer> map = new LinkedHashMap<>(16, 0.75f, true);
        map.put("A", 1);
        map.put("B", 2);
        map.put("C", 3);

        map.get("A");
        map.get("B");

        System.out.println(map.keySet());
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
[C, A, B]
```

**Explanation:**
- The third constructor parameter `true` enables **access-order** mode (instead of default insertion-order).
- In access-order mode, every `get()` or `put()` moves the entry to the **end** of the linked list.
- Initial insertion order: `A, B, C`.
- `get("A")` moves A to end: `B, C, A`.
- `get("B")` moves B to end: `C, A, B`.
- This behavior is the foundation for **LRU cache** implementations:

```java
Map<String, Integer> lruCache = new LinkedHashMap<>(16, 0.75f, true) {
    @Override
    protected boolean removeEldestEntry(Map.Entry<String, Integer> eldest) {
        return size() > MAX_SIZE;
    }
};
```

**Interview Tip:** "`LinkedHashMap` with access-order mode is the simplest LRU cache in Java. Override `removeEldestEntry()` to auto-evict."

</details>

---

## Snippet 8 — PriorityQueue Natural Order 🟡

**What does this code print?**

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.add(30);
        pq.add(10);
        pq.add(20);

        System.out.println(pq);

        while (!pq.isEmpty()) {
            System.out.print(pq.poll() + " ");
        }
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
[10, 30, 20]
10 20 30
```

**Explanation:**
- `PriorityQueue` is a **min-heap** by default (natural ordering).
- `toString()` / `println(pq)` shows the **internal array representation** — this is NOT sorted order. The heap only guarantees the root (index 0) is the minimum.
- `poll()` extracts elements in **priority order** (ascending for natural ordering): `10, 20, 30`.
- If you want max-heap: `new PriorityQueue<>(Comparator.reverseOrder())`.

**Common wrong answer:** "[10, 20, 30]" for the print — the internal array is a heap structure, not sorted.

**Interview Tip:** "`PriorityQueue.toString()` does NOT show sorted order — it shows the heap array. Only `poll()` guarantees priority ordering."

</details>

---

## Snippet 9 — HashMap Iteration Order 🟢

**Is the output guaranteed?**

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Map<String, Integer> map = new HashMap<>();
        map.put("Apple", 1);
        map.put("Banana", 2);
        map.put("Cherry", 3);

        for (String key : map.keySet()) {
            System.out.print(key + " ");
        }
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Order is NOT guaranteed. Could be any permutation like:
Apple Banana Cherry
or
Banana Cherry Apple
or any other order
```

**Explanation:**
- `HashMap` does NOT guarantee iteration order. The order depends on hash codes and internal bucket structure.
- The order can even change between JVM runs or after rehashing (when the map grows).
- If you need **insertion order**: use `LinkedHashMap`.
- If you need **sorted order**: use `TreeMap`.

| Map Type | Iteration Order |
|---|---|
| `HashMap` | No guarantee |
| `LinkedHashMap` | Insertion order (or access order) |
| `TreeMap` | Sorted key order |

**Interview Tip:** "Never rely on `HashMap` iteration order. Use `LinkedHashMap` for insertion order or `TreeMap` for sorted order."

</details>

---

## Snippet 10 — ConcurrentHashMap Does Not Allow Null 🟢

**What happens when this code runs?**

```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        ConcurrentHashMap<String, String> map = new ConcurrentHashMap<>();
        map.put("key1", "value1");

        try {
            map.put("key2", null);
        } catch (NullPointerException e) {
            System.out.println("Null value not allowed");
        }

        try {
            map.put(null, "value2");
        } catch (NullPointerException e) {
            System.out.println("Null key not allowed");
        }

        System.out.println("Size: " + map.size());
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Null value not allowed
Null key not allowed
Size: 1
```

**Explanation:**
- `ConcurrentHashMap` does NOT allow `null` keys or `null` values — both throw `NullPointerException`.
- This is by design: in concurrent environments, `null` creates ambiguity. If `map.get(key)` returns `null`, you can't tell if the key maps to `null` or if the key is absent.
- `HashMap` allows one `null` key and multiple `null` values.
- `Hashtable` also disallows `null` keys and values.

| Map Type | Null Key | Null Value |
|---|---|---|
| `HashMap` | 1 allowed | Multiple allowed |
| `ConcurrentHashMap` | Not allowed | Not allowed |
| `Hashtable` | Not allowed | Not allowed |
| `TreeMap` | Not allowed | Allowed |

**Interview Tip:** "`ConcurrentHashMap` rejects nulls to avoid ambiguity in concurrent `get()`. If `null` were allowed, `containsKey()` would need an extra check, hurting performance."

</details>

---

## Quick Review Table

| # | Concept Tested | Key Rule |
|---|---|---|
| 1 | ConcurrentModificationException | Don't modify collection during enhanced for-loop |
| 2 | Mutable HashMap key | Mutating a key orphans the entry |
| 3 | equals without hashCode | Hash-based collections won't find the entry |
| 4 | List.of vs Arrays.asList | Fixed-size mutable vs fully immutable |
| 5 | TreeSet without Comparable | ClassCastException on add |
| 6 | unmodifiableList view | View reflects mutations on original |
| 7 | LinkedHashMap access-order | LRU cache foundation via access-order mode |
| 8 | PriorityQueue toString | Heap array ≠ sorted order |
| 9 | HashMap iteration order | Never guaranteed |
| 10 | ConcurrentHashMap null | Rejects null keys and values |
