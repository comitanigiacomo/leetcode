class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n == 1 : return  0
        if n % 2 == 0:
            return self.numberOfMatches(n/2) + n/2
        return  self.numberOfMatches((n - 1) / 2 + 1)  + (n - 1) / 2
        
        
n = 7
sol = Solution()
result = sol.numberOfMatches(n)
print(result)