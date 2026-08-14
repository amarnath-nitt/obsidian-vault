# Hibernate & JPA Interview Questions

Comprehensive interview preparation for Hibernate ORM, JPA, and database persistence. This guide covers entity lifecycle, relationships, caching, locking, and performance optimization.

> [!note] Scope
> This guide focuses on **Hibernate ORM** (the JPA implementation used by Spring Boot). Spring Boot integration details are in the [Spring Boot Guide](../Spring%20Boot/Spring-Boot-Interview-Questions.md).

---

## 1. Hibernate Fundamentals

### Q: What is Hibernate? What is JPA? What's the difference?

| | JPA (Jakarta Persistence API) | Hibernate |
|---|---|---|
| What | Specification/standard for ORM in Java | Implementation of the JPA spec |
| Type | Interface definitions + annotations | Concrete classes (`SessionFactory`, `Session`) |
| Analogy | JDBC (spec) → MySQL driver (impl) | JPA (spec) → Hibernate (impl) |
| Created by | Java EE expert group (JSR 317) | JBoss/Red Hat |

**Interview answer:** "JPA is the standardized API for object-relational mapping in Java. Hibernate is a JPA implementation — one of many (EclipseLink, OpenJPA are others). You code against JPA interfaces/annotations, and Hibernate provides the runtime behavior. This lets you switch implementations if needed, although in practice most teams use Hibernate."

### Q: What does Hibernate do under the hood?

**Mechanism:**
1. **Mapping:** Reads `@Entity` classes and maps fields to database columns
2. **Session:** Creates a persistence context (session) that tracks entity state
3. **Dirty checking:** On flush, compares managed entities to their snapshot → generates UPDATE if changed
4. **SQL generation:** Converts entity operations to SQL (INSERT, UPDATE, DELETE, SELECT)
5. **Object identity:** Uses primary key to maintain identity within a session (two loads of same ID = same object)

### Q: What is the Hibernate architecture / core interfaces?

```
Application
    ↓
SessionFactory  (thread-safe, one per database)
    ↓
Session  (not thread-safe, one per unit of work)
    ↓
Transaction  (bound to session)
    ↓
JDBC Connection → Database
```

| Interface | Purpose |
|---|---|
| `SessionFactory` | Heavyweight, thread-safe, creates Sessions. One per database. Created once at startup |
| `Session` | Lightweight, NOT thread-safe. Represents a unit of work / persistence context. Wraps a JDBC connection |
| `Transaction` | Represents a DB transaction, controls commit/rollback |
| `Query`/`TypedQuery` | Executes HQL/JPQL queries |
| `CriteriaBuilder` | Programmatic type-safe queries |

---

## 2. Entity Lifecycle (States)

### Q: What are the entity states in Hibernate?

```
Transient → Persistent (Managed) → Detached → Removed
    ↑           │                    │
    └───────────┘                    ↓
                              Garbage (GC)
```

| State | How You Get There | Description |
|---|---|---|
| **Transient** | `new Entity()` | Not associated with any Session. Not in DB. No ID yet (or no persistent identity) |
| **Persistent/Managed** | `session.save()`, `session.persist()`, `session.get()`, `session.find()`, `session.merge()` | Associated with Session. Tracked for changes. Has a DB identity |
| **Detached** | Session closed, `session.clear()`, `session.evict()` | Was managed but no longer attached. Changes NOT auto-saved |
| **Removed** | `session.delete()`, `session.remove()` | Marked for deletion. Deleted on flush |

```java
// Example
Person p = new Person("Alice");       // TRANSIENT
Session session = sessionFactory.openSession();
session.beginTransaction();
session.persist(p);                    // PERSISTENT (managed)
p.setName("Alicia");                   // Auto-detected by dirty checking
session.getTransaction().commit();     // UPDATE generated + executed
session.close();                       // DETACHED — changes no longer tracked
p.setName("Bob");                      // NOT saved — detached!
```

### Q: `save()` vs `persist()` vs `saveOrUpdate()` vs `merge()`

