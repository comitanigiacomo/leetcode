from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        n  = len(nums)

        df = [0] * (n+1)

        for l, r in queries:
            df[l] += 1

            if r+1 < len(df):
                df[r+1] -= 1

        pf = [0]*n
        summ = 0

        for i in range(n):
            summ += df[i]
            pf[i] = summ

        for i in range(n):
            if nums[i] > pf[i]:
                return False

        return True

nums = [1, 0, 1]
queries = [[0,2]]
sol = Solution()
print(sol.isZeroArray(nums, queries))
