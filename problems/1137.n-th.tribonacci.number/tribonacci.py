class Solution:
    def tribonacci(self, n: int) -> int:
        arrTribonacci = [0,1,1]

        if n == 0: return 0
        if n == 1 or n == 2: return 1
        else :
            count = 3
            while len(arrTribonacci) <= n: 
               arrTribonacci.append(arrTribonacci[count-3] + arrTribonacci[count-2] + arrTribonacci[count-1])
               count = count + 1
        return arrTribonacci[len(arrTribonacci)-1]
               
        
n = 4
sol1 = Solution()
print(sol1.tribonacci(n))