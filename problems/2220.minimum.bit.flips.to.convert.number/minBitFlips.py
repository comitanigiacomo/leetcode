from numpy import diff


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        
        return bin(xor).count('1')
            
sol = Solution()
start = 10
goal = 7
print(sol.minBitFlips(start, goal))