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
            
        
words = ["cat","bt","hat","tree"]
chars = "atach"
sol1 = Solution()
result = sol1.countCharacters(words, chars)
print(result)
        