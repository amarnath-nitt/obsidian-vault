# Convert Sorted Array to BST

**LeetCode 108** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

### Approach

- Middle element → root (ensures balance)
- Recursively do the same for left and right halves

### Java Solution

```java
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        return build(nums, 0, nums.length - 1);
    }

    private TreeNode build(int[] nums, int l, int r) {
        if (l > r) return null;
        int mid = l + (r - l) / 2;
        TreeNode node = new TreeNode(nums[mid]);
        node.left = build(nums, l, mid - 1);
        node.right = build(nums, mid + 1, r);
        return node;
    }
}
```

**Complexity:** Time O(n) · Space O(log n)

---
