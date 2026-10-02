# Floor and Ceil in BST

**Floor(key):** Largest value ≤ key
**Ceil(key):** Smallest value ≥ key

```java
int floor(TreeNode root, int key) {
    int floor = -1;
    while (root != null) {
        if (root.val == key) return key;
        if (root.val > key) root = root.left;  // too big, go left
        else { floor = root.val; root = root.right; } // might have closer answer
    }
    return floor;
}

int ceil(TreeNode root, int key) {
    int ceil = -1;
    while (root != null) {
        if (root.val == key) return key;
        if (root.val < key) root = root.right; // too small, go right
        else { ceil = root.val; root = root.left; } // might have closer answer
    }
    return ceil;
}
```

---
