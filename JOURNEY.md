# LeetCode Journey

Welcome to my LeetCode journey. While you can find the complete list of solved problems and their respective solutions in the [README.md](./README.md), this document captures my core insights, problem-solving intuitions, and the standard algorithms I master and apply. It serves both as a showcase of my technical preparation for others to review, and as a personal reference to revise key concepts when needed.

> [!WARNING]
> This file is under continuous development. To see the most up-to-date list of solved problems and direct links to code files, please refer to the [README.md](./README.md).

The ultimate goal of this log is to help me structure my thoughts, consolidate my learning, and build a reliable reference system for revision and interview preparation.

---

## Key Insights & Algorithmic Notes

### Sort Integers by The Number of 1 Bits (LC 1356)

* **First thing to note:** The problem asks to sort the elements based on two criteria: a primary one, and a secondary one used in case of a tie. In Python, the most efficient way to achieve this is by using **tuples**. Since tuples are compared element-by-element, we can define the sorting key as a tuple:
  ```python
  arr.sort(key=lambda x: (count_bits(x), x))
  ```
  This way, each element is mapped to a tuple `(number of 1s, value)`. Python will handle both the primary sorting and the tie-breaker by looking at the second value of the tuple (the actual integer value, which the problem requires to be in ascending order).

* **Important: Difference between Go and Python:** In Python, a solution like this is already optimized:
  ```python
  class Solution:
      def sortByBits(self, arr: List[int]) -> List[int]:
          arr.sort(key=lambda x: (x.bit_count(), x))
          return arr
  ```
  Under the hood, Python uses the **Schwartzian Transform** pattern:
  * It iterates through the array once to calculate the key for each element ($O(N)$).
  * It creates temporary `(key, original element)` pairs.
  * It sorts based on the pairs.
  * It reconstructs the original array.

  In Go, however, you must provide a comparator function which is called for every comparison step, resulting in $O(N \log N)$ key evaluations.

> [!NOTE]
> **Multi-Key Sorting Standard:**
> To sort by multiple criteria, return a tuple `(primary_key, secondary_key)` in Python to leverage lexicographical comparison. In Go, use a comparator fallback: `if keyA == keyB { return valA < valB }`.

> [!TIP]
> **Efficient Bit Counting:**
> For bit manipulation, avoid shifting loops where possible. Instead, use `int.bit_count()`.




