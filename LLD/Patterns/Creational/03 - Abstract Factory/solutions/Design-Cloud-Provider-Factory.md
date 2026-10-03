# Design Cloud Provider Factory

**Source:** AlgoMaster · Low-Level Design Practice · **hard** · **Pattern:** Abstract Factory
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-cloud-provider-factory)

### Problem

An infrastructure manager provisions a **family** of cloud resources (`Storage`, `Compute`, `Queue`)
for a chosen provider. Resources from different providers are not interchangeable, so the manager
must obtain a **consistent set** from one provider's factory.

### Approach

- Abstract products: `Storage`, `Compute`, `Queue`.
- `CloudProviderFactory` — declares `createStorage()`, `createCompute()`, `createQueue()`.
- One concrete factory per provider (`AwsFactory`, `GcpFactory`, `AzureFactory`).
- A registry maps a provider name → factory; the client requests a family by name.

### Java Solution

```java
// Abstract products
interface Storage { String put(String key, String value); }
interface Compute { String run(String task); }
interface Queue   { void publish(String message); }

// AWS family
class S3Storage    implements Storage { public String put(String k, String v) { return "S3:" + k + "=" + v; } }
class Ec2Compute   implements Compute { public String run(String t) { return "EC2 ran " + t; } }
class SqsQueue     implements Queue   { public void publish(String m) { System.out.println("SQS: " + m); } }

// GCP family
class GcsStorage   implements Storage { public String put(String k, String v) { return "GCS:" + k + "=" + v; } }
class GceCompute   implements Compute { public String run(String t) { return "GCE ran " + t; } }
class PubSubQueue  implements Queue   { public void publish(String m) { System.out.println("PubSub: " + m); } }

// Abstract factory
interface CloudProviderFactory {
    Storage createStorage();
    Compute createCompute();
    Queue   createQueue();
}

class AwsFactory implements CloudProviderFactory {
    public Storage createStorage() { return new S3Storage(); }
    public Compute createCompute() { return new Ec2Compute(); }
    public Queue   createQueue()   { return new SqsQueue(); }
}
class GcpFactory implements CloudProviderFactory {
    public Storage createStorage() { return new GcsStorage(); }
    public Compute createCompute() { return new GceCompute(); }
    public Queue   createQueue()   { return new PubSubQueue(); }
}
```

**Provider registry (pick a family by name)**
```java
import java.util.*;
import java.util.function.Supplier;

class CloudProviderRegistry {
    private static final Map<String, Supplier<CloudProviderFactory>> PROVIDERS = new HashMap<>();
    static {
        PROVIDERS.put("aws", AwsFactory::new);
        PROVIDERS.put("gcp", GcpFactory::new);
    }
    static CloudProviderFactory of(String name) {
        Supplier<CloudProviderFactory> s = PROVIDERS.get(name.toLowerCase());
        if (s == null) throw new IllegalArgumentException("Unknown provider: " + name);
        return s.get();
    }
}
```

**Client — one provider, consistent resources**
```java
class InfraManager {
    private final Storage storage;
    private final Compute compute;
    private final Queue   queue;

    InfraManager(CloudProviderFactory factory) {
        this.storage = factory.createStorage();
        this.compute = factory.createCompute();
        this.queue   = factory.createQueue();
    }
    void deploy() {
        System.out.println(storage.put("config", "v1"));
        System.out.println(compute.run("build"));
        queue.publish("deployed");
    }
}

// usage
new InfraManager(CloudProviderRegistry.of("gcp")).deploy();
```

### Design points
- **Family consistency** — `storage`, `compute`, `queue` always come from the same provider.
- **Swappable provider** — one line (`of("gcp")`) migrates the whole stack.
- **Trade-off** — adding a new **resource type** means editing the abstract factory and **all** providers.

**Complexity:** O(1) per resource · Space O(1)

---
#abstract-factory #cloud #lld #practice