# Sorting & Counting (Greedy)

## Core Concepts & Patterns

### 1. State Accumulation on Sorted Arrays

When a problem requires counting operations based on size differences or "flattening" elements to a minimum/maximum, sorting is usually the first step. After sorting, you can often solve the problem in a single pass by accumulating a state variable.

* **The Duplicate Trap:** A very common edge case in these problems is failing to apply the accumulated state to duplicate elements.
* **The Pattern:** Maintain a running `operations` counter. Increment it *only* when the current element differs from the previous one (e.g., `nums[i] > nums[i - 1]`). However, **add this counter to your total result at every single step**, including for duplicates.

---

## Applied Problems

### LC 1887 - Reduction Operations to Make the Array Elements Equal
* **Focus**: Sorting and continuous state accumulation.
* **Key takeaway**: Counting "steps" to reduce elements to the minimum is equivalent to incrementing an operations counter at each value change, and summing this counter at every index across the sorted array.
