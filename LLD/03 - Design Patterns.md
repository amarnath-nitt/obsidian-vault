# 3. Design Patterns

### 📝 Revision Notes
- **Creational Patterns**: Deal with object creation mechanisms, trying to create objects in a manner suitable to the situation. (e.g., Singleton, Factory Method, Abstract Factory, Builder, Prototype).
- **Structural Patterns**: Deal with the composition of classes and objects. (e.g., Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy).
- **Behavioral Patterns**: Deal with the communication between objects and classes. (e.g., Chain of Responsibility, Command, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor).

### Common Patterns
- **Singleton**: Ensures a class has only one instance and provides a global point of access to it.
- **Factory Method**: Defines an interface for creating an object, but lets subclasses decide which class to instantiate.
- **Observer**: Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- **Strategy**: Defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
- **Decorator**: Attaches additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

### 💬 Interview Q&A

> [!question] What is a Design Pattern, and why are they important?
> A Design Pattern is a general, reusable solution to a commonly occurring problem within a given context in software design. They are not finished designs that can be directly transformed into code, but rather templates or guidelines. They are important because they provide proven solutions, promote common vocabulary among developers, improve code readability, maintainability, and flexibility, and help avoid common pitfalls.

> [!question] Explain the Singleton pattern and its use cases.
> The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance. It's useful for resources that should be unique across the application, such as a database connection pool, a logger, or a configuration manager. Care must be taken to implement it correctly in multithreaded environments (e.g., using double-checked locking or `Enum` singletons).

> [!question] Describe the Observer pattern. When would you use it?
> The Observer pattern defines a one-to-many dependency between objects. When a "subject" object changes state, all its "observer" dependents are notified and updated automatically. It's used when a change in one object requires changes in others, but you don't want tight coupling between them. Common use cases include event handling systems, GUI components (e.g., a button notifying listeners), and stock market applications.

> [!question] What's the difference between a Factory Method and an Abstract Factory?
> - **Factory Method**: Defines an interface for creating an object, but lets subclasses decide which class to instantiate. It defers instantiation to subclasses. It's about creating *one* product.
> - **Abstract Factory**: Provides an interface for creating *families* of related or dependent objects without specifying their concrete classes. It's about creating *multiple* related products.

> [!question] When would you choose the Strategy pattern over a series of if-else statements?
> The Strategy pattern is preferred when you have multiple related algorithms or behaviors that can be interchanged at runtime. It encapsulates each algorithm into a separate class, making them independent and easily extensible. This avoids long, complex `if-else` or `switch-case` blocks, improves readability, and adheres to OCP by allowing new strategies to be added without modifying existing client code.

---
## 🔗 Related
- [[00 - Roadmap]]