# 🚀 Final Sprint — 24 Hours Before Your Coforge Java Interview

> **Interview:** Java Developer at **Coforge**  
> **When:** Tomorrow at **1:00 PM**  
> **Current time:** Evening of Aug 14 → Morning of Aug 15  
> **Strategy:** High-impact topics only, active recall, explain aloud. No new concepts.

---

## ⏰ Time Budget

| Block | Time | Focus |
|---|---|---|
| **Tonight** (Aug 14, ~7 PM – 11 PM) | 3–4 hrs | Core Java fundamentals + SQL |
| **Tomorrow AM** (Aug 15, ~9 AM – 12:30 PM) | 3.5 hrs | Java 8 + Spring Boot + Coding warm-up + Behavioral |
| **Last 30 min** (12:30 – 1 PM) | 30 min | Quick scan of key cards, relax, prepare materials |

---

## 🎯 Priority Map — What Coforge Interviews Test Most

Based on typical Coforge Java developer interviews, these are the **highest-yield** topics:

| Priority        | Topic                                                                                        | Why it's tested                          | Your source files                           |
| --------------- | -------------------------------------------------------------------------------------------- | ---------------------------------------- | ------------------------------------------- |
| 🔴 **Critical** | **Core Java** (OOP, Collections, Exceptions, JVM, `==`/`equals`, String pool)                | Foundation every candidate must clear    | [[Java Core/Core-Java-Interview-Questions]] |
| 🔴 **Critical** | **Java 8+** (Lambdas, Streams, Optional, Functional Interfaces)                              | Used daily in Spring Boot codebases      | [[Java Core/Java-8-and-Streams-Interview-Questions]] |
| 🔴 **Critical** | **Multithreading** (`synchronized`, `volatile`, thread lifecycle, deadlock)                  | Concurrency is a major differentiator    | Same Core Java link above                   |
| 🟠 **High**     | **SQL** (Joins, GROUP BY, HAVING, Subqueries, Window functions, Nth highest)                 | Most Coforge interviews have a SQL round | [[SQL/SQL-Interview-Questions]]             |
| 🟠 **High**     | **Spring Boot** (IoC/DI, `@SpringBootApplication`, `@RestController`, `@Transactional`, N+1) | Backend standard                         | [[Spring Boot/Spring-Boot-Interview-Questions]] |
| 🟡 **Medium**   | **Coding/DSA** (Arrays, Strings, HashMap problems — easy/medium LeetCode)                    | Codings round or pair-coding             | [[DSA/Patterns/00 - Index]]                 |
| 🟡 **Medium**   | **OOP Design / LLD basics** (SOLID, Singleton, Factory, basic class design)                  | System design / HLD section              | LLD files in vault                          |
| 🟢 **Soft**     | **Behavioral** ("Tell me about yourself", STAR stories, questions for them)                  | Almost always included                   | See below                                   |

---

## 📋 NIGHT BEFORE (Tonight) — Focus: Core Java Deep Dive

### Block 1: OOP + Java Fundamentals (~45 min)
- [ ] **Q1: What are the 4 pillars of OOP?** Explain each with a tiny code example. *(Source: Core Java §1)*
- [ ] **Q2: Abstract class vs Interface?** Compare, when to use each. *(§3)*
- [ ] **Q3: `==` vs `.equals()`?** String pool behavior. *(§6, §7)*
- [ ] **Q3b: String literal `"Hello"` vs `new String("Hello")`?** Pooled vs heap, `==` behavior, `.intern()`. *(Q7b — Coforge classic)*
- [ ] **Q4: `String` vs `StringBuilder` vs `StringBuffer`?** Thread safety & performance. *(§9)*
- [ ] **Q4b: `int` vs `Integer`?** Autoboxing, Integer cache (-128 to 127), `==` trap, null handling. *(Q30b — Coforge classic)*
- [ ] **Q5: `final`, `finally`, `finalize()`?** *(§10)*
- [ ] **Code drill:** Predict output of a snippet with String pool + `==` + `.equals()`. *(Core Java Code Snippet Practice)*
- [ ] **Checkpoint:** Explain each aloud without notes — if stuck, re-read then re-explain.

