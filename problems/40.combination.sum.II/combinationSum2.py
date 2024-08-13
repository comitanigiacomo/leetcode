from typing import List 

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                results.append(path)
                return
            if target < 0:
                return
            prev = -1
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])
                prev = candidates[i]

        candidates.sort()
        results = []
        backtrack(0, target, [])
        return results

        
        
candidates = [10,1,2,7,6,1,5]
target = 8
sol = Solution()
print(sol.combinationSum2(candidates, target))