class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        n = len(str1)
        m = len(str2)

        i,j = 0, 0
        
        while i < n and j < m :
            if str1[i] == str2[j] or chr((ord(str1[i]) - ord('a') + 1) % 26 + ord('a')) == str2[j]:
                j += 1
            i += 1
        
        return j == m
    
str1 = "abc"
str2 = "ad"
sol = Solution()
print(sol.canMakeSubsequence(str1, str2))
