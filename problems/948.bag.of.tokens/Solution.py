from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        count = len(tokens)-1
        i = 0
        
        # I am interested in maximizing the output: surely sorting the tokens helps.
        tokens.sort()
        
        print(tokens)
        
        # I notice that in the topics he wants a greedy approach that uses two pointers: I imagine he wants one at the end and one at the beginning.
        # According to the logic of the game, I have to use face-up on the lowest tokens and face down on the highest ones.
        
        # Instead of using two pointers, I can directly exploit the length of the list.

        
       # It makes sense to isolate the case where initially power is not large enough, or the list of tokens is empty.
        if len(tokens) > 0 and power < tokens[0]: return 0
        
        while i <= count: 
            if power < tokens[i] and score > 0:
                power += tokens[count]
                count -= 1
                score -= 1
            
            power -= tokens[i]
            score += 1
            i += 1
        
        return score                 
            
input = [71,55,82]
power = 54
sol1 = Solution()
print(sol1.bagOfTokensScore(input, power))        
        
