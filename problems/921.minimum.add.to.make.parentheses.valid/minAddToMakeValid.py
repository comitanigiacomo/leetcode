class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        stack = 0
        
        for char in s:
            if char == '(':
                stack += 1
            else:
                if stack == 0:
                    count += 1
                else:
                    stack -= 1
            
        return count + stack
      
s = "())"  
sol = Solution()
print(sol.minAddToMakeValid(s))