# Design a File Tree

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Composite
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-file-tree)

### Problem

Model an in-memory **file tree**: files have a size; folders contain files and other folders.
Support computing the **total size** of any subtree and printing the tree with its structure.

### Approach — Composite

- **Component** = `FsNode` (`size`, `print`).
- **Leaf** = `FileNode`.
- **Composite** = `FolderNode` (children, recursion).

### Java Solution

```java
import java.util.*;

interface FsNode {
    String name();
    long size();
    void print(String indent);
}

// Leaf
class FileNode implements FsNode {
    private final String name;
    private final long bytes;
    FileNode(String name, long bytes) { this.name = name; this.bytes = bytes; }

    public String name() { return name; }
    public long size()   { return bytes; }
    public void print(String indent) {
        System.out.println(indent + "📄 " + name + " (" + bytes + "b)");
    }
}

// Composite
class FolderNode implements FsNode {
    private final String name;
    private final List<FsNode> children = new ArrayList<>();
    FolderNode(String name) { this.name = name; }

    FolderNode add(FsNode n) { children.add(n); return this; }

    public String name() { return name; }
    public long size() {
        long total = 0;
        for (FsNode c : children) total += c.size();       // recursion
        return total;
    }
    public void print(String indent) {
        System.out.println(indent + "📁 " + name + "/");
        for (FsNode c : children) c.print(indent + "  ");  // recursion
    }
}
```

**Usage**
```java
FolderNode root = new FolderNode("root")
        .add(new FileNode("a.txt", 100))
        .add(new FolderNode("docs")
                .add(new FileNode("b.md", 250))
                .add(new FileNode("c.pdf", 1000)));

System.out.println("Total: " + root.size() + " bytes");   // 1350
root.print("");
```

### Design points
- **Aggregate method recurses** — `size()` sums over children at every level.
- **Print with indentation** — the depth parameter renders the tree structure.
- **Safe composite** — only `FolderNode` exposes `add`.

**Complexity:** O(n) per aggregate · Space O(depth)

---
#composite #lld #practice