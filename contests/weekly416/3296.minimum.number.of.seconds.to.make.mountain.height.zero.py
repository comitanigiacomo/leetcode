from typing import List

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        times = [workerTimes[0]]
        for i in range(1,len(workerTimes)):
            times.append(times[i-1] + (workerTimes[i]*i+1))
        print(times)
        print(max(times))
        
        
mountainHeight = 4
workerTimes = [2,1,1]
sol = Solution()
print(sol.minNumberOfSeconds(mountainHeight, workerTimes))