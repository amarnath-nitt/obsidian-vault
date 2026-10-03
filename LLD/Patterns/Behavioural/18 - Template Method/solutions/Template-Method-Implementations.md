# Template Method — Implementations & Examples

**Pattern:** Template Method (Behavioural) · **Skill:** shared algorithm skeleton with varying steps

### Approach

- Put the fixed sequence in a `final` **template method**.
- Declare **abstract** primitive operations for mandatory steps and **hooks** for optional ones.
- Subclasses implement the steps — never the sequence.

### Java Solutions

**1. Beverage Preparation**
```java
abstract class Beverage {
    // template method — the skeleton, protected from override
    final void prepare() {
        boilWater();
        brew();
        pourInCup();
        if (customerWantsCondiments()) addCondiments();   // hook
        System.out.println("--- done ---");
    }
    protected void boilWater() { System.out.println("Boiling water"); }
    protected void pourInCup() { System.out.println("Pouring into cup"); }
    protected abstract void brew();                       // mandatory step
    protected abstract void addCondiments();              // mandatory step
    protected boolean customerWantsCondiments() { return true; }   // hook (optional)
}

class Tea extends Beverage {
    protected void brew()           { System.out.println("Steeping tea"); }
    protected void addCondiments()  { System.out.println("Adding lemon"); }
}
class Coffee extends Beverage {
    protected void brew()           { System.out.println("Dripping coffee"); }
    protected void addCondiments()  { System.out.println("Adding sugar & milk"); }
    @Override protected boolean customerWantsCondiments() { return false; }  // overrides hook
}
// usage
new Tea().prepare();
new Coffee().prepare();
```

**2. Data Processing Pipeline**
```java
abstract class DataImporter {
    final void importData(String source) {                // fixed pipeline
        String raw = read(source);
        Object parsed = parse(raw);
        Object validated = validate(parsed);
        save(validated);
        cleanup();                                        // hook
    }
    protected abstract String read(String source);
    protected abstract Object parse(String raw);
    protected abstract Object validate(Object data);
    protected abstract void save(Object data);
    protected void cleanup() { /* optional */ }
}

class CsvImporter extends DataImporter {
    protected String read(String s)          { return "a,b,c"; }
    protected Object parse(String raw)       { return raw.split(","); }
    protected Object validate(Object data)   { return data; }
    protected void save(Object data)         { System.out.println("Saved CSV rows"); }
}
class JsonImporter extends DataImporter {
    protected String read(String s)          { return "{\"k\":1}"; }
    protected Object parse(String raw)       { return raw; }
    protected Object validate(Object data)   { return data; }
    protected void save(Object data)         { System.out.println("Saved JSON doc"); }
    @Override protected void cleanup()        { System.out.println("cleanup temp"); }
}
```

**3. Game Turn Sequence**
```java
abstract class Game {
    final void play(int turns) {
        initialize();
        for (int i = 0; i < turns; i++) {
            collectInput();
            update();
            render();
        }
        endGame();
    }
    protected abstract void initialize();
    protected abstract void collectInput();
    protected abstract void update();
    protected abstract void render();
    protected void endGame() { System.out.println("Game over"); }
}
class ChessGame extends Game {
    protected void initialize()   { System.out.println("Set up pieces"); }
    protected void collectInput() { System.out.println("Read move"); }
    protected void update()       { System.out.println("Apply move"); }
    protected void render()       { System.out.println("Draw board"); }
}
```

**4. Template Method + Factory Method**
```java
abstract class DocumentProcessor {
    final void process() {                    // template
        Document doc = createDocument();      // factory method
        doc.open();
        doc.parse();
        doc.close();
    }
    protected abstract Document createDocument();
}
interface Document { void open(); void parse(); void close(); }
```

**Complexity:** O(steps) per run · Space O(1) beyond subclass state

**Design note:** template method gives the **base class control of the sequence**, which is exactly what frameworks need to enforce invariants across all subclasses.