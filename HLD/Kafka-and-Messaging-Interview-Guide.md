# Kafka & Messaging Interview Guide

Comprehensive interview preparation for Apache Kafka, message queues, event-driven architecture, and distributed messaging patterns for Java backend roles.

---

## 1. Kafka Core Concepts

### Q: What is Apache Kafka?

**Answer shape:** Definition → Purpose → Mechanism → Example → Trade-off

Kafka is a **distributed event streaming platform**. It is a distributed, partitioned, replicated commit log that provides:
- **Publish/subscribe** messaging
- **Storage** of events (replayable)
- **Stream processing** capabilities

### Core Model

```
Producers → Kafka Cluster (Topics → Partitions) → Consumers (Consumer Groups)
```

### Topic & Partitions

| Concept | Description |
|---|---|
| **Topic** | Named logical stream of events |
| **Partition** | Ordered, immutable sequence of records. Ordering is guaranteed **within a partition**, not across partitions |
| **Offset** | Sequential ID of a record within a partition |
| **Replication** | Each partition has replicas across brokers for fault tolerance |
| **Leader/Follower** | One replica is leader (handles reads/writes); followers replicate |
| **ISR (In-Sync Replicas)** | Replicas that are caught up with the leader |

**Key interview point:** Kafka does NOT guarantee global ordering — only per-partition ordering.

### Partition key

```java
// Producer sends with key
producer.send(new ProducerRecord<>("orders", orderId, orderJson));
```

- Same key → same partition (hash-based)
- Use order_id as key → all events for an order in the same partition → ordered
- Without key → round-robin → no ordering guarantee per order

---

## 2. Producer & Consumer Deep Dive

### Producer

```
Producer → Serializer → Partitioner → RecordAccumulator (batch) → Sender Thread → Broker
```

**Key producer configs:**

| Config | Default | What It Controls |
|---|---|---|
| `bootstrap.servers` | — | Initial brokers to connect to |
| `acks` | `all` | `0` = fire and forget, `1` = leader confirms, `all` = all ISRs confirm |
| `compression.type` | `none` | `gzip`, `snappy`, `lz4`, `zstd` |
| `linger.ms` | 0 | How long to wait before sending a batch (trade-off: latency vs throughput) |
| `batch.size` | 16 KB | Max batch size |
| `buffer.memory` | 32 MB | Total memory for buffering |
| `retries` | MAX_INT | Retry count on transient failures |
| `max.in.flight.requests.per.connection` | 5 | With retries > 0 and this > 1, ordering can break unless `enable.idempotence=true` |

**Idempotent producer:**

```java
props.setProperty("enable.idempotence", "true");
props.setProperty("acks", "all");
```

Prevents duplicate messages on retry (producer assigns sequence numbers, broker dedupes).

### Consumer

```
Consumer Group → Assign partitions → Poll loop (poll()) → Process → Commit offset → Repeat
```

**Key consumer configs:**

| Config | Default | What It Controls |
|---|---|---|
| `group.id` | — | Consumer group membership |
| `auto.offset.reset` | `latest` | `earliest` = read from beginning, `latest` = read new only, `none` = error if no offset |
| `enable.auto.commit` | true | Auto-commit offsets (can lose messages!) |
| `max.poll.records` | 500 | Max records per poll |
| `max.poll.interval.ms` | 300000 | If processing takes longer, consumer is considered dead → rebalance |
| `session.timeout.ms` | 45000 | Heartbeat timeout |
| `heartbeat.interval.ms` | 3000 | Heartbeat frequency |

### Consumer Group Rebalancing

```
1. Consumer joins/leaves group → triggers rebalance
2. Group coordinator (broker) assigns partitions to consumers
3. Old partition assignments revoked → new assignments
    During rebalance: NO consumer processes messages (stop-the-world)
    Double rebalance (old protocol) → partition hopping
```

**Static group membership** (`group.instance.id`): consumer can leave and rejoin without rebalance.

### Commit Offset Strategies

| Strategy | Behavior | At-least-once? | Risk |
|---|---|---|---|
| Auto-commit | Commit every `auto.commit.interval.ms` | NO — can lose messages between commit and crash | At-most-once |
| Commit after process | Process → commit | YES | Duplicate processing on crash |
| Commit before process | Commit → process | NO | Message loss |
| Commit in poll loop | `commitSync()` in poll loop | YES | Subtle duplicate window |

