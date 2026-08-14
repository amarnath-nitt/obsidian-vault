# Spring Boot Interview Questions

Comprehensive interview preparation for Spring Boot covering core concepts, auto-configuration, annotations, transactions, testing, and common production issues.

---

## 1. Spring Core Fundamentals

### Q: What is the Spring IoC Container?

**Answer shape:** Definition → Purpose → Mechanism → Example → Trade-off

The Spring IoC (Inversion of Control) container manages object creation, wiring, and lifecycle. Instead of your code creating dependencies with `new`, the container injects them.

**Mechanism:**
1. Container reads configuration (XML, annotations, or Java config)
2. Creates bean definitions
3. Instantiates beans and resolves dependencies
4. Manages lifecycle (init, destroy)
5. Provides beans to requesting code

**Key interfaces:**
- `ApplicationContext` — the primary container interface
- `BeanFactory` — lower-level container (lazy initialization)

### Q: What are the bean scopes in Spring?

| Scope | Description | When to Use |
|---|---|---|
| `singleton` | One instance per container (default) | Stateless services, repositories |
| `prototype` | New instance per request for bean | Stateful beans |
| `request` | One instance per HTTP request (web only) | Request-scoped state |
| `session` | One instance per HTTP session (web only) | User session data |
| `application` | One instance per `ServletContext` | App-wide shared state |
| `websocket` | One instance per WebSocket | WebSocket session state |

**Interview trap:** A singleton bean injected with a `@Scope("prototype")` bean gets the prototype instance **at injection time** — it does not get a new instance per method call unless you use `ObjectProvider<T>` or `@Lookup`.

### Q: Explain dependency injection types

| Type | How | Pros | Cons |
|---|---|---|---|
| Constructor | `@Autowired` on constructor | Immutable, testable, fails fast | Verbose with many deps |
| Setter | `@Autowired` on setter | Optional deps, reconfigurable | Mutable state |
| Field | `@Autowired` on field | Concise | Hard to test, hidden deps, not recommended |

**Best practice:** Use **constructor injection** → required dependencies become `final`, explicit, and impossible to forget.

```java
@Service
public class OrderService {
    private final OrderRepository orderRepository;
    private final PaymentGateway paymentGateway;

    // Constructor injection - Spring 4.3+ can autowire with single constructor
    public OrderService(OrderRepository orderRepository, PaymentGateway paymentGateway) {
        this.orderRepository = orderRepository;
        this.paymentGateway = paymentGateway;
    }
}
```

### Q: What is circular dependency? How do you solve it?

Circular dependency = Bean A depends on B, B depends on A.

**Symptom:** `BeanCurrentlyInCreationException` at startup.

**Solutions:**
1. **Refactor** — split the dependency, break the cycle (best)
2. Use `@Lazy` on one dependency to break eager initialization
3. Use `ObjectProvider<T>` for lazy resolution
4. Use setter/field injection (not recommended — hides the problem)

> ⚠️ **Interview insight:** Circular dependencies indicate a design problem. The right answer is usually "refactor to remove the cycle" — not "use @Lazy."

---

## 2. Spring Boot Auto-Configuration

### Q: How does Spring Boot auto-configuration work?

**Mechanism:**
1. `@SpringBootApplication` includes `@EnableAutoConfiguration`
2. Spring Boot looks for `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports` on the classpath
3. Each auto-configuration class has `@Conditional*` annotations
4. Conditions decide **if** a configuration is active based on:
   - `@ConditionalOnClass` — class on classpath
   - `@ConditionalOnMissingBean` — bean not already defined
   - `@ConditionalOnProperty` — property value
   - `@ConditionalOnWebApplication` — web context type
5. Matching configurations create beans with sensible defaults

**Example:** Adding `spring-boot-starter-data-jpa` + a `DataSource` on classpath → `@ConditionalOnClass` triggers `HibernateJpaAutoConfiguration` → creates `EntityManagerFactory`, `TransactionManager`, etc.

### Q: How do you override auto-configured beans?

