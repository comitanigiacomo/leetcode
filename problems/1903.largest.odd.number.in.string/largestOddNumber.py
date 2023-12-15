class Solution:
    def largestOddNumber(self, num: str) -> str:
      count = len(num)-1
      for char in reversed(num):
        if int(char) % 2 != 0:  
          return num[:count+1]
        count -= 1
      return ''          
        
num = "52"   
sol1 = Solution()
result = sol1.largestOddNumber(num)
print(result)       
