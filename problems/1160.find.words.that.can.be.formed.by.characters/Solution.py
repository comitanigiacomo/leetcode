from typing import List

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
        
words = ["cat","bt","hat","tree"]
chars = "atach"
sol1 = Solution()
result = sol1.countCharacters(words, chars)
print(result)
        