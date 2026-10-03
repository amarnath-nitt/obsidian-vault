# Design a Caching Weather Proxy

**Source:** AlgoMaster · Low-Level Design Practice · **hard (premium)** · **Pattern:** Proxy
🔗 [AlgoMaster index](https://algomaster.io/practice/low-level-design)

### Problem

A weather service fetches data from a slow external API. Repeated lookups for the same city within a
short window should **not** hit the API again. Insert a **caching proxy** that returns a cached value
when fresh and calls the real service (and refreshes the cache) when stale.

### Approach — Proxy

- **Subject** = `WeatherService` (`getTemperature(city)`).
- **RealSubject** = `RemoteWeatherService` (slow, external).
- **Proxy** = `CachingWeatherProxy` — a cache with a **TTL** per entry.

### Java Solution

```java
import java.util.*;
import java.util.function.LongSupplier;

// Subject
interface WeatherService {
    double getTemperature(String city);
}

// RealSubject — slow external API
class RemoteWeatherService implements WeatherService {
    @Override public double getTemperature(String city) {
        System.out.println("Calling external API for " + city + "...");
        return switch (city.toLowerCase()) {
            case "london" -> 12.5;
            case "delhi"  -> 31.0;
            default       -> 20.0;
        };
    }
}

// Proxy with TTL cache
class CachingWeatherProxy implements WeatherService {

    private record Entry(double temperature, long expiresAt) {}

    private final WeatherService real;
    private final long ttlMillis;
    private final LongSupplier clock;                 // injectable for testing
    private final Map<String, Entry> cache = new HashMap<>();

    CachingWeatherProxy(WeatherService real, long ttlMillis) {
        this(real, ttlMillis, System::currentTimeMillis);
    }
    CachingWeatherProxy(WeatherService real, long ttlMillis, LongSupplier clock) {
        this.real = real; this.ttlMillis = ttlMillis; this.clock = clock;
    }

    @Override
    public synchronized double getTemperature(String city) {
        long now = clock.getAsLong();
        Entry cached = cache.get(city);
        if (cached != null && cached.expiresAt() > now) {
            System.out.println("Cache HIT for " + city);
            return cached.temperature();
        }
        double fresh = real.getTemperature(city);     // cache miss / expired
        cache.put(city, new Entry(fresh, now + ttlMillis));
        return fresh;
    }
}
```

**Usage**
```java
WeatherService svc = new CachingWeatherProxy(new RemoteWeatherService(), 60_000);
svc.getTemperature("London");   // "Calling external API..." then 12.5
svc.getTemperature("London");   // "Cache HIT for London" → 12.5 (no API call)

// with an injected clock you can advance time and force a refresh
```

### Design points
- **TTL caching** — entries expire, so data cannot go stale forever.
- **Transparent to callers** — the same `getTemperature(city)` signature is used.
- **One lock per proxy** — `synchronized` keeps the cache consistent under concurrency (finer-grained
  `ConcurrentHashMap` + per-key locks improve throughput).
- **Injectable clock** — makes TTL behaviour deterministically testable.

**Complexity:** O(1) per lookup (cache hit) · Space O(cities)

---
#proxy #caching #lld #practice