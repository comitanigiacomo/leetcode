import numpy as np
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        arr = np.array(nums)
        unique_elements = np.unique(arr)
        min_dist = float('inf')
        
        for elem in unique_elements:
            indices = np.where(arr == elem)[0]
            
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    idx1, idx2, idx3 = indices[i], indices[i+1], indices[i+2]
                    current_dist = abs(idx1-idx2) + abs(idx2-idx3) + abs(idx3-idx1)
                    if current_dist < min_dist:
                        min_dist = current_dist
                        
        return int(min_dist) if min_dist != float('inf') else -1

nums = [1, 2, 1, 1, 3]
sol = Solution()
print(sol.minimumDistance(nums))