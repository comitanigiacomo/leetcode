from typing import List
from functools import cmp_to_key

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        def comp(a, b):
            if a in arr2 and b in arr2:
                return arr2.index(a) - arr2.index(b)
            if a in arr2:
                return -1
            if b in arr2:
                return 1
            return a - b
        
        return sorted(arr1, key=cmp_to_key(comp)) 
        
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
sol = Solution()
print(sol.relativeSortArray(arr1, arr2))
    