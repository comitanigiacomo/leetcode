# 1688.Count.of.matches.in.tournament

Here's the full description of the [problem](https://leetcode.com/problems/count-of-matches-in-tournament/description/?envType=daily-question&envId=2023-12-05)

# Approach

The recursive function `numberOfMatches` takes an integer `n` as input and calculates the total number of matches played in the tournament.

- If `n` is equal to `1`, meaning there is only one team left, return `0` as no matches are played.
- If `n` is even, calculate the number of matches played in the current round as `n/2`, and recursively call numberOfMatches with `n/2`. Add the matches played in the current round to the result.
- If `n` is odd, calculate the number of matches played in the current round as `(n - 1) / 2`, and recursively call numberOfMatches with `(n - 1) / 2 + 1`. Add the matches played in the current round to the result.

# Complexity

- Time complexity: O(log n)
- Space complexity: O(log n)

# Code

```python 
class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n == 1 : return  0
        if n % 2 == 0:
            return self.numberOfMatches(n/2) + n/2
        return  self.numberOfMatches((n - 1) / 2 + 1)  + (n - 1) / 2
```

For other solutions to LeetCode problems, you can visit my GitHub account by clicking [here](https://github.com/comitanigiacomo/leetcode)