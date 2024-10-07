class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        
        for c in s:
            if stack:
                last = stack[-1]
                
                if (last == "A" and c == "B") or (last == "C" and c == "D"):
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        return len(stack)
        
s = "CCCCDDDD"
sol = Solution()
print(sol.minLength(s))