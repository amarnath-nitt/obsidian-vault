# OOPs — Code Snippet Practice

Practice these "What does this code print?" questions to build the mental model interviewers test. Attempt each snippet before revealing the answer.

Related theory: [Core Java Interview Questions](Java Core/Core-Java-Interview-Questions.mdCore-Java-Interview-Questions.md)

---

## Snippet 1 — Constructor Chaining With Inheritance 🟢

**What does this code print?**

```java
class Animal {
    Animal() {
        System.out.println("Animal constructor");
    }
}

class Dog extends Animal {
    Dog() {
        System.out.println("Dog constructor");
    }
}

class Puppy extends Dog {
    Puppy() {
        System.out.println("Puppy constructor");
    }
}

public class Main {
    public static void main(String[] args) {
        Puppy p = new Puppy();
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Animal constructor
Dog constructor
Puppy constructor
```

**Explanation:**
- Java inserts an implicit `super()` call as the first statement of every constructor if no explicit `super()` or `this()` is present.
- Constructor execution goes from the **topmost parent down** to the child: `Animal → Dog → Puppy`.
- This ensures parent state is initialized before child uses it.

**Common wrong answer:** "Puppy constructor" only — forgetting that parent constructors always run first.

**Interview Tip:** "Constructors chain upward via implicit `super()`, so the topmost parent runs first."

</details>

---

## Snippet 2 — Method Overriding With Reference Type 🟡

**What does this code print?**

```java
class Vehicle {
    void start() {
        System.out.println("Vehicle starts");
    }
}

class Car extends Vehicle {
    @Override
    void start() {
        System.out.println("Car starts");
    }
}

public class Main {
    public static void main(String[] args) {
        Vehicle v = new Car();
        v.start();
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Car starts
```

**Explanation:**
- The **reference type** is `Vehicle`, but the **object type** is `Car`.
- Method overriding uses **runtime polymorphism** — the JVM dispatches to the actual object's method, not the reference type's method.
- This is the foundation of polymorphism in Java.

**Common wrong answer:** "Vehicle starts" — confusing compile-time type with runtime dispatch.

**Interview Tip:** "For overridden instance methods, Java always calls the method on the actual object type, not the reference type."

</details>

---

## Snippet 3 — Static Method Hiding (NOT Overriding) 🟡

**What does this code print?**

```java
class Parent {
    static void greet() {
        System.out.println("Hello from Parent");
    }
}

class Child extends Parent {
    static void greet() {
        System.out.println("Hello from Child");
    }
}

public class Main {
    public static void main(String[] args) {
        Parent obj = new Child();
        obj.greet();
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Hello from Parent
```

**Explanation:**
- Static methods are **not overridden** — they are **hidden** (method hiding).
- Static method resolution happens at **compile time** based on the **reference type**, not the object type.
- Since the reference type is `Parent`, `Parent.greet()` is called.
- This is fundamentally different from instance method overriding.

**Common wrong answer:** "Hello from Child" — confusing static method hiding with instance method overriding.

**Interview Tip:** "Static methods bind at compile time to the reference type. Instance methods bind at runtime to the object type. This is method hiding vs overriding."

</details>

---

## Snippet 4 — Overloading Resolution With Inheritance 🟡

**What does this code print?**

```java
class Printer {
    void print(Object obj) {
        System.out.println("Object version");
    }

    void print(String str) {
        System.out.println("String version");
    }
}

public class Main {
    public static void main(String[] args) {
        Printer printer = new Printer();
        printer.print(null);
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
String version
```

**Explanation:**
- When `null` is passed, both `print(Object)` and `print(String)` are valid candidates.
- Java picks the **most specific** overloaded method — `String` is more specific than `Object` because `String extends Object`.
- If two equally specific overloads existed (e.g., `String` and `Integer`), the compiler would report an ambiguity error.

**Common wrong answer:** "Object version" or "Compilation error" — not knowing that Java resolves to the most specific type.

**Interview Tip:** "Overloading is resolved at compile time. Java picks the most specific applicable method."

</details>

---

## Snippet 5 — Constructor With super() And this() 🟡

**What does this code print?**

```java
class Base {
    Base() {
        System.out.println("Base no-arg");
    }

    Base(String name) {
        System.out.println("Base with name: " + name);
    }
}

class Derived extends Base {
    Derived() {
        this("default");
        System.out.println("Derived no-arg");
    }

    Derived(String name) {
        super(name);
        System.out.println("Derived with name: " + name);
    }
}

public class Main {
    public static void main(String[] args) {
        Derived d = new Derived();
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Base with name: default
Derived with name: default
Derived no-arg
```

