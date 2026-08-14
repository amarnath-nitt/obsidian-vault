# System Design (HLD) Interview Guide

Master high-level design for senior Java developer interviews. This guide covers the structured framework, must-know components, and common interview problems.

---

## 1. The HLD Interview Framework

Every system design answer follows the same structure. Memorize this:

```
1. Requirements (Functional + Non-functional)
2. Capacity Estimation (Traffic, Storage, Bandwidth)
3. API Design (Endpoints + payloads)
4. Database Schema (Tables + relationships)
5. High-Level Architecture (Components + data flow)
6. Deep Dive (Bottlenecks + key features)
7. Scaling (Horizontal/Vertical, caching, partitioning)
8. Failure Handling (Degradation, retries, backup)
9. Trade-offs (Consistency vs availability, etc.)
```

### Interview Scoring Rubric

| Dimension | What interviewers look for |
|---|---|
| **Requirements gathering** | Ask clarifying questions — don't assume |
| **Estimation** | Rough numbers with units, sanity checks |
| **Breadth** | Covers API, DB, cache, queue, search, CDN |
| **Depth** | Goes deep on ONE bottleneck the interviewer asks about |
| **Trade-offs** | Can explain WHY a choice over alternatives |
| **Communication** | Clear structure, draws diagrams, active thinking aloud |

---

## 2. Requirements Gathering

### Functional Requirements (FRs)

Ask "what should the system do?"

**Example — Design URL Shortener:**
- Create short URL from long URL
- Redirect short URL → long URL
- Optional: analytics, custom aliases, expiration, user accounts

### Non-Functional Requirements (NFRs)

| NFR | Typical Ask | Question to Clarify |
|---|---|---|
| Availability | 99.9%? 99.99%? | "What's the downtime budget?" |
| Latency | p95 < 200ms? | "What's acceptable response time?" |
| Consistency | Strong or eventual? | "Can users see stale data?" |
| Scalability | 10M? 100M? 1B users? | "What scale should we design for?" |
| Durability | Is data loss acceptable? | "What's the RPO (recovery point objective)?" |
| Security | Private/public data? | "What compliance needs exist?" |

### Questioning Technique

Don't ask "how many users?" — that's weak. Instead:

> "Let's assume we're targeting 100 million monthly active users with a 1:10 daily/monthly ratio. That gives us roughly 10M DAU. With each user performing ~5 write operations daily, we get ~50M writes/day. That's about 580 writes/second average, with maybe 5x peak = ~2,900 writes/sec. Is that the right ballpark?"

This shows you can:
1. Make reasonable assumptions
2. Compute derived numbers
3. Sanity-check the scale

---

## 3. Capacity Estimation Cheat Sheet

### Conversion Factors

```
1 day = 86,400 seconds        ≈ 10^5 seconds
1 month ≈ 2.5 × 10^6 seconds
1 year ≈ 3 × 10^7 seconds

1 KB  = 10^3 bytes
1 MB  = 10^6 bytes
1 GB  = 10^9 bytes
1 TB  = 10^12 bytes
1 PB  = 10^15 bytes
```

### Storage Estimation Example

**Twitter-like system:**
- 200M MAU, 50% DAU = 100M DAU
- Each user tweets 2x/day = 200M tweets/day
- Average tweet size: 280 chars + metadata + media ≈ 1 KB
- Daily storage: 200M × 1 KB = 200 GB/day
- Yearly storage: 200 GB × 365 ≈ 73 TB/year
- 5-year storage: ~365 TB (before compression/dedup)

### Bandwidth Estimation

- Read:Write ratio for social feeds ≈ 10:1
- Total reads/day: 200M tweets × 10 = 2B reads/day
- Read rate: 2B / 86,400 ≈ 23K reads/sec
- Read bandwidth: 23K × 1 KB ≈ 23 MB/sec
- Peak (5x): ~115 MB/sec

### Cache Estimation

