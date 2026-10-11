class Solution(object):
    def sumOfSquares(self, nums):
        sum = 0

        for i in range(len(nums)):
            if len(nums) % (i + 1) == 0:
                sum = sum + nums[i] * nums[i]

        return sum