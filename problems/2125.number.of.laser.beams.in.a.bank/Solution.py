from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        beam = 0
        tmp = 0
        out = 0
        
        for row in  bank:
            for cell in row:
                if cell == '1':
                    tmp += 1
                    
            if tmp > 0:
                out += beam * tmp
                beam = tmp
                tmp = 0
            
        return out
        
        
bank = ["011001","000000","010100","001000"]
sol = Solution()
print(sol.numberOfBeams(bank))