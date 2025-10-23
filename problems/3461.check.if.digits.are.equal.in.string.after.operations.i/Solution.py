class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            tmp = []
            for i in range(1, len(s)):
                tmp.append(str((int(s[i]) + int(s[i-1])) % 10))
            s = ''.join(tmp)
        return s[0] == s[1]
    
s = "3902"
sol = Solution()
print(sol.hasSameDigits(s))