Assuming 80/20 rule:
- 20% of tweets = "hot" content
- Need capacity for ~5 days of hot tweets
- 5 days × 20% of 200 GB/day = 200 GB
- Single cache node with 32 GB RAM → ~7 nodes → round up: 8-10 nodes

---

## 4. Common Building Blocks

### Load Balancer

| Type | Layer | Uses |
|---|---|---|
| L4 (TCP) | Transport | Fast, no content inspection |
| L7 (HTTP) | Application | Path-based routing, sticky sessions, SSL |

**Algorithms:** Round-robin, least connections, least response time, consistent hashing (for cache).

### Caching

| Level | Example | Hit Rate |
|---|---|---|
| Client/Edge | Browser cache, CDN | High for static |
| Application | Redis, Memcached | High for hot data |
| Database | Buffer pool, query cache | Medium |

**Patterns:**

```
Read-through:  App → Cache → Miss → DB → Populate cache → Return
Write-through: App → Cache → Write → DB → Write
Write-back:    App → Cache → Write (async flush to DB)
Write-around:  Write directly to DB, cache only on read
```

**Eviction:** LRU, LFU, FIFO, TTL

**Consistency patterns:**
- **Cache-aside:** App reads cache → on miss reads DB → populates cache. Best for read-heavy.
- **Cache invalidation:** Update DB → delete cache entry → next read repopulates. Avoids stale data.
- **TTL-based:** Simple but can serve stale data within TTL window.

### Message Queues / Event Streaming

| Feature | Kafka | RabbitMQ | SQS |
|---|---|---|---|
| Model | Log-based | Queue/Broker | Queue |
| Ordering | Per-partition | Per-queue (with limits) | Standard: no guarantee; FIFO: yes |
| Replay | Yes (offsets) | Limited | No |
| Throughput | Very high | Medium | High |
| Delivery | At-least-once | At-least-once | At-least-once |
| Use case | Event sourcing, log aggregation, CDC | Task queues, RPC | Simple job queues |

**Key patterns:**
- **Outbox pattern**: Write to DB + outbox table in same transaction → poller publishes to Kafka → avoids distributed transaction
- **Dead-letter queue (DLQ)**: Failed messages routed for manual/async retry
- **Idempotent consumers**: Store processed message IDs to handle at-least-once delivery

### Database Choices

| DB | Type | Best For | Example |
|---|---|---|---|
| PostgreSQL/MySQL | Relational | ACID, joins, relationships | Orders, users, inventory |
| MongoDB | Document | Flexible schema, JSON-like data | Product catalog, analytics |
| Cassandra | Wide-column | High write throughput, scale | Time-series, IoT data |
| Redis | In-memory KV | Caching, sessions, rate limiting | Hot data, leaderboards |
| Elasticsearch | Search index | Full-text search, aggregation | Logs, product search |
| S3 | Object storage | Files, images, videos | Media storage |

### CAP Theorem

```
CAP: Consistency, Availability, Partition Tolerance
In a distributed system, you can only guarantee 2 of 3.
Network partitions are inevitable → you must choose between C and A.
```

- **CP:** Consistent but may reject requests during partition (HBase, MongoDB with default, ZooKeeper)
- **AP:** Available but may return stale data during partition (Cassandra, DynamoDB, CouchDB)

**Interview answer tip:** Don't just name the theorem — explain it with a real scenario. "If a network partition splits our nodes, do we serve stale reads (AP) or return errors (CP)? For our order service, we choose CP because consistency matters more than temporary unavailability."

### Consistent Hashing

Distributes keys across nodes so adding/removing a node only remaps ~1/n of keys.

**Why it matters:** With simple `hash(key) % n`, adding a node remaps ALL keys → cache stampede.

---

## 5. High-Level Architecture Pattern

### Three-Tier Architecture (Web + App + DB)

