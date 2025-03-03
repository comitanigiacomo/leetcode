from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Convert dictionary to a set for faster lookups
        word_set = set(dictionary)
        n = len(s)
        
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            
            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])
        
        return dp[n]

s = "sayhelloworld"
dictionary = ["hello", "world"]
sol = Solution()
print(sol.minExtraChar(s, dictionary))  # Output: 3
