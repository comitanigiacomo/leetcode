from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        out = 0
        letters = Counter(s)
        Flag = False
        for elem in letters.values(): 
            if elem % 2 != 0: 
                if Flag == False: 
                    out += elem
                    Flag = True
                else: out += elem -1
            if elem % 2 == 0: out += elem
        
        return out 
                
s = "bananas"
sol1 = Solution()
print(sol1.longestPalindrome(s))