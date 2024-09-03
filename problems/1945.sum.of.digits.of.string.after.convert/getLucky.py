class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_str = ''.join(str(ord(elem)% 96) for elem in s)
        
        for i in range(0,k):
            somma = sum(int(digit) for digit in num_str)
            num_str = str(somma)
            
        return somma
        
        
s = "iiii"
k = 1
sol = Solution()
print(sol.getLucky(s,k))    
        