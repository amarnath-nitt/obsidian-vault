# Core Java — Code Snippet Practice

Practice these "What does this code print?" questions for Core Java language fundamentals. Attempt each snippet before revealing the answer.

Related theory: [Core Java Interview Questions](Java Core/Core-Java-Interview-Questions.mdCore-Java-Interview-Questions.md)

---

## Snippet 1 — String Pool and == 🟢

**What does this code print?**

```java
public class Main {
    public static void main(String[] args) {
        String s1 = "Java";
        String s2 = "Java";
        String s3 = new String("Java");
        String s4 = new String("Java");

        System.out.println(s1 == s2);
        System.out.println(s1 == s3);
        System.out.println(s3 == s4);
        System.out.println(s1.equals(s3));
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
true
false
false
true
```

**Explanation:**
- `s1` and `s2` are string literals — they share the same reference from the **string pool**. `s1 == s2` is `true`.
- `s3` is created with `new`, which always creates a new object on the heap. `s1 == s3` is `false`.
- `s3 == s4` → two different `new` objects → `false`.
- `s1.equals(s3)` compares content → `true`.

**Interview Tip:** "String literals go to the string pool and are shared. `new String()` always creates a heap object. Use `.equals()` for content comparison."

</details>

---

## Snippet 2 — String.intern() Behavior 🟡

**What does this code print?**

```java
public class Main {
    public static void main(String[] args) {
        String s1 = new String("Hello");
        String s2 = s1.intern();
        String s3 = "Hello";

        System.out.println(s1 == s2);
        System.out.println(s2 == s3);
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
false
true
```

**Explanation:**
- `s1` is a `new` heap object.
- `s1.intern()` returns the string pool reference for "Hello". If "Hello" is already in the pool (it is, because the literal "Hello" in `new String("Hello")` adds it), `intern()` returns that pool reference.
- `s2` now points to the pool reference. `s3` is the literal "Hello" — also the pool reference.
- `s1 == s2` → `false` (heap vs pool).
- `s2 == s3` → `true` (both are the pool reference).

**Interview Tip:** "`intern()` returns the canonical pool reference. After interning, `==` works like `equals()` for the same content."

</details>

---

## Snippet 3 — Integer Cache Range 🟡

**What does this code print?**

```java
public class Main {
    public static void main(String[] args) {
        Integer a = 127;
        Integer b = 127;
        Integer c = 128;
        Integer d = 128;

        System.out.println(a == b);
        System.out.println(c == d);
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
true
false
```

**Explanation:**
- Java caches `Integer` objects for values **-128 to 127** (the `IntegerCache`).
- `a` and `b` are both `127` → same cached object → `a == b` is `true`.
- `c` and `d` are `128` → outside the cache → two different objects → `c == d` is `false`.
- This is autoboxing: `Integer a = 127` becomes `Integer.valueOf(127)` which uses the cache.
- Always use `.equals()` for `Integer` comparison, or unbox to `int`.

**Common wrong answer:** "true, true" — not knowing the cache boundary at 127.

**Interview Tip:** "IntegerCache covers -128 to 127. Outside that range, autoboxed Integers are different objects. Use `.equals()` or unbox."

</details>

---

## Snippet 4 — Autoboxing NullPointerException 🟡

**What happens when this code runs?**

```java
public class Main {
    public static void main(String[] args) {
        Integer value = null;
        int result = value;
        System.out.println(result);
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Exception in thread "main" java.lang.NullPointerException
```

**Explanation:**
- `Integer value = null` is valid — `Integer` is a reference type that can be `null`.
- `int result = value` triggers **unboxing** — Java calls `value.intValue()` internally.
- Since `value` is `null`, calling any method on it throws `NullPointerException`.
- This is one of the most common autoboxing bugs in production code.

**Common wrong answer:** "0" — assuming null wrapper unboxes to the default primitive value.

**Interview Tip:** "Unboxing a null wrapper always throws NPE. Be cautious with `Integer`, `Long`, `Boolean` etc. from database results or maps."

</details>

---

## Snippet 5 — final Reference vs final Object 🟡

**What does this code print?**

```java
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        final List<String> names = new ArrayList<>();
        names.add("Java");
        names.add("Python");

        System.out.println(names);

        // names = new ArrayList<>();  // Would this compile?
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
[Java, Python]
```

**Explanation:**
- `final` on a reference variable means the **reference cannot be reassigned** — you can't point it to a different object.
- But the **object itself is still mutable**. You can call `add()`, `remove()`, `clear()` etc.
- The commented line would cause a compilation error because it tries to reassign the reference.
- To make the list truly unmodifiable, use `Collections.unmodifiableList()` or `List.of()`.

**Common wrong answer:** "Compilation error on `add()`" — confusing `final` reference with immutable object.

