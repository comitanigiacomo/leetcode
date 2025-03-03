from typing import List 

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] += min(matrix[i-1][max(0, j-1):min(len(matrix[0]), j+2)])
        return min(matrix[-1])
        
        
matrix = [[2,1,3],[6,5,4],[7,8,9]]
sol1 = Solution()
print(sol1.minFallingPathSum(matrix))