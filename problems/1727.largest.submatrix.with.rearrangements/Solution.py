from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        count = [0] * cols
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    count[j] = count[j] + 1 if i > 0 else 1
                else:
                    count[j] = 0

            sorted_count = sorted(count)
            for k in range(cols):
                max_area = max(max_area, sorted_count[k] * (cols - k))

        return max_area
            
                    
                        
        
        