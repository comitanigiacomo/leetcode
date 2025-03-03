from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        if not height:
            return water
        
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        
        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])
        
        right_max[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        for i in range(len(height)):
            water += min(left_max[i], right_max[i]) - height[i]
        
        return water

height = [0,1,0,2,1,0,1,3,2,1,2,1]
sol = Solution()
print(sol.trap(height))
