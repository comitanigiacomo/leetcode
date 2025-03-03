from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        transposed = [[0] * rows for _ in range(cols)]
        
        for i in range(rows):
            for j in range(cols):
                transposed[j][i] = matrix[i][j]
        
        return transposed
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol1 = Solution()
result = sol1.transpose(matrix)
print(result)