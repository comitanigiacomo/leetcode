# Coding Rules

## Hash Table & Counting
* **Use Counter**: Prefer `collections.Counter` over manual loops for frequency counting to leverage its optimized C implementation.
* **Short-circuit with all()**: Use `all()` with generator expressions to stop evaluation at the first falsy element.

## Bit Manipulation & Sorting
* **Multi-key Sorting**: Use tuple keys `(primary_key, secondary_key)` in Python's `sort(key=...)` for clean tie-breaking.
* **Schwartzian Transform**: Python's `sort(key=...)` evaluates the key function only once per element (O(N) evaluations total).
* **Bit Counting**: Use `int.bit_count()` instead of manual bit-shifting loops for set bit counting.
