# 2. SOLID Principles

### 📝 Revision Notes
- **S - Single Responsibility Principle (SRP)**: A class should have only one reason to change. It should have only one job.
- **O - Open/Closed Principle (OCP)**: Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.
- **L - Liskov Substitution Principle (LSP)**: Subtypes must be substitutable for their base types without altering the correctness of the program. (If S is a subtype of T, then objects of type T may be replaced with objects of type S without altering any of the desirable properties of that program).
- **I - Interface Segregation Principle (ISP)**: Clients should not be forced to depend on interfaces they do not use. Many client-specific interfaces are better than one general-purpose interface.
- **D - Dependency Inversion Principle (DIP)**: High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.

### 💬 Interview Q&A

> [!question] Explain the Single Responsibility Principle (SRP) with an example.
> SRP states that a class should have only one reason to change, meaning it should have only one job or responsibility. For example, a `User` class should only manage user data (name, email). If it also handled saving users to a database or sending emails, it would violate SRP. Instead, `UserRepository` could handle persistence, and `EmailService` could handle emails.

> [!question] How does the Open/Closed Principle (OCP) promote maintainability?
> OCP promotes maintainability by advocating that software entities should be open for extension but closed for modification. This means you can add new functionality without changing existing, tested code. This is typically achieved through abstraction (interfaces or abstract classes) and polymorphism, allowing new implementations to be plugged in without altering the core logic.

> [!question] What is the Liskov Substitution Principle (LSP) and why is it important?
> LSP states that objects of a superclass should be replaceable with objects of its subclasses without breaking the application. It ensures that inheritance is used correctly, maintaining behavioral consistency. Violating LSP can lead to unexpected behavior, runtime errors, and difficulty in understanding and maintaining the code. A classic example is a `Square` inheriting from `Rectangle` where `setHeight` and `setWidth` behave differently for `Square`.

> [!question] When would you apply the Interface Segregation Principle (ISP)?
> ISP is applied when a single, large interface forces clients to implement methods they don't need. It suggests breaking down large interfaces into smaller, more specific ones. For example, instead of a single `Worker` interface with `work()` and `eat()`, you might have `Workable` and `Feedable` interfaces. This prevents clients from having to implement irrelevant methods and reduces coupling.

> [!question] Describe the Dependency Inversion Principle (DIP) and its benefits.
> DIP states that high-level modules should not depend on low-level modules; both should depend on abstractions. Also, abstractions should not depend on details; details should depend on abstractions. This means using interfaces or abstract classes to decouple components. Benefits include increased modularity, testability (easy to mock dependencies), and flexibility, as implementations can be swapped without affecting high-level logic. Dependency Injection is a common technique to achieve DIP.

---
## 🔗 Related
- [[00 - Roadmap]]