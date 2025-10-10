from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0] * len(energy)
        
        for i in range(n-1, -1, -1):
            if i + k < len(energy):
                dp[i] = dp[i+k] + energy[i]
            else:
                dp[i] = energy[i]
                
        return max(dp)
    
energy = [-2,-3,-1]
k = 3
sol = Solution()
print(sol.maximumEnergy(energy, k))
