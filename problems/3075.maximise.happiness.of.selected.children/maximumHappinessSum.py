# Inizialmente penso al ordinare l'array in ordine crescente 
# Poi prendo sempre l'ultimo elemento, lo tolgo , e devo decrementare tutti di uno 

from typing import List 

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        sum = 0
        tmp = 0
        happiness.sort()
        for i in range(k):
            if happiness[len(happiness)-1] - tmp > 0 : 
                sum = sum + happiness[len(happiness)-1] - tmp
            happiness.pop()
            tmp = tmp + 1
        return sum 
happiness = [12,1,42]
k = 3
sol1 = Solution()
print(sol1.maximumHappinessSum(happiness, k))
        