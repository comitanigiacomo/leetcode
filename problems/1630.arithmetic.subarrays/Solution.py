class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        out = []
        for idx, v in enumerate(l):
            arr = nums[v:r[idx] + 1]
            print(arr)
            out.append(self.is_arithmetic(arr))
        return out

    def is_arithmetic(self, arr):
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False
        return True
