# Bit Manipulation - Practice Notes

## Pattern Overview
Using bitwise operations to solve problems efficiently with better space and time complexity.

## Key Concepts
- **AND (&)**: Both bits must be 1
- **OR (|)**: At least one bit is 1
- **XOR (^)**: Bits are different
- **NOT (~)**: Flip all bits
- **Left Shift (<<)**: Multiply by 2^n
- **Right Shift (>>)**: Divide by 2^n

## Template Code

### Common Operations
```java
// Check if i-th bit is set
boolean isSet = (num & (1 << i)) != 0;

// Set i-th bit
num = num | (1 << i);

// Clear i-th bit
num = num & ~(1 << i);

// Toggle i-th bit
num = num ^ (1 << i);

// Check if power of 2
boolean isPowerOf2 = (num & (num - 1)) == 0;

// Count set bits
int count = Integer.bitCount(num);
```

### XOR Properties
```java
// a ^ a = 0
// a ^ 0 = a
// XOR is commutative and associative

// Find single number (all others appear twice)
int single = 0;
for (int num : nums) {
    single ^= num;
}
```

## Practice Problems

### Easy
- [ ] [Single Number](https://leetcode.com/problems/single-number/) (LC 136) → [Solution](solutions/LC-136-Single-Number.md)
- [ ] [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) (LC 191) → [Solution](solutions/LC-191-Number-of-1-Bits.md)
- [ ] [Reverse Bits](https://leetcode.com/problems/reverse-bits/) (LC 190) → [Solution](solutions/LC-190-Reverse-Bits.md)
- [ ] [Power of Two](https://leetcode.com/problems/power-of-two/) (LC 231) → [Solution](solutions/LC-231-Power-of-Two.md)
- [ ] [Power of Four](https://leetcode.com/problems/power-of-four/) (LC 342) → [Solution](solutions/LC-342-Power-of-Four.md)
- [ ] [Missing Number](https://leetcode.com/problems/missing-number/) (LC 268) → [Solution](solutions/LC-268-Missing-Number.md)

### Medium
- [ ] [Single Number II](https://leetcode.com/problems/single-number-ii/) (LC 137) → [Solution](solutions/LC-137-Single-Number-II.md)
- [ ] [Single Number III](https://leetcode.com/problems/single-number-iii/) (LC 260) → [Solution](solutions/LC-260-Single-Number-III.md)
- [ ] [Counting Bits](https://leetcode.com/problems/counting-bits/) (LC 338) → [Solution](solutions/LC-338-Counting-Bits.md)
- [ ] [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) (LC 371) → [Solution](solutions/LC-371-Sum-of-Two-Integers.md)
- [ ] [Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/) (LC 201) → [Solution](solutions/LC-201-Bitwise-AND-Range.md)

### Hard
- [ ] [Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) (LC 421) → [Solution](solutions/LC-421-Maximum-XOR-Two-Numbers.md)

## Reference
[LeetCode Pattern Guide](https://lnkd.in/gXHFx-iA)
