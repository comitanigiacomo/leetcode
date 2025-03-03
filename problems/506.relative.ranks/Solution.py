from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        initial = score.copy()
        # Ordino i risultati in ordine decrescente
        score.sort(reverse = True)
        mapping = {}
        out = []
        # per ogni score salvo la posizione finale dell'atleta
        for elem in score: 
            if len(mapping) == 0: 
                mapping[elem] = 'Gold Medal'
            elif len(mapping) == 1 : 
                mapping[elem] ='Silver Medal'
            elif len(mapping) == 2: 
                mapping[elem] = 'Bronze Medal'
            else: 
                mapping[elem] = (str(len(mapping)+1))
        # Ritorno le posizioni finali degli atleti nello stesso ordine di score 
        for elem in initial : 
            out.append(mapping[elem])
        return out
        
score = [10,3,8,9,4]
sol1 = Solution()
print(sol1.findRelativeRanks(score))