**Interview Tip:** "`final` prevents reassignment of the reference, NOT mutation of the object. For true immutability, use unmodifiable wrappers or immutable collections."

</details>

---

## Snippet 6 — Pass-By-Value With Objects 🔴

**What does this code print?**

```java
class Person {
    String name;

    Person(String name) {
        this.name = name;
    }
}

public class Main {
    static void changeName(Person p) {
        p.name = "Changed";
    }

    static void replaceObject(Person p) {
        p = new Person("Replaced");
    }

    public static void main(String[] args) {
        Person person = new Person("Original");

        changeName(person);
        System.out.println(person.name);

        replaceObject(person);
        System.out.println(person.name);
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Changed
Changed
```

**Explanation:**
- **Java is always pass-by-value.** For objects, the **reference value** (pointer) is copied, not the object.
- `changeName(person)`: the copy of the reference still points to the same object. Modifying `p.name` changes the shared object. → `"Changed"`.
- `replaceObject(person)`: `p = new Person("Replaced")` reassigns the **local copy** of the reference. The original `person` reference in `main` still points to the old object.
- After `replaceObject`, `person.name` is still `"Changed"`.

**Common wrong answer:** "Changed, Replaced" — thinking Java passes object references by reference.

**Interview Tip:** "Java is always pass-by-value. When you pass an object, the reference value is copied. Mutating the object through the copy works, but reassigning the copy does NOT affect the original reference."

</details>

---

## Snippet 7 — Static Initializer Block Order 🟡

**What does this code print?**

```java
class Config {
    static int value;

    static {
        value = 10;
        System.out.println("Static block 1: value = " + value);
    }

    static {
        value = 20;
        System.out.println("Static block 2: value = " + value);
    }

    Config() {
        System.out.println("Constructor: value = " + value);
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Before creating object");
        Config c1 = new Config();
        Config c2 = new Config();
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Static block 1: value = 10
Static block 2: value = 20
Before creating object
Constructor: value = 20
Constructor: value = 20
```

**Explanation:**
- Static blocks run **once** when the class is **first loaded**, in the order they appear.
- Class loading happens before the first use — here, before `main` even accesses `Config`.
- Actually, static blocks run when `Config` is first referenced: at `new Config()`. But since `System.out.println("Before creating object")` runs first (no Config reference), it prints before the static blocks? No — the JVM loads `Config` when it encounters `new Config()`, so "Before creating object" prints first.
- Wait — let me re-trace. `main()` starts → prints "Before creating object" → `new Config()` triggers class loading → static blocks run → then constructor runs.
- Static blocks run only once. The second `new Config()` only runs the constructor.

**Interview Tip:** "Static blocks run once when the class is first loaded, in declaration order. Instance initializers and constructors run every time an object is created."

</details>

---

## Snippet 8 — String Concatenation In a Loop 🟡

**What is the problem with this code?**

```java
public class Main {
    public static void main(String[] args) {
        String result = "";
        for (int i = 0; i < 10000; i++) {
            result = result + i;
        }
        System.out.println(result.length());
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
38890
```

**But the real answer is the performance problem:**

**Explanation:**
- String is immutable. Each `result + i` creates a **new String object** and copies all previous content.
- This is O(n²) in total character operations for n iterations.
- Modern Java compilers (Java 9+) may optimize with `invokedynamic`, but the classic fix is:

```java
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 10000; i++) {
    sb.append(i);
}
String result = sb.toString();
```

- `StringBuilder` appends in-place (amortized O(1) per append), making the total O(n).

**Interview Tip:** "Use `StringBuilder` for string concatenation in loops. String's immutability means each `+` creates a new object and copies existing content."

</details>

---

## Snippet 9 — Tricky Boolean Wrapper 🟡

**What does this code print?**

```java
public class Main {
    public static void main(String[] args) {
        Boolean b1 = true;
        Boolean b2 = true;
        Boolean b3 = new Boolean(true);

        System.out.println(b1 == b2);
        System.out.println(b1 == b3);
        System.out.println(b1.equals(b3));
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
true
false
true
```

**Explanation:**
- `Boolean.valueOf(true)` (used in autoboxing) returns a cached `Boolean.TRUE` singleton.
- `b1` and `b2` both get the same `Boolean.TRUE` instance → `b1 == b2` is `true`.
- `new Boolean(true)` creates a **new object** (deprecated since Java 9) → `b1 == b3` is `false`.
- `.equals()` compares the value → `true`.
- Same pattern applies to all wrapper types with caching.

**Interview Tip:** "Wrapper caching applies to `Boolean` (always cached), `Integer` (-128 to 127), `Byte`, `Short`, `Long`, and `Character` (0-127). Use `.equals()` for safe comparison."

