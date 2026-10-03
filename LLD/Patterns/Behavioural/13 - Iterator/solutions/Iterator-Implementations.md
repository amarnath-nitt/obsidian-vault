# Iterator — Implementations & Examples

**Pattern:** Iterator (Behavioural) · **Skill:** sequential access without exposing internals

### Approach

- Define an **Iterator** interface (`hasNext`, `next`).
- Define an **Aggregate** interface with an `iterator()` factory method.
- Keep traversal state inside a **ConcreteIterator**; the aggregate just creates it.

### Java Solutions

**1. Playlist Iterator (custom)**
```java
import java.util.*;

interface Iterator<T> { boolean hasNext(); T next(); }
interface IterableCollection<T> { Iterator<T> iterator(); }

class Song { final String title; Song(String t) { title = t; } @Override public String toString() { return title; } }

class Playlist implements IterableCollection<Song> {
    private final List<Song> songs = new ArrayList<>();
    public Playlist add(Song s) { songs.add(s); return this; }

    public Iterator<Song> iterator() {
        return new Iterator<Song>() {                 // anonymous concrete iterator
            private int index = 0;
            public boolean hasNext() { return index < songs.size(); }
            public Song next() {
                if (!hasNext()) throw new NoSuchElementException();
                return songs.get(index++);
            }
        };
    }
}
// usage
Playlist p = new Playlist().add(new Song("A")).add(new Song("B"));
Iterator<Song> it = p.iterator();
while (it.hasNext()) System.out.println(it.next());
```

**2. Custom Collection with for-each (`Iterable`)**
```java
import java.util.*;

class NumberBag implements Iterable<Integer> {
    private final List<Integer> data = new ArrayList<>();
    public NumberBag add(int n) { data.add(n); return this; }
    @Override public java.util.Iterator<Integer> iterator() {
        return new java.util.Iterator<Integer>() {
            private int i = 0;
            public boolean hasNext() { return i < data.size(); }
            public Integer next() { return data.get(i++); }
        };
    }
}
// for-each now works automatically
for (int n : new NumberBag().add(1).add(2).add(3)) System.out.print(n + " ");
```

**3. Binary Tree In-order Iterator (lazy, stack-based)**
```java
import java.util.*;

class TreeNode { int val; TreeNode left, right; TreeNode(int v) { val = v; } }

class InOrderIterator implements Iterator<Integer> {
    private final Deque<TreeNode> stack = new ArrayDeque<>();
    InOrderIterator(TreeNode root) { pushLeft(root); }
    private void pushLeft(TreeNode node) { while (node != null) { stack.push(node); node = node.left; } }
    public boolean hasNext() { return !stack.isEmpty(); }
    public Integer next() {
        if (!hasNext()) throw new NoSuchElementException();
        TreeNode node = stack.pop();
        pushLeft(node.right);                         // descend right subtree lazily
        return node.val;
    }
}
```

**4. Round-robin (Cycling) Iterator**
```java
import java.util.*;

class RoundRobin<T> implements Iterator<T> {
    private final List<T> items;
    private int index = 0;
    RoundRobin(List<T> items) { this.items = items; }
    public boolean hasNext() { return !items.isEmpty(); }   // never ends (cycles)
    public T next() {
        T item = items.get(index);
        index = (index + 1) % items.size();
        return item;
    }
}
```

**5. Filtered Iterator**
```java
import java.util.*;
import java.util.function.Predicate;

class FilteredIterator<T> implements Iterator<T> {
    private final Iterator<T> source;
    private final Predicate<T> predicate;
    private T nextItem;
    FilteredIterator(Iterator<T> source, Predicate<T> predicate) {
        this.source = source; this.predicate = predicate;
    }
    public boolean hasNext() {
        while (nextItem == null && source.hasNext()) {
            T candidate = source.next();
            if (predicate.test(candidate)) nextItem = candidate;
        }
        return nextItem != null;
    }
    public T next() {
        if (!hasNext()) throw new NoSuchElementException();
        T item = nextItem; nextItem = null; return item;
    }
}
```

**Complexity:** `hasNext` / `next` O(1) amortised · Space O(1) (O(height) for a tree iterator's stack)

**Design note:** the aggregate never leaks its internal list; each call to `iterator()` yields a **fresh** independent traversal.