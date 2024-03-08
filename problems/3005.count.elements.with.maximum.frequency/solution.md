# 3005.count.elements.with.maximum.frequency

Here's the full description of the [problem](https://leetcode.com/problems/count-elements-with-maximum-frequency/description/?envType=daily-question&envId=2024-03-08)

# Approach

1. Utilize a Counter from the collections module to count the frequency of each element in the input list nums.
2. Identify the maximum frequency among all the elements using the max() function.
3. Extract all elements from the counter that have the maximum frequency using a list comprehension.
4. Calculate the total frequency by multiplying the maximum frequency with the count of elements having that frequency.

# Complexity

- Time complexity: O(n), where `n` is the length of the input list nums.

- Space complexity: O(n), where `n` is the number of unique elements in the input list nums

# Code

```Python
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq_counter = collections.Counter(nums)
        
        max_frequency = max(freq_counter.values())
        
        max_freq_elements = [num for num, freq in freq_counter.items() if freq == max_frequency]
        
        total_frequency = max_frequency * len(max_freq_elements)
        
        return total_frequency
```