# 5. UML Diagrams

### 📝 Revision Notes
- **UML (Unified Modeling Language)**: A standard for visualizing, specifying, constructing, and documenting the artifacts of a software system.
- **Class Diagram**: Shows the static structure of a system, including classes, their attributes, operations (methods), and the relationships among objects.
    - **Relationships**: Association, Aggregation, Composition, Generalization (Inheritance), Realization (Interface Implementation), Dependency.
- **Sequence Diagram**: Shows the dynamic interaction between objects in a time-ordered sequence. It depicts the objects and the messages they exchange to perform a particular function.

### 💬 Interview Q&A

> [!question] What is a Class Diagram and what elements does it typically show?
> A Class Diagram is a static UML diagram that illustrates the structure of a system by showing its classes, their attributes (data members), operations (methods), and the relationships between classes. Key elements include:
> - **Classes**: Represented by a rectangle divided into three compartments (name, attributes, operations).
> - **Attributes**: Variables within a class, often with visibility (`+` public, `-` private, `#` protected).
> - **Operations**: Methods of a class, also with visibility.
> - **Relationships**: Association (general link), Aggregation (whole-part, parts can exist independently), Composition (strong whole-part, parts cannot exist independently), Generalization (inheritance), Realization (interface implementation), Dependency.

> [!question] When would you use a Sequence Diagram?
> A Sequence Diagram is a dynamic UML diagram used to model the interactions between objects in a system over time. It's particularly useful for:
> - Visualizing the flow of control for a specific use case or scenario.
> - Understanding how objects collaborate to achieve a goal.
> - Debugging and identifying potential bottlenecks or communication issues.
> - Documenting the behavior of a system.

---
## 🔗 Related
- [[00 - Roadmap]]