from typing import List
from collections import Counter

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        if not power:
            return 0
        
        count = Counter(power)
        values = sorted(count.keys())
        
        dp = {}
        
        for val in values:
            gain = val * count[val]
            
            skip = dp.get(val - 1, 0)
            
            take = gain + max(dp.get(val - 3, 0), dp.get(val - 4, 0))
            
            dp[val] = max(skip, take)
        
        return max(dp.values())

