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
