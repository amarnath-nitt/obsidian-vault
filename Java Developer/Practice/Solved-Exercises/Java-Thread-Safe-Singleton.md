# Thread-Safe Singleton

**Concept tested**: Double-checked locking, `volatile`, enum singleton

## Solution: Double-Checked Locking
```java
class Singleton {
    private static volatile Singleton instance;

    private Singleton() {
    }

    public static Singleton getInstance() {
        if (instance == null) {
            synchronized (Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}
```

## Better Option: Enum Singleton
```java
enum SingletonEnum {
    INSTANCE;

    public void doSomething() {
        // business logic
    }
}
```

## Complexity
- **Time**: O(1)
- **Space**: O(1)

## Interview Explanation
Double-checked locking avoids synchronization after initialization. `volatile` prevents visibility and instruction reordering issues. In most cases, enum singleton is simpler and safer.