**Best practice:** Process messages → commit offset AFTER processing. This gives at-least-once delivery, but consumers must be **idempotent**.

---

## 3. Delivery Semantics

| Semantics | Meaning | How |
|---|---|---|
| **At-most-once** | Messages may be lost, never duplicated | Commit offsets before processing |
| **At-least-once** | Messages never lost, may be duplicated | Process then commit; or producer retries |
| **Exactly-once** | Each message processed exactly once | Idempotent producer + transactions, or consumer idempotency |

**Exactly-once in Kafka:**

```
Idempotent Producer (enable.idempotence=true)
  + Transactions (producer.initTransactions())
    → Use with Kafka Streams or read-process-write pattern
```

**Pragmatic approach for most systems:** At-least-once + idempotent consumer. Exactly-once is complex and usually overkill.

### Idempotent Consumer Pattern

```java
@KafkaListener(topics = "orders")
public void handleOrder(OrderEvent event) {
    String eventId = event.getEventId();
    
    // Store processed event IDs (Redis or DB table with unique constraint)
    boolean isDuplicate = processedEventRepository.existsById(eventId);
    if (isDuplicate) {
        log.info("Skipping duplicate event: {}", eventId);
        return;
    }
    
    try {
        processOrder(event);
        processedEventRepository.save(new ProcessedEvent(eventId));
    } catch (Exception e) {
        throw e; // Retry
    }
}
```

---

## 4. Kafka vs Traditional Message Queues

### Q: Kafka vs RabbitMQ — which and when?

| Dimension | Kafka | RabbitMQ |
|---|---|---|
| **Model** | Distributed commit log | Smart broker, queuing model |
| **Ordering** | Per-partition | Per-queue (with single consumer) |
| **Consumption** | Pull-based (consumer polls) | Push-based (broker pushes) |
| **Retention** | Configurable (days/years) | Deleted after ack |
| **Replay** | Yes (rewind offsets) | No |
| **Throughput** | Very high (100s K msg/sec) | Medium (10s K msg/sec) |
| **Consumer groups** | Yes (partition-level parallelism) | Competing consumers |
| **Use case** | Event streaming, log aggregation, CDC, event sourcing, big data | Task queues, RPC, workflow steps, request/response |

### When to use Kafka:
- High-throughput event streams
- Event sourcing / audit logs
- Data pipeline / CDC
- Multiple consumers needing the same events
- Replay capability needed

### When to use RabbitMQ:
- Task/Job queues with complex routing
- Low latency, small message volume
- Per-message acknowledgments
- Request/reply patterns

---

## 5. Critical Kafka Patterns

### Outbox Pattern (Transactional Outbox)

**Problem:** Write to DB and publish to Kafka — if one fails, you get inconsistency.

```
Solution:
1. In DB transaction: INSERT order + INSERT outbox_event (same transaction!)
2. Outbox relay (poller) scans outbox table
3. Publishes events to Kafka
4. Marks event as published (or deletes row)
5. Events can be replayed on failure until successful
```

```java
@Service
public class OrderService {
    @Transactional
    public void placeOrder(Order order) {
        orderRepository.save(order);
        
        // Same transaction as order
        outboxRepository.save(OutboxEvent.builder()
            .aggregateType("ORDER")
            .aggregateId(order.getId())
            .eventType("ORDER_PLACED")
            .payload(objectMapper.writeValueAsString(order))
            .build());
    }
}
```

**Why this works:** The outbox write and order write are atomic in the DB. The relay can retry forever — no message loss.

### Dead Letter Queue (DLQ)

**Problem:** Poison messages crash the consumer repeatedly.

```
main-topic → Consumer (fail) → Retry topic (exponential backoff)
    → still failing → DLQ topic
    → DLQ consumer (manual intervention / alerting)
```

**Retry strategy:**

| Attempt | Wait |
|---|---|
| 1st failure | 1 second |
| 2nd failure | 4 seconds (or 2^n exponential) |
| 3rd failure | 16 seconds |
| ... | ... |
| Max | Send to DLQ |

**Backoff with Spring Kafka:**

```java
@Configuration
public class KafkaConsumerConfig {
    @Bean
    public DefaultErrorHandler errorHandler() {
        FixedBackOff backOff = new FixedBackOff(1000L, 3); // 1s, 3 attempts
        return new DefaultErrorHandler(backOff, 
            DeadLetterPublishingRecoverer(this::dlqSender));
    }
}
```

