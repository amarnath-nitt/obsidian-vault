# Design a Build Pipeline

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Template Method
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-build-pipeline)

### Problem

A CI build runs the same stages in a fixed order — **checkout → compile → test → package → deploy** —
but the concrete commands differ per project type (Java, Node, Python). Enforce the stage sequence
once and let each project supply its own steps.

### Approach — Template Method

- `BuildPipeline` defines the `final` `run()` sequence with short-circuit on failure.
- Abstract steps: `checkout()`, `compile()`, `test()`, `packageArtifact()`, `deploy()`.
- A `shouldDeploy()` hook lets projects skip deployment.

### Java Solution

```java
abstract class BuildPipeline {
    // Template method — fixed stage order, stops on failure
    final void run() {
        try {
            checkout();
            compile();
            test();
            packageArtifact();
            if (shouldDeploy()) deploy();
            System.out.println("✔ Pipeline succeeded (" + projectName() + ")");
        } catch (RuntimeException e) {
            System.out.println("✘ Pipeline failed (" + projectName() + "): " + e.getMessage());
        }
    }

    abstract String projectName();
    protected abstract void checkout();
    protected abstract void compile();
    protected abstract void test();
    protected abstract void packageArtifact();
    protected void deploy() { System.out.println("Deploying artifact"); }   // shared default
    protected boolean shouldDeploy() { return true; }                       // hook
}

class JavaPipeline extends BuildPipeline {
    String projectName() { return "java"; }
    protected void checkout()        { System.out.println("git clone"); }
    protected void compile()         { System.out.println("mvn compile"); }
    protected void test()            { System.out.println("mvn test"); }
    protected void packageArtifact() { System.out.println("mvn package → app.jar"); }
}

class NodePipeline extends BuildPipeline {
    String projectName() { return "node"; }
    protected void checkout()        { System.out.println("git clone"); }
    protected void compile()         { System.out.println("tsc"); }
    protected void test()            { System.out.println("npm test"); }
    protected void packageArtifact() { System.out.println("npm pack"); }
    @Override protected void deploy()        { System.out.println("npm publish"); }
    @Override protected boolean shouldDeploy() { return false; }   // skip deploy for this project
}
```

**Usage**
```java
new JavaPipeline().run();
new NodePipeline().run();   // deploy skipped (hook returns false)
```

### Design points
- **Fixed stage order** — the base class owns the sequence (and the failure short-circuit).
- **Varying steps abstract** — each project supplies its own commands.
- **Hooks** — `deploy`/`shouldDeploy` are optional extension points.

**Complexity:** O(stages) per run · Space O(1)

---
#template-method #ci #lld #practice