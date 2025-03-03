from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))
        
        rank_dict = {val: rank + 1 for rank, val in enumerate(sorted_unique)}
        
        return [rank_dict[val] for val in arr]
    
arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
sol = Solution()
print(sol.arrayRankTransform(arr))

