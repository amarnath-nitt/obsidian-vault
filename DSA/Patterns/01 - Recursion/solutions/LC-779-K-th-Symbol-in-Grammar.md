# K-th Symbol in Grammar (LC 779)

**Difficulty**: Medium  
**Pattern**: Recursion / Divide and Conquer  
**LeetCode**: https://leetcode.com/problems/k-th-symbol-in-grammar/

## Problem Statement
The grammar starts with `0`. Each `0` becomes `01`, and each `1` becomes `10`. Return the `k`th symbol in row `n`.

## Recursive Idea
The first half of row `n` is the same as row `n - 1`. The second half is the flipped version of row `n - 1`.

## Intuition: Divide & Conquer + Transformation

### The Pattern Generation Rule
Starting with row 1:
```
Row 1:            0
Row 2:            0 1           (0→01, 1→10)
Row 3:            0 1 1 0       (0→01, 1→10, 1→10, 0→01)
Row 4:            0 1 1 0 1 0 0 1
```

**Key observation**: Each row = [Previous row] + [Flipped(Previous row)]

Example for Row 3:
- First half: copy Row 2 = [0, 1]
- Second half: flip Row 2 = [NOT(0), NOT(1)] = [1, 0]
- Row 3: [0, 1] + [1, 0] = [0, 1, 1, 0] ✓

### The Key Insight for Finding K-th Symbol
We DON'T need to build the entire row. We just need:
1. Is k in the first half or second half?
2. If first half: answer = same symbol from row n-1 at position k
3. If second half: answer = flipped symbol from row n-1 at position k-half

### Divide & Conquer Algorithm

```
Half size = 2^(n-2)

kthGrammar(n, k):
    if n == 1:
        return 0
    
    half = 2^(n-2)
    
    if k <= half:
        # k is in first half (unchanged from row n-1)
        return kthGrammar(n-1, k)
    else:
        # k is in second half (flipped from row n-1)
        return 1 - kthGrammar(n-1, k - half)
```

### Worked Example: n=4, k=7

Let me trace through completely:
```
Build Row 4 logically (for reference):
Row 1: 0
Row 2: 0 1
Row 3: 0 1 1 0
Row 4: 0 1 1 0 | 1 0 0 1  ← k=7 is in position 7, value should be 0
                    ↑

Now solve with algorithm:

kthGrammar(4, 7):
  n=4, k=7
  Half = 2^(4-2) = 2^2 = 4
  k=7 > 4? Yes, so in second half
  → 1 - kthGrammar(3, 7-4)
  → 1 - kthGrammar(3, 3)

kthGrammar(3, 3):
  n=3, k=3
  Half = 2^(3-2) = 2^1 = 2
  k=3 > 2? Yes, so in second half
  → 1 - kthGrammar(2, 3-2)
  → 1 - kthGrammar(2, 1)

kthGrammar(2, 1):
  n=2, k=1
  Half = 2^(2-2) = 2^0 = 1
  k=1 <= 1? Yes, so in first half
  → kthGrammar(1, 1)

kthGrammar(1, 1):
  n=1, base case
  → return 0

Back-track:
  kthGrammar(2, 1) = 0
  kthGrammar(3, 3) = 1 - 0 = 1
  kthGrammar(4, 7) = 1 - 1 = 0 ✓
```

Row 4 at position 7 is indeed 0! Algorithm works perfectly.

### Why Divide & Conquer Works
Each recursion level answers: "Is this in the unchanged half or the flipped half?"
- Unchanged → keep exploring that subtree
- Flipped → flip the result at the end

This reduces O(2^n) generation to just O(n) recursive lookups.

### Bonus: Bit Count Trick
The value at position k is simply: `Integer.bitCount(k-1) % 2`
- Even number of 1-bits in (k-1) → 0
- Odd number of 1-bits in (k-1) → 1

This works because the XOR-like transformation creates this parity pattern. It's O(1) but less intuitive for interviews.

## Java Code
```java
class Solution {
    public int kthGrammar(int n, int k) {
        // Row 1 contains only 0  
		if (n == 1) {  
		    return 0;  
		}  
		  
		// Size of half of row n  
		int half = 1 << (n - 2);  
		  
		// k is in first half  
		if (k <= half) {  
		    return kthGrammar(n - 1, k);  
		}  
		  
		// k is in second half  
		// Convert k to corresponding position  
		// in previous row and flip the result  
		return 1 - kthGrammar(n - 1, k - half);
    }
}
```

## Alternative Optimal Solution: Bit Count Parity
The value is the parity of the number of set bits in `k - 1`. Even parity gives `0`, odd parity gives `1`.

```java
class Solution {
    public int kthGrammar(int n, int k) {
        return Integer.bitCount(k - 1) % 2;
    }
}
```

### Alternative Complexity
- **Time**: O(1) for Java `int`
- **Space**: O(1)

## Complexity
- **Time**: O(n)
- **Space**: O(n)

## Key Takeaways
- Avoid building the row; its length grows exponentially.
- Find which half contains `k`.
