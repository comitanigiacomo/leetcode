from typing import List
import numpy as np

from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Verifica se la lunghezza dell'array è compatibile con le dimensioni m x n
        if len(original) != m * n:
            return []  # Se non è compatibile, ritorna una lista vuota

        # Trasformazione dell'array unidimensionale in un array bidimensionale
        array_bidimensionale = [original[i*n:(i+1)*n] for i in range(m)]
        return array_bidimensionale

        
original = [1,2,3,4]
m = 2
n = 2
sol = Solution()
print(sol.construct2DArray(original,m,n))