# 948.bag.of.tokens

Here's the full description of the [problem](https://leetcode.com/problems/bag-of-tokens/description/?envType=daily-question&envId=2024-03-04)

# Approach

# Approach

The problem can be solved using a greedy approach. The program starts by sorting the tokens in ascending order. Then, it iterates through the tokens with two pointers, one pointing to the start of the sorted list and the other pointing to the end. The program maintains two variables: `score` to keep track of the maximum score obtained so far, and `power` to represent the current power available.

At each step, the program checks if the current power is less than the value of the token pointed to by the left pointer. If it is, and if the `score` is greater than 0, the program trades tokens for power by incrementing the left pointer and decrementing the right pointer. Otherwise, if the current power is sufficient, the program consumes tokens to increase the score by incrementing the left pointer.

After iterating through all the tokens, the program returns the maximum `score` obtained.

# Complexity

- Time complexity: O(nlogn), where n is the number of tokens

- Space complexity: O(1)

# Code

```Python
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        count = len(tokens)-1
        i = 0
        
        tokens.sort()
        
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
```