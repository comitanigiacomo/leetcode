# 1160.find.words.that.can.be.formed.by.characters

Here's the full description of the [problem](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/)

# Approach

To solve this problem, I can count the frequency of each character in the chars string and then check if each word in the words array can be formed using the characters in chars.

ff
# Complexity

- Time complexity: O(N * M), where `N` is the length of the words array and `M` is the maximum length of a word in words 
- Space complexity: O(C), where `C` is the number of unique characters in the chars 

## Code

```python
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        char_count = {}
        
        for char in chars:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        for word in words:
            word_count = {}
            valid = True
            
            for char in word:
                if char in word_count:
                    word_count[char] += 1
                else:
                    word_count[char] = 1
                
                if char not in char_count or word_count[char] > char_count[char]:
                    valid = False
                    break
            
            if valid:
                count += len(word)
        
        return count
```