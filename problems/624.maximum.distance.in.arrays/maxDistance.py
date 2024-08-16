from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest = arrays[0][0]
        biggest = arrays[0][-1]
        max_distance = 0 
        
        for i in range(1, len(arrays)):
            arr = arrays[i]
            max_distance = max(max_distance, abs(arr[-1]- smallest), abs(biggest - arr[0]))
            smallest = min(arr[0], smallest)
            biggest = max((arr[-1], biggest))
            
        return max_distance
    
arrays = [[1,2,3],[4,5],[1,2,3]]
sol = Solution()
print(sol.maxDistance(arrays))