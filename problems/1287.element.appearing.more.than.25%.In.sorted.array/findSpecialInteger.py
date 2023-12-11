from collections import Counter
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        occurrences = Counter(arr)
        length = len(arr) // 4
        for elem, count in occurrences.items():
            if count > length:
                return elem

        
            
arr = [1,2,2,6,6,6,6,7,10]
sol1 = Solution()
result = sol1.findSpecialInteger(arr)
print(result)