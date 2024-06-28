Here's the full description of the [problem](https://leetcode.com/problems/maximum-total-importance-of-roads/description/)

# Intuition

To maximize the importance value of the network, I should assign higher values to the cities that are connected by the most roads. By doing this, I ensure that the roads involving the most connected cities contribute the highest possible value to the total importance.

# Approach

1. Count the Connections: Use a dictionary to count how many times each city appears in the road list.
2. Sort Cities by Frequency: Sort the cities based on the number of times they appear in descending order.
3. Assign Values: Assign values to cities starting from `n` (the total number of cities) for the most frequent city, decrementing the value for each subsequent city.
4. Calculate Total Importance: Sum up the values for each road by adding the values assigned to both cities in each road.

# Complexity

- Time complexity: 𝑂(𝑚+𝑛log𝑛, where 𝑚 is the number of roads and 𝑛 is the number of cities

- Space complexity: O(n)

# Code
```python
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Initialize the dictionary with default value 0
        my_dict = defaultdict(int)
        for road in roads: 
            my_dict[road[0]] += 1
            my_dict[road[1]] += 1
        sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
        
        cities_val = {}
        for elem in sorted_dict: 
            cities_val[elem] = n
            n -= 1
        
        count = 0
        for elem in roads: 
            count += cities_val[elem[0]] + cities_val[elem[1]]
        return count
```