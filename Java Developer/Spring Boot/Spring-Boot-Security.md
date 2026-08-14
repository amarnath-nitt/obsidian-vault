# Spring Boot - Security & Authentication

Spring Security configuration, authentication, authorization, JWT tokens, and best practices.

---

## 🔐 Spring Security Basics

Spring Security handles authentication (who are you?) and authorization (what can you do?).

---

## 📌 Core Concepts

### 1. Authentication vs Authorization

| Concept | Meaning | Example |
|---------|---------|---------|
| **Authentication** | Proving your identity | Login with username/password |
| **Authorization** | Verifying you have permission | Only admin can delete users |

### 2. Principal, Credentials, Authority

```
Principal (User) ← has → Credentials (Password) ← grants → Authorities (Roles)
```

---

## 🛡️ Security Configuration

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {
    
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(authz -> authz
                .requestMatchers("/public/**").permitAll()
                .requestMatchers("/admin/**").hasRole("ADMIN")
                .requestMatchers("/user/**").hasAnyRole("USER", "ADMIN")
                .anyRequest().authenticated()
            )
            .formLogin(form -> form
                .loginPage("/login")
                .defaultSuccessUrl("/dashboard")
            )
            .logout(logout -> logout
                .logoutUrl("/logout")
                .logoutSuccessUrl("/login")
            )
            .csrf().disable();  // ⚠️ Only for APIs without frontend
        
        return http.build();
    }
    
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
```

---

## 🔑 JWT Authentication

JWT (JSON Web Token) is stateless authentication commonly used in REST APIs.

```java
// 1. Generate JWT on login
@RestController
@RequestMapping("/auth")
public class AuthController {
    
    @Autowired
    private AuthenticationManager authenticationManager;
    
    @Autowired
    private JwtTokenProvider tokenProvider;
    
    @PostMapping("/login")
    public ResponseEntity<AuthResponse> login(@RequestBody LoginRequest request) {
        Authentication authentication = authenticationManager.authenticate(
            new UsernamePasswordAuthenticationToken(
                request.getUsername(),
                request.getPassword()
            )
        );
        
        String token = tokenProvider.generateToken(authentication);
        return ResponseEntity.ok(new AuthResponse(token));
    }
}

// 2. JWT Token Provider
@Component
public class JwtTokenProvider {
    
    @Value("${app.jwtSecret}")
    private String jwtSecret;
    
    @Value("${app.jwtExpiration}")
    private long jwtExpiration;
    
    public String generateToken(Authentication authentication) {
        UserPrincipal userPrincipal = (UserPrincipal) authentication.getPrincipal();
        
        return Jwts.builder()
            .setSubject(String.valueOf(userPrincipal.getId()))
            .setIssuedAt(new Date())
            .setExpiration(new Date(System.currentTimeMillis() + jwtExpiration))
            .signWith(SignatureAlgorithm.HS512, jwtSecret)
            .compact();
    }
    
    public Long getUserIdFromJWT(String token) {
        Claims claims = Jwts.parser()
            .setSigningKey(jwtSecret)
            .parseClaimsJws(token)
            .getBody();
        
        return Long.parseLong(claims.getSubject());
    }
    
    public boolean validateToken(String token) {
        try {
            Jwts.parser().setSigningKey(jwtSecret).parseClaimsJws(token);
            return true;
        } catch (JwtException | IllegalArgumentException e) {
            return false;
        }
    }
}

// 3. JWT Filter
@Component
public class JwtAuthenticationFilter extends OncePerRequestFilter {
    
    @Autowired
    private JwtTokenProvider tokenProvider;
    
    @Autowired
    private UserRepository userRepository;
    
    @Override
    protected void doFilterInternal(HttpServletRequest request, 
                                    HttpServletResponse response, 
                                    FilterChain filterChain) 
            throws ServletException, IOException {
        
        String jwt = getJwtFromRequest(request);
        
        if (jwt != null && tokenProvider.validateToken(jwt)) {
            Long userId = tokenProvider.getUserIdFromJWT(jwt);
            User user = userRepository.findById(userId).orElse(null);
            
            if (user != null) {
                UserPrincipal userPrincipal = UserPrincipal.create(user);
                Authentication authentication = new UsernamePasswordAuthenticationToken(
                    userPrincipal, null, userPrincipal.getAuthorities()
                );
                SecurityContextHolder.getContext().setAuthentication(authentication);
            }
        }
        
        filterChain.doFilter(request, response);
    }
    
    private String getJwtFromRequest(HttpServletRequest request) {
        String bearerToken = request.getHeader("Authorization");
        if (bearerToken != null && bearerToken.startsWith("Bearer ")) {
            return bearerToken.substring(7);
        }
        return null;
    }
}

// 4. Register JWT Filter
@Configuration
@EnableWebSecurity
public class SecurityConfig {
    
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http, JwtAuthenticationFilter jwtFilter) throws Exception {
        http
            .addFilterBefore(jwtFilter, UsernamePasswordAuthenticationFilter.class)
            // ... other config
            .csrf().disable();
        
        return http.build();
    }
}
```

---

## 👤 Getting Current User

```java
// Method 1: Inject Principal
@GetMapping("/me")
public ResponseEntity<UserDto> getCurrentUser(Principal principal) {
    String username = principal.getName();
    User user = userRepository.findByUsername(username);
    return ResponseEntity.ok(UserDto.from(user));
}

// Method 2: Use SecurityContext
@GetMapping("/me")
public ResponseEntity<UserDto> getCurrentUser() {
    Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
    UserPrincipal userPrincipal = (UserPrincipal) authentication.getPrincipal();
    return ResponseEntity.ok(UserDto.from(userPrincipal.getUser()));
}

// Method 3: Inject Authentication
@GetMapping("/me")
public ResponseEntity<UserDto> getCurrentUser(Authentication authentication) {
    UserPrincipal userPrincipal = (UserPrincipal) authentication.getPrincipal();
    return ResponseEntity.ok(UserDto.from(userPrincipal.getUser()));
}
```

---

## 🔒 Method-Level Security

```java
@Configuration
@EnableGlobalMethodSecurity(securedEnabled = true, prePostEnabled = true)
public class SecurityConfig {
    // ... config
}

// Usage in service
@Service
public class UserService {
    
    @PreAuthorize("hasRole('ADMIN')")
    public void deleteUser(Long id) {
        // Only ADMIN can access
    }
    
    @PreAuthorize("@userService.isUserOwner(#id)")
    public UserDto getUser(Long id) {
        // Only owner or ADMIN can access
    }
    
    public boolean isUserOwner(Long userId) {
        Long currentUserId = getCurrentUserId();
        return userId.equals(currentUserId);
    }
}
```

---

## 🚫 CORS Configuration

```java
@Configuration
public class CorsConfig {
    
    @Bean
    public WebMvcConfigurer corsConfigurer() {
        return new WebMvcConfigurer() {
            @Override
            public void addCorsMappings(CorsRegistry registry) {
                registry.addMapping("/api/**")
                    .allowedOrigins("http://localhost:3000")
                    .allowedMethods("GET", "POST", "PUT", "DELETE", "PATCH")
                    .allowedHeaders("*")
                    .allowCredentials(true)
                    .maxAge(3600);
            }
        };
    }
}
```

---

## Related

- [Spring Boot Index](Java%20Developer/Spring%20Boot/00%20-%20Index.md)
- [Spring Boot Interview Questions](Spring-Boot-Interview-Questions.md)
- [Java Developer Index](../00%20-%20Index.md)