| Method | JPA? | Behavior |
|---|---|---|
| `save()` | Hibernate-only | Immediately assigns ID, returns it. Works for transient or persistent |
| `persist()` | ✅ JPA | Transient → persistent. Does NOT guarantee ID immediately |
| `saveOrUpdate()` | Hibernate-only | Save if transient, update if detached. Knows by ID presence |
| `merge()` | ✅ JPA | Copies state from detached entity into a (new) managed instance. Returns managed instance |
| `update()` | Hibernate-only | Reattaches a detached entity. Throws if entity is already managed |

**Key interview distinction:**
- `merge()` returns a **different (managed) instance**; the input object remains detached
- `update()` reattaches the same instance but throws if one already exists in the session

---

## 3. Mapping & Relationships

### Q: What JPA mapping annotations exist?

| Annotation | Purpose |
|---|---|
| `@Entity` | Marks class as persistent entity (with `@Table`) |
| `@Id` | Primary key |
| `@GeneratedValue` | ID generation strategy (`IDENTITY`, `SEQUENCE`, `TABLE`, `AUTO`) |
| `@Column(name, nullable, unique, length)` | Column mapping + constraints |
| `@Transient` | Field NOT persisted |
| `@Enumerated(EnumType.STRING)` | Enum mapping (STRING preferred over ORDINAL) |
| `@Lob` | Large object (BLOB/CLOB) |
| `@Version` | Optimistic lock version column |
| `@CreatedDate`, `@LastModifiedDate` | Auditing (with Spring Data JPA) |
| `@ManyToOne`, `@OneToMany` | Relationships |
| `@OneToOne`, `@ManyToMany` | Relationships |
| `@JoinColumn(name)` | Foreign key column |
| `@JoinTable` | Join table for ManyToMany |
| `@Embedded` / `@Embeddable` | Value objects (Address, Money) |
| `@Inheritance` | Inheritance strategies (`SINGLE_TABLE`, `JOINED`, `TABLE_PER_CLASS`) |

### Q: What generation strategies exist?

| Strategy | How | Pros | Cons |
|---|---|---|---|
| `IDENTITY` | DB auto-increment | Simple, standard on MySQL/Postgres | Batch insert disabled; insert happens immediately |
| `SEQUENCE` | DB sequence (`nextval`) | Supports batch, optimal | Needs sequence (Postgres/Oracle) |
| `TABLE` | Separate table for IDs | Portable | Slow, not recommended |
| `AUTO` | Hibernate picks | Simple | Not predictable |

