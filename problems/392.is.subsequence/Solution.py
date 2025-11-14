class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        righe = len(s) + 1
        colonne = len(t) + 1

        dp = [[0 for _ in range(colonne)] for _ in range(righe)]

        for i in range(1, righe):
            for j in range(1, colonne):
                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1] == len(s)

s = "abc"
t = "ahbgdc"
sol = Solution()
print(sol.isSubsequence(s, t))
