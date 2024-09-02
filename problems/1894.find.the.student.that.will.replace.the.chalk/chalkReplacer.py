from typing import List 

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        tmp =  k % sum(chalk) # evito di ciclare più volte sull'array 

        for i in range(0, len(chalk)):
            if chalk[i] <= tmp: 
                tmp -= chalk[i]
            else: return i
       
chalk = [5,1,5]
k = 22 
sol = Solution()
print(sol.chalkReplacer(chalk, k))