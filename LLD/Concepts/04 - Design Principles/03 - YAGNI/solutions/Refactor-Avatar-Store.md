# Refactor Avatar Store (YAGNI)

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Principle:** YAGNI
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/refactor-avatar-store)

### Problem

An avatar store was built with speculative features "just in case" — pluggable storage backends,
an unused CDN strategy, and a resize pipeline — none of which are required. Apply **YAGNI**: remove
what is not needed now and keep only the single required behaviour.

### The Smell (before)

```java
// ❌ Speculative machinery for a store that just needs to keep an avatar URL
interface StorageBackend { void put(String key, byte[] data); byte[] get(String key); }
class S3Backend implements StorageBackend { /* unused */ }
class LocalBackend implements StorageBackend { /* unused */ }

interface CdnStrategy { String rewrite(String url); }
class NoCdn implements CdnStrategy { /* unused */ }

class AvatarStore {
    private final StorageBackend backend;      // pluggable but only one is ever used
    private final CdnStrategy cdn;
    private final List<ResizeRule> rules;      // never configured

    AvatarStore(StorageBackend backend, CdnStrategy cdn, List<ResizeRule> rules) { ... }

    void setAvatar(String userId, byte[] image) { backend.put(userId, image); }
    byte[] getAvatar(String userId)             { return backend.get(userId); }
    // ...plugin registry, resize engine, etc. — all unused
}
```

### The Fix (after)

```java
import java.util.*;

// The single behaviour actually required: store and retrieve a user's avatar bytes.
class AvatarStore {
    private final Map<String, byte[]> avatars = new HashMap<>();

    void setAvatar(String userId, byte[] image) {
        if (image == null || image.length == 0) throw new IllegalArgumentException("empty image");
        avatars.put(userId, image.clone());
    }

    Optional<byte[]> getAvatar(String userId) {
        byte[] image = avatars.get(userId);
        return image == null ? Optional.empty() : Optional.of(image.clone());
    }

    void removeAvatar(String userId) { avatars.remove(userId); }
}
```

### Design points
- **Delete speculative abstractions** — the storage/CDN/resize machinery is gone.
- **YAGNI** — no code for features nobody asked for.
- **Easier to read** — one small class with obvious behaviour.
- **Easy to grow later** — if a second backend is genuinely needed, refactor *then*.

> **YAGNI principle:** build what is required now. Speculative generality costs maintenance today for
> a benefit that may never arrive. (Note the tension with OCP — design *for* change, don't *build*
> it pre-emptively.)

**Complexity:** O(1) per operation · Space O(avatars)

---
#design-principles #yagni #lld #practice