```
Client → CDN → Load Balancer → Web Servers → App Servers → Databases
                                      ↓              ↓
                                 Cache (Redis)  Search (ES)
                                      ↓
                              Message Queue → Workers
```

Tip: Always draw this high-level view FIRST. Then go deep on areas the interviewer asks about.

---

## 6. Deep Dive Topics

### Database Scaling

| Strategy | How | When |
|---|---|---|
| Indexing | Add indexes on query patterns | Early optimization |
| Read replicas | Slave copies for reads | Read-heavy workloads |
| Caching | Redis layer on top | Hot data, read-heavy |
| Vertical scaling | Bigger machine | Simple but has limits |
| Sharding | Split data across nodes | Write-heavy, massive data |
| Denormalization | Flatten joins | Complex query performance |

### Sharding Strategy

| Strategy | Key | Pros | Cons |
|---|---|---|---|
| Range-based | ID ranges | Simple, good for ordered scans | Hotspots at range edges |
| Hash-based | `hash(key) % N` | Even distribution | Re-hash on node changes |
| Geographical | Location | Local data lookup | Uneven load |
| Tenant-based | Tenant ID | Natural boundaries | Hot tenant problem |

**Critical question:** "What do we shard on?" For a social app, shard on `user_id` so all a user's data is on one shard.

### Rate Limiting

| Algorithm | Pros | Cons |
|---|---|---|
| Token bucket | Bursts allowed, simple | Two params to tune |
| Leaky bucket | Smooth output | Limits bursts |
| Fixed window | Simple | Edge burst issue |
| Sliding window | Smooth, precise | More state |

```java
// Token bucket implementation
public class TokenBucket {
    private final double capacity;
    private final double refillRate; // tokens per second
    private double tokens;
    private long lastRefill;

    public synchronized boolean allow() {
        long now = System.nanoTime();
        double elapsed = (now - lastRefill) / 1e9;
        tokens = Math.min(capacity, tokens + elapsed * refillRate);
        lastRefill = now;
        if (tokens < 1) return false;
        tokens -= 1;
        return true;
    }
}
```

---

## 7. Common HLD Problems Framework

### Problem 1: Design URL Shortener

**FRs:** Shorten URL, redirect, custom alias, analytics
**NFRs:** 100M new URLs/month, p99 < 100ms redirect, high availability

**Estimation:**
- 100M new/month → 3.3M/day → 38/sec creates
- Reads: 100x writes → 3,800 reads/sec
- Storage: 100M × 100 bytes (short code + long URL + metadata) ≈ 10 GB/month → 120 GB/year

**API:**
```
POST /api/shorten    { longUrl } → { shortCode }
GET  /{shortCode}    → 301 Redirect
```

**Database:**

```
URLs(short_code PK, long_url, user_id, created_at, expires_at)
```

**Short code generation:**
- Base62 encoding of counter: 7 chars → 62^7 = 3.5 trillion combinations
- Or hash long URL (MD5/SHA) → take first 7 chars → collision check
- Or distributed ID (Snowflake) → Base62 encode

**Architecture:**

```
Client → LB → Web (stateless) → Cache (recent mapping) → DB
                                      ↓
                             Analytics worker (Kafka)
```

### Problem 2: Design Twitter / Social Feed

**FRs:** Post tweet, view feed, follow/unfollow, like/retweet
**NFRs:** 200M MAU, feed < 200ms, high write throughput

**Feed Generation — Two Approaches:**

| | Push (Fan-out-on-write) | Pull (Fan-out-on-read) |
|---|---|---|
| When | On tweet, push to all followers' feeds | On view, query all followees' tweets |
| Speed | Instant read | Slow read (100s of queries) |
| Write cost | High for celebrities | Low |
| Storage | Redundant copies | Single copy |
| Best for | Most users | Celebrities / inactive heavy users |

**Hybrid approach:** Push for normal users, pull for celebrities (identify by follower count > 10K).