### Block 2: Collections + HashMap Internals (~60 min)
- [ ] **Q6: Collections hierarchy?** Know the tree. *(§11, Quick Reference §Collection Hierarchy)*
- [ ] **Q7: `ArrayList` vs `LinkedList`?** Time complexities, memory. *(§12, Quick Reference)*
- [ ] **Q8: `HashMap` vs `Hashtable` vs `ConcurrentHashMap`?** Thread safety, nulls. *(§13)*
- [ ] **Q9: How does `HashMap` work internally?** Hashing, collisions, resizing, treeification (Java 8, >8 entries → tree). *(§14)*
- [ ] **Q10: `HashSet` vs `TreeSet`?** Backed by data structure, complexity. *(§15)*
- [ ] **Q10b: `HashMap` vs `TreeMap`?** Sorted keys (Red-Black tree), O(log n), navigable methods vs O(1) HashMap. *(Q13d)*
- [ ] **Q10c: `HashMap` vs `LinkedHashMap`?** Linked list for insertion/access order, O(1) + LRU cache use case. *(Q13e)*
- [ ] **Q11: Fail-fast vs fail-safe iterators?** `ConcurrentModificationException`. *(§16)*
- [ ] **Q12: `hashCode()` and `equals()` contract?** Why override together? *(§39, Roadmap §Equality)*
- [ ] **Quick scan:** `Quick Reference` → Collection Hierarchy + Key Differences cards.
- [ ] **Checkpoint:** Draw HashMap put/get flow on paper + explain treeification.

### Block 3: Exception Handling (~30 min)
- [ ] **Q13: Checked vs Unchecked exceptions?** Examples. *(§17)*
- [ ] **Q14: Exception hierarchy?** `Throwable → Error / Exception → RuntimeException`. *(§18, Quick Reference §Exception Hierarchy)*
- [ ] **Q15: `try-with-resources`?** `AutoCloseable`. *(§20)*
- [ ] **Q16: `throw` vs `throws`?**
- [ ] **Q16b: Serialization in Java?** A **Coforge favourite** at 3–6 yrs. Know:
  - `Serializable` is a marker interface (no methods). `ObjectOutputStream.writeObject()` → `ObjectInputStream.readObject()`.
  - `transient` fields are **skipped** during serialization (e.g., sensitive password fields).
  - `serialVersionUID` — static, final, long. If not declared, JVM generates it from class structure → **mismatched UID throws `InvalidClassException`** on deserialization. Always declare it explicitly (`private static final long serialVersionUID = 1L;`).
  - `Externalizable` — lets you control the serialization logic entirely (write `writeExternal`/`readExternal`).
  - **When to use:** caching objects, sending objects over network (RMI), HTTP session persistence. **Modern alternative:** prefer JSON/DTO over Java serialization (security concerns).
- [ ] **Checkpoint:** Write a small try-catch-finally with custom exception.

### Block 4: SQL (~45 min)
- [ ] **Q17: All 4 JOIN types** (INNER, LEFT, RIGHT, FULL) — draw the Venn diagrams. *(SQL §5, Quick Reference §SQL JOINs Visual)*
- [ ] **Q18: `WHERE` vs `HAVING`?** *(SQL §2)*
- [ ] **Q19: Find Nth highest salary** — 2 methods (LIMIT/OFFSET + DENSE_RANK). *(SQL §17)*
- [ ] **Q20: Find duplicate rows** (GROUP BY + HAVING, ROW_NUMBER). *(SQL §18)*
- [ ] **Q21: Running total / cumulative sum** (window function). *(SQL §22, Quick Reference)*
- [ ] **Q22: Subqueries — correlated vs non-correlated vs EXISTS.** *(SQL §8)*
- [ ] **Checkpoint:** Solve 2–3 SQL problems on paper (no IDE needed). Use HackerRank or LeetCode SQL if you want to verify.

### Block 5: Quick Wind-Down (~15 min)
- [ ] Re-read the **Pre-Interview Checklist** in your Master Plan — check off what you can do confidently.
- [ ] Prepare your **"Tell me about yourself"** (2-minute version).
- [ ] Write your **3+ STAR stories** (situation, task, action, result with numbers).
- [ ] **Sleep early!** Brain consolidation happens during sleep.

---

## 📋 INTERVIEW DAY (Tomorrow Morning) — Focus: Java 8, Spring Boot, Coding Warm-up

### Block 6: Java 8 + Streams (~60 min)
- [ ] **Q23: What is a Lambda expression?** Syntax, capture rules (effectively final). *(Java 8 §1, §2)*
- [ ] **Q24: Functional Interfaces?** `Predicate`, `Function`, `Consumer`, `Supplier`, `BiFunction`. *(§2)*
- [ ] **Q25: Stream pipeline?** Source → intermediate (lazy) → terminal (eager). *(§3, §4)*
- [ ] **Q26: `map()` vs `flatMap()`?** *(§11)*
- [ ] **Q27: `Optional`?** Why use it, methods (`orElse`, `orElseGet`, `ifPresent`, `map`). Pitfalls. *(§7)*
- [ ] **Q28: Method references?** 4 types. *(§6)*
- [ ] **Q29: Parallel streams?** When to use/not use. *(§12)*
- [ ] **Quick scan:** `Reference → Java Stream Creation Guide` for creating streams from different sources.
- [ ] **Checkpoint:** Write a stream pipeline that filters, maps, and collects to a Map (groupingBy or toMap).

