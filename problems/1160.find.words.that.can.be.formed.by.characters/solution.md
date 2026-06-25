# 1160. Find Words That Can Be Formed by Characters

Here's the full description of the [problem](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/)

# Approach

To solve this problem efficiently in Python:
1. **Character Frequency Mapping:** We compute the frequency of each character in the `chars` string using `collections.Counter`.
2. **Word Checking & Verification:** For each word in the list, we build its frequency map using `Counter(word)`.
3. **Optimized Validation:** We verify if the word can be formed by checking if the frequency of every character in the word is less than or equal to its frequency in `chars`. We leverage `all(...)` for short-circuit evaluation.

### Key Python Optimizations:
* **C-Underhood Performance:** `collections.Counter` is implemented in C within the CPython interpreter. Delegating the frequency counting to `Counter` is significantly faster than writing a manual `for` loop in Python, as it minimizes line-by-line interpreter overhead.
* **Short-Circuit Evaluation:** The `all()` built-in operator short-circuits. As soon as it encounters the first character where `word_count[char] <= char_count[char]` is `False`, it immediately stops evaluation and returns `False`, saving CPU cycles.

# Complexity

- **Time complexity**: $O(N \cdot M)$ where $N$ is the number of words and $M$ is the average length of a word (since we construct a `Counter` for each word and potentially check its characters).
- **Space complexity**: $O(C)$ where $C$ is the number of unique characters in `chars` to store their frequencies.

## Code

```python
from typing import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        total_length = 0
        
        for word in words:
            word_count = Counter(word)
            
            if all(word_count[char] <= char_count[char] for char in word):
                total_length += len(word)
                
        return total_length
```