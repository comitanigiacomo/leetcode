# 1814.count.nice.paris.in.an.array

Here's the full description of the [problem](https://leetcode.com/problems/count-nice-pairs-in-an-array/description/?envType=daily-question&envId=2023-11-21)


# Approach

The approach involves iterating through the given array and, for each element, finding its reverse and calculating the difference between the original element and its reverse. By keeping track of these differences in a dictionary (`visited`), we can count the number of pairs that satisfy the condition `nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])`. The count is then returned after applying the modulo operation.



# Complexity

- Time complexity: O(N), where `N` is the length of the input array nums
- Space complexity: O(N)

# code

```python
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
```