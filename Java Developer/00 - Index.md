# Java Developer - Index

Welcome to the Java Developer interview preparation vault. This directory is organized by topic to help you prepare systematically for Java developer interviews.

---

## 📖 Quick Navigation

| Area             | Guide                                                      | Description                                                          |
| ---------------- | ---------------------------------------------------------- | -------------------------------------------------------------------- |
| **Java Core**    | [Java Core Index](Java%20Core/00%20-%20Index.md)           | OOP, collections, streams, concurrency, JVM internals, code snippets |
| **Spring Boot**  | [Spring Boot Index](Spring%20Boot/00%20-%20Index.md)       | IoC, DI, REST, JPA, transactions, security, testing                  |
| **Hibernate**    | [Hibernate Index](Hibernate/00%20-%20Index.md)             | JPA, entity lifecycle, relationships, caching, performance           |
| **SQL**          | [SQL Index](SQL/00%20-%20Index.md)                         | Joins, aggregations, window functions, practice queries              |
| **Git & GitHub** | [Git & GitHub Index](Git%20&%20GitHub/00%20-%20Index.md) | Version control, branching, remotes, workflows, cheat sheet          |
| **Practice**     | [Practice Index](Practice/00%20-%20Index.md)               | Solved exercises and code practice                                   |
| **Reference**    | [Reference Index](Reference/00%20-%20Index.md)             | Quick reference cards and cheat sheets                               |
| **Roadmap**      | [Roadmap Index](Roadmap/Java-Backend-Interview-Roadmap.md) | Learning path and topic dependencies                                 |

---

## 📚 Recommended Study Path

### For Beginners
1. Start with **Java Core** — OOP, collections, exceptions, generics
2. Move to **Java 8 & Streams** — lambdas, functional operations
3. Learn **Spring Boot** — build REST APIs with JPA
4. Understand **SQL** — queries, joins, window functions
5. Practice **Git & GitHub** — version control workflows
6. Study **Hibernate** — JPA deep dive for persistence

### For Experienced Developers
1. Review **Modern Java** (Java 9-17+ features)
2. Deep dive **Hibernate** internals (caching, dirty checking, optimization)
3. Master **SQL** window functions and performance tuning
4. Study **Spring Security** and advanced **Spring Boot** features
5. Practice system design with **HLD** guides

---

## 📊 Progress Tracker

Check off topics as you complete them:

- [ ] **Java Core:** ☐ Core Java Interview Questions ☐ Code Snippet Practice
- [ ] **Spring Boot:** ☐ Spring Boot Interview Questions ☐ Data JPA
- [ ] **Hibernate:** ☐ Hibernate Interview Questions
- [ ] **SQL:** ☐ SQL Interview Questions ☐ SQL Practice Questions
- [ ] **Git & GitHub:** ☐ Git Interview Questions ☐ Git Commands Cheat Sheet
- [ ] **System Design:** ☐ HLD Interview Guide

---

## 🔗 Related Areas

- [Java Developer Master Plan](Interview-Preparation-Master-Plan.md) — 10-week preparation roadmap
- [Java Backend Interview Roadmap](Roadmap/Java-Backend-Interview-Roadmap.md) — topic dependencies
- [LLD Roadmap](../LLD/00%20-%20Roadmap.md) — Low-Level Design practice problems
- [HLD Index](../HLD/00%20-%20Index.md) — High-Level Design, system design, Docker, Kafka
- [DSA Patterns](DSA/Patterns/00%20-%20Index.md) — Data structures & algorithms by pattern
- [LeetCode Index](../DSA/LeetCode/00%20-%20Index.md) — LeetCode problems and solutions

---

## 📁 Folder Structure Overview

