# Spring Boot - Transactions and JPA

Understanding transactions, propagation levels, isolation levels, and common JPA patterns in Spring Boot.

---

## 🔄 What is a Transaction?

A **transaction** is a sequence of database operations treated as a single unit of work. Either **all succeed** (commit) or **all fail** (rollback).

### ACID Properties

| Property | Meaning | Example |
|----------|---------|---------|
| **Atomicity** | All or nothing — entire operation succeeds or fails | Money transfer: both debit and credit happen |
| **Consistency** | Data remains valid after transaction | Account balance never negative |
| **Isolation** | Concurrent transactions don't interfere | Two simultaneous transfers don't corrupt data |
| **Durability** | Committed changes persist | Data survives system crash |

---

## 📌 @Transactional Annotation

```java
@Service
public class UserService {
    
    @Autowired
    private UserRepository userRepository;
    
    @Transactional  // Transaction starts here
    public void transferBalance(Long fromUserId, Long toUserId, BigDecimal amount) {
        User from = userRepository.findById(fromUserId).orElseThrow();
        User to = userRepository.findById(toUserId).orElseThrow();
        
        from.setBalance(from.getBalance().subtract(amount));
        to.setBalance(to.getBalance().add(amount));
        
        userRepository.save(from);
        userRepository.save(to);
        
        // Automatically committed if no exception
        // Automatically rolled back if exception occurs
    }
}
```

---

## 🔀 Propagation Levels

**Propagation** determines how transactions interact when one `@Transactional` method calls another.

| Level | Behavior |
|-------|----------|
| **REQUIRED** (default) | Use existing transaction, or create new one |
| **REQUIRES_NEW** | Always create new transaction (suspend existing) |
| **NESTED** | Create nested transaction (if supported) |
| **SUPPORTS** | Use existing transaction if available, otherwise non-transactional |
| **NOT_SUPPORTED** | Execute non-transactional (suspend if in transaction) |
| **NEVER** | Throw exception if in transaction |
| **MANDATORY** | Throw exception if not in transaction |

### Example

```java
@Service
public class UserService {
    
    @Autowired
    private UserRepository userRepository;
    
    @Autowired
    private AuditService auditService;
    
    // Scenario: Transfer fails, audit should still record it
    @Transactional
    public void transferBalance(Long fromId, Long toId, BigDecimal amount) {
        // ... transfer logic ...
        auditService.logTransaction(fromId, toId, amount);  // Different transaction
    }
}

@Service
public class AuditService {
    
    @Autowired
    private AuditRepository auditRepository;
    
    @Transactional(propagation = Propagation.REQUIRES_NEW)
    public void logTransaction(Long fromId, Long toId, BigDecimal amount) {
        // This runs in a separate transaction
        // If it fails, the main transfer is not affected
        AuditLog log = new AuditLog(fromId, toId, amount);
        auditRepository.save(log);
    }
}
```

---

## 🔐 Isolation Levels

**Isolation** controls how concurrent transactions interact. (Database-dependent)

| Level | Dirty Read | Non-Repeatable Read | Phantom Read |
|-------|-----------|-------------------|--------------|
| **READ_UNCOMMITTED** | ✅ Possible | ✅ Possible | ✅ Possible |
| **READ_COMMITTED** | ❌ No | ✅ Possible | ✅ Possible |
| **REPEATABLE_READ** | ❌ No | ❌ No | ✅ Possible |
| **SERIALIZABLE** | ❌ No | ❌ No | ❌ No |

```java
@Transactional(isolation = Isolation.READ_COMMITTED)
public void getAccountBalance(Long accountId) {
    // Can read committed data from other transactions
    // Prevents dirty reads but allows non-repeatable reads
}

@Transactional(isolation = Isolation.REPEATABLE_READ)
public void transferFunds() {
    // If you read a row twice in this transaction, values are same
}

@Transactional(isolation = Isolation.SERIALIZABLE)
public void criticalOperation() {
    // Safest but slowest — acts as if single-threaded
}
```