**Explanation:**
- `new Derived()` calls the no-arg constructor.
- `this("default")` redirects to `Derived(String)`.
- `super(name)` calls `Base(String)` → prints "Base with name: default".
- Then "Derived with name: default" prints.
- Control returns to `Derived()` → prints "Derived no-arg".
- Key rule: `super()` and `this()` must be the first statement in a constructor. You cannot have both.

**Common wrong answer:** Including "Base no-arg" — forgetting that `this()` redirects to the other constructor which calls `super(String)`, not `super()`.

**Interview Tip:** "Either `super()` or `this()` can be the first statement in a constructor, but never both. Trace the chain step by step."

</details>

---

## Snippet 6 — Polymorphism With Fields 🔴

**What does this code print?**

```java
class A {
    int value = 10;

    int getValue() {
        return value;
    }
}

class B extends A {
    int value = 20;

    @Override
    int getValue() {
        return value;
    }
}

public class Main {
    public static void main(String[] args) {
        A obj = new B();
        System.out.println(obj.value);
        System.out.println(obj.getValue());
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
10
20
```

**Explanation:**
- **Fields are NOT polymorphic** in Java. Field access is resolved at compile time based on the **reference type**. `obj.value` → `A.value` → `10`.
- **Methods ARE polymorphic**. `obj.getValue()` dispatches to `B.getValue()` at runtime → returns `B.value` → `20`.
- This is a critical distinction: methods override, fields hide.

**Common wrong answer:** "20, 20" — assuming fields also follow runtime polymorphism like methods.

**Interview Tip:** "Fields are resolved by reference type at compile time. Only instance methods are dispatched polymorphically at runtime."

</details>

---

## Snippet 7 — Abstract Class With Constructor 🟡

**What does this code print?**

```java
abstract class Shape {
    Shape() {
        System.out.println("Shape created");
        draw();
    }

    abstract void draw();
}

class Circle extends Shape {
    private int radius = 5;

    Circle() {
        System.out.println("Circle created, radius = " + radius);
    }

    @Override
    void draw() {
        System.out.println("Drawing circle with radius = " + radius);
    }
}

public class Main {
    public static void main(String[] args) {
        Circle c = new Circle();
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Shape created
Drawing circle with radius = 0
Circle created, radius = 5
```

**Explanation:**
- `Shape()` constructor runs first (parent before child).
- Inside `Shape()`, `draw()` is called — but due to polymorphism, it calls `Circle.draw()`.
- At this point, `Circle`'s instance initializers haven't run yet, so `radius` is still `0` (default int value).
- After `Shape()` completes, `Circle()`'s body runs. By then `radius = 5` is initialized.
- **Key trap:** Calling an overridable method from a constructor is dangerous because the child's state isn't initialized yet.

**Common wrong answer:** "Drawing circle with radius = 5" — forgetting initialization order.

**Interview Tip:** "Never call overridable methods from constructors. The child's fields may not be initialized, leading to unexpected defaults."

</details>

---

## Snippet 8 — Covariant Return Type 🟢

**What does this code print?**

```java
class Animal {
    Animal create() {
        System.out.println("Creating Animal");
        return new Animal();
    }
}

class Dog extends Animal {
    @Override
    Dog create() {
        System.out.println("Creating Dog");
        return new Dog();
    }
}

public class Main {
    public static void main(String[] args) {
        Animal a = new Dog();
        Animal result = a.create();
        System.out.println(result.getClass().getSimpleName());
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Creating Dog
Dog
```

**Explanation:**
- Java allows **covariant return types**: an overriding method can return a subtype of the original return type.
- `Dog.create()` returns `Dog` instead of `Animal` — this is valid because `Dog` IS-A `Animal`.
- Due to runtime polymorphism, `a.create()` calls `Dog.create()`.
- `result.getClass().getSimpleName()` returns `"Dog"` because the actual object is a `Dog`.

**Interview Tip:** "Covariant return types allow the overriding method to return a more specific type. This is valid since Java 5."

</details>

---

## Snippet 9 — Upcasting and Downcasting 🟡

**What happens when this code runs?**

