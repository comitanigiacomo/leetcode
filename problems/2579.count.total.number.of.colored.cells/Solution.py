class Solution:
    def coloredCells(self, n: int) -> int:
        return n * n + (n - 1) * (n - 1)
       
n = 1
print(Solution().coloredCells(n))