```
Java Developer/
├── 00 - Index.md                    ← This file (main entry point)
├── README.md                        ← Vault home page
├── Interview-Preparation-Master-Plan.md
├── 📁 Java Core/                      ← OOP, collections, streams, concurrency
│   ├── 00 - Index.md
│   ├── Core-Java-Interview-Questions.md
│   ├── Java-8-and-Streams-Interview-Questions.md
│   ├── Java-9-to-17-Features-Interview-Questions.md
│   ├── Modern-Java-Interview-Questions.md
│   ├── Core-Java-Code-Snippet-Practice.md
│   ├── OOP-Code-Snippet-Practice.md
│   ├── Java-8-and-Streams-Code-Snippet-Practice.md
│   ├── Exception-Handling-Code-Snippet-Practice.md
│   ├── Java-Concurrency-Code-Snippet-Practice.md
│   ├── JVM-Memory-Code-Snippet-Practice.md
│   └── Modern-Java-Code-Snippet-Practice.md
├── 📁 Spring Boot/                    ← REST API, JPA, transactions, security
│   ├── 00 - Index.md
│   ├── Spring-Boot-Interview-Questions.md
│   └── Spring-Data-JPA-Stored-Procedures.md
├── 📁 Hibernate/                      ← JPA entity lifecycle, relationships, caching
│   └── Hibernate-Interview-Questions.md
├── 📁 SQL/                            ← Database queries, joins, window functions
│   ├── 00 - Index.md
│   └── SQL-Practice-Questions.md
├── 📁 Git & GitHub/                    ← Version control, branching, remotes
│   ├── 00 - Index.md
│   ├── Git-Interview-Questions.md
│   └── Git-Commands-Cheat-Sheet.md
├── 📁 Practice/                       ← Solved exercises
├── 📁 Reference/                      ← Quick reference cards
└── 📁 Roadmap/                        ← Learning paths and topic dependencies
```

---

## ✅ Interview Checklist (Core Java)

- [ ] Can explain OOP principles (encapsulation, inheritance, polymorphism, abstraction)
- [ ] Can write `equals()` and `hashCode()` correctly
- [ ] Can explain `final`, `finally`, `finalize` differences
- [ ] Can explain `static` vs `instance` members
- [ ] Can explain `this` vs `super` keywords
- [ ] Can explain `String` vs `StringBuilder` vs `StringBuffer`
- [ ] Can explain `ArrayList` vs `LinkedList` vs `Vector`
- [ ] Can explain `HashMap` internals (collisions, treeification, load factor)
- [ ] Can explain `Collections.synchronizedList` vs `ConcurrentHashMap`
- [ ] Can explain `final` keyword behavior with references

---

## ✅ Interview Checklist (Spring Boot)

- [ ] Can explain IoC and DI
- [ ] Can explain bean scopes (singleton, prototype)
- [ ] Can explain `@Autowired` vs `@Inject`
- [ ] Can explain `@Configuration` vs `@Component`
- [ ] Can explain `@SpringBootApplication` composition
- [ ] Can explain auto-configuration conditions
- [ ] Can write `@RestController` with validation
- [ ] Can implement global exception handling
- [ ] Can explain N+1 problem with 3 solutions
- [ ] Can explain `@Transactional` propagation and common traps
- [ ] Can configure Spring Security + JWT
- [ ] Can write tests with MockMvc

---

## ✅ Interview Checklist (Hibernate/JPA)

- [ ] Can explain entity lifecycle (transient → persistent → detached → removed)
- [ ] Can explain `save()` vs `persist()` vs `merge()` vs `update()`
- [ ] Can explain relationship types and owning side
- [ ] Can explain N+1 problem with 4 solutions
- [ ] Can explain EAGER vs LAZY loading
- [ ] Can explain `@Version` optimistic locking
- [ ] Can explain first-level vs second-level cache
- [ ] Can explain dirty checking
- [ ] Can explain cascade types and orphan removal
- [ ] Can explain JPQL vs Native SQL vs Criteria API

---

## ✅ Interview Checklist (SQL)

- [ ] Can write JOIN queries (INNER, LEFT, RIGHT, FULL)
- [ ] Can write GROUP BY with HAVING
- [ ] Can write subqueries and CTEs
- [ ] Can write window functions (ROW_NUMBER, RANK, LEAD, LAG)
- [ ] Can optimize queries with proper indexes
- [ ] Can explain execution plans
- [ ] Can write pagination queries

---

## 📅 Weekly Study Template

At the end of every week, fill this in:

| Question | Your Answer |
|---|---|
| What did I learn this week? | |
| What is still confusing? | |
| How many problems did I solve? | |
| Did I explain concepts aloud? | ✅ / ❌ |
| What will I focus on next week? | |

---

*Last updated: August 14, 2026*

## Related Notes

- [Java Developer README](../README.md)
- [Java Backend Interview Roadmap](../Roadmap/Java-Backend-Interview-Roadmap.md)
- [LLD Roadmap](../LLD/00%20-%20Roadmap.md)
- [DSA Patterns](DSA/Patterns/00%20-%20Index.md)