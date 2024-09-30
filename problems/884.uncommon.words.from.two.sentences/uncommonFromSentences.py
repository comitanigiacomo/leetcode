from collections import Counter
from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans = []
        s = s1 + " " + s2
        c = Counter(s.split(" "))

        for word in c.keys(): 
            if c[word] == 1: 
                ans.append(word)

        return ans
    
s1 = "this apple is sweet"
s2 = "this apple is sour"
sol = Solution()
print(sol.uncommonFromSentences(s1,s2))