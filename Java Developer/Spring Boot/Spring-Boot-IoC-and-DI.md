# Spring Boot - IoC and Dependency Injection

Understanding Inversion of Control (IoC) and Dependency Injection (DI) — the core concepts of the Spring Framework.

---

## 🎯 Key Concepts

### What is IoC (Inversion of Control)?

IoC means **the control of object creation and lifecycle is transferred to the Spring Framework** instead of your code manually creating and managing objects.

**Without IoC (Traditional approach):**
```java
public class UserService {
    private UserRepository userRepository = new UserRepository();  // Manual creation
}
```

**With IoC (Spring approach):**
```java
@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;  // Spring creates & injects
}
```

### What is Dependency Injection (DI)?

DI is a technique where **objects receive their dependencies from external sources** rather than creating them internally.

---

## 📌 Types of Dependency Injection

### 1. Constructor Injection (⭐ Recommended)
```java
@Service
public class UserService {
    private final UserRepository userRepository;
    private final EmailService emailService;
    
    // Constructor injection
    public UserService(UserRepository userRepository, EmailService emailService) {
        this.userRepository = userRepository;
        this.emailService = emailService;
    }
}
```
✅ **Pros:** Immutable, testable, explicit dependencies
❌ **Cons:** Verbose

### 2. Setter Injection
```java
@Service
public class UserService {
    private UserRepository userRepository;
    
    @Autowired
    public void setUserRepository(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
}
```
✅ **Pros:** Flexible, optional dependencies
❌ **Cons:** Mutable, can be null

### 3. Field Injection (❌ Not Recommended)
```java
@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;
}
```
❌ **Cons:** Hard to test, hard to debug, mutable, hidden dependencies

---

## 🔄 Bean Lifecycle

**When Spring creates a bean, it goes through these phases:**

1. **Instantiation** — Object created
2. **Populate Properties** — Fields set via DI
3. **Set Bean Name** (if `BeanNameAware`)
4. **Set Bean Factory** (if `BeanFactoryAware`)
5. **Post-process Before Init** (`@PostConstruct`)
6. **Init** (if `InitializingBean` or `@Bean(initMethod=...)`)
7. **Post-process After Init** (AOP proxies created here)
8. **Ready to use** ✅
9. **Destroy** (on shutdown) — `@PreDestroy` called

```java
@Component
public class MyBean implements InitializingBean, DisposableBean {
    
    @PostConstruct
    public void init() {
        System.out.println("1. After dependencies injected");
    }
    
    @Override
    public void afterPropertiesSet() {
        System.out.println("2. InitializingBean.afterPropertiesSet()");
    }
    
    @PreDestroy
    public void cleanup() {
        System.out.println("3. Before bean destroyed");
    }
    
    @Override
    public void destroy() {
        System.out.println("4. DisposableBean.destroy()");
    }
}
```

---

## 🎯 Bean Scopes

| Scope | Lifetime | Use Case |
|-------|----------|----------|
| **singleton** (default) | Entire app | Stateless services, repositories |
| **prototype** | New instance per request | Stateful objects |
| **request** | Per HTTP request | Web only, request-scoped data |
| **session** | Per user session | Web only, session-scoped data |
| **application** | Entire web application | App-wide singleton in web context |
| **websocket** | Per WebSocket session | WebSocket connections |

```java
@Component
@Scope("singleton")  // Default
public class SingletonBean { }

@Component
@Scope("prototype")
public class PrototypeBean { }

@Component
@Scope("request")  // Web only
public class RequestScopedBean { }
```

---

## 🔍 Autowiring

### 1. By Type (Default)
```java
@Autowired
private UserRepository userRepository;  // Matches by type
```

### 2. By Name
```java
@Autowired
@Qualifier("userRepositoryImpl")
private UserRepository userRepository;
```

### 3. By Custom Annotation
```java
@Autowired
@Qualifier("primary")
private UserRepository userRepository;
```

### 4. Primary Bean
```java
@Configuration
public class BeanConfig {
    @Bean
    @Primary
    public UserRepository primaryRepo() {
        return new UserRepositoryImpl();
    }
}
```

---

## ⚠️ Common Interview Questions

1. **What's the difference between IoC and DI?**
   - IoC: Framework controls object creation
   - DI: Framework injects dependencies into objects

2. **Which DI type should you use?**
   - Constructor injection (recommended — immutable, testable)
   - Setter injection (optional dependencies)
   - Field injection (avoid — hard to test)

3. **What happens if two beans of the same type exist?**
   - `NoUniqueBeanDefinitionException`
   - Solution: Use `@Primary` or `@Qualifier`

4. **Can you explain the bean lifecycle?**
   - Instantiation → DI → PostConstruct → Ready → Destroy

5. **What's the difference between singleton and prototype?**
   - Singleton: One instance for entire app
   - Prototype: New instance every time

---

## 🧪 Testing with Dependency Injection

```java
@SpringBootTest
class UserServiceTest {
    
    @MockBean
    private UserRepository userRepository;
    
    @Autowired
    private UserService userService;
    
    @Test
    void testGetUser() {
        when(userRepository.findById(1L))
            .thenReturn(Optional.of(new User(1L, "John")));
        
        User result = userService.getUser(1L);
        
        assertEquals("John", result.getName());
    }
}
```

---

## Related

- [Spring Boot Index](Java%20Developer/Spring%20Boot/00%20-%20Index.md)
- [Spring Boot Interview Questions](Spring-Boot-Interview-Questions.md)
- [Java Developer Index](../00%20-%20Index.md)
