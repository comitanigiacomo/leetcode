from typing import List

class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        count = 0
        banned = set(bannedWords)
        for m in message:
            if m in banned :
                print(m)
                count += 1
        if count >= 2:
            return True
        return False

message = ["l","i","l","i","l"]
bannedWords = ["d","a","i","v","a"]
sol = Solution()
print(sol.reportSpam(message, bannedWords))