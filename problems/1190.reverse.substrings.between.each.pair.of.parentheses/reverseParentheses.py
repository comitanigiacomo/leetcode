from collections import deque

class Solution:
    def reverseParentheses(self, s: str) -> str:
        sub = list(s)
        print(sub)
        i = len(sub) - 1
        while "(" in sub:
            print(sub)
            if sub[i] == "(":
                for j in range(i, len(sub)):
                    if sub[j] == ")":
                        sub[i + 1 : j] = sub[i + 1 : j][::-1]
                        sub.pop(j)
                        sub.pop(i)
                        break
            i -= 1
        return "".join(sub)
        
        
s = "(u(love)i)"
sol = Solution()
print(sol.reverseParentheses(s))