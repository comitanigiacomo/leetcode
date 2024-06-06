from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()
        count = Counter(hand)
        
        for card in hand:
            if count[card] > 0:
                for i in range(groupSize):
                    if count[card + i] > 0:
                        count[card + i] -= 1
                    else:
                        return False
        return True


hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3
sol1 = Solution()
print(sol1.isNStraightHand(hand, groupSize))  

 