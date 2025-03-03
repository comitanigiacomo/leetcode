from typing import List 
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        intersection = Counter(words[0])
        for i in range(1, len(words)):
            intersection = Counter(words[i]) & intersection
            
        output = []
        for elem in intersection.keys():
            for i in range(intersection[elem]):
                output.append(elem)
            
        return output
        
            
        
        
words = ["bella","label","roller"]
sol1 = Solution()
print(sol1.commonChars(words))
        
        