```java
class Animal {
    void eat() {
        System.out.println("Animal eats");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("Dog barks");
    }
}

class Cat extends Animal {
    void meow() {
        System.out.println("Cat meows");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal a = new Dog();     // upcasting
        a.eat();

        Dog d = (Dog) a;          // downcasting
        d.bark();

        Cat c = (Cat) a;          // what happens?
        c.meow();
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Animal eats
Dog barks
Exception in thread "main" java.lang.ClassCastException: Dog cannot be cast to Cat
```

**Explanation:**
- **Upcasting** (`Animal a = new Dog()`) is always safe and implicit.
- **Downcasting** (`Dog d = (Dog) a`) works because `a` actually holds a `Dog` object.
- **Invalid downcast** (`Cat c = (Cat) a`) compiles fine but throws `ClassCastException` at runtime because the actual object is `Dog`, not `Cat`.
- Always use `instanceof` before downcasting to avoid `ClassCastException`.

**Common wrong answer:** "Compilation error on Cat cast" — the compiler only checks if the cast is theoretically possible (both extend Animal), not the actual runtime type.

**Interview Tip:** "Use `instanceof` before downcasting. The compiler allows casts within the same hierarchy, but the JVM throws ClassCastException if the actual type doesn't match."

</details>

---

## Snippet 10 — Interface Default Method Conflict 🟡

**What does this code print?**

```java
interface Flyable {
    default void move() {
        System.out.println("Flying");
    }
}

interface Swimmable {
    default void move() {
        System.out.println("Swimming");
    }
}

class Duck implements Flyable, Swimmable {
    @Override
    public void move() {
        Flyable.super.move();
        System.out.println("and also");
        Swimmable.super.move();
    }
}

public class Main {
    public static void main(String[] args) {
        Duck duck = new Duck();
        duck.move();
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Flying
and also
Swimming
```

**Explanation:**
- When two interfaces provide the same default method, the implementing class **must override** it to resolve the conflict — otherwise it won't compile.
- The class can call a specific interface's default method using `InterfaceName.super.method()`.
- This is Java's solution to the diamond problem with interfaces.

**Common wrong answer:** "Compilation error" — true only if the class does NOT override `move()`. Here it does.

**Interview Tip:** "When default method conflicts occur, the class must explicitly override and can selectively delegate using `InterfaceName.super.method()`."

</details>

---

## Snippet 11 — instanceof With Null And Inheritance 🟢

**What does this code print?**

```java
class Animal {}
class Dog extends Animal {}

public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog();
        Animal animal = null;

        System.out.println(dog instanceof Animal);
        System.out.println(dog instanceof Dog);
        System.out.println(animal instanceof Animal);
        System.out.println(animal instanceof Dog);
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
true
true
false
false
```

**Explanation:**
- `dog instanceof Animal` → `true` because `Dog` IS-A `Animal`.
- `dog instanceof Dog` → `true` obviously.
- `animal instanceof Animal` → `false` because `null` is not an instance of anything.
- `animal instanceof Dog` → `false` — same reason, `null` always returns `false` for `instanceof`.
- **Key rule:** `instanceof` never throws `NullPointerException`. It simply returns `false` for `null`.

**Common wrong answer:** "NullPointerException on `animal instanceof`" — `instanceof` is null-safe.

**Interview Tip:** "`instanceof` returns `false` for `null`, never throws NPE. It's a safe null check pattern."

</details>

---

## Snippet 12 — Overriding equals() Without hashCode() 🔴

**What does this code print?**

```java
import java.util.HashSet;
import java.util.Set;

class Employee {
    private String name;

    Employee(String name) {
        this.name = name;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Employee)) return false;
        return this.name.equals(((Employee) obj).name);
    }

    // hashCode() is NOT overridden
}

public class Main {
    public static void main(String[] args) {
        Set<Employee> set = new HashSet<>();
        set.add(new Employee("Asha"));
        set.add(new Employee("Asha"));

        System.out.println(set.size());
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
2
```

**Explanation:**
- Even though both employees are logically equal (same name, `equals()` returns `true`), `hashCode()` is not overridden.
- `HashSet` uses `hashCode()` first to find the bucket. Since `hashCode()` is inherited from `Object`, each `new Employee(...)` gets a different hash based on memory address.
- They land in different buckets, so `equals()` is never even called.
- **Contract violation:** If `a.equals(b)` is `true`, then `a.hashCode()` must equal `b.hashCode()`.

**Common wrong answer:** "1" — assuming `equals()` alone is enough for `HashSet` deduplication.

