# 2225.find.players.with.zero.or.one.losses

Here's the full description of the [problem](https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/?envType=daily-question&envId=2024-01-15)

# Approach 

The code uses a dictionary `counter` to keep track of the number of losses for each player. It then iterates through the list of matches and updates the `counter` accordingly. Finally, it populates the two lists in the result based on the number of losses.

# Complexity 

- Time complexity : O(N), where `N` is the number of matches
- Space complexity : O(M), where `M` is the number of unique players

# Code

```Python
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        counter = {}
        answer = []
        answer.append([])
        answer.append([])
        for i in range(0,len(matches)) :
            if matches[i][1] not in counter :
                counter[matches[i][1]] = 0
            if matches[i][0] not in counter :
                counter[matches[i][0]] = 0
            counter[matches[i][1]] += 1
        for elem in counter:
            if counter[elem] == 0: 
                answer[0].append(elem)
            elif counter[elem] == 1: 
                answer[1].append(elem)
        answer[0].sort()
        answer[1].sort()
        return(answer)
```