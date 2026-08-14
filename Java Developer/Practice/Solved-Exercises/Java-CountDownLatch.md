# CountDownLatch

**Concept tested**: Waiting for multiple threads

## Solution
```java
class CountDownLatchExample {
    public static void main(String[] args) throws InterruptedException {
        int numThreads = 3;
        CountDownLatch latch = new CountDownLatch(numThreads);

        for (int i = 0; i < numThreads; i++) {
            final int id = i;
            new Thread(() -> {
                try {
                    System.out.println("Thread " + id + " initializing");
                } finally {
                    latch.countDown();
                }
            }).start();
        }

        latch.await();
        System.out.println("All threads initialized");
    }
}
```

## Complexity
- **Time**: Depends on worker duration
- **Space**: O(t), where `t` is number of threads

## Interview Explanation
`CountDownLatch` lets one thread wait until other threads complete a required step. Each worker calls `countDown`, and the main thread resumes after the count reaches zero.
