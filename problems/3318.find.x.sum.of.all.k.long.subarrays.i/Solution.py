from typing import List
from collections import Counter
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        out = []
        for i in range(0, len(nums)- k + 1):
            c = Counter(nums[i:i+k])

            sorted_list = sorted(c.items(), key=lambda x: (-x[1], -x[0]))[:x]
            
            somma = 0

            for key, elem in sorted_list:
                somma += key * elem

            out.append(somma)


        return out

nums = [1,1,2,2,3,4,2,3] 
k = 6
x = 2
sol = Solution()
print(sol.findXSum(nums, k, x))