**Feed Cache structure (Redis):**

```
Key: feed:{user_id}
Value: List of tweet IDs (latest 800)
```

**Architecture:**

```
Tweet → Kafka → Timeline Service → Cache
              → Analytics Worker
              → Fan-out Worker (push to followers)
```

### Problem 3: Design Chat Messaging (WhatsApp-style)

**FRs:** 1:1 messages, group chats, delivery receipts, online status
**NFRs:** 400M messages/day, < 100ms delivery, end-to-end encryption

**Key decisions:**
- WebSocket for real-time, REST for upload/download
- Messages in DB (durable) + Redis (session/online status)
- Each client maintains only 1 active connection (connection pooling)

**Inbox model (per user):**

```
inbox:{chat_id}:messages → sorted by timestamp
```

**Message flow:**

```
Sender → WS Gateway → Message Service → DB
                        ↓
                   Kafka → Receiver's Gateway (if online)
                        ↓
                   Push Notification (if offline)
```

**Group chat:** Fan-out on write to each member's inbox. For large groups (10K+), lazy fan-out on read.

### Problem 4: Design Notification System

**FRs:** Send push/SMS/email notifications, user preferences, rate limiting
**NFRs:** 10M notifications/day, < 1 min delivery, high reliability

```
Notification Service → Kafka → Workers (per channel)
                            → Email Worker (sendgrid)
                            → Push Worker (FCM/APNs)
                            → SMS Worker (twilio)
                            → DLQ for failures
```

**Key topics:**
- **Retry policy:** Exponential backoff + DLQ
- **Rate limiting:** Per-user, per-channel (SMS is expensive!)
- **User preferences:** Opt-out, channel priority
- **Big-bang problem:** 1M users get the same notification at once → batch + stagger

### Problem 5: Design Ticket Booking (BookMyShow/Eventbrite)

**FRs:** Browse events, show seats, book, hold seats, payment
**NFRs:** High concurrency on hot events, no oversell, strong consistency on bookings

**Key challenges:**
1. **Concurrency:** Two users selecting the same seat
2. **Seat holding timeout:** Release after 10 min if not paid
3. **Payment integration:** Indempotency, partial failures

**Solution patterns:**
- Database **transaction with `SELECT ... FOR UPDATE`** on seat row
- **Optimistic locking** with version column
- **Redis distributed lock** for critical sections
- **Seat status state machine:** AVAILABLE → HELD → BOOKED → CANCELLED

```sql
BEGIN;
SELECT * FROM seats WHERE id = ? FOR UPDATE;
-- Check status = AVAILABLE
UPDATE seats SET status = 'HELD', hold_until = NOW() + INTERVAL '10 minutes'
WHERE id = ? AND status = 'AVAILABLE';
COMMIT;
```

**If using optimistic locking:**

```java
@Entity
public class Seat {
    @Id Long id;
    String status; // AVAILABLE, HELD, BOOKED
    @Version Long version;

    // UPDATE WHERE id=? AND version=?
    // If 0 rows updated → conflict → return "seat taken"
}
```

---

## 8. Common Interview Questions Bank

### Design these systems (know at least 5 well):

| System | Key challenge | Core pattern |
|---|---|---|
| URL Shortener | Unique code generation | Base62 + cache |
| Twitter Feed | Fan-out strategy | Push + hybrid |
| Chat (WhatsApp) | Real-time, ordering | WebSocket + per-user inbox |
| Notification System | Reliability, rate limit | Queue + DLQ + channels |
| Ticket Booking | No oversell | Lock + timeouts |
| Search Autocomplete | Suggestion ranking | Trie + top-K |
| File Storage Dropbox | Sync conflicts | CRDTs + versioning |
| Payment System | Exactly-once, fraud | Idempotency + ledger |
| Rate Limiter | Distributed counters | Redis + token bucket |
| News Feed Ranking | Relevance scoring | ML + features + candidates |
| Uber/Lyft | Matching drivers/riders | Geo-index + push |
| Video Streaming | Distributed media | CDN + chunked encoding |
| E-commerce Cart | Consistency | Sessions + optimistic locks |
| Inventory System | Over-sell prevention | Transactions + prechecks |
| Logging/Metrics | High throughput ingest | Kafka + time-series DB |

