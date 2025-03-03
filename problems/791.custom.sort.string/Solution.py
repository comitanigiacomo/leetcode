import math

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        inOrder = ''
        out = ''
        chars = list(s)
        
        for elem in order: 
            for ch in s:
                if ch == elem: 
                    inOrder += elem
                    chars.remove(elem)
            
        return inOrder + out.join(chars)
        
        
order = "kqep"
s = "pekeq" 
sol1 = Solution()
print(sol1.customSortString(order, s))