### Consumer Retry Template

```java
@Service
public class OrderConsumer {
    
    @KafkaListener(topics = "orders", errorHandler = "errorHandler")
    public void consumeOrder(OrderEvent event) {
        try {
            orderService.process(event);  // may throw transient exception
        } catch (TransientException e) {
            throw new RetryableException(e); // triggers retry
        } catch (PermanentException e) {
            log.error("Permanent failure, sending to DLQ", e);
            // send to DLQ manually or rely on error handler
        }
    }
}
```

### Event Sourcing & CQRS

- **Event Sourcing:** Store events as the source of truth; current state is derived by replaying events
- **CQRS:** Separate read and write models — write model handles commands, read model handles queries (often built from Kafka projections)

```
Write: Command → Aggregate → Events → Kafka (event store)
Read:  Projection Service ← Kafka → Materialized view → Read DB (elasticsearch, etc.)
```

---

## 6. Spring Kafka Interview Questions

### Basic Producer

```java
@Configuration
public class KafkaProducerConfig {
    @Bean
    public ProducerFactory<String, String> producerFactory() {
        Map<String, Object> props = new HashMap<>();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        props.put(ProducerConfig.ACKS_CONFIG, "all");
        props.put(ProducerConfig.ENABLE_IDEMPOTENCE_CONFIG, true);
        return new DefaultKafkaProducerFactory<>(props);
    }

    @Bean
    public KafkaTemplate<String, String> kafkaTemplate() {
        return new KafkaTemplate<>(producerFactory());
    }
}

// Usage
@Autowired KafkaTemplate<String, String> kafkaTemplate;

public void publishOrder(Order order) {
    kafkaTemplate.send("orders", order.getId().toString(), orderJson)
        .whenComplete((result, ex) -> {
            if (ex != null) log.error("Failed to send order", ex);
        });
}
```

### Consumer with Group

```java
@Configuration
@EnableKafka
public class KafkaConsumerConfig {
    @Bean
    public ConsumerFactory<String, String> consumerFactory() {
        Map<String, Object> props = new HashMap<>();
        props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ConsumerConfig.GROUP_ID_CONFIG, "order-service");
        props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
        props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
        props.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
        props.put(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, false);
        return new DefaultKafkaConsumerFactory<>(props);
    }
}

@Service
public class OrderEventListener {
    @KafkaListener(topics = "orders", groupId = "order-service")
    public void onOrderCreated(OrderEvent event) {
        // Process event, commit after processing
        // @KafkaListener commits after method returns successfully by default
    }
    
    // Subscribe to multiple topics
    @KafkaListener(topics = {"orders", "order-updates"}, groupId = "order-service")
    public void onOrderEvent(String message) { }
    
    // With partitions
    @KafkaListener(topicPartitions = @TopicPartition(topic = "orders", partitions = {"0", "1"}))
    public void listenSpecificPartitions(String message) { }
}
```

### Ack Modes

| Ack Mode | Behavior |
|---|---|
| `RECORD` | Ack after each record processed |
| `BATCH` | Ack after all records in poll batch processed |
| `TIME` | Ack after `ackTime` milliseconds |
| `COUNT` | Ack after `ackCount` records processed |
| `MANUAL` | Call `acknowledgment.acknowledge()` manually |
| `MANUAL_IMMEDIATE` | Same, immediate |

```java
@KafkaListener(topics = "orders")
public void listen(String message, Acknowledgment ack) {
    try {
        processMessage(message);
        ack.acknowledge(); // manual ack after successful processing
    } catch (Exception e) {
        // do NOT ack → will retry/rebalance → redeliver
    }
}
```

---

## 7. Kafka Monitoring & Operational Questions

### Q: How do you know if Kafka is healthy?

| Metric | What to Watch |
|---|---|
| `under-replicated partitions` | Should be 0; if > 0, replicas falling behind |
| `active controller count` | Should be 1; > 1 = split-brain problem |
| `offline partitions` | Should be 0; > 0 = broker down with no in-sync replica |
| Consumer lag | Should be low; growing = consumer can't keep up |
| Request queue time | Should be < 100ms; high = broker overloaded |
| Network throughput | Watch for saturation |

### Q: How do you check consumer lag?

```bash
kafka-consumer-groups --bootstrap-server localhost:9092 \
  --describe --group order-service
```

