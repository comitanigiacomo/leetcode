class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

s = "anagram" 
t = "nagaram"
sol1 = Solution()
result = sol1.isAnagram(s,t)
print(result)
