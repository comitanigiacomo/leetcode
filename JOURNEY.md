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

### Find Mode in Binary Search Tree (LC 501)

* **BST & In-order Traversal Property:**
  In a Binary Search Tree (BST), the left child is less than or equal to the node, and the right child is greater than or equal to the node. This allows us to traverse the tree using in-order traversal to visit nodes sequentially, meaning that any duplicate values will appear adjacent to each other.


* **Morris In-order Traversal ($O(1)$ Space Optimization):**
  While a recursive traversal avoids helper data structures, it still uses $O(H)$ space (where $H$ is the tree height) due to the execution call stack. To achieve true $O(1)$ auxiliary space, we can use the **Morris Traversal** algorithm:
  * **How it works:**
    1. Start at `current = root`.
    2. If `current.left` is `None`: Process `current.val` and move right (`current = current.right`).
    3. If `current.left` is not `None`: Find the **in-order predecessor** (the rightmost node in the left subtree):
       * **If its right child is `None`:** Create a temporary link (thread) back to `current` (`predecessor.right = current`) to remember the return path, then go left (`current = current.left`).
       * **If its right child is `current`:** It means we have finished visiting the left subtree and returned. Break the thread (`predecessor.right = None`), process `current.val`, and go right (`current = current.right`).

  ```python
  class Solution:
      def findMode(self, root: Optional[TreeNode]) -> List[int]:
          current_element = None
          current_count = 0
          max_count = 0
          modes = []

          def handle_value(val):
              nonlocal current_element, current_count, max_count, modes
              if val != current_element:
                  current_element = val
                  current_count = 1
              else:
                  current_count += 1

              if current_count > max_count:
                  max_count = current_count
                  modes = [val]
              elif current_count == max_count:
                  modes.append(val)

          current = root
          while current:
              if not current.left:
                  handle_value(current.val)
                  current = current.right
              else:
                  predecessor = current.left
                  while predecessor.right and predecessor.right != current:
                      predecessor = predecessor.right

                  if not predecessor.right:
                      predecessor.right = current
                      current = current.left
                  else:
                      predecessor.right = None
                      handle_value(current.val)
                      current = current.right

          return modes
  ```

> [!NOTE]
> **BST Sorted Order Property:**
> An in-order traversal (Left $\rightarrow$ Node $\rightarrow$ Right) of a Binary Search Tree (BST) always yields elements in **ascending (sorted) order**. This allows adjacent comparisons to find modes or duplicates in a single pass without extra memory (no hash map needed).

> [!NOTE]
> **Enclosing Scope and `nonlocal`:**
> When using nested helper functions in Python (like `handle_value` inside `findMode`), use the `nonlocal` keyword to modify variables defined in the outer scope. This prevents Python from creating a new local variable during assignment.
