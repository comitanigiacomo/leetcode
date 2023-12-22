from collections import Counter
  
class Solution:
    def maxScore(self, s: str) -> int:
        max = 0
        zeros = 0
        unos = Counter(s)['1']
        for i in range(len(s)-1):
            if s[i] == '0': 
                zeros += 1
            else: unos -= 1
            if zeros + unos > max :
                max = zeros + unos
        return max

s = "011101"
sol1 = Solution()
result = sol1.maxScore(s)
print(result)
