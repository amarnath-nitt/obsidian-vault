# Implement a Lazy Image Proxy

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Proxy
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/implement-lazy-image-proxy)

### Problem

An image gallery shows many thumbnails, but loading a full-resolution image is expensive. Create the
real image **only when it is first displayed**, while presenting the same interface the gallery
already uses. This is a **virtual proxy**.

### Approach — Proxy

- **Subject** = `Image` (`display`).
- **RealSubject** = `RealImage` (expensive load in its constructor).
- **Proxy** = `ImageProxy` — holds the file name, creates the real image on first use.

### Java Solution

```java
interface Image {
    void display();
}

class RealImage implements Image {
    private final String file;

    RealImage(String file) {
        this.file = file;
        loadFromDisk();                       // expensive
    }
    private void loadFromDisk() { System.out.println("Loading " + file + " from disk..."); }
    @Override public void display() { System.out.println("Displaying " + file); }
}

class ImageProxy implements Image {
    private final String file;
    private RealImage real;                    // created lazily

    ImageProxy(String file) { this.file = file; }

    @Override
    public void display() {
        if (real == null) real = new RealImage(file);   // load only on first display
        real.display();
    }
}
```

**Usage**
```java
Image img = new ImageProxy("wallpaper.png");  // nothing loaded yet
System.out.println("Proxy created");
img.display();   // now "Loading wallpaper.png..." then "Displaying wallpaper.png"
img.display();   // cached — only "Displaying wallpaper.png"
```

### Design points
- **Deferred creation** — the heavy `RealImage` is built on first `display()`, not at construction.
- **Same interface** — the gallery calls `display()` and never knows a proxy is in play.
- **Memoised** — the second `display()` reuses the already-loaded image.

### Thread-safety note
For concurrent access, guard the lazy init with **double-checked locking** (`volatile real` + a
synchronised block) so only one `RealImage` is ever created.

**Complexity:** O(1) after first load · Space O(1) per proxy

---
#proxy #lld #practice