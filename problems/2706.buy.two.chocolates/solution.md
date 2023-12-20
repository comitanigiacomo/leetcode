# 2706.buy.two.chocolates

Here's the full description of the [problem](https://leetcode.com/problems/buy-two-chocolates/description/?envType=daily-question&envId=2023-12-20)

# Approach

My idea is to order the prices in ascending order and, by considering the first two chocolates, minimize their sum

# Complexity

- Time complexity: O(n log n) due to sorting steps
- Space complexity: O(1)

# Code

```Python
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if prices[0] + prices[1] > money: return money
        return money - ( prices[0]+prices[1])
```
