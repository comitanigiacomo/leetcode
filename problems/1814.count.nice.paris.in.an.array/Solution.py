from typing import List

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod = 1000000007
        count = 0
        visited = {}

        def reverse_string(s):
            return s[::-1]

        for i in range(len(nums)):
            num_str = str(nums[i])
            n = int(reverse_string(num_str))
            nums[i] -= n

            if nums[i] in visited:
                count += visited[nums[i]]

            visited[nums[i]] = visited.get(nums[i], 0) + 1

        print(nums, visited)
        return count % mod

sol1 = Solution()
nums = [42,11,1,97]
result = sol1.countNicePairs(nums)
print(result)