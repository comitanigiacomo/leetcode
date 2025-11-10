from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        stack = []

        for elem in nums:
            while stack and stack[-1] > elem:
                stack.pop()
            if elem > 0 and (len(stack) == 0 or stack[-1] < elem):
                stack.append(elem)
                count += 1

        return count

nums = [3,1,2,1]
sol = Solution()
print(sol.minOperations(nums))
