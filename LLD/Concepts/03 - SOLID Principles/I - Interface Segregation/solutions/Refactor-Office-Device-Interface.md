# Refactor an Office Device Interface (Interface Segregation)

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Principle:** Interface Segregation
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/refactor-office-device-interface)

### Problem

An office `AllInOneDevice` interface declares `print`, `scan`, `fax`, and `staple`. A basic printer
that only prints is forced to implement (and stub out) the other three. Refactor into focused
interfaces so each device depends only on the capabilities it has.

### The Smell (before)

```java
// ❌ Fat interface — SimplePrinter must stub 3 methods it cannot do
interface AllInOneDevice {
    void print(String doc);
    void scan(String doc);
    void fax(String doc);
    void staple(String doc);
}

class SimplePrinter implements AllInOneDevice {
    public void print(String doc)  { System.out.println("Printing " + doc); }
    public void scan(String doc)   { throw new UnsupportedOperationException(); }  // noise
    public void fax(String doc)    { throw new UnsupportedOperationException(); }  // noise
    public void staple(String doc) { throw new UnsupportedOperationException(); }  // noise
}
```

### The Fix (after)

```java
interface Printer { void print(String doc); }
interface Scanner { void scan(String doc); }
interface Fax     { void fax(String doc); }
interface Stapler { void staple(String doc); }

class SimplePrinter implements Printer {                       // only what it can do
    public void print(String doc) { System.out.println("Printing " + doc); }
}

class OfficeAllInOne implements Printer, Scanner, Fax, Stapler {
    public void print(String doc)  { System.out.println("Printing " + doc); }
    public void scan(String doc)   { System.out.println("Scanning " + doc); }
    public void fax(String doc)    { System.out.println("Faxing " + doc); }
    public void staple(String doc) { System.out.println("Stapling " + doc); }
}

// Clients depend only on the capability they need
class PrintService {
    void printAll(java.util.List<Printer> printers, String doc) {
        for (Printer p : printers) p.print(doc);       // never needs scan/fax/staple
    }
}
```

**Usage**
```java
PrintService service = new PrintService();
service.printAll(List.of(new SimplePrinter(), new OfficeAllInOne()), "report.pdf");
```

### Design points
- **No empty stubs** — `SimplePrinter` implements exactly one method.
- **Clients depend on the smallest contract** — `PrintService` needs only `Printer`.
- **Capabilities compose** — `OfficeAllInOne` implements four interfaces; a scanner-only device
  implements just `Scanner`.
- **No false "is-a"** — a simple printer is not forced to claim it can fax.

**Complexity:** O(devices) per print job · Space O(1)

---
#solid #isp #lld #practice