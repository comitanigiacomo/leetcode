from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        initial_xor = nums[0]
        for elem in nums[1:]:
            initial_xor ^= elem
        
        binary_xor = bin(initial_xor)[2:] 
        binary_k = bin(k)[2:] 
        
        max_len = max(len(binary_xor), len(binary_k))
        binary_xor = binary_xor.zfill(max_len)
        binary_k = binary_k.zfill(max_len)
        
        count_diff_bits = sum(1 for bit_xor, bit_k in zip(binary_xor, binary_k) if bit_xor != bit_k)
        
        return count_diff_bits
