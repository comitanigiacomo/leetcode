class Solution:
    def romanToInt(self, s: str) -> int:
        conversions = {"I":1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        out = 0
        
        for i in range(len(s)-1, -1, -1):
            if i < len(s)-1 and conversions[s[i]] < conversions[s[i+1]]:
                out -= conversions[s[i]]
            else: 
                out += conversions[s[i]]
            
        return out
        
input = "MCMXCIV"
sol1=Solution()
print(sol1.romanToInt(input))