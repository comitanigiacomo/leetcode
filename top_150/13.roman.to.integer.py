class Solution:
    def romanToInt(self, s: str) -> int:
        conversions = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        out = 0
        for i in range(len(s)):
            current = conversions[s[i]]
            if i < len(s)-1 and current < conversions[s[i+1]]:
                out -= current
            else: 
                out += current
        return out
        
s = "LVIII"
sol = Solution()
print(sol.romanToInt(s))