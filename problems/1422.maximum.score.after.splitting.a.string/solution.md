# 1422.maximum.score.after.splitting.a.string

Here's the full description of the [problem](https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/?envType=daily-question&envId=2023-12-22)

# Approach

1. Count the total number of ones in the string using `Counter(s)['1']` and initialize the variable `ones`.
2. Iterate through the string, keeping track of the number of `zeros` and updating the count of ones accordingly.
3. Calculate the current score at each step as the sum of zeros and ones.
4. Update the maximum score if the current score is greater than the current maximum.
5. Return the final maximum score.

# Complexity

- Time complexity: : O(n), where `n`is the length of the input string `s`.
- Space complexity: O(1)

# Code:

```Python
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
```
