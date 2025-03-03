from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        out = j = maxp = 0
        worker.sort()
        
        for work in worker: 
            while j < len(jobs) and  jobs[j][0] <= work :
                maxp = max(maxp, jobs[j][1])
                j += 1
            out += maxp
        return out


difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]
sol = Solution()
print(sol.maxProfitAssignment(difficulty, profit, worker))