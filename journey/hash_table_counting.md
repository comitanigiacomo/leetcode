# Hash Table & Counting

## Core Concepts & Patterns

### 1. Python's C-Underhood: `Counter` Optimization

When counting frequencies of elements (like characters in a string), utilizing built-in tools is always preferred over manual loops:
* **Interpreter Overhead:** A manual `for` loop in Python to count characters introduces line-by-line interpreter overhead, which is relatively slow.
* **C Implementation:** `collections.Counter` is implemented in C within the CPython interpreter. Delegating the entire counting process to `Counter` runs at compiled C speed, significantly improving performance.

---

### 2. Short-Circuit Evaluation with `all()`

Evaluating conditions across collection items can be optimized using short-circuiting:
* **Short-Circuit Logic:** The `all()` operator in Python implements short-circuit evaluation. It iterates through the generator expression and, as soon as it encounters the first element that evaluates to `False`, it immediately terminates and returns `False`.
* **Resource Savings:** In problems like checking if a word can be formed by a set of characters (`word_count[char] <= char_count[char]`), `all()` avoids checking the rest of the word once a mismatch is found. This saves CPU cycles compared to processes that count or validate the entire word unconditionally.

---

## Applied Problems

### [LC 1160 - Find Words That Can Be Formed by Characters](../problems/1160.find.words.that.can.be.formed.by.characters/)
* **Focus**: Character counting and string validation.
* **Key takeaway**: Utilizing `Counter` for fast frequency mapping and `all()` to short-circuit validation checks.
* **Code & Explanations**:
  * [Python Solution](../problems/1160.find.words.that.can.be.formed.by.characters/Solution.py)
  * [Explanation Notes](../problems/1160.find.words.that.can.be.formed.by.characters/solution.md)

---

> [!TIP]
> For more solved problems under this category, you can cross-reference the [README.md](../README.md) table with the `#Hash Table` and `#Counting` tags.
