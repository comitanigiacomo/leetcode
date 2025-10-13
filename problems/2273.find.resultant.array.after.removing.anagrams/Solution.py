from typing import List
from collections import defaultdict

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        out = [words[0]]
        
        for i in range(1, len(words)):
            key1 = "".join(sorted(words[i-1]))
            key2 = "".join(sorted(words[i]))

            if key1 != key2:
                out.append(words[i])
        return out
    
words = ["abba","baba","bbaa","cd","cd"]
sol = Solution()
print(sol.removeAnagrams(words))