| Level | Method |
|---|---|
| Application | Define your own `@Bean` — `@ConditionalOnMissingBean` defers to yours |
| Property | Set `spring.*` properties in `application.yml` |
| Exclude | `@SpringBootApplication(exclude = DataSourceAutoConfiguration.class)` |
| Profile | Use `@Profile` for environment-specific beans |

```java
@Configuration
@Profile("prod")
public class ProdDataSourceConfig {
    @Bean
    public DataSource dataSource() {
        // custom production DataSource
    }
}
```

### Q: What is `@ConditionalOnMissingBean` vs `@ConditionalOnClass`?

- `@ConditionalOnClass`: activates condition based on **classpath presence**
- `@ConditionalOnMissingBean`: activates only if **no bean of that type exists**
- `@ConditionalOnProperty`: activates based on **property value**

```java
@Configuration
@ConditionalOnClass(DataSource.class)
@ConditionalOnProperty(name = "app.db.enabled", havingValue = "true")
public class DatabaseConfig {
    @Bean
    @ConditionalOnMissingBean
    public JdbcTemplate jdbcTemplate(DataSource ds) {
        return new JdbcTemplate(ds);
    }
}
```

---

## 3. Spring Boot Annotations Cheat Sheet

### Core Composition Annotations

| Annotation | Composes | Purpose |
|---|---|---|
| `@SpringBootApplication` | `@Configuration` + `@EnableAutoConfiguration` + `@ComponentScan` | Entry point |
| `@RestController` | `@Controller` + `@ResponseBody` | REST API handler |
| `@Service` | `@Component` | Business logic |
| `@Repository` | `@Component` | Data access, persistence exception translation |
| `@Configuration` | — | Bean definitions |
| `@ControllerAdvice` | `@Component` | Global exception handling |

### Request Mapping

| Annotation | HTTP Method |
|---|---|
| `@GetMapping` | GET |
| `@PostMapping` | POST |
| `@PutMapping` | PUT (full update) |
| `@PatchMapping` | PATCH (partial update) |
| `@DeleteMapping` | DELETE |
| `@RequestMapping` | General mapping (method level or class level) |

### Request Data Binding

| Annotation | Binds From |
|---|---|
| `@PathVariable` | URL path: `/users/{id}` |
| `@RequestParam` | Query string: `?page=1` |
| `@RequestBody` | Request body (JSON) |
| `@RequestHeader` | HTTP headers |
| `@RequestPart` | Multipart file/part |
| `@CookieValue` | Cookie |
| `@ModelAttribute` | Form data / query params to object |

### Response

| Annotation | Purpose |
|---|---|
| `@ResponseStatus(HttpStatus.CREATED)` | Fixed status code |
| `ResponseEntity<T>` | Full control (status, headers, body) |
| `@ResponseBody` | Serialize to JSON/XML |

---

## 4. Spring MVC & REST API Design

### Q: Design a REST API for an Order resource

```
GET    /api/orders          → List orders (paginated)
GET    /api/orders/{id}     → Get order by id
POST   /api/orders          → Create order
PUT    /api/orders/{id}     → Full update
PATCH  /api/orders/{id}     → Partial update
DELETE /api/orders/{id}     → Delete order
```

**Best practices:**
- Use plural nouns for resources
- Use HTTP methods for semantics
- Return proper status codes (200, 201, 204, 400, 401, 403, 404, 409, 422, 500)
- Use DTOs — never expose entities directly
- Validate at the API boundary
- Support pagination (`page`, `size`, `sort`)
- Return consistent error responses
- Use idempotency keys for POST when needed

