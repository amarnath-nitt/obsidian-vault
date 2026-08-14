# Encode and Decode Strings

**Difficulty:** Medium (Premium)  
**Category:** Arrays & Hashing  
**LeetCode Link:** [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/)

---

## Problem Statement

Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Implement `encode` and `decode` methods.

**Example 1:**
```
Input: ["Hello","World"]
Output: ["Hello","World"]
Explanation:
encode: "Hello" and "World" → "5#Hello5#World"
decode: "5#Hello5#World" → ["Hello", "World"]
```

**Example 2:**
```
Input: [""]
Output: [""]
```

**Constraints:**
- `0 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` contains any possible characters out of 256 valid ASCII characters.

---

## Intuition

We need a way to encode multiple strings into one string such that we can uniquely decode them back. The challenge is handling special characters and empty strings.

---

## Approach 1: Delimiter (Naive Solution - INCORRECT)

### Algorithm
1. Join strings with a delimiter like `","`
2. Split by delimiter to decode

### Java Code
```java
public class Codec {
    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        return String.join(",", strs);
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        if (s.isEmpty()) return new ArrayList<>();
        return Arrays.asList(s.split(","));
    }
}
```

### Why This FAILS
- ❌ What if a string contains the delimiter ","?
- ❌ Example: `["Hello,World"]` → `"Hello,World"` → `["Hello", "World"]` (WRONG!)
- ❌ Can't distinguish between delimiter and actual comma in string

### Drawbacks
- Doesn't handle all possible characters
- Ambiguous encoding

---

## Approach 2: Escape Characters (Better but Complex)

### Algorithm
1. Escape delimiters in the original strings
2. Use escaped delimiter to join
3. Unescape during decode

### Issues
- Complex escape logic
- Multiple passes needed
- Still error-prone

---

## Approach 3: Length Prefix (Optimized Solution)

### Algorithm
1. **Encode:** For each string, store `length + delimiter + string`
2. **Decode:** Read length, skip delimiter, read that many characters
3. Use a delimiter that won't be confused (e.g., `#`)

### Java Code
```java
public class Codec {
    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();
        
        for (String str : strs) {
            // Format: "length#string"
            encoded.append(str.length());
            encoded.append('#');
            encoded.append(str);
        }
        
        return encoded.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> decoded = new ArrayList<>();
        int i = 0;
        
        while (i < s.length()) {
            // Find the delimiter '#'
            int delimiterPos = s.indexOf('#', i);
            
            // Extract length
            int length = Integer.parseInt(s.substring(i, delimiterPos));
            
            // Extract string of that length
            int start = delimiterPos + 1;
            int end = start + length;
            decoded.add(s.substring(start, end));
            
            // Move to next encoded string
            i = end;
        }
        
        return decoded;
    }
}
```

### Example Walkthrough

**Encoding `["Hello", "World", ""]`:**
```
"Hello" → length=5 → "5#Hello"
"World" → length=5 → "5#World"
""      → length=0 → "0#"

Result: "5#Hello5#World0#"
```

**Decoding `"5#Hello5#World0#"`:**
```
i=0: Find '#' at 1, length=5, extract "Hello" (2 to 7), i=7
i=7: Find '#' at 8, length=5, extract "World" (9 to 14), i=14
i=14: Find '#' at 15, length=0, extract "" (16 to 16), i=16

Result: ["Hello", "World", ""]
```

### Complexity Analysis
- **Time Complexity:** 
  - Encode: O(n) where n = total characters in all strings
  - Decode: O(n) single pass through encoded string
- **Space Complexity:** O(n) for the encoded string

### Why This is Better
- ✅ Handles ALL possible characters (including delimiters)
- ✅ Unambiguous encoding/decoding
- ✅ Works with empty strings
- ✅ Simple and efficient
- ✅ No escaping needed

---

## Alternative: Non-ASCII Delimiter

### Algorithm
Use a non-ASCII character as delimiter (if allowed)

### Java Code
```java
public class Codec {
    private static final String DELIMITER = "\u0001"; // Non-printable ASCII
    
    public String encode(List<String> strs) {
        return String.join(DELIMITER, strs);
    }

    public List<String> decode(String s) {
        return Arrays.asList(s.split(DELIMITER, -1));
    }
}
```

### Note
- Only works if strings are guaranteed not to contain this character
- Less robust than length-prefix approach

---

## Key Takeaways

1. **Pattern:** Length-prefix encoding for variable-length data
2. **Robustness:** Always consider edge cases with delimiters
3. **Unambiguous encoding:** Length prefix eliminates ambiguity
4. **Format:** `length + delimiter + data` is a common serialization pattern
5. **Edge cases:** Empty strings, strings containing delimiters

---

## Edge Cases

- Empty list: `[]` → `""` → `[]`
- Empty strings: `["", ""]` → `"0#0#"` → `["", ""]`
- Delimiter in string: `["a#b"]` → `"3#a#b"` → `["a#b"]` ✓
- Special characters: `["a,b;c"]` → `"5#a,b;c"` → `["a,b;c"]` ✓

---

## Related Problems
- [[Serialize-and-Deserialize-Binary-Tree]] - Similar encoding concept
- [[Design-Compressed-String-Iterator]] - String encoding
- [[String-Compression]] - Data compression

---

## Tags
#strings #design #encoding #serialization #medium #blind75