```
GROUP          TOPIC  PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG
order-service  orders 0          1000            1100            100
order-service  orders 1          2000            2200            200
```

**Lag > threshold** → consumer too slow → increase consumers (more partitions needed), optimize processing, or batch better.

### Q: What happens if a broker dies?

1. Followers in ISR elect a new leader per partition (`min.insync.replicas` matters)
2. Producers with `acks=all` and `min.insync.replicas=2` continue without data loss
3. Consumers rebalance (new partitions assigned)
4. Under-replicated partitions return to healthy when broker recovers

**Availability settings:**
- `replication.factor=3` → survive 2 broker failures
- `min.insync.replicas=2` → guarantee at least 2 replicas have the message
- `acks=all` → producer waits for all ISRs → strongest durability

### Q: How do you scale Kafka consumers?

1. **Max parallelism = number of partitions** — a consumer can only read one partition at a time from a topic
2. To scale: add more partitions (can't reduce later!) + add consumers in same group
3. If consumers > partitions → some consumers idle

**Key interview point:** Partition count is the unit of parallelism. Design partition count for future scaling (e.g., set 24 partitions for a topic that may need 12-24 consumers).

---

## 8. Event-Driven Design Principles

### Q: When to use synchronous API vs async event?

| Scenario | Prefer |
|---|---|
| User needs immediate confirmation | Sync REST |
| Can return "accepted" and process later | Async event |
| Cross-service state change that must be atomic | DB transaction (not events) |
| Fan-out to multiple services | Events |
| Exactly-once financial transaction | Sync + DB transaction |
| High-throughput data pipeline | Async events |

### Event-driven pitfalls to discuss in interviews:

1. **Distributed transactions are hard** → use outbox pattern + idempotency
2. **Event ordering** → key by aggregate ID, accept per-partition ordering only
3. **Schema evolution** → use Avro/Schema Registry for compatibility
4. **Event replay** → design consumers to be naturally replayable (destructive operations need thought)
5. **Event schema changes** → backward/forward compatibility policies

---

## 9. Kafka Interview Quick Answers

### "Explain Kafka in 2-3 sentences" (Elevator Pitch)

> "Kafka is a distributed event streaming platform built around a replicated commit log. Producers write ordered, immutable events to partitioned topics, and consumers read from those topics in consumer groups with independent offsets. This design enables high throughput, replayable history, and asynchronous decoupling between services — making it the backbone of modern event-driven architectures."

### "What's the difference between Kafka and a database?"

| | Database | Kafka |
|---|---|---|
| Primary | Store current state | Store event history |
| Updates | In-place (UPDATE) | Append-only (no UPDATE) |
| Query | Arbitrary searches | Sequential reads by offset |
| Index | Yes | Partition + offset |
| Use | Source of truth for current state | Source of truth for events |

### "What are the trade-offs of using Kafka?"

**Pros:**
- High throughput (100K+ msg/sec on commodity hardware)
- Decoupling producers/consumers
- Replayable events (audit, reprocessing)
- Durable (configurable retention)

**Cons:**
- Operational complexity (ZooKeeper/KRaft, brokers, monitoring)
- At-least-once → needs idempotent consumers
- Ordering limited to partition level
- Latency: batch-oriented — not ideal for sub-ms deliveries
- Can't do arbitrary queries (need database for current state)

---

## 10. Practice Checklist

- [ ] Can explain topic, partition, offset, consumer group
- [ ] Can explain ordering guarantees and partition keys
- [ ] Can explain acks semantics (0, 1, all)
- [ ] Can explain at-most-once vs at-least-once vs exactly-once
- [ ] Can implement idempotent consumer pattern
- [ ] Can explain outbox pattern and why it's needed
- [ ] Can explain DLQ flow and retry strategy
- [ ] Can configure Spring Kafka producer/consumer
- [ ] Can explain rebalance and its impact
- [ ] Can explain how to scale consumers (partitions = parallelism)
- [ ] Can explain Kafka vs RabbitMQ use cases
- [ ] Can monitor consumer lag and diagnose slow consumers

---

## Related Notes

- [[Java-Backend-Interview-Roadmap]]
- [[Spring-Boot-Interview-Questions]]
- [[System-Design-Interview-Guide]]
- [[SQL-Interview-Questions]]
- [[Docker-for-Java-Developers-Interview-Guide]]