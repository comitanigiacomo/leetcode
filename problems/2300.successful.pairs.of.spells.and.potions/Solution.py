from typing import List

class Solution:
    def binaria(self, lista, spell, success):
        inf = 0
        sup = len(lista) - 1
        ris = -1
        
        while inf <= sup:
            
            centro = (inf + sup)// 2
            
            if lista[centro] * spell >= success:
                ris = centro
                sup = centro - 1
                
            else:
                inf = centro + 1
                
        return ris

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        out = []
        potions.sort()

        for spell in spells:
            idx = Solution.binaria(self, potions, spell, success)
            if idx == -1:
                out.append(0)
            else:
                out.append(len(potions) - idx )

        return out
        
        
spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7

sol = Solution()
print(sol.successfulPairs(spells, potions, success))