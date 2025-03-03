from typing import List

class Solution:
    def is_sequential(self, lst: List[int]) -> bool:
        if not lst:
            return False
        return len(lst) == len(set(lst)) and max(lst) - min(lst) + 1 == len(lst)

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        output = []
        for i in range(k-1, len(nums)):
            tmp = nums[i-k+1:i+1]
            if tmp == sorted(tmp) and self.is_sequential(tmp):
                output.append(max(tmp))
            else:
                output.append(-1)
        return output


nums = [1, 2, 3, 4, 3, 2, 5]
k = 3
sol = Solution()
print(sol.resultsArray(nums, k))