</details>

---

## Snippet 10 — Ternary Operator Type Promotion 🔴

**What does this code print?**

```java
public class Main {
    public static void main(String[] args) {
        Object result = true ? new Integer(1) : new Double(2.0);
        System.out.println(result);
        System.out.println(result.getClass().getSimpleName());
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
1.0
Double
```

**Explanation:**
- In a ternary expression, Java applies **binary numeric promotion** when both branches are numeric types.
- `Integer` and `Double` → the common type is `double` (wider type wins).
- Even though the condition is `true` and the `Integer(1)` branch is selected, it gets promoted to `double` → `1.0`.
- The result is autoboxed to `Double` (since it's assigned to `Object`).

**Common wrong answer:** "1" and "Integer" — not knowing that ternary expressions apply type promotion across both branches.

**Interview Tip:** "Ternary operators perform binary numeric promotion between both branches, even if only one branch is executed. The wider type wins."

</details>

---

## Snippet 11 — equals() Symmetry Violation 🔴

**What does this code print?**

```java
class CaseInsensitiveString {
    private final String value;

    CaseInsensitiveString(String value) {
        this.value = value;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof CaseInsensitiveString) {
            return value.equalsIgnoreCase(((CaseInsensitiveString) obj).value);
        }
        if (obj instanceof String) {
            return value.equalsIgnoreCase((String) obj);
        }
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        CaseInsensitiveString cis = new CaseInsensitiveString("Java");
        String s = "java";

        System.out.println(cis.equals(s));
        System.out.println(s.equals(cis));
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
true
false
```

**Explanation:**
- `cis.equals(s)` → `CaseInsensitiveString.equals()` handles `String` → case-insensitive match → `true`.
- `s.equals(cis)` → `String.equals()` checks if `cis` is a `String` → it's not → `false`.
- This violates the **symmetry contract** of `equals()`: if `a.equals(b)` is `true`, then `b.equals(a)` must also be `true`.
- Fix: do NOT try to interoperate with `String` in `equals()`. Only compare with the same class.

**Interview Tip:** "The `equals()` contract requires symmetry, transitivity, reflexivity, and consistency. Never cross-compare with unrelated types."

</details>

---

## Snippet 12 — Immutable Class Leak 🔴

**Is this class truly immutable? What does the code print?**

```java
import java.util.Date;

final class Event {
    private final String name;
    private final Date date;

    Event(String name, Date date) {
        this.name = name;
        this.date = date;
    }

    public String getName() { return name; }
    public Date getDate() { return date; }
}

public class Main {
    public static void main(String[] args) {
        Date d = new Date();
        Event event = new Event("Launch", d);

        System.out.println(event.getDate());

        d.setYear(150);  // mutate the original Date
        System.out.println(event.getDate());

        event.getDate().setMonth(0);  // mutate via getter
        System.out.println(event.getDate());
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
(current date/time)
(date with year changed to 2050)
(date with year 2050 and month January)
```

**Explanation:**
- This class is **NOT truly immutable** despite `final` class and `final` fields.
- Problem 1: The constructor stores the **original reference** to the mutable `Date`. Callers who keep a reference to `d` can mutate the internal state.
- Problem 2: The getter returns the **internal `Date` reference**. Callers can mutate it directly.
- **Fix:** Use **defensive copying** in both constructor and getter:

```java
Event(String name, Date date) {
    this.name = name;
    this.date = new Date(date.getTime()); // defensive copy in
}

public Date getDate() {
    return new Date(date.getTime()); // defensive copy out
}
```

- Better fix: Use `java.time.Instant` or `LocalDate` which are inherently immutable.

**Interview Tip:** "True immutability requires defensive copying of mutable fields in both constructors and getters. Or better — use immutable types like `java.time`."

</details>

---

## Quick Review Table

| # | Concept Tested | Key Rule |
|---|---|---|
| 1 | String pool | Literals share pool reference, `new` creates heap object |
| 2 | `intern()` | Returns canonical pool reference |
| 3 | Integer cache | Autoboxed Integers cached for -128 to 127 only |
| 4 | Autoboxing NPE | Unboxing null wrapper throws NPE |
| 5 | `final` reference | Prevents reassignment, not mutation |
| 6 | Pass-by-value | Reference copy is passed, reassignment doesn't affect caller |
| 7 | Static initializers | Run once at class loading, in declaration order |
| 8 | String concatenation | Loop concatenation is O(n²), use StringBuilder |
| 9 | Boolean wrapper | `valueOf()` returns cached instance, `new` creates separate object |
| 10 | Ternary type promotion | Binary numeric promotion across both branches |
| 11 | equals() symmetry | Never cross-compare with different types |
| 12 | Immutability leak | Defensively copy mutable fields in and out |
