# Bit Manipulation & Custom Sorting

## Core Concepts & Patterns

### 1. Multi-Key Sorting Standard

When a problem requires sorting elements based on a primary criterion and breaking ties with a secondary criterion:

* **Python (Lexicographical Tuples):** The most pythonic and efficient way is to return a tuple `(primary_key, secondary_key)` inside the key function:
  ```python
  arr.sort(key=lambda x: (primary_key(x), x))
  ```
  Since Python compares tuples element-by-element, this naturally handles the primary sorting and fallback tie-breaker in a single step.

---

### 2. Python Sort Performance (Schwartzian Transform)
Understanding runtime behavior is critical for writing high-performance code:
* **Schwartzian Transform:** Python's `arr.sort(key=...)` implements a pattern called the **Schwartzian Transform**. It evaluates the key function exactly once per element ($O(N)$), pairs the keys with the elements, sorts the pairs, and then extracts the elements.
* **On-the-fly Evaluations:** In contrast, languages that use standard comparison-based sort functions without key caching evaluate the comparator on-the-fly, leading to $O(N \log N)$ evaluations of the sorting key.

---

### 3. Efficient Bit Counting
* **Built-in methods:** Avoid manual bit-shifting loops when a built-in function is available. In Python, prefer using `int.bit_count()`.
* **Low-level fallback:**
  If manual bit counting is required, use a bitwise mask and shift:
  ```python
  def count_bits(n: int) -> int:
      count = 0
      while n > 0:
          count += n & 1
          n >>= 1
      return count
  ```

---

## Applied Problems

### [LC 1356 - Sort Integers by The Number of 1 Bits](../problems/1356.sort.integers.by.the.number.of.1.bits/)
* **Focus**: Multi-criteria sorting and set bit counting.
* **Key takeaway**: Leveraging Python's tuple sorting to handle primary and secondary criteria in a single pass.
* **Code & Explanations**:
  * [Go Solution](../problems/1356.sort.integers.by.the.number.of.1.bits/Solution.go)
  * [Explanation Notes](../problems/1356.sort.integers.by.the.number.of.1.bits/solution.md)

---

> [!TIP]
> For more solved problems under this category, you can cross-reference the [README.md](../README.md) table with the `#Bit Manipulation` and `#Sorting` tags.

