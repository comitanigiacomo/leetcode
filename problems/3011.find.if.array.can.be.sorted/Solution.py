from itertools import groupby, pairwise
from typing import List


class Solution:
    def can_sort_array(self, nums: List[int]) -> bool:
        reordered = []

        for _, item in groupby(nums, key=int.bit_count):
            reordered.extend(sorted(item))

        return all(x <= y for x, y in pairwise(reordered))


nums = [8, 4, 2, 30, 15]
sol = Solution()
print(sol.can_sort_array(nums))
