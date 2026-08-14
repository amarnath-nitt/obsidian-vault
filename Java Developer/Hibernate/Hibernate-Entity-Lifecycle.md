# Hibernate - Entity Lifecycle

Understanding the four states of Hibernate entities and how to manage them effectively.

---

## 🔄 Four Entity States

Every JPA entity transitions through these four states during its lifetime:

### 1. **Transient** (New)
- Object created but **not yet associated** with any Hibernate session
- **Not in database**
- Hibernate doesn't track it

```java
User user = new User("Alice", "alice@example.com");  // Transient
// user is not tracked by Hibernate
// Changing user.name won't be persisted
```

### 2. **Persistent** (Managed)
- Entity is **associated with active Hibernate session**
- **Changes automatically tracked** and persisted
- Saved to database in transaction
- Exists in session cache (identity map)

```java
User user = new User("Alice", "alice@example.com");
userRepository.save(user);  // Now Persistent

user.setName("Alice Smith");  // ✅ Change auto-tracked
// Hibernate detects change and updates DB
```

### 3. **Detached** (Disconnected)
- Entity was persistent but **session is closed**
- **Not tracked anymore** by Hibernate
- Changes won't be persisted automatically
- Data still exists in database

```java
@Transactional
public User getUser(Long id) {
    return userRepository.findById(id).orElse(null);
}  // Transaction ends, session closes, entity becomes Detached

User user = getUser(1L);
user.setName("New Name");  // ❌ Change is NOT persisted
// Need to merge() or saveAndFlush() to persist changes
```

### 4. **Removed** (Deleted)
- Entity was persistent but **marked for deletion**
- **Deleted from database** when transaction commits
- After deletion, entity is detached

```java
@Transactional
public void deleteUser(Long id) {
    User user = userRepository.findById(id).orElseThrow();
    userRepository.delete(user);  // Removed state
    // Deleted from DB when transaction commits
}
```

---

## 📊 State Transitions Diagram

```
Transient ──save()──> Persistent
   ↑                      ↓ flush()
   │                  Database
   │                      ↑
   └──merge()────← Detached
   
Persistent ──close()──> Detached
   ↓
delete()
   ↓
Removed ──commit()──> (deleted from DB)
```

---

## 🔍 Code Examples

### Transient to Persistent

```java
User user = new User("Bob", "bob@example.com");  // Transient

userRepository.save(user);  // Persistent (within transaction)
// Hibernate tracks and auto-persists

user.setName("Bob Smith");  // Auto-tracked, will update DB
```

### Persistent to Detached

```java
@Transactional
public User getUser(Long id) {
    User user = userRepository.findById(id).orElseThrow();  // Persistent
    return user;  // Still persistent while in transaction
}  // Transaction ends, entity becomes Detached

User user = getUser(1L);
user.setName("New Name");
// ❌ NOT persisted
userRepository.save(user);  // Need to save again
```

### Detached to Persistent (Merge)

```java
User detachedUser = ...;  // Not tracked

@Transactional
public void updateDetachedUser(User detachedUser) {
    User managedUser = entityManager.merge(detachedUser);  // Merge back
    managedUser.setName("Updated");  // Now tracked
    // Auto-persisted
}
```

### Persistent to Removed

```java
@Transactional
public void deleteUser(Long id) {
    User user = userRepository.findById(id).orElseThrow();  // Persistent
    userRepository.delete(user);  // Removed state
    // Deleted from DB on transaction commit
}
```

---

## ⚙️ Persistence Context

The **persistence context** is the cache of all persistent entities in a session.

```java
@Transactional
public void demonstratePersistenceContext() {
    User user1 = userRepository.findById(1L).orElseThrow();
    User user2 = userRepository.findById(1L).orElseThrow();
    
    // Same object reference! Retrieved from persistence context
    System.out.println(user1 == user2);  // true
    
    // Changes to either reference are tracked
    user1.setName("Updated");
    // Hibernate detects change and updates DB
}
```

---

## 🧪 Common Patterns

### Pattern: Update Detached Entity

```java
// Service layer (outside transaction)
public void updateUser(UserDto dto) {
    // dto maps to entity created earlier (detached)
    userService.saveUser(dto);
}

// Repository/Service layer (with transaction)
@Transactional
public void saveUser(UserDto dto) {
    User user = new User();  // Transient
    user.setId(dto.getId());
    user.setName(dto.getName());
    
    userRepository.saveAndFlush(user);  // Merge + Persistent + Flush
}
```

### Pattern: Avoid N+1 Queries

Use EAGER loading or JOIN FETCH to keep entities persistent and avoid separate queries when accessing relationships:

```java
@Entity
public class User {
    @OneToMany(mappedBy = "user", fetch = FetchType.EAGER)  // Load posts with user
    private List<Post> posts;
}

@Transactional
public void printAllPosts(List<User> users) {
    for (User user : users) {
        for (Post post : user.getPosts()) {  // ✅ No extra queries
            System.out.println(post.getTitle());
        }
    }
}
```

---

## ⚠️ Common Issues

### LazyInitializationException

```java
@Transactional
public List<User> getUsers() {
    return userRepository.findAll();  // Persistent within transaction
}

// Later, outside transaction:
List<User> users = getUsers();
System.out.println(users.get(0).getPosts().size());
// ❌ LazyInitializationException: posts not loaded and session closed

// Fix: Load within transaction
@Transactional(readOnly = true)
public List<User> getUsersWithPosts() {
    List<User> users = userRepository.findAll();
    users.forEach(u -> u.getPosts().size());  // Force load
    return users;
}
```

### Stale Data from Detached Entity

```java
User user = getUser(1L);  // Detached
Thread.sleep(5000);  // Some other process updates the database
System.out.println(user.getName());  // ❌ Stale data

// Fix: Refresh from database
@Transactional
public void refreshUser(User user) {
    entityManager.refresh(user);  // Re-fetch from DB
}
```

---

## ⚠️ Common Interview Questions

1. **What's the difference between transient and detached?**
   - Transient: Never saved to DB
   - Detached: Was saved but session closed

2. **What happens when you modify a detached entity?**
   - Change is NOT persisted unless you call merge() or save()

3. **Why do we get LazyInitializationException?**
   - Accessing lazy collection after session closed
   - Fix: Load within transaction or use EAGER fetch

4. **What's persistence context?**
   - Cache of all persistent entities in session
   - Same entity ID returns same object reference

---

## Related

- [Hibernate Index](Java%20Developer/Hibernate/00%20-%20Index.md)
- [Spring Boot Transactions](../Spring%20Boot/Spring-Boot-Transactions-and-JPA.md)
- [Java Developer Index](../00%20-%20Index.md)
