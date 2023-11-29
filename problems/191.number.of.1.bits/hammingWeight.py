class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_str = bin(n)[2:]  
        count = 0
        for bit in binary_str:
            if bit == '1':
                count += 1
        return count

n = 0o00000000000000000000000000001011
sol1 = Solution()
result = sol1.hammingWeight(n)
print(result)