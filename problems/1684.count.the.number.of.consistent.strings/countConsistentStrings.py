from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = len(words)
        allowed_set = set(allowed)
        for word in words:
            for letter in word:
                if letter not in allowed_set:
                    count -= 1
                    break

        return count
        
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
sol = Solution()
print(sol.countConsistentStrings(allowed, words))