### Typical follow-up questions (practice these):

1. "How would you handle a viral traffic spike (10x)?"
2. "What happens if a database node dies?"
3. "How do you keep the cache consistent with the DB?"
4. "How do you scale the read path? Write path?"
5. "Where are the single points of failure?"
6. "How do you ensure data durability and recovery?"
7. "How would you add a new feature without downtime?"
8. "How do you monitor this system in production?"

---

## 9. Trade-off Phrases to Use in Answers

| Instead of saying | Say |
|---|---|
| "We'll use Redis" | "We'll add a Redis cache **to absorb read traffic and reduce DB load — this trades eventual consistency of cached data for ~10x read throughput**." |
| "We'll use Kafka" | "We'll use Kafka to **decouple producers from consumers** — this adds delivery latency but gives us buffering, replay, and asynchronous scaling." |
| "We'll shard the DB" | "We'll shard by user_id so **all of a user's data lives on one shard** — this trades node elasticity for simpler queries and avoids cross-shard joins." |
| "We'll use strong consistency" | "We'll use strong consistency because **payments need to be exactly-once** — this may increase latency in partition scenarios but correctness here exceeds availability." |
| "We'll use eventual consistency" | "We'll use eventual consistency because **feed staleness of a few seconds is acceptable** — this gives us higher availability and lower latency for reads." |

---

## 10. System Design Interview Checklist

### Before the interview
- [ ] Know the 9-step framework by heart
- [ ] Can do quick capacity math without a calculator
- [ ] Have practiced 5+ design problems aloud
- [ ] Can draw 3-tier architecture blind
- [ ] Know the difference between all building blocks (LB, cache, queue, etc.)
- [ ] Can explain CAP and consistency models with examples

### During the interview
- [ ] Clarify requirements before designing
- [ ] Confirm scale before jumping to architecture
- [ ] Write down your estimates visibly
- [ ] Keep the diagram visible and labeled
- [ ] Use "I'd like to go deeper on X — is that where you want to go?" for deep dives
- [ ] Explicitly state trade-offs
- [ ] Proactively mention failure handling

### After the design
- [ ] Summarize the architecture in 2-3 sentences
- [ ] Mention the 2-3 most important design decisions
- [ ] State what you'd improve given more time

---

## 11. HLD Practice Plan (14 Days)

| Day | Focus | Deliverable |
|---|---|---|
| 1 | Framework memorization | Write 9-step framework blind |
| 2 | Capacity estimation drills | 5 scenarios, 10 min each |
| 3 | Load balancer + caching deep dive | Explain 4 caching patterns aloud |
| 4 | Messaging patterns deep dive | Outbox, DLQ, idempotency |
| 5 | URL Shortener | Full design aloud |
| 6 | Twitter Feed | Full design aloud |
| 7 | Review + mock session | 45-min timed mock |
| 8 | Chat System | Full design aloud |
| 9 | Notification System | Full design aloud |
| 10 | Ticket Booking | Full design aloud |
| 11 | Payment System | Full design aloud |
| 12 | Rate Limiter + Search Autocomplete | Full design aloud |
| 13 | Database sharding deep dive | Explain strategies with trade-offs |
| 14 | Full mock interview | 60-min timed + feedback |

---

## Related Notes

- [[Java-Backend-Interview-Roadmap]]
- [[Spring-Boot-Interview-Questions]]
- [[SQL-Interview-Questions]]
- [[Docker-for-Java-Developers-Interview-Guide]]
- [LLD Roadmap](../LLD/00%20-%20Roadmap.md)