**Modern recommendation:** `SEQUENCE` with `@SequenceGenerator` (or identity on MySQL if you don't need batch).

### Q: Explain relationship types, owning side, and mappedBy

```java
@Entity
public class Order {
    @Id Long id;

    // OWNING side: holds the foreign key (order_id column in order_items)
    @OneToMany(mappedBy = "order", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<OrderItem> items;
}

@Entity
public class OrderItem {
    @Id Long id;

    // OWNED side / inverse side: mappedBy tells Hibernate who owns the FK
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "order_id")
    private Order order;
}
```

**Key rules:**
- `@JoinColumn` goes on the **owning side** (usually @ManyToOne)
- `mappedBy` goes on the **inverse side** (usually @OneToMany)
- Only the owning side's changes affect the FK
- ManyOne is **EAGER** by default in JPA spec — change to LAZY!

### Q: What is the N+1 query problem? How do you fix it?

**Problem:** 1 query for the parent + N queries for each child.

```java
// N+1: Each order triggers a separate user query
List<Order> orders = orderRepository.findAll();
for (Order order : orders) {
    System.out.println(order.getUser().getName()); // N queries!
}
```

**4 Solutions:**
1. **`JOIN FETCH`** — eager fetch in a query:
   ```java
   @Query("SELECT o FROM Order o JOIN FETCH o.user")
   List<Order> findAllWithUser();
   ```
2. **`@EntityGraph`** — named attribute paths:
   ```java
   @EntityGraph(attributePaths = {"user", "items"})
   @Query("SELECT o FROM Order o")
   List<Order> findAllWithDetails();
   ```
3. **`@BatchSize(size = 20)`** — loads N children in batches:
   ```java
   @Entity
   public class User {
       @OneToMany(mappedBy = "user")
       @BatchSize(size = 20)
       private List<Order> orders;
   }
   ```
4. **DTO projections** — select only needed columns:
   ```java
   public interface OrderDTO {
       String getOrderNumber();
       String getUserName();
   }
   @Query("SELECT o.orderNumber AS orderNumber, u.name AS userName FROM Order o JOIN o.user u")
   List<OrderDTO> findAllDTOs();
   ```

### Q: What is the difference between EAGER and LAZY loading?

| | EAGER | LAZY |
|---|---|---|
| When loaded | Immediately when parent loads | On first access (`getUser()`) |
| SQL | Join/subquery in initial query | Separate query on access |
| Default for | `@OneToOne`, `@ManyToOne` | `@OneToMany`, `@ManyToMany` |
| Feature usage | Large result sets, reduced queries | Typically NOT more performant |

**Best practice:** Use **LAZY everywhere**; use `JOIN FETCH`/`@EntityGraph` where you KNOW you'll need the data.

**LAZY outside transaction → `LazyInitializationException`**

```java
@Transactional
public void serviceMethod() {
    Order order = orderRepository.findById(1L).orElseThrow();
    order.getUser().getName();  // ✅ OK — inside transaction
}
// ❌ LazyInitializationException if accessed after transaction ends
```

**Fixes:** Keep the session/transaction open, use DTO projections, or access before return.

---

## 4. Hibernate Internals

### Q: What is the first-level cache?

- **First-level cache** = the **Session** (persistence context). Every entity loaded in a session is cached. Same `find(id)` within same session returns the same object without a SELECT.
- Default: always on, **not** configurable off.
- Scope: per-session (per unit of work).

```java
Session session = sessionFactory.openSession();
Person p1 = session.find(Person.class, 1L);  // SELECT issued
Person p2 = session.find(Person.class, 1L);  // NO SELECT — from first-level cache
System.out.println(p1 == p2);  // true — same instance
```

### Q: What is the second-level cache?

- **Second-level cache** = shared cache across **sessions/factories**. Enabled via provider (EHCache, Redis).
- Purpose: avoid repeated DB reads for rarely-changing data (reference data, product catalogs).
- NOT used for: frequently-changing entities, possibly stale data.

```properties
# application.properties
spring.jpa.properties.hibernate.cache.use_second_level_cache=true
spring.jpa.properties.hibernate.cache.region.factory_class=org.hibernate.cache.ehcache.EhCacheRegionFactory
```

```java
@Entity
@Cacheable
@org.hibernate.annotations.Cache(usage = CacheConcurrencyStrategy.READ_WRITE)
public class Product { }
```

**Cache strategies:**
- `READ_ONLY` — never modified. Cheapest, safest
- `READ_WRITE` — application updates, soft locks used
- `NONSTRICT_READ_WRITE` — eventual consistency, may stale
- `TRANSACTIONAL` — strong consistency (requires JTA)

### Q: What is dirty checking?

Hibernate tracks the state of every managed entity as a **snapshot** when first loaded. On `flush()`, it compares current field values to the snapshot. If different → generates `UPDATE`.

```java
session.persist(person);
person.setName("NewName");   // change detected on flush
// flush: UPDATE person SET name=? WHERE id=?
```

Without dirty checking, you'd need to explicitly call `session.update()` every time.

### Q: What is the `@Version` annotation? How does optimistic locking work?

- Every entity has a version number column (starts at 0, increments on each update).
- On update: `UPDATE ... SET version = version + 1 WHERE id = ? AND version = ?`
- If no rows match → `OptimisticLockException` → retry or notify user.

```java
@Entity
public class Account {
    @Id Long id;
    BigDecimal balance;
    @Version Long version;  // Hibernate manages it
}
```

```java
try {
    accountService.withdraw(accountId, amount);
} catch (OptimisticLockException e) {
    // Someone else updated it. Retry or show "please refresh"
}
```

**Optimistic vs Pessimistic locking:**

| | Optimistic (`@Version`) | Pessimistic (`SELECT ... FOR UPDATE`) |
|---|---|---|
| When | Check at commit | Locks at read |
| Concurrency | High — no lock held | Low — holds lock |
| Conflicts | Throws at commit | Blocks immediately |
| Use | Most web apps | Financial transactions, rare conflicts |

---

## 5. Cascading & Orphan Removal

### Q: What cascade types exist?

| Cascade | Applies To |
|---|---|
| `PERSIST` | Save parent → save children |
| `MERGE` | Merge parent → merge children |
| `REMOVE` | Delete parent → delete children |
| `REFRESH` | Refresh parent → refresh children |
| `DETACH` | Detach parent → detach children |
| `ALL` | All of the above |

### Q: `cascade = REMOVE` vs `orphanRemoval = true`?

| | Cascade REMOVE | OrphanRemoval |
|---|---|---|
| Delete parent | Deletes children ✅ | Deletes children ✅ |
| Remove child from list | Child NOT deleted (still has FK) | Child DELETED from DB |
| Removal from collection | No DB change | DELETE issued |

**Best practice:**
- `OneToMany(mappedBy="order", cascade = CascadeType.ALL, orphanRemoval = true)` for parent-owned children (OrderItems)
- Do NOT cascade REMOVE/ALL on ManyToOne/ManyToMany — can delete data unexpectedly

---

## 6. Querying

### Q: JPQL vs Native SQL vs Criteria API?

| | JPQL | Native SQL | Criteria API |
|---|---|---|---|
| Type | Entity-based | Table-based | Programmatic |
| Example | `SELECT o FROM Order o WHERE o.status = :status` | `SELECT * FROM orders WHERE status = ?` | `cb.createQuery(Order.class)` |
| Portability | Portable across DBs | DB-specific | Portable |
| Compile check | Not at build, validated at runtime | Not validated | Type-safe if using metamodel |
| Use case | Most queries | Complex/DB-specific queries | Dynamic queries (search filters) |

**JPQL example:**
```java
@Query("SELECT o FROM Order o WHERE o.user.email = :email AND o.status = :status")
List<Order> findOrdersByUserAndStatus(@Param("email") String email,
                                       @Param("status") OrderStatus status);
```

**Native query example:**
```java
@Query(value = "SELECT * FROM orders WHERE DATE(created_at) = CURDATE()", nativeQuery = true)
List<Order> findTodayOrders();
```

---

## 7. Performance Optimization

### Q: What causes slow Hibernate applications?

1. **N+1 queries** — missing fetch strategy
2. **EAGER loading everywhere** — loads too much at once
3. **Large pagination with offset** — `LIMIT 10000, 20` is slow
4. **Long transactions** — hold locks, increase deadlock risk
5. **Missing indexes** — full table scans
6. **Too many queries** — batch lacks (`hibernate.jdbc.batch_size`)
7. **Memory leaks** — unbounded first-level caches in long-lived sessions

### Q: How do you tune Hibernate?

```properties
# Batch processing
spring.jpa.properties.hibernate.jdbc.batch_size=20
spring.jpa.properties.hibernate.order_inserts=true
spring.jpa.properties.hibernate.order_updates=true

# SQL logging (dev only)
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true

# Fetching
spring.jpa.properties.hibernate.default_batch_fetch_size=20

# Pool
spring.datasource.hikari.maximum-pool-size=20
```

### Q: What are common Hibernate pitfalls?

| Pitfall | Fix |
|---|---|
| N+1 queries | `JOIN FETCH`, `@EntityGraph`, `@BatchSize` |
| `LazyInitializationException` | Fetch in transaction / DTO projections |
| Modifying detached entities silently | Use `merge()` |
| Using entity directly in API response | Use DTOs |
| EAGER on ManyToOne by default | Set `fetch = FetchType.LAZY` |
| Massive paging (LIMIT with large offset) | Keyset/cursor pagination |
| Updating whole aggregate when only one field changed | Let dirty checking handle it, avoid `update()` on all |

---

## 8. Hibernate vs Spring Data JPA

| | Hibernate (raw) | Spring Data JPA |
|---|---|---|
| API | `Session`, `SessionFactory` | `JpaRepository<T, ID>` interfaces |

---

## Related Notes

- [Spring Boot Interview Questions](../Spring%20Boot/Spring-Boot-Interview-Questions.md)
- [Java Core Interview Questions](../Java%20Core/Core-Java-Interview-Questions.md)
- [SQL Interview Questions](../SQL/SQL-Interview-Questions.md)