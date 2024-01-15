from pstats import SortKey
from typing import List  

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
            
                 
matches = [[2,3],[1,3],[5,4],[6,4]]
sol1 = Solution()
result = sol1.findWinners(matches)
print(result)