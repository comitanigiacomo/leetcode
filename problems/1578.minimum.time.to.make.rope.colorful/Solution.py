from typing import Counter, List

class Solution: 

    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        costo_totale = 0

        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                costo_totale += min(neededTime[i], neededTime[i-1])
                neededTime[i] = max(neededTime[i], neededTime[i-1])


        return costo_totale

colors = "aabaa"
neededTime = [1,2,3,4,1]
sol = Solution()
print(sol.minCost(colors, neededTime))
