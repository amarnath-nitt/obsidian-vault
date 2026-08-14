# 🎯 Java Developer Interview Preparation — Master Plan

> [!info] What is this?
> A **beginner-friendly, step-by-step guide** to prepare for Java Developer interviews. You don't need any interview experience to start. Just follow the phases in order and check off each box as you go.

>[!tip] How to use this plan
> 1. **Go top to bottom** — each phase builds on the previous one
> 2. **Check off boxes** as you complete each item (click them in Reading Mode)
> 3. **Don't skip phases** — even if you think you know a topic, do the checkpoint first
> 4. **Study 2 hours daily** — consistency beats cramming
> 5. Open linked notes in a new tab and study them when you reach that step

---

## 🗺️ The Big Picture (Read This First)

Your interview preparation happens in **7 clear phases**:

```
PHASE 0: Get Ready        →  Setup your study environment & mindset        (1-2 days)
PHASE 1: Java Basics      →  Learn core Java step by step                  (1.5 weeks)
PHASE 2: DSA Foundation   →  Solve problems with patterns                  (2 weeks)
PHASE 3: Spring Boot      →  Build a REST API, understand the framework    (2 weeks)
PHASE 4: Interviews Prep  →  SQL, LLD, HLD, Kafka — interview questions    (2 weeks)
PHASE 5: Mock Interviews  →  Practice under real interview conditions      (1 week)
PHASE 6: Final Sprint     →  Review everything, fix weak areas             (3 days)
```

**Estimated total time: ~9-10 weeks** (studying 2 hours/day)

> [!note] For absolute beginners
> If you have **never written Java code**, start with Phase 0 and follow the Java Basics links inside each step. If you already know Java, Phase 1 will be a quick review & checkpoint.

---

# 📌 PHASE 0: Get Ready (Days 1-2)

**Goal:** Set up your computer, understand how to study, and know what's coming.

### Step 0.1 — Install Required Tools