### Block 7: Multithreading & Concurrency (~45 min)
- [ ] **Q30: Ways to create a thread?** Thread class, Runnable, Callable/Future, ExecutorService. *(§21)*
- [ ] **Q31: `start()` vs `run()`?** *(§22)*
- [ ] **Q32: `synchronized`?** Methods, blocks, static. *(§23)*
- [ ] **Q33: `volatile` vs `synchronized`?** *(§46)*
- [ ] **Q34: `wait()` vs `sleep()`?** Lock release, wake-up. *(§24)*
- [ ] **Q35: Deadlock?** Prevention strategies (lock ordering, `tryLock`). *(§25)*
- [ ] **Q36: `ConcurrentHashMap` internals?** Segment/bucket-level locking (Java 8+ uses CAS + synchronized on bins). *(§51)*
- [ ] **Q36b: `ConcurrentHashMap` vs `Collections.synchronizedMap(new HashMap<>())`?** Coforge favourite at 3–6 yrs. Know the locking granularity difference: synchronizedMap uses a single object lock → serial access; ConcurrentHashMap uses bucket-level locking → concurrent access. Also iterator behavior (CME vs weakly-consistent). *(Q13c)*
- [ ] **Q37: Thread pool?** `Executors`, `ThreadPoolExecutor` basics.
- [ ] **Checkpoint:** Explain a producer-consumer scenario with `wait`/`notify` or `BlockingQueue`.

### Block 8: Spring Boot (~60 min)
> Coforge backend interviews almost always test Spring. Even if the role is "Java" only, expect 2–3 Spring questions.

- [ ] **Q38: What is Spring IoC / DI?** Container manages beans, injects dependencies. *(Spring §1, §3)*
- [ ] **Q39: `@SpringBootApplication`?** Composition of `@Configuration + @EnableAutoConfiguration + @ComponentScan`. *(Card 1)*
- [ ] **Q40: Auto-configuration mechanism?** `@ConditionalOnClass`, `@ConditionalOnMissingBean`. *(§2)*
- [ ] **Q41: `@RestController` vs `@Controller`?** *(§4)*
- [ ] **Q42: REST status codes?** Use the Quick Reference Card 5. *(Card 5)*
- [ ] **Q43: Global exception handling?** `@RestControllerAdvice` + `@ExceptionHandler`. *(§4)*
- [ ] **Q44: N+1 problem?** 3 solutions: JOIN FETCH, @EntityGraph, @BatchSize. *(§5, Card 4)*
- [ ] **Q45: `@Transactional`?** Propagation (REQUIRED, REQUIRES_NEW), isolation, rollback rules. **Self-invocation trap!** *(§6, Card 3)*
- [ ] **Q46: Bean scopes?** singleton vs prototype (and the prototype-in-singleton trap). *(§2)*
- [ ] **Q47: `@Component` vs `@Service` vs `@Repository`?** Semantic differences. *(§12)*
- [ ] **Checkpoint:** Write a small `@RestController` + `@Service` + `@Repository` + `@Transactional` code snippet on paper.

### Block 9: Coding / DSA Warm-up (~45 min)
> If Coforge includes a coding round, these patterns cover ~80% of easy/medium problems.

- [ ] **Two Sum / Two Sum II** (HashMap or Two Pointers) — *(Pattern: Two Pointers)*
- [ ] **Valid Anagram / Group Anagrams** (Frequency counting) — *(Pattern: Frequency Counting)*
- [ ] **Reverse a String / Valid Palindrome** (Two pointers) — *(Pattern: Two Pointers)*
- [ ] **Binary Search** (on sorted array) — *(Pattern: Modified Binary Search)*
- [ ] **Fibonacci / Factorial** (recursion) — *(Pattern: Recursion)*
- [ ] **Sliding Window: Longest Substring Without Repeating Characters** — *(Pattern: Sliding Window)*
- [ ] **Quick reference:** Open `DSA/Patterns/00 - Index.md` for any pattern refresher.
- [ ] **Checkpoint:** For each problem, state **time + space complexity** and whether a brute-force → optimized path exists.

