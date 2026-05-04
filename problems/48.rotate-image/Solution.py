import numpy as np
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # I can think of the rotation like the combination of two simple transformation:

        n = len(matrix)

        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # At this point i only have to invert the order of the rows:

        for i in range(n):
            r = matrix[i][::-1]
            matrix[i] = r
            
matrix = [[1,2,3],[4,5,6],[7,8,9]]

sol = Solution()
print(sol.rotate(matrix))
        