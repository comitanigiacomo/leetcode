import random
from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # Calcolo la somma totale richiesta
        m = len(rolls)
        total_sum = mean * (n + m)  # Somma totale per avere la media richiesta
        current_sum = sum(rolls)  # Somma corrente dei tiri noti
        missing_sum = total_sum - current_sum  # Somma mancante da distribuire

        # Se la somma mancante non può essere distribuita tra i tiri mancanti
        if missing_sum < n or missing_sum > 6 * n:
            return []

        # Distribuisci la somma mancante sugli n tiri
        quotient, remainder = divmod(missing_sum, n)
        result = [quotient] * n  # Pre-assegna la parte intera della divisione

        # Distribuisci il resto (se presente)
        for i in range(remainder):
            result[i] += 1

        return result
        
        
rolls = [3,2,4,3]
mean = 4
n = 2
sol = Solution()
print(sol.missingRolls(rolls,mean,n))