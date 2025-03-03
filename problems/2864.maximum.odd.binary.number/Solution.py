class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        l = list(s)
        l.sort(reverse=True)
        str_sorted = ''.join(l)
        if str_sorted[-1] != '1':
            for i in range(len(str_sorted) - 1, -1, -1):
                if str_sorted[i] == '1':
                    str_sorted = str_sorted[:i] + str_sorted[-1] + str_sorted[i+1:-1] + str_sorted[i] 
                    break
        return str_sorted

            
sol1 = Solution()
input = "010"
print(sol1.maximumOddBinaryNumber(input))