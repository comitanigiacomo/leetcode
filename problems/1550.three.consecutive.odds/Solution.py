# First approach:
from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for num in arr: 
            if num % 2 != 0: count+= 1
            else: count = 0
            if count == 3 : return True
        return False
    
# Second approach
#class Solution:
    #def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        #for i in range(1, len(arr)-1):
            #if arr[i-1] % 2 + arr[i] % 2 + arr[i+1] % 2 == 3: return True
        #return False

arr = [2,6,4,1]
sol = Solution()
print(sol.threeConsecutiveOdds(arr))