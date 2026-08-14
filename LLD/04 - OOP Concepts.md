# 4. Object-Oriented Programming (OOP) Concepts

### 📝 Revision Notes
- **Encapsulation**: Bundling data (attributes) and methods that operate on the data within a single unit (class), and restricting direct access to some of the object's components (data hiding). Achieved using access modifiers (private, public, protected).
- **Abstraction**: Hiding the complex implementation details and showing only the essential features of an object. Achieved using abstract classes and interfaces.
- **Inheritance**: A mechanism where one class acquires the properties and behaviors of another class. Promotes code reusability. (e.g., `class Dog extends Animal`).
- **Polymorphism**: The ability of an object to take on many forms. It allows objects of different classes to be treated as objects of a common superclass. (e.g., Method Overloading, Method Overriding).
- **Composition vs. Inheritance**:
    - **Inheritance (is-a relationship)**: `Dog is-a Animal`. Strong coupling, "white-box" reuse.
    - **Composition (has-a relationship)**: `Car has-a Engine`. Flexible, "black-box" reuse, preferred for loose coupling.

### 💬 Interview Q&A

> [!question] Explain Encapsulation and its benefits.
> Encapsulation is the bundling of data and methods that operate on that data within a single unit (a class), and restricting direct access to the data from outside the bundle. This is typically achieved by making fields `private` and providing `public` getter/setter methods. Benefits include data hiding (protecting internal state), better control over data access, easier debugging, and improved maintainability as internal implementation can change without affecting external code.

> [!question] What is Abstraction in OOP? How is it different from Encapsulation?
> Abstraction is the process of hiding complex implementation details and showing only the essential features of an object. It focuses on *what* an object does rather than *how* it does it. It's achieved through abstract classes and interfaces.
> Encapsulation is about *how* to achieve this hiding by bundling data and methods and controlling access. Abstraction is about *what* to hide. Encapsulation is a mechanism, while abstraction is a concept.

> [!question] Describe Polymorphism with an example.
> Polymorphism means "many forms." In OOP, it allows objects of different classes to be treated as objects of a common superclass. For example, if `Dog` and `Cat` both extend `Animal` and override an `makeSound()` method, you can have a `List<Animal>` containing both `Dog` and `Cat` objects. When you call `animal.makeSound()` on each, the appropriate `makeSound()` method (from `Dog` or `Cat`) is invoked at runtime. This is runtime polymorphism (method overriding). Compile-time polymorphism is method overloading.

> [!question] When would you prefer Composition over Inheritance?
> You should generally prefer composition over inheritance ("has-a" over "is-a") because it offers greater flexibility and reduces coupling. Inheritance creates a strong, rigid relationship where a subclass is tightly coupled to its superclass. Composition allows you to build complex objects by combining simpler ones, enabling dynamic behavior changes and easier testing. For example, instead of a `Car` inheriting `Engine`, `Car` *has-a* `Engine`. This allows `Car` to easily swap out different `Engine` types.

---
## 🔗 Related
- [[00 - Roadmap]]