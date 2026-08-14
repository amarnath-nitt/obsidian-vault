# 6. Core Design Principles (DRY, KISS, YAGNI)

### 📝 Revision Notes
- **DRY (Don't Repeat Yourself)**: Avoid duplicating code or knowledge. Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.
- **KISS (Keep It Simple, Stupid)**: Most systems work best if they are kept simple rather than made complex. Simplicity should be a key goal in design.
- **YAGNI (You Ain't Gonna Need It)**: Do not add functionality until it is necessary. Avoid building features that are not currently required, as they often lead to unnecessary complexity and maintenance overhead.

### 💬 Interview Q&A

> [!question] Explain the DRY principle and how it applies to LLD.
> The DRY (Don't Repeat Yourself) principle states that every piece of knowledge or logic should have a single, unambiguous, authoritative representation within a system. In LLD, this means avoiding duplicate code, configuration, or design decisions. It's applied by using techniques like inheritance, composition, utility classes, and design patterns to centralize common logic, making the system easier to maintain and less prone to errors.

> [!question] How does the KISS principle guide your design decisions?
> The KISS (Keep It Simple, Stupid) principle guides design by advocating for simplicity as a primary goal. It encourages developers to choose the simplest possible solution that meets the requirements, avoiding unnecessary complexity, features, or convoluted logic. Simple designs are generally easier to understand, implement, test, and maintain, reducing the likelihood of bugs and long-term costs.

> [!question] What is the YAGNI principle, and why is it important in agile development?
> YAGNI (You Ain't Gonna Need It) is a principle that advises against adding functionality until it is absolutely necessary. It's crucial in agile development because agile methodologies emphasize iterative development and responding to change. Building features "just in case" often leads to wasted effort, increased complexity, and code that may never be used. YAGNI helps keep the codebase lean, focused, and adaptable to evolving requirements.

---
## 🔗 Related
- [[00 - Roadmap]]