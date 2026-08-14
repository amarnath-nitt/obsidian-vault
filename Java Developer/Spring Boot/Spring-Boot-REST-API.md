# Spring Boot - REST API Development

Building RESTful APIs with Spring Boot — endpoints, validation, error handling, and content negotiation.

---

## 🚀 REST API Basics

REST (Representational State Transfer) uses HTTP methods to represent actions on resources.

### HTTP Methods

| Method | Purpose | Idempotent | Safe |
|--------|---------|-----------|------|
| **GET** | Retrieve resource | ✅ Yes | ✅ Yes |
| **POST** | Create resource | ❌ No | ❌ No |
| **PUT** | Replace entire resource | ✅ Yes | ❌ No |
| **PATCH** | Partial update | ❌ No* | ❌ No |
| **DELETE** | Delete resource | ✅ Yes | ❌ No |

---

## 📝 Building Controllers

### Basic REST Controller

```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @Autowired
    private UserService userService;
    
    // GET /api/users
    @GetMapping
    public ResponseEntity<List<UserDto>> getAllUsers() {
        return ResponseEntity.ok(userService.getAllUsers());
    }
    
    // GET /api/users/1
    @GetMapping("/{id}")
    public ResponseEntity<UserDto> getUser(@PathVariable Long id) {
        return ResponseEntity.ok(userService.getUserById(id));
    }
    
    // POST /api/users
    @PostMapping
    public ResponseEntity<UserDto> createUser(@RequestBody UserDto userDto) {
        UserDto created = userService.createUser(userDto);
        return ResponseEntity.status(HttpStatus.CREATED).body(created);
    }
    
    // PUT /api/users/1
    @PutMapping("/{id}")
    public ResponseEntity<UserDto> updateUser(
            @PathVariable Long id,
            @RequestBody UserDto userDto) {
        return ResponseEntity.ok(userService.updateUser(id, userDto));
    }
    
    // DELETE /api/users/1
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
        return ResponseEntity.noContent().build();
    }
}
```

---

## ✅ Input Validation

Use `@Valid` and `@Validated` with JSR-380 Bean Validation annotations.

```java
public class UserDto {
    @NotNull(message = "Name cannot be null")
    @Size(min = 2, max = 50, message = "Name must be 2-50 characters")
    private String name;
    
    @Email(message = "Email must be valid")
    private String email;
    
    @Positive(message = "Age must be positive")
    @Max(value = 120, message = "Age must be <= 120")
    private int age;
}

@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @PostMapping
    public ResponseEntity<UserDto> createUser(@Valid @RequestBody UserDto userDto) {
        // userDto is automatically validated before reaching this method
        return ResponseEntity.status(HttpStatus.CREATED).body(userService.createUser(userDto));
    }
}
```

---

## 🛑 Exception Handling

### Global Exception Handler

```java
@RestControllerAdvice
public class GlobalExceptionHandler {
    
    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleResourceNotFound(
            ResourceNotFoundException e, HttpServletRequest request) {
        ErrorResponse error = ErrorResponse.builder()
            .timestamp(LocalDateTime.now())
            .status(HttpStatus.NOT_FOUND.value())
            .message(e.getMessage())
            .path(request.getRequestURI())
            .build();
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
    }
    
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ErrorResponse> handleValidationException(
            MethodArgumentNotValidException e, HttpServletRequest request) {
        Map<String, String> errors = new HashMap<>();
        e.getBindingResult().getFieldErrors().forEach(
            error -> errors.put(error.getField(), error.getDefaultMessage())
        );
        ErrorResponse error = ErrorResponse.builder()
            .timestamp(LocalDateTime.now())
            .status(HttpStatus.BAD_REQUEST.value())
            .message("Validation failed")
            .details(errors)
            .path(request.getRequestURI())
            .build();
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(error);
    }
    
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleGenericException(
            Exception e, HttpServletRequest request) {
        ErrorResponse error = ErrorResponse.builder()
            .timestamp(LocalDateTime.now())
            .status(HttpStatus.INTERNAL_SERVER_ERROR.value())
            .message("An unexpected error occurred")
            .path(request.getRequestURI())
            .build();
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(error);
    }
}
```

---

## 📤 Content Negotiation

Spring automatically negotiates response format based on Accept header.

```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @GetMapping(produces = {MediaType.APPLICATION_JSON_VALUE, MediaType.APPLICATION_XML_VALUE})
    public ResponseEntity<List<UserDto>> getAllUsers() {
        // Responds with JSON (default) or XML based on Accept header
        return ResponseEntity.ok(userService.getAllUsers());
    }
}
```

---

## 📍 Path Variables & Request Parameters

```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    // /api/users/1 → path variable
    @GetMapping("/{id}")
    public ResponseEntity<UserDto> getUser(@PathVariable Long id) {
        return ResponseEntity.ok(userService.getUserById(id));
    }
    
    // /api/users/search?name=John&age=25 → query parameters
    @GetMapping("/search")
    public ResponseEntity<List<UserDto>> searchUsers(
            @RequestParam(required = false) String name,
            @RequestParam(required = false) Integer age) {
        return ResponseEntity.ok(userService.search(name, age));
    }
    
    // /api/users?page=0&size=10 → pagination
    @GetMapping
    public ResponseEntity<Page<UserDto>> getAllUsers(
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size) {
        return ResponseEntity.ok(userService.getAllUsers(PageRequest.of(page, size)));
    }
}
```

---

## 🔗 HATEOAS (Links in Response)

```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @GetMapping("/{id}")
    public ResponseEntity<EntityModel<UserDto>> getUser(@PathVariable Long id) {
        UserDto user = userService.getUserById(id);
        EntityModel<UserDto> model = EntityModel.of(user);
        model.add(linkTo(methodOn(UserController.class).getUser(id)).withSelfRel());
        model.add(linkTo(methodOn(UserController.class).getAllUsers(0, 10)).withRel("all-users"));
        return ResponseEntity.ok(model);
    }
}
```

---

## ⚠️ Common Interview Questions

1. **Difference between `@RestController` and `@Controller`?**
   - `@RestController` = `@Controller` + `@ResponseBody` on every method
   - Returns data (JSON/XML), not views

2. **How do you handle validation errors?**
   - Use `@Valid` on request parameters
   - Use `@ControllerAdvice` for global exception handling
   - Return 400 Bad Request with error details

3. **When should you use PUT vs PATCH?**
   - PUT: Replace entire resource (requires all fields)
   - PATCH: Partial update (only changed fields)

4. **What's the purpose of `ResponseEntity`?**
   - Allows control over HTTP status, headers, and body
   - Example: `ResponseEntity.status(201).body(data)`

---

## Related

- [Spring Boot Index](Java%20Developer/Spring%20Boot/00%20-%20Index.md)
- [Spring Boot Interview Questions](Spring-Boot-Interview-Questions.md)
- [Spring Boot Exception Handling](Spring-Boot-Exception-Handling.md)
- [Java Developer Index](../00%20-%20Index.md)
