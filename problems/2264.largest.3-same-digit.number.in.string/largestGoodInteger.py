class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max = ''
        for i in range(len(num)-2):
            
            for j in range(i+1, i+3):
                if num[i] != num[j]: break
                string = num[i: j+1]
                if len(string) == 3 and string > max: max = string
        return max
        
num = "6777133339"
sol1 = Solution()
result = sol1.largestGoodInteger(num)
print(result)