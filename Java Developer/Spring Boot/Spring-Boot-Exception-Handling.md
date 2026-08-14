# Spring Boot - Exception Handling

Global exception handling strategies, error responses, and best practices.

---

## 🛑 Why Global Exception Handling?

Without global handling, each controller needs try-catch. With `@ControllerAdvice`, handle all exceptions in one place.

---

## 📋 @ControllerAdvice Pattern

```java
@RestControllerAdvice  // or @ControllerAdvice + @ResponseBody
public class GlobalExceptionHandler {
    
    // Handles specific exceptions
    @ExceptionHandler(ResourceNotFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public ErrorResponse handleResourceNotFound(ResourceNotFoundException e, HttpServletRequest request) {
        return ErrorResponse.builder()
            .timestamp(LocalDateTime.now())
            .status(HttpStatus.NOT_FOUND.value())
            .message(e.getMessage())
            .path(request.getRequestURI())
            .build();
    }
    
    // Handles validation errors
    @ExceptionHandler(MethodArgumentNotValidException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public ErrorResponse handleValidationException(MethodArgumentNotValidException e) {
        Map<String, String> errors = new HashMap<>();
        e.getBindingResult().getFieldErrors().forEach(
            error -> errors.put(error.getField(), error.getDefaultMessage())
        );
        return ErrorResponse.builder()
            .timestamp(LocalDateTime.now())
            .status(HttpStatus.BAD_REQUEST.value())
            .message("Validation failed")
            .errors(errors)
            .build();
    }
    
    // Handles binding errors
    @ExceptionHandler(HttpMessageNotReadableException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public ErrorResponse handleHttpMessageNotReadable(HttpMessageNotReadableException e) {
        return ErrorResponse.builder()
            .timestamp(LocalDateTime.now())
            .status(HttpStatus.BAD_REQUEST.value())
            .message("Invalid request body: " + e.getMessage())
            .build();
    }
    
    // Generic catch-all
    @ExceptionHandler(Exception.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public ErrorResponse handleGenericException(Exception e) {
        return ErrorResponse.builder()
            .timestamp(LocalDateTime.now())
            .status(HttpStatus.INTERNAL_SERVER_ERROR.value())
            .message("An unexpected error occurred")
            .details(e.getMessage())
            .build();
    }
}
```

---

## 📝 Error Response DTO

```java
@Data
@Builder
@AllArgsConstructor
public class ErrorResponse {
    private LocalDateTime timestamp;
    private int status;
    private String message;
    private String path;
    private Map<String, String> errors;  // For validation errors
    private String details;              // For debug info
}
```

**Example Response:**
```json
{
  "timestamp": "2024-08-14T10:30:00",
  "status": 400,
  "message": "Validation failed",
  "errors": {
    "email": "Email must be valid",
    "age": "Age must be positive"
  }
}
```

---

## 🎯 Best Practices

### 1. Create Custom Exceptions

```java
public class ResourceNotFoundException extends RuntimeException {
    public ResourceNotFoundException(String message) {
        super(message);
    }
}

public class DuplicateResourceException extends RuntimeException {
    public DuplicateResourceException(String message) {
        super(message);
    }
}

public class InvalidInputException extends RuntimeException {
    public InvalidInputException(String message) {
        super(message);
    }
}
```

### 2. Use Appropriate HTTP Status Codes

| Status | When to Use |
|--------|-------------|
| **400 Bad Request** | Invalid input, validation error |
| **401 Unauthorized** | Authentication required |
| **403 Forbidden** | Authenticated but not authorized |
| **404 Not Found** | Resource doesn't exist |
| **409 Conflict** | Duplicate or conflict (e.g., email already exists) |
| **500 Internal Server Error** | Unexpected server error |

### 3. Logging Exceptions

```java
@RestControllerAdvice
@Slf4j
public class GlobalExceptionHandler {
    
    @ExceptionHandler(Exception.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public ErrorResponse handleGenericException(Exception e) {
        log.error("Unexpected error occurred", e);  // Log stack trace
        
        return ErrorResponse.builder()
            .timestamp(LocalDateTime.now())
            .status(HttpStatus.INTERNAL_SERVER_ERROR.value())
            .message("An unexpected error occurred")
            .build();
    }
}
```

### 4. Never Expose Internal Details

❌ **Bad:**
```java
return ErrorResponse.builder()
    .message(e.getMessage())  // Might expose DB details
    .details(e.getStackTrace())  // Never expose stack trace to client
    .build();
```

✅ **Good:**
```java
return ErrorResponse.builder()
    .message("An error occurred while processing your request")
    .build();
```

---

## 🧪 Testing Exception Handling

```java
@WebMvcTest(UserController.class)
class UserControllerTest {
    
    @MockBean
    private UserService userService;
    
    @Autowired
    private MockMvc mockMvc;
    
    @Test
    void testNotFound() throws Exception {
        when(userService.getUserById(1L))
            .thenThrow(new ResourceNotFoundException("User not found"));
        
        mockMvc.perform(get("/api/users/1"))
            .andExpect(status().isNotFound())
            .andExpect(jsonPath("$.status").value(404))
            .andExpect(jsonPath("$.message").value("User not found"));
    }
    
    @Test
    void testValidationError() throws Exception {
        mockMvc.perform(post("/api/users")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"name\":\"\"}"))  // Empty name
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.status").value(400))
            .andExpect(jsonPath("$.message").value("Validation failed"));
    }
}
```

---

## 📊 Exception Hierarchy

```
Exception
├── RuntimeException (Unchecked)
│   ├── ResourceNotFoundException (Custom)
│   ├── DuplicateResourceException (Custom)
│   └── InvalidInputException (Custom)
└── Checked Exception
    └── IOException
```

---

## ⚠️ Common Interview Questions

1. **What's the difference between `@ControllerAdvice` and `@RestControllerAdvice`?**
   - `@ControllerAdvice`: Returns view
   - `@RestControllerAdvice`: Returns JSON (adds `@ResponseBody`)

2. **How do you handle validation errors?**
   - Catch `MethodArgumentNotValidException`
   - Extract field errors and return 400 Bad Request

3. **Should you log exceptions?**
   - Yes, always log to server logs
   - But don't expose stack traces to clients

4. **When should exceptions be logged vs handled?**
   - Log: All exceptions at global handler
   - Handle: Business logic exceptions (not found, duplicates)

---

## Related

- [Spring Boot Index](Java%20Developer/Spring%20Boot/00%20-%20Index.md)
- [Spring Boot REST API](Spring-Boot-REST-API.md)
- [Spring Boot Interview Questions](Spring-Boot-Interview-Questions.md)
- [Java Developer Index](../00%20-%20Index.md)
