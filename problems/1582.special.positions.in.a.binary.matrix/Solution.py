from collections import Counter
from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def get_column_sum(col_idx):
            return sum(row[col_idx] for row in mat)

        special = 0
        for row in mat:
            if sum(row) == 1:
                col_idx = row.index(1)
                special += get_column_sum(col_idx) == 1

        return special

sol1 = Solution()
result = sol1.numSpecial([[0,0,0,1],[1,0,0,0],[0,1,1,0],[0,0,0,0]])
print(result)
