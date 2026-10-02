# Top View of Binary Tree

**Problem:** For each HD, show the top-most (first seen) node.

### Approach

Same as Bottom View but only insert if HD not already in map.

```java
if (!map.containsKey(hd)) map.put(hd, node.val); // first seen = top view
```

---