### Q: How do you implement global exception handling?

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(ResourceNotFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public ErrorResponse handleNotFound(ResourceNotFoundException ex) {
        return new ErrorResponse("NOT_FOUND", ex.getMessage());
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public ErrorResponse handleValidation(MethodArgumentNotValidException ex) {
        Map<String, String> errors = ex.getBindingResult()
            .getFieldErrors()
            .stream()
            .collect(Collectors.toMap(FieldError::getField, FieldError::getDefaultMessage));
        return new ErrorResponse("VALIDATION_FAILED", errors);
    }

    @ExceptionHandler(Exception.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public ErrorResponse handleGeneric(Exception ex) {
        // Log full stack trace, return generic message
        return new ErrorResponse("INTERNAL_ERROR", "Something went wrong");
    }
}
```

**Best practice:** Never expose internal exception messages/stacks to clients. Log them server-side.

### Q: What is the difference between `@Controller` and `@RestController`?

| | `@Controller` | `@RestController` |
|---|---|---|
| Returns | View name (JSP/Thymeleaf) | Object → JSON/XML directly |
| `@ResponseBody` | Required on each method | Implicit |
| Use case | MVC pages | REST APIs |

---

## 5. Spring Data JPA & Hibernate

### Q: What is the N+1 query problem and how do you solve it?

**Problem:** For one entity fetch + N child fetches = N+1 queries.

```java
// N+1: Each order triggers a separate query for user
List<Order> orders = orderRepository.findAll();
for (Order order : orders) {
    System.out.println(order.getUser().getName()); // N queries!
}
```

**Solutions:**
1. **`JOIN FETCH`** — eager fetch in a custom query
   ```java
   @Query("SELECT o FROM Order o JOIN FETCH o.user")
   List<Order> findAllWithUser();
   ```
2. **`@EntityGraph`** — named entity graph attribute paths
   ```java
   @EntityGraph(attributePaths = {"user", "items"})
   @Query("SELECT o FROM Order o")
   List<Order> findAllWithDetails();
   ```
3. **Batch fetching** — `@BatchSize(size = 20)`
4. **DTO projections** — select only needed columns

### Q: Explain JPA relationship types & fetch strategies

| Annotation | Default Fetch | Use Case |
|---|---|---|
| `@OneToOne` | EAGER | User ↔ Profile |
| `@OneToMany` | LAZY | Order → Items |
| `@ManyToOne` | EAGER (change to LAZY!) | Item → Category |
| `@ManyToMany` | LAZY | Student ↔ Course |

**Best practice:** Use `LAZY` everywhere, then use `JOIN FETCH` or `@EntityGraph` where you know you need the data.

### Q: What JPA cascade types exist?

| Cascade | Impact |
|---|---|
| `PERSIST` | Save operation cascades |
| `MERGE` | Update cascades |
| `REMOVE` | Delete cascades |
| `REFRESH` | Refresh cascades |
| `DETACH` | Detach cascades |
| `ALL` | All of the above |

```java
@Entity
public class Order {
    @OneToMany(mappedBy = "order", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<OrderItem> items;
}
```

> ⚠️ Do NOT cascade `REMOVE`/`ALL` on `@ManyToOne` or `@ManyToMany` — you may delete data unexpectedly.

### Q: What is the difference between `save()` and `saveAndFlush()`?

- `save()`: persists/merges entity; may not immediately flush to DB
- `saveAndFlush()`: saves and forces a flush to ensure the query runs immediately

**Why flush matters:** To get the generated ID, read DB-generated values in the same transaction, or make changes visible to a native query.

### Q: What are the JPA states of an entity?

```
New/Transient → Managed (persist) → Detached (clear/close) → Removed
```

| State | Description |
|---|---|
| **Transient** | New entity, not yet associated with PersistenceContext |
| **Managed** | Attached to PersistenceContext, tracked for changes |
| **Detached** | Was managed, context closed/cleared. Changes not tracked |
| **Removed** | Marked for deletion, removed on flush |

### Q: Explain transaction propagation

| Propagation | Behavior |
|---|---|
| `REQUIRED` (default) | Join existing transaction or create new |
| `REQUIRES_NEW` | Suspend current, always create new |
| `SUPPORTS` | Join if exists, otherwise run without |
| `NOT_SUPPORTED` | Suspend current, run without |
| `MANDATORY` | Must join existing, throw if none |
| `NEVER` | Must NOT run in a transaction |
| `NESTED` | Savepoint within existing transaction |

**Interview example:**

```java
@Service
public class OrderService {
    @Transactional
    public void createOrder(Order order) {
        orderRepository.save(order);
        auditService.record(order); // would auditService failure roll back the order? 
    }
}
```

**Answer:** If `record()` throws a runtime exception, the whole transaction rolls back — including the order save. To keep the audit independent, use `REQUIRES_NEW` propagation.

### Q: What transaction isolation levels exist?

| Level | Dirty Read | Non-repeatable Read | Phantom Read |
|---|---|---|---|
| `READ_UNCOMMITTED` | Possible | Possible | Possible |
| `READ_COMMITTED` | Prevented | Possible | Possible |
| `REPEATABLE_READ` | Prevented | Prevented | Possible |
| `SERIALIZABLE` | Prevented | Prevented | Prevented |

- **Dirty Read:** Read uncommitted data from another transaction
- **Non-repeatable Read:** Same row read twice, different values (row updated between reads)
- **Phantom Read:** Same query returns different rows (rows inserted/deleted between reads)

> 💡 **Hibernate tip:** In JPA, `REPEATABLE_READ` behavior can also be achieved with optimistic locking (`@Version`) — check for `OptimisticLockException` in distributed/high-concurrency scenarios.

### Q: How do you implement pagination with Spring Data JPA?

```java
Page<Order> page = orderRepository.findAll(PageRequest.of(0, 10, Sort.by("createdAt").descending()));
List<Order> orders = page.getContent();
int totalPages = page.getTotalPages();
long totalElements = page.getTotalElements();
```

For large datasets, prefer **cursor-based (keyset) pagination**:

```java
@Query("SELECT o FROM Order o WHERE o.id < :lastId ORDER BY o.id DESC LIMIT :size")
List<Order> findNextPage(@Param("lastId") Long lastId, @Param("size") int size);
```

---

## 6. Spring Transactions — Common Traps

### Trap 1: Self-invocation bypasses the proxy

```java
@Service
public class OrderService {
    @Transactional
    public void processOrder() {
        // This call does NOT go through the proxy
        // → sendNotification() runs WITHOUT a transaction
        sendNotification();
    }

    @Transactional(propagation = Propagation.REQUIRES_NEW)
    public void sendNotification() { }
}
```

**Fixes:**
1. Inject `self` via `@Lazy`:
   ```java
   @Service
   public class OrderService {
       private final OrderService self;

       public OrderService(@Lazy OrderService self) {
           this.self = self;
       }
   }
   ```
2. Use `TransactionTemplate`
3. Extract to a separate bean

### Trap 2: `@Transactional` on non-public methods

Spring's proxy-based `@Transactional` only applies to **public methods**. Protected/private methods silently ignore the annotation.

### Trap 3: Exceptions not triggering rollback

```java
@Transactional
public void createOrder() {
    try {
        // ...
    } catch (Exception e) {
        log.error("Error", e);
        // Exception swallowed → transaction COMMITS!
    }
}
```

**Default rollback rule:** Runtime exceptions (unchecked) trigger rollback. Checked exceptions do NOT. Use `rollbackFor`:

```java
@Transactional(rollbackFor = Exception.class)
```

---

## 7. Spring Boot Testing

### Test Pyramid for Spring Boot

| Level | What | Tools | Speed |
|---|---|---|---|
| Unit | Single class, mock deps | JUnit 5, Mockito | Very fast |
| Slice | Layer in isolation | `@WebMvcTest`, `@DataJpaTest` | Fast |
| Integration | Multiple layers | `@SpringBootTest`, Testcontainers | Slow |

### Q: `@WebMvcTest` vs `@SpringBootTest`

| | `@WebMvcTest` | `@SpringBootTest` |
|---|---|---|
| Scope | Only web layer (controllers, filters, advice) | Full context |
| Mocks | `@MockBean` services | Real beans (use `@MockBean` selectively) |
| Speed | Fast, no DB | Slow, full context |
| Use | Controller tests | End-to-end integration tests |

### Example: Controller test

```java
@WebMvcTest(OrderController.class)
class OrderControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private OrderService orderService;

    @Test
    void shouldReturnOrder() throws Exception {
        OrderResponse order = new OrderResponse(1L, 100.00, "PENDING");
        when(orderService.getOrder(1L)).thenReturn(order);

        mockMvc.perform(get("/api/orders/1"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.id").value(1))
            .andExpect(jsonPath("$.status").value("PENDING"));
    }
}
```

### Example: JPA slice test with Testcontainers

```java
@DataJpaTest
@Testcontainers
class OrderRepositoryTest {

    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:16");

    @DynamicPropertySource
    static void datasourceProps(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgres::getJdbcUrl);
        registry.add("spring.datasource.username", postgres::getUsername);
        registry.add("spring.datasource.password", postgres::getPassword);
    }

    @Autowired
    private OrderRepository orderRepository;

    @Test
    void shouldFindOrdersByStatus() {
        // ...
    }
}
```

---

## 8. Spring Boot Production Considerations

### Q: How do you handle configuration for different environments?

1. **Properties files:** `application-{profile}.yml`
   - `application-dev.yml`
   - `application-prod.yml`
   - Activate with `SPRING_PROFILES_ACTIVE=prod`
2. **Environment variables:** `SPRING_DATASOURCE_URL`, etc.
3. **External config:** Spring Cloud Config, Kubernetes ConfigMap/Secret
4. **Never commit secrets:** use environment-specific secret management (Vault, AWS Secrets Manager, K8s Secrets)

```yaml
# application.yml
spring:
  profiles:
    active: ${SPRING_PROFILES_ACTIVE:dev}
---
spring:
  config:
    activate:
      on-profile: prod
datasource:
  url: ${DB_URL}
  username: ${DB_USERNAME}
  password: ${DB_PASSWORD}
```

### Q: How do you handle idempotency in REST APIs?

**Problem:** Client retries a POST → duplicate resource created.

**Solution:** Idempotency key header.

```java
@PostMapping("/payments")
public ResponseEntity<?> createPayment(
    @RequestHeader("Idempotency-Key") String idempotencyKey,
    @RequestBody PaymentRequest request) {
    
    // Check if already processed
    Optional<Payment> existing = paymentRepository.findByIdempotencyKey(idempotencyKey);
    if (existing.isPresent()) {
        return ResponseEntity.ok(existing.get()); // Return cached result
    }
    
    Payment payment = paymentService.process(request, idempotencyKey);
    return ResponseEntity.status(HttpStatus.CREATED).body(payment);
}
```

**Patterns:**
- Store idempotency key in DB with unique constraint
- Use `UniqueConstraint` on the key column
- Return the original response on retry

### Q: How do you handle retries with Spring Retry?

```java
@Retryable(
    retryFor = {TimeoutException.class, IOException.class},
    noRetryFor = {IllegalArgumentException.class},
    maxAttempts = 3,
    backoff = @Backoff(delay = 1000, multiplier = 2))
public Invoice generateInvoice(Long orderId) {
    return externalBillingClient.generate(orderId);
}

// Only retry idempotent/safe operations!
// Never retry non-idempotent POST without idempotency key
```

### Q: How do you implement caching in Spring Boot?

```java
@Configuration
@EnableCaching
public class CacheConfig {
    @Bean
    public CacheManager cacheManager() {
        CaffeineCacheManager manager = new CaffeineCacheManager();
        manager.setCaffeine(Caffeine.newBuilder()
            .maximumSize(500)
            .expireAfterWrite(Duration.ofMinutes(10)));
        return manager;
    }
}

@Service
public class ProductService {
    @Cacheable(value = "products", key = "#id")
    public Product getProduct(Long id) {
        // Expensive DB call - result cached
    }

    @CacheEvict(value = "products", key = "#product.id")
    public void updateProduct(Product product) {
        // Invalidates cache entry
    }

    @CachePut(value = "products", key = "#product.id")
    public Product saveProduct(Product product) {
        // Always executes and updates cache
    }
}
```

**Important:** Annotate only the **public method called from outside the bean** — self-invocation bypasses the cache proxy too.

---

## 9. Spring Security Essentials

### Q: How does Spring Security filter chain work?

```
Client → FilterChain
    ├── SecurityContextPersistenceFilter  → Load/save security context
    ├── CsrfFilter                         → CSRF token validation
    ├── UsernamePasswordAuthenticationFilter → Form login / JSON auth
    ├── BasicAuthenticationFilter          → HTTP Basic auth
    ├── BearerTokenAuthenticationFilter    → JWT/OAuth2 token
    ├── AuthorizationFilter                → URL authorization
    └── Controller
```

### Q: Configure JWT authentication

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .csrf(csrf -> csrf.disable())
            .sessionManagement(sm -> sm.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/auth/**", "/actuator/health").permitAll()
                .requestMatchers("/api/admin/**").hasRole("ADMIN")
                .anyRequest().authenticated())
            .addFilterBefore(jwtFilter, UsernamePasswordAuthenticationFilter.class);
        return http.build();
    }
}
```

### Q: What is the difference between authentication and authorization?

- **Authentication:** Who are you? (verify identity — username/password, JWT, OAuth2)
- **Authorization:** What can you do? (roles/permissions — ROLE_ADMIN, SCOPE_read)

---

## 10. Spring Boot Performance & Troubleshooting

### Q: Common causes of slow Spring Boot applications

1. **N+1 queries** — missing `JOIN FETCH`/`@EntityGraph`
2. **Missing indexes** — full table scans
3. **Connection pool exhaustion** — too few connections, slow queries holding them
4. **Synchronous blocking calls** — external HTTP calls without timeout
5. **Large payloads** — no pagination, EAGER loading
6. **Memory leaks** — caches growing unbounded, no eviction
7. **GC pressure** — too many short-lived objects, large heap allocations

### Q: How do you diagnose a slow endpoint?

1. Check metrics (Micrometer/Prometheus): latency, throughput, error rate
2. Check DB query logs / slow query log
3. Use distributed tracing (Zipkin, Jaeger) for span latency
4. Profile with JFR (Java Flight Recorder)
5. Check connection pool stats
6. Load test with k6/JMeter to reproduce

### Q: How do you enable health checks and metrics?

```yaml
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus
  health:
    probes:
      enabled: true
```

---

## 11. Spring Boot Advanced Topics

### Q: What is Spring AOP and `@Aspect`?

Spring AOP intercepts method calls using **dynamic proxies**.

```java
@Aspect
@Component
public class LoggingAspect {

    @Around("@annotation(LogExecutionTime)")
    public Object logExecutionTime(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();
        Object result = joinPoint.proceed();
        long elapsed = System.currentTimeMillis() - start;
        log.info("{} executed in {} ms", joinPoint.getSignature(), elapsed);
        return result;
    }
}
```

**Limitations:** Only intercepts calls **through Spring proxies** (public methods, called from outside the bean).

### Q: What is Spring Boot Actuator?

Actuator provides production-ready endpoints:
- `/actuator/health` — liveness/readiness
- `/actuator/metrics` — JVM, HTTP, DB metrics
- `/actuator/loggers` — change log levels at runtime
- `/actuator/env` — environment properties (secure!)
- `/actuator/threaddump` — thread dump
- `/actuator/heapdump` — heap dump

### Q: What is the difference between `@Component`, `@Service`, `@Repository`, `@Controller`?

All are `@Component` specializations — they enable component scanning. The difference is semantic:

| Annotation | Purpose | Special behavior? |
|---|---|---|
| `@Component` | Generic bean | — |
| `@Service` | Business logic layer | None (semantic only) |
| `@Repository` | Data access layer | Persistence exception translation |
| `@Controller` | Web controllers | View resolution, `@ResponseBody` |
| `@RestController` | REST API | Implicit `@ResponseBody` |

---

## 12. Spring Boot Interview Quick Reference Cards

### Card 1: `@SpringBootApplication` = Composition

```
@SpringBootApplication = @Configuration + @EnableAutoConfiguration + @ComponentScan
```

### Card 2: Common Annotations Summary

```
Bean creation:     @Component, @Service, @Repository, @Controller, @Bean, @Configuration
Dependency:        @Autowired, @Qualifier, @Primary, @Value
Web:               @RestController, @RequestMapping, @GetMapping, @PostMapping, @RequestBody
Validation:        @Valid, @Validated, @NotNull, @Size, @Email, @Pattern
Transaction:       @Transactional, @EnableTransactionManagement
Data:              @Entity, @Table, @Id, @GeneratedValue, @Column, @OneToMany, @ManyToOne
Cache:             @EnableCaching, @Cacheable, @CacheEvict, @CachePut
Async:             @EnableAsync, @Async
Scheduling:        @EnableScheduling, @Scheduled
Testing:           @SpringBootTest, @WebMvcTest, @DataJpaTest, @MockBean, @Testcontainers
```

### Card 3: `@Transactional` Checklist

```
1. Only public methods are proxied
2. Self-invocation must be refactored (@Lazy self or separate bean)
3. Runtime exceptions roll back by default
4. Checked exceptions need rollbackFor = Exception.class
5. Propagation: REQUIRED (default), REQUIRES_NEW for independent work
6. Isolation: READ_COMMITTED most common; SERIALIZABLE for strict consistency
7. Keep transactions SHORT — never do external HTTP calls inside a transaction
```

### Card 4: JPA Pitfalls Checklist

```
❌ N+1 queries            → ✅ JOIN FETCH / @EntityGraph / @BatchSize
❌ EAGER fetch everywhere → ✅ LAZY + explicit fetch when needed
❌ Exposing entities as DTOs → ✅ Use DTOs / projections
❌ Massive page sizes     → ✅ Cursor pagination for large datasets
❌ Cascade ALL everywhere → ✅ Cascade ALL/REMOVE only on owning relationships
❌ Long transactions      → ✅ Short transactions, no I/O inside
❌ LazyLoadingException   → ✅ Fetch in transaction or use DTO projections
```

### Card 5: REST API Status Codes

```
200 OK          — Success
201 Created     — Resource created (POST)
204 No Content  — Success no body (DELETE)
400 Bad Request — Validation failed / malformed request
401 Unauthorized — Missing/invalid credentials
403 Forbidden   — Authenticated but no permission
404 Not Found   — Resource doesn't exist
409 Conflict    — State conflict (duplicate, version mismatch)
422 Unprocessable Entity — Semantic validation failure
429 Too Many Requests — Rate limited
500 Internal Server Error — Unexpected error
```

---

## Quick Practice Checklist

- [ ] Can explain IoC, DI, bean lifecycle, scopes
- [ ] Can explain auto-configuration conditions
- [ ] Can write `@RestController` with validation and proper status codes
- [ ] Can implement global exception handling
- [ ] Can explain N+1 problem with 3 solutions
- [ ] Can explain entity states and cascade types
- [ ] Can choose transaction propagation and isolation correctly
- [ ] Can explain why self-invocation breaks `@Transactional`
- [ ] Can write controller tests with MockMvc
- [ ] Can write repository tests with Testcontainers
- [ ] Can explain security filter chain and configure JWT auth
- [ ] Can set up health, metrics, and logging
- [ ] Can identify slow endpoint causes
- [ ] Can explain caching with `@Cacheable`

---

## Related Notes

- [[Java-Backend-Interview-Roadmap]]
- [[SQL-Interview-Questions]]
- [[Current-Java-and-Spring-Backend-Standards]]
- [[Core-Java-Interview-Questions]]
- [[Java-8-and-Streams-Interview-Questions]]
- [[Docker-for-Java-Developers-Interview-Guide|Docker Guide (HLD)]]
