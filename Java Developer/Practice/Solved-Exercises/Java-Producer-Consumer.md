# Producer-Consumer Pattern

**Concept tested**: `BlockingQueue`, thread coordination

## Solution
```java
class ProducerConsumer {
    public static void main(String[] args) {
        BlockingQueue<Integer> queue = new ArrayBlockingQueue<>(10);

        Thread producer = new Thread(() -> {
            try {
                for (int i = 1; i <= 20; i++) {
                    queue.put(i);
                    System.out.println("Produced: " + i);
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });

        Thread consumer = new Thread(() -> {
            try {
                while (!Thread.currentThread().isInterrupted()) {
                    Integer value = queue.take();
                    System.out.println("Consumed: " + value);
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });

        producer.start();
        consumer.start();
    }
}
```

## Complexity
- **Time**: O(n) for `n` produced items
- **Space**: O(capacity)

## Interview Explanation
`BlockingQueue` handles the wait-notify logic internally. The producer blocks when the queue is full, and the consumer blocks when the queue is empty.