- [ ] Install **JDK 21** (or 25) from [Oracle JDK](https://www.oracle.com/java/technologies/downloads/) or [OpenJDK](https://adoptium.net/)
- [ ] Install **IntelliJ IDEA Community Edition** (free) from [jetbrains.com](https://www.jetbrains.com/idea/download/)
- [ ] Install **Git** from [git-scm.com](https://git-scm.com/downloads)
- [ ] Create a free account on [LeetCode](https://leetcode.com/)
- [ ] Create a free account on [GeeksforGeeks](https://www.geeksforgeeks.org/) (for reading articles)
- [ ] Install **Postman** (for testing APIs later) from [postman.com](https://www.postman.com/downloads/)

### Step 0.2 — Understand How to Study

- [ ] Read [Java Backend Interview Roadmap](Roadmap/Java-Backend-Interview-Roadmap.md) — this explains *what* interviewers ask
- [ ] Understand the study method: **Learn → Practice → Explain aloud**
- [ ] Watch/read one beginner Java intro video/article (any is fine)

### Step 0.3 — Set Your Schedule

- [ ] Decide your daily study time (recommended: **2 hours/day**)
- [ ] Decide your interview date (gives you a deadline)
- [ ] Write it down somewhere visible

> [!tip] Weekly schedule template (2 hours/day)
> - **Mon-Fri:** 1 hour theory + 1 hour coding practice
> - **Saturday:** 2 hours of mock problems (timed)
> - **Sunday:** Review mistakes, take notes, rest

---

# 📌 PHASE 1: Java Basics (Days 3-12)

**Goal:** Understand core Java well enough to write small programs confidently.
**Prerequisite:** Phase 0 complete

> [!info] If you already know Java
> Take the checkpoint test on Day 12. If you score 80%+, skip to Phase 2.

### Week 1: Core Building Blocks

- [ ] **Day 3:** Variables, data types, operators
  - [ ] Study: [Core Java Guide](Interview-Guides/Core-Java-Interview-Questions.md) — sections on basics
  - [ ] Practice: Write 5 small programs (calculator, temperature converter, etc.)
- [ ] **Day 4:** Control flow (if/else, loops, switch)
  - [ ] Practice: Write a program that prints Fibonacci series, checks prime numbers
- [ ] **Day 5:** Classes & Objects (OOP basics)
  - [ ] Study: [Core Java Guide](Interview-Guides/Core-Java-Interview-Questions.md) — OOP sections
  - [ ] Practice: Create a `Student` class with name, age, marks; add methods
- [ ] **Day 6:** Methods, parameters, return values
  - [ ] Practice: Create a class with overloaded methods

### Week 1: Key Java Concepts

- [ ] **Day 7:** Arrays & Strings
  - [ ] Practice: Reverse a string, find max in array, count vowels
- [ ] **Day 8:** Collections (ArrayList, HashMap, HashSet)
  - [ ] Study: Collections section in [Core Java Guide](Interview-Guides/Core-Java-Interview-Questions.md)
  - [ ] Practice: Add/remove/search items in each collection type
- [ ] **Day 9:** Exception handling (try-catch, throw, custom exceptions)
  - [ ] Practice: Handle division by zero, invalid input
- [ ] **Day 10:** Java 8 basics — Lambda expressions & Streams (simple version)
  - [ ] Study: [Java 8 and Streams Interview Questions](Interview-Guides/Java-8-and-Streams-Interview-Questions.md) — first sections only
  - [ ] Practice: Filter a list, map values, sum numbers using streams

### Week 1: Checkpoint

- [ ] **Day 11:** Review everything from Day 3-10 — re-read your code
- [ ] **Day 12:** ✅ **CHECKPOINT TEST** — Answer these aloud:
  - What is a class? What is an object?
  - What is the difference between `ArrayList` and `LinkedList`?
  - What is a lambda expression?
  - Write a simple `for` loop that prints 1 to 10
  - If you can answer these → **Phase 1 complete!**

---

# 📌 PHASE 2: DSA Foundation (Days 13-26)

**Goal:** Recognize 10 common coding problem patterns and solve easy/medium LeetCode problems.
**Prerequisite:** Phase 1 checkpoint passed

> [!info] Why patterns?
> Interviewers don't ask random problems — they ask problems that fit patterns. Learning patterns = solving many different problems with the same technique.

### Week 1: Level 1 Patterns (Easy)

- [ ] **Day 13:** **Recursion** — understand base case + recursive call
  - [ ] Study: [Recursion Pattern](../DSA/Patterns/01%20-%20Recursion/Practice.md)
  - [ ] Practice: Factorial, Fibonacci (recursive version)
- [ ] **Day 14:** **Two Pointers** — used on sorted arrays/pairs
  - [ ] Study: [Two Pointers Pattern](../DSA/Patterns/04%20-%20TwoPointers/Practice.md)
  - [ ] Practice: [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) (LC 125), [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) (LC 167)
- [ ] **Day 15:** **Frequency Counting** — count occurrences with HashMap
  - [ ] Study: [Frequency Counting Pattern](../DSA/Patterns/03%20-%20FrequencyCounting/Practice.md)
  - [ ] Practice: [Valid Anagram](https://leetcode.com/problems/valid-anagram/) (LC 242)
- [ ] **Day 16:** **Prefix Sum** — cumulative sums for range queries
  - [ ] Study: [Prefix Sum Pattern](../DSA/Patterns/02%20-%20PrefixSum/Practice.md)
  - [ ] Practice: [Range Sum Query](https://leetcode.com/problems/range-sum-query-immutable/) (LC 303)

### Week 2: Level 2 Patterns (Medium)

- [ ] **Day 17:** **Sliding Window** — contiguous subarray/substring problems
  - [ ] Study: [Sliding Window Pattern](../DSA/Patterns/06%20-%20SlidingWindow/Practice.md)
  - [ ] Practice: [Longest Substring Without Repeating](https://leetcode.com/problems/longest-substring-without-repeating-characters/) (LC 3)
- [ ] **Day 18:** **Binary Search** — searching sorted data
  - [ ] Study: [Modified Binary Search Pattern](../DSA/Patterns/09%20-%20ModifiedBinarySearch/Practice.md)
  - [ ] Practice: [Binary Search](https://leetcode.com/problems/binary-search/) (LC 704)
- [ ] **Day 19:** **Linked List Reversal** — reverse a linked list
  - [ ] Study: [Linked List Reversal Pattern](../DSA/Patterns/08%20-%20LinkedListReversal/Practice.md)
  - [ ] Practice: [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (LC 206)
- [ ] **Day 20:** **Tree Traversal** — DFS/BFS on trees
  - [ ] Study: [Binary Tree Traversal Pattern](../DSA/Patterns/05%20-%20BinaryTreeTraversal/Practice.md)
  - [ ] Practice: [Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) (LC 94), [Max Depth](https://leetcode.com/problems/maximum-depth-of-binary-tree/) (LC 104)

### Week 3: Level 3 Patterns (Harder)

- [ ] **Day 21:** **BFS/DFS on Graphs** — level order, connected components
  - [ ] Study: [BFS Pattern](../DSA/Patterns/10%20-%20BreadthFirstSearch/Practice.md), [DFS Pattern](../DSA/Patterns/11%20-%20DepthFirstSearch/Practice.md)
  - [ ] Practice: [Number of Islands](https://leetcode.com/problems/number-of-islands/) (LC 200)
- [ ] **Day 22:** **Backtracking** — generate all combinations/permutations
  - [ ] Study: [Backtracking Pattern](../DSA/Patterns/19%20-%20Backtracking/Practice.md)
  - [ ] Practice: [Subsets](https://leetcode.com/problems/subsets/) (LC 78)
- [ ] **Day 23:** **Dynamic Programming (basics)** — memoization, state definition
  - [ ] Study: [DP Pattern](../DSA/Patterns/20%20-%20DynamicProgramming/Practice.md)
  - [ ] Practice: [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) (LC 70)
- [ ] **Day 24:** **Heap/Top K** — k largest/smallest, frequent elements
  - [ ] Study: [Top K Elements Pattern](../DSA/Patterns/15%20-%20TopKElements/Practice.md)
  - [ ] Practice: [Kth Largest Element](https://leetcode.com/problems/kth-largest-element-in-an-array/) (LC 215)

### Week 3: Checkpoint

- [ ] **Day 25:** **Timed Practice** — Solve 3 problems in 1 hour (Pick from: Two Sum, Valid Anagram, Binary Search, Reverse Linked List)
- [ ] **Day 26:** ✅ **CHECKPOINT TEST** — Answer aloud:
  - When do you use Two Pointers? Sliding Window?
  - What is the time complexity of Binary Search?
  - How does backtracking work? (steps)
  - What is DP memoization?
  - If you can answer these → **Phase 2 complete!**

---

# 📌 PHASE 3: Spring Boot Backend (Days 27-40)

**Goal:** Build a working REST API with Spring Boot and understand what happens under the hood.
**Prerequisite:** Phase 2 checkpoint passed

> [!info] Why Spring Boot?
> It's the #1 framework for Java backend jobs. Most interviews ask: *"Explain how Spring works"*, *"How does auto-configuration work"*, *"What is @Transactional?"*

### Week 1: Spring Boot Fundamentals

- [ ] **Day 27:** **What is Spring Boot?** — IoC, DI, beans
  - [ ] Study: [Spring Boot Interview Questions](Interview-Guides/Spring-Boot-Interview-Questions.md) — Section 1 (Spring Core)
  - [ ] Hands-on: Create your first Spring Boot project with [Spring Initializr](https://start.spring.io/)
- [ ] **Day 28:** **REST API Basics** — @RestController, @GetMapping, @PostMapping
  - [ ] Study: [Spring Boot Interview Questions](Interview-Guides/Spring-Boot-Interview-Questions.md) — Section 3 & 4
  - [ ] Hands-on: Build a simple `GET /api/hello` endpoint
- [ ] **Day 29:** **Request handling** — @PathVariable, @RequestParam, @RequestBody
  - [ ] Practice: Build a `User` API with GET by id, POST create, DELETE
  - [ ] Test with **Postman**
- [ ] **Day 30:** **Validation + Error handling** — @Valid, @ControllerAdvice
  - [ ] Study: Global exception handling section in [Spring Boot Guide](Interview-Guides/Spring-Boot-Interview-Questions.md) §4
  - [ ] Practice: Add validation to your User API

### Week 2: Spring Data JPA

- [ ] **Day 31:** **Database basics** — what is an entity, repository, table
  - [ ] Study: [SQL Interview Questions](Interview-Guides/SQL-Interview-Questions.md) — first sections
  - [ ] Study: JPA section in [Spring Boot Guide](Interview-Guides/Spring-Boot-Interview-Questions.md) §5
- [ ] **Day 32:** **JPA Entity + Repository hands-on**
  - [ ] Hands-on: Create `User` entity with `@Entity`, `@Id`, `@GeneratedValue`
  - [ ] Hands-on: Create `UserRepository` with `JpaRepository`
  - [ ] Hands-on: Connect your User API to the database
- [ ] **Day 33:** **Relationships** — @OneToOne, @OneToMany, @ManyToOne
  - [ ] Practice: Add Orders to your User API (User has many Orders)
- [ ] **Day 34:** **N+1 problem + JOIN FETCH**
  - [ ] Study: N+1 section in [Spring Boot Guide](Interview-Guides/Spring-Boot-Interview-Questions.md) §5
  - [ ] Practice: Fix N+1 in your code with `JOIN FETCH` or `@EntityGraph`

### Week 3: Transactions & Advanced Spring

- [ ] **Day 35:** **@Transactional** — propagation, isolation levels
  - [ ] Study: [Spring Boot Guide](Interview-Guides/Spring-Boot-Interview-Questions.md) §5 (transactions) & §6 (traps)
  - [ ] Practice: Write a method that uses `@Transactional`
- [ ] **Day 36:** **Spring Security** — authentication & authorization basics
  - [ ] Study: [Spring Boot Guide](Interview-Guides/Spring-Boot-Interview-Questions.md) §9
  - [ ] Practice: Add basic authentication to your API
- [ ] **Day 37:** **Testing** — @WebMvcTest, @SpringBootTest
  - [ ] Study: [Spring Boot Guide](Interview-Guides/Spring-Boot-Interview-Questions.md) §7
  - [ ] Practice: Write 3 tests for your API (success case, not found, validation error)

### Week 3: Checkpoint

- [ ] **Day 38:** **Mini Project** — Build a **Book Store API**:
  - [ ] `GET /api/books` — list all books (paginated)
  - [ ] `POST /api/books` — create a book (with validation)
  - [ ] `GET /api/books/{id}` — get one book
  - [ ] `PUT /api/books/{id}` — update a book
  - [ ] Connect to H2 or PostgreSQL database
  - [ ] Handle errors with @ControllerAdvice
- [ ] **Day 39:** Continue building Book Store API (add authors, categories with JPA relationships)
- [ ] **Day 40:** ✅ **CHECKPOINT TEST** — Answer aloud:
  - What is dependency injection?
  - What does @SpringBootApplication do?
  - What is the N+1 problem?
  - What is @Transactional? When does it roll back?
  - Explain the difference between @Controller and @RestController
  - If you can answer these → **Phase 3 complete!**

---

# 📌 PHASE 4: Interview Preparation Topics (Days 41-54)

**Goal:** Learn the remaining interview topics at a high level — enough to answer questions confidently.
**Prerequisite:** Phase 3 checkpoint passed

### Week 1: SQL & LLD

- [ ] **Day 41:** **SQL Deep Dive** — joins, group by, aggregations
  - [ ] Study: [SQL Interview Questions](Interview-Guides/SQL-Interview-Questions.md)
  - [ ] Practice: Write 10 SQL queries (join, group by, having, subquery)
- [ ] **Day 42:** **SQL Practice** — solve interview-style queries
  - [ ] Practice: "Find second highest salary", "Find duplicate emails" from LeetCode SQL problems
- [ ] **Day 43:** **LLD Basics** — what is low-level design? SOLID principles
  - [ ] Study: [SOLID Principles](../LLD/02%20-%20SOLID%20Principles.md)
  - [ ] Practice: Identify SOLID violations in simple code
- [ ] **Day 44:** **Design Patterns (key ones)** — Singleton, Factory, Strategy, Observer
  - [ ] Study: [Design Patterns](../LLD/03%20-%20Design%20Patterns.md)
  - [ ] Practice: Implement each pattern in Java (small examples)

### Week 2: LLD Problems & HLD

- [ ] **Day 45:** **LLD Problem: Vending Machine**
  - [ ] Study: [Vending Machine Design](../LLD/Problems/Vending-Machine.md)
  - [ ] Practice: Draw the class diagram from memory
- [ ] **Day 46:** **LLD Problem: Parking Lot**
  - [ ] Study: [Parking Lot Design](../LLD/Problems/Parking-Lot.md)
  - [ ] Practice: Draw the class diagram from memory
- [ ] **Day 47:** **LLD Problem: Elevator System**
  - [ ] Study: [Elevator System Design](../LLD/Problems/Elevator-System.md)
  - [ ] Practice: Draw the class diagram from memory
- [ ] **Day 48:** **HLD Basics** — what is high-level design? (different from LLD!)
  - [ ] Study: [System Design Interview Guide](../HLD/System-Design-Interview-Guide.md) — Sections 1-3 only (framework + estimation)
  - [ ] Practice: Estimate capacity for a simple app (like a notes app)

### Week 3: HLD & Kafka

- [ ] **Day 49:** **HLD Building Blocks** — load balancers, caching, message queues
  - [ ] Study: [System Design Guide](../HLD/System-Design-Interview-Guide.md) — Section 4
- [ ] **Day 50:** **HLD Problem: URL Shortener**
  - [ ] Study: [System Design Guide](../HLD/System-Design-Interview-Guide.md) — Section 7 (Problem 1)
  - [ ] Practice: Draw the architecture from memory
- [ ] **Day 51:** **HLD Problem: Twitter Feed**
  - [ ] Study: [System Design Guide](../HLD/System-Design-Interview-Guide.md) — Section 7 (Problem 2)
  - [ ] Practice: Explain push vs pull approach aloud
- [ ] **Day 52:** **Kafka Basics** — topics, partitions, consumer groups
  - [ ] Study: [Kafka and Messaging Interview Guide](../HLD/Kafka-and-Messaging-Interview-Guide.md) — Sections 1-3 only
  - [ ] Practice: Draw producer → topic → consumer diagram from memory

### Week 3: Checkpoint

- [ ] **Day 53:** **Timed Practice** — Answer 5 questions from each:
  - [ ] 5 questions from [Core Java Guide](Interview-Guides/Core-Java-Interview-Questions.md)
  - [ ] 5 questions from [Spring Boot Guide](Interview-Guides/Spring-Boot-Interview-Questions.md)
  - [ ] 5 questions from [SQL Guide](Interview-Guides/SQL-Interview-Questions.md)
- [ ] **Day 54:** ✅ **CHECKPOINT TEST** — Answer aloud:
  - What are SOLID principles? Give one example each
  - Difference between Singleton and Factory patterns?
  - What goes into a class diagram? What goes into a system architecture diagram?
  - What is a Kafka partition? Why does it matter?
  - If you can answer these → **Phase 4 complete!**

---

# 📌 PHASE 5: Mock Interviews (Days 55-61)

**Goal:** Practice answering questions under interview conditions — before the real thing.

> [!warning] Don't skip this phase!
> Mock interviews feel awkward, but they are the **best predictor** of real interview performance.

- [ ] **Day 55:** **Mock: Core Java** (45 min)
  - [ ] Set a timer for 45 minutes
  - [ ] Open [Core Java Guide](Interview-Guides/Core-Java-Interview-Questions.md)
  - [ ] Answer 15 questions aloud — no notes!
  - [ ] **Did poorly?** → Note weak topics, re-study those sections
  - [ ] **Did well?** → Mark this complete:
  - [ ] ✅ Passed (answered 12+/15 confidently)

- [ ] **Day 56:** **Mock: Spring Boot** (45 min)
  - [ ] Open [Spring Boot Guide](Interview-Guides/Spring-Boot-Interview-Questions.md)
  - [ ] Answer 15 questions aloud — no notes!
  - [ ] Write 2 code snippets: one `@RestController`, one `@Transactional` method
  - [ ] ✅ Passed (answered 12+/15 confidently)

- [ ] **Day 57:** **Mock: DSA** (45 min)
  - [ ] Open [Blind 75 Index](../DSA/LeetCode/Blind75/Top-75-Index.md)
  - [ ] Pick 2 problems: 1 Easy + 1 Medium
  - [ ] Solve each in 20 minutes — talk while you code
  - [ ] Don't open solutions until after time runs out!
  - [ ] ✅ Passed (solved both, even with help)

- [ ] **Day 58:** **Mock: LLD** (45 min)
  - [ ] Pick 1 problem: Vending Machine, Parking Lot, or Elevator
  - [ ] Draw the full class diagram on paper
  - [ ] Explain your design aloud (5-10 minutes)
  - [ ] ✅ Passed (drew diagram, explained patterns used)

- [ ] **Day 59:** **Mock: HLD** (60 min)
  - [ ] Pick 1 problem: URL Shortener or Twitter Feed
  - [ ] Follow the 9-step framework: requirements → estimate → API → DB → architecture → deep dive → scaling
  - [ ] ✅ Passed (used framework, estimated numbers, drew architecture)

- [ ] **Day 60:** **Behavioral Interview Prep**
  - [ ] Write 3 STAR stories (Situation, Task, Action, Result) from your own experience
  - [ ] Practice "Tell me about yourself" (2 minutes, aloud)
  - [ ] Write 3 questions to ask interviewers
  - [ ] ✅ Completed

- [ ] **Day 61:** **Review + Gap Analysis**
  - [ ] List everything you couldn't answer confidently
  - [ ] Re-study those exact topics (checkboxes below)
  - [ ] ✅ Completed

---

# 📌 PHASE 6: Final Sprint (Days 62-64)

**Goal:** Quick review of everything, day before interview prep.

- [ ] **Day 62:** Re-read the [Pre-Interview Checklist](#-pre-interview-checklist-24-hours-before)
  - [ ] Check off what you can do
  - [ ] Re-study anything you can't
- [ ] **Day 63:** Review quick reference cards
  - [ ] [Java and SQL Quick Reference](Reference/Java-and-SQL-Interview-Quick-Reference.md)
  - [ ] [Current Java and Spring Backend Standards](Reference/Current-Java-and-Spring-Backend-Standards.md)
- [ ] **Day 64:** Rest + light review
  - [ ] NO heavy studying — you know it by now
  - [ ] Read through your notes one last time
  - [ ] ✅ **Interview ready!**

---

## ✅ Pre-Interview Checklist (24 hours before)

### Technical Readiness

- [ ] Can explain HashMap internals (collisions, resizing, treeification)
- [ ] Can write `equals()` + `hashCode()` correctly
- [ ] Can explain stream laziness and parallel streams
- [ ] Can explain `@Transactional` propagation and common traps
- [ ] Can explain N+1 problem and 3 solutions
- [ ] Can draw 3-tier architecture (Client → Server → Database)

### Soft Skills

- [ ] Prepared 3+ STAR stories with numbers
- [ ] Prepared "Tell me about yourself" (2-minute version)
- [ ] Prepared 3+ questions to ask the interviewer

### Logistics

- [ ] Test microphone + camera (for online interviews)
- [ ] Quiet room, stable internet
- [ ] Pen + paper ready (for LLD/HLD drawings)
- [ ] Resume + portfolio links open

---

## 📚 Quick Resource Map (Every Link You Need)

### DSA Resources

| Resource | Use For |
|---|---|
| [DSA Patterns](DSA/Patterns/00%20-%20Index.md) | Main index of all 22 patterns |
| [Blind 75 Index](../DSA/LeetCode/Blind75/Top-75-Index.md) | 75 most common interview problems |
| [SDE Sheet](../DSA/LeetCode/SDE_Sheet/SDE-Sheet-Index.md) | 30-day daily DSA practice plan |
| [Topological Sort Guide](../DSA/LeetCode/Topological-Sorting-Guide.md) | Special topic: dependencies |

### Java & Spring Resources

| Resource | Use For |
|---|---|
| [Core Java Guide](Interview-Guides/Core-Java-Interview-Questions.md) | OOP, collections, concurrency, JVM |
| [Java 8 Guide](Interview-Guides/Java-8-and-Streams-Interview-Questions.md) | Lambdas, streams, Optional |
| [Modern Java Guide](Interview-Guides/Modern-Java-Interview-Questions.md) | Records, virtual threads, pattern matching |
| [Spring Boot Guide](Interview-Guides/Spring-Boot-Interview-Questions.md) | IoC, REST, JPA, transactions, security |
| [SQL Guide](Interview-Guides/SQL-Interview-Questions.md) | Joins, indexes, queries |
| [Docker Guide](../HLD/Docker-for-Java-Developers-Interview-Guide.md) | Containers, deployment |

### Design Resources

| Resource | Use For |
|---|---|
| [LLD Roadmap](../LLD/00%20-%20Roadmap.md) | All LLD concepts + practice problems |
| [Vending Machine](../LLD/Problems/Vending-Machine.md) | LLD practice problem |
| [Parking Lot](../LLD/Problems/Parking-Lot.md) | LLD practice problem |
| [Elevator System](../LLD/Problems/Elevator-System.md) | LLD practice problem |
| [System Design Guide](../HLD/System-Design-Interview-Guide.md) | HLD framework + practice problems |
| [Kafka Guide](../HLD/Kafka-and-Messaging-Interview-Guide.md) | Messaging, event-driven architecture |

---

## 📈 Progress Tracker (Overall)

Check these off as you complete each **phase**:

- [ ] **Phase 0 Complete:** Tools installed, schedule set
- [ ] **Phase 1 Complete:** Java Basics checkpoint passed
- [ ] **Phase 2 Complete:** DSA Foundation checkpoint passed
- [ ] **Phase 3 Complete:** Spring Boot Book API built
- [ ] **Phase 4 Complete:** SQL, LLD, HLD, Kafka topics covered
- [ ] **Phase 5 Complete:** 6 mock interviews completed
- [ ] **Phase 6 Complete:** Final review finished

---

## 🔄 Weekly Review Template

At the end of every week, fill this in:

| Question | Your Answer |
|---|---|
| What did I learn this week? | |
| What is still confusing? | |
| How many DSA problems did I solve? | |
| Did I explain concepts aloud? | ✅ / ❌ |
| What will I focus on next week? | |

---

## ⚡ Interview Day Tips (Read the morning of your interview)

1. **Stay calm** — the interviewer wants to see how you think, not perfection
2. **Clarify before coding** — ask questions about DSA problem constraints
3. **Think aloud** — always explain your reasoning
4. **Write clean code** — use meaningful variable names
5. **Test your code** — walk through examples with sample inputs
6. **State complexity** — always say Time + Space complexity
7. **You don't know something?** — Say "I'm not sure, but here's what I think..."
8. **Ask good questions** — shows genuine interest

---

*Last updated: August 14, 2026*

## Related Notes

- [Java Developer README](README.md)
- [Java Backend Interview Roadmap](Roadmap/Java-Backend-Interview-Roadmap.md)
- [LLD Roadmap](../LLD/00%20-%20Roadmap.md)
- [DSA Patterns](DSA/Patterns/00%20-%20Index.md)