### Block 10: LLD / Design Basics (~30 min)
- [ ] **Q48: SOLID principles?** One line each + example. *(Roadmap SOLID)*
- [ ] **Q49: Singleton pattern?** Thread-safe implementation (double-checked locking, enum). *(LLD §Design Patterns)*
- [ ] **Q50: Factory pattern?** *(LLD §Design Patterns)*
- [ ] **Checkpoint:** Sketch a simple class design for "Vending Machine" or "Parking Lot" — just classes + relationships.

### Block 11: Behavioral Questions (~15 min)
- [ ] **"Tell me about yourself"** — 2-minute, structured (background → key skills → why Coforge).
- [ ] **3 STAR stories** ready (e.g., solved a bug, improved performance, led a task, handled conflict).
- [ ] **3 questions to ask the interviewer:**
  - Team's tech stack & Java version?
  - How do you handle code reviews / what's the dev workflow?
  - Opportunities for learning/growth or recent technical challenges the team solved?

---

## 🃏 Quick Reference Cards (Review Last)

Keep these tabs open for a final 10-minute scan before the interview:

| Card | File | What to verify |
|---|---|---|
| **Core Java** | [[Java Core/Core-Java-Interview-Questions]] §31–62 | Modern Java (17/21/25), virtual threads, JFR |
| **Collections** | [[Reference/Java-and-SQL-Interview-Quick-Reference]] §Collection Hierarchy + Key Differences | Internal structure, complexity |
| **Exceptions** | Same ref §Exception Hierarchy | When to use checked vs unchecked |
| **Streams** | Same ref §Stream API Quick Reference | Intermediate vs terminal, collect patterns |
| **Spring Boot** | [[Spring Boot/Spring-Boot-Interview-Questions]] Cards 1–5 | `@SpringBootApplication`, annotations, `@Transactional` checklist, JPA pitfalls, REST codes |

---

## 🔑 Key Answer Framework (Use for Every Question)

> **Definition → Why it matters → Example → Trade-off**

This is from your roadmap. Use it for every conceptual question:

1. **Definition** — one direct sentence.
2. **Why it matters** — performance, safety, readability, or correctness.
3. **Example** — small code snippet or real scenario.
4. **Trade-off** — when it fails, hurts performance, or is over-engineering.

---

## 💬 Interview Day Reminders

- [ ] Stay calm — interviewer wants to see **how you think**, not perfection.
- [ ] **Clarify before coding** — ask about input constraints, edge cases.
- [ ] **Think aloud** — narrate your reasoning; this is often scored.
- [ ] **Write clean code** — descriptive variable names, consistent indentation.
- [ ] **Test mentally** — walk through with a sample input.
- [ ] **State complexity** — always mention Time + Space.
- [ ] **Don't know something?** Say "I'm not sure, but here's my reasoning..." — honesty beats guessing.
- [ ] **Ask good questions** — shows genuine interest.

---

## ✅ Final Readiness Check (2 hours before interview)

- [ ] Can explain OOP principles with code (not just definitions).
- [ ] Can explain HashMap internals (collisions, resizing, treeification).
- [ ] Can write `equals()` + `hashCode()` and explain the contract.
- [ ] Can explain stream laziness + when parallel streams are harmful.
- [ ] Can explain `@Transactional` propagation + self-invocation trap.
- [ ] Can explain N+1 problem with 2–3 solutions.
- [ ] Can draw 3-tier architecture (Client → Server → Database).
- [ ] Can write SQL: JOINs, GROUP BY/HAVING, window function, Nth highest.
- [ ] Can solve 2–3 easy LeetCode-style problems with complexity.
- [ ] Prepared "Tell me about yourself" + STAR stories + questions for them.
- [ ] Resume + portfolio links open in browser (if needed for screen share).
- [ ] Pen + paper ready (for LLD diagramming or code on whiteboard).

---

## 📁 Resources to Keep Open (Click to open in Obsidian)

1. [[Final-Sprint-24-Hours-Before-Interview]] ← this file (your checklist)
2. [[Java Core/Core-Java-Interview-Questions]]
3. [[Java Core/Java-8-and-Streams-Interview-Questions]]
4. [[Spring Boot/Spring-Boot-Interview-Questions]]
5. [[SQL/SQL-Interview-Questions]]
6. [[Reference/Java-and-SQL-Interview-Quick-Reference]]
7. [[DSA/Patterns/00 - Index]]

---

> **You've got this!** This vault has 580+ lines of curated material — review strategically, not exhaustively. Focus on **depth over breadth** for the topics you know best.

*Last updated: August 14, 2026, 7:57 PM*

---

## Related

- [[Interview-Preparation-Master-Plan]] — Phase 6: Final Sprint
- [[Roadmap/Java-Backend-Interview-Roadmap]] — Interview Readiness Checklist
- [[Reference/Java-and-SQL-Interview-Quick-Reference]]