---

## ⚠️ Common Issues & Solutions

### N+1 Query Problem

❌ **Problem:** Getting list of users triggers query for each user's posts

```java
@Entity
public class User {
    @OneToMany(mappedBy = "user")  // Default: LAZY
    private List<Post> posts;
}

@Service
public class UserService {
    @Transactional
    public void printAllUserPosts(List<User> users) {
        for (User user : users) {
            for (Post post : user.getPosts()) {  // ❌ N+1: separate query per user!
                System.out.println(post.getTitle());
            }
        }
    }
}
```

✅ **Solution 1: Eager Loading**
```java
@Entity
public class User {
    @OneToMany(mappedBy = "user", fetch = FetchType.EAGER)
    private List<Post> posts;
}
```

✅ **Solution 2: JPQL JOIN FETCH**
```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    @Query("SELECT u FROM User u JOIN FETCH u.posts")
    List<User> findAllWithPosts();
}
```

✅ **Solution 3: Entity Graph**
```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    @EntityGraph(attributePaths = "posts")
    @Query("SELECT u FROM User u")
    List<User> findAllWithPosts();
}
```

### LazyInitializationException

❌ **Problem:** Accessing lazy collection outside transaction

```java
@Transactional
public List<User> getAllUsers() {
    return userRepository.findAll();  // Returns within transaction
}

// Later, outside transaction:
List<User> users = getAllUsers();
for (User user : users) {
    System.out.println(user.getPosts().size());  // ❌ LazyInitializationException!
}
```

✅ **Solution: Load within transaction**
```java
@Transactional
public List<User> getAllUsersWithPosts() {
    List<User> users = userRepository.findAll();
    users.forEach(u -> u.getPosts().size());  // Force load within transaction
    return users;
}
```

---

## 🧪 Testing Transactions

```java
@SpringBootTest
class UserServiceTest {
    
    @Autowired
    private UserService userService;
    
    @Autowired
    private UserRepository userRepository;
    
    @Test
    @Transactional
    void testTransfer() {
        User from = userRepository.save(new User("Alice", BigDecimal.valueOf(100)));
        User to = userRepository.save(new User("Bob", BigDecimal.valueOf(50)));
        
        userService.transferBalance(from.getId(), to.getId(), BigDecimal.valueOf(30));
        
        assertEquals(BigDecimal.valueOf(70), from.getBalance());
        assertEquals(BigDecimal.valueOf(80), to.getBalance());
    }
    
    @Test
    @Transactional
    void testRollback() {
        User user = userRepository.save(new User("Charlie", BigDecimal.valueOf(100)));
        
        assertThrows(Exception.class, () -> userService.failingOperation(user.getId()));
        
        // Transaction rolled back
        assertEquals(BigDecimal.valueOf(100), userRepository.findById(user.getId()).get().getBalance());
    }
}
```

---

## ⚠️ Common Interview Questions

1. **What's ACID?**
   - Atomicity, Consistency, Isolation, Durability — fundamental transaction properties

2. **Difference between READ_COMMITTED and REPEATABLE_READ?**
   - READ_COMMITTED: Can read newly committed data
   - REPEATABLE_READ: Same row always reads same value in transaction

3. **What causes N+1 problem?**
   - Lazy loading associations trigger additional queries
   - Solution: JOIN FETCH or Entity Graph

4. **When should you use `@Transactional(propagation = Propagation.REQUIRES_NEW)`?**
   - When you want child operation in separate transaction
   - Example: Audit logging should succeed even if main transaction fails

---

## Related

- [Spring Boot Index](Java%20Developer/Spring%20Boot/00%20-%20Index.md)
- [Spring Boot Interview Questions](Spring-Boot-Interview-Questions.md)
- [Hibernate Caching Strategy](../Hibernate/Hibernate-Caching-Strategy.md)
- [Java Developer Index](../00%20-%20Index.md)
