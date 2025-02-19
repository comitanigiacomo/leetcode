class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.result = []
        self.backtrack("",n)
        
        return self.result[k-1] if k <= len(self.result) else ""
        
        
    def backtrack(self, current:str, n: int):
        if len(current) == n:
            self.result.append(current)
            return
        
        for char in "abc":
            if not current or current[-1] != char:
                self.backtrack(current + char, n)
    
n = 3
k = 9
sol = Solution()
print(sol.getHappyString(n,k))