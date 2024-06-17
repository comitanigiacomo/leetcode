import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(math.sqrt(c)) + 1):
            b_squared = c - a * a
            b = int(math.sqrt(b_squared))
            if b * b == b_squared:
                return True
        return False

        
c = 4
sol1= Solution()
print(sol1.judgeSquareSum(c))