**Interview Tip:** "Always override `hashCode()` when you override `equals()`. Hash-based collections check `hashCode()` first, and if the hashes differ, `equals()` is never called."

</details>

---

## Snippet 13 — final Method Cannot Be Overridden 🟢

**Will this code compile?**

```java
class Base {
    final void show() {
        System.out.println("Base show");
    }
}

class Derived extends Base {
    void show() {
        System.out.println("Derived show");
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Compilation Error: Cannot override the final method from Base
```

**Explanation:**
- A `final` method cannot be overridden by any subclass.
- This is used when a class wants to guarantee that specific behavior cannot be changed by subclasses.
- Common examples: `Object.getClass()` is `final`.
- Note: `final` on a class prevents inheritance entirely. `final` on a method prevents overriding but allows inheritance.

**Interview Tip:** "`final` methods prevent overriding, `final` classes prevent inheritance, and `final` variables prevent reassignment."

</details>

---

## Snippet 14 — Overriding With Wider Access Modifier 🟡

**Will this code compile?**

```java
class Parent {
    protected void display() {
        System.out.println("Parent");
    }
}

class Child extends Parent {
    @Override
    public void display() {
        System.out.println("Child");
    }
}

class AnotherChild extends Parent {
    @Override
    private void display() {
        System.out.println("AnotherChild");
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Compilation Error on AnotherChild: Cannot reduce the visibility of the inherited method
```

**Explanation:**
- `Child` compiles fine: `public` is wider than `protected` — you CAN increase visibility when overriding.
- `AnotherChild` fails: `private` is narrower than `protected` — you CANNOT reduce visibility when overriding.
- Rule: Overriding method's access modifier must be the **same or wider** than the parent method's.
- Order: `private` < default < `protected` < `public`.

**Common wrong answer:** "Both compile fine" — not knowing the access modifier rule for overriding.

**Interview Tip:** "When overriding, you can widen access but never narrow it. This upholds the Liskov Substitution Principle — anywhere the parent is used, the child must work."

</details>

---

## Snippet 15 — Method Resolution: Overloading + Overriding Combined 🔴

**What does this code print?**

```java
class Animal {
    void speak(Object obj) {
        System.out.println("Animal speaks to Object");
    }
}

class Dog extends Animal {
    @Override
    void speak(Object obj) {
        System.out.println("Dog speaks to Object");
    }

    void speak(String name) {
        System.out.println("Dog speaks to " + name);
    }
}

public class Main {
    public static void main(String[] args) {
        Animal a = new Dog();
        a.speak("Buddy");
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Dog speaks to Object
```

**Explanation:**
- **Overloading** is resolved at **compile time** based on the reference type.
- The reference type is `Animal`, which only has `speak(Object)`. The compiler doesn't see `speak(String)` because it only exists in `Dog`.
- So the compiler binds to `speak(Object)`.
- **Overriding** is resolved at **runtime**. The actual object is `Dog`, so `Dog.speak(Object)` runs.
- "Buddy" (a String) is passed as an `Object` parameter.

**Common wrong answer:** "Dog speaks to Buddy" — assuming the compiler considers subclass overloads.

**Interview Tip:** "Overloading is compile-time (reference type), overriding is runtime (object type). The compiler can only see methods declared in the reference type."

</details>

---

## Quick Review Table

| # | Concept Tested | Key Rule |
|---|---|---|
| 1 | Constructor chaining | Parent constructor runs first via implicit `super()` |
| 2 | Method overriding | Runtime dispatch based on actual object type |
| 3 | Static method hiding | Compile-time resolution based on reference type |
| 4 | Overloading with null | Most specific applicable method is chosen |
| 5 | `super()` vs `this()` | Only one allowed as first statement |
| 6 | Fields vs methods | Fields are NOT polymorphic |
| 7 | Abstract constructor calling overridable method | Child fields aren't initialized yet |
| 8 | Covariant return types | Override can return subtype |
| 9 | Upcasting/Downcasting | Invalid downcast → ClassCastException |
| 10 | Default method conflict | Must override to resolve diamond |
| 11 | instanceof with null | Always returns false, never NPE |
| 12 | equals without hashCode | HashSet won't deduplicate |
| 13 | final method | Cannot be overridden |
| 14 | Access modifier widening | Cannot narrow when overriding |
| 15 | Overloading + Overriding | Overloading = compile time, Overriding = runtime |
