# 1716.calculate.money.in.leetcode.bank

Here's the full description of the [problem](https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/?envType=daily-question&envId=2023-12-06)

# Approach

The given Python code defines a class Solution with a method totalMoney that calculates the total amount of money in a simulated bank account after a specified number of days. The approach involves iterating through each day, simulating a week by tracking the days of the week and updating the amount to put in the bank. On Mondays, the amount is reset to the previous Monday value + 1

# Complexity

- Time complexity: O(n)
- Space complexity: O(1)

# Code

```python
class Solution:
    def totalMoney(self, n: int) -> int:
        count = 0
        money_bank = 0
        to_put = 1
        monday = 1
        for i in range(n):
            count+= 1
            if count == 8:
                count = 1
                monday += 1
                to_put = monday
            money_bank += to_put
            to_put += 1
